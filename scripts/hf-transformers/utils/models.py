import os
from functools import partial
from typing import Dict, List, Optional, Tuple, Union, cast

import datasets
import numpy as np
import torch
from torch.utils.data import DataLoader
from tqdm import tqdm
from transformers import (
    AutoModel,
    AutoModelForSequenceClassification,
    AutoTokenizer,
    BatchEncoding,
    DataCollatorWithPadding,
    PreTrainedTokenizerFast,
    is_torch_npu_available,
)


def _transform_func(
    examples: Dict[str, List], tokenizer: PreTrainedTokenizerFast, max_length: int
) -> BatchEncoding:
    return tokenizer(
        examples["text"],
        max_length=max_length,
        padding=True,
        return_token_type_ids=False,
        truncation=True,
        return_tensors="pt",
    )


def _transform_func_for_last_pooling(
    examples: Dict[str, List],
    tokenizer: PreTrainedTokenizerFast,
    max_length: int = 8192,
) -> BatchEncoding:

    if tokenizer.eos_token_id is None:
        raise ValueError(
            f"tokenizer.eos_token_id should not be `None`. tokenizer.eos_token_id={tokenizer.eos_token_id}"
        )
    inputs = tokenizer(
        examples["text"],
        max_length=max_length - 1,
        padding=False,
        return_attention_mask=False,
        truncation=True,
    )
    inputs["input_ids"] = [
        input_ids + [tokenizer.eos_token_id] for input_ids in inputs["input_ids"]
    ]
    inputs = tokenizer.pad(
        inputs, padding=True, return_attention_mask=True, return_tensors="pt"
    )
    return inputs


class DRESModel:
    """
    Dense Retrieval Exact Search Models
    """

    def __init__(
        self,
        model_name_or_path: str,
        pooling_method: str = "cls",
        normalize_embeddings: bool = True,
        use_fp16: bool = True,
        query_instruction_for_retrieval: Optional[str] = None,
        passage_instruction_for_retrieval: Optional[str] = None,
        max_query_length: int = 512,
        max_passage_length: int = 8192,
        batch_size: int = 256,
        corpus_batch_size: int = 0,
        **kwargs,
    ) -> None:
        self.name = os.path.basename(model_name_or_path)

        self.tokenizer = AutoTokenizer.from_pretrained(model_name_or_path, **kwargs)
        self.model = AutoModel.from_pretrained(model_name_or_path, **kwargs)
        self.query_instruction_for_retrieval = query_instruction_for_retrieval
        self.passage_instruction_for_retrieval = passage_instruction_for_retrieval
        self.normalize_embeddings = normalize_embeddings
        self.pooling_method = pooling_method
        self.batch_size = batch_size
        self.corpus_batch_size = (
            corpus_batch_size if corpus_batch_size > 0 else batch_size
        )
        self.max_query_length = max_query_length
        self.max_passage_length = max_passage_length

        if use_fp16:
            self.model.half()
        if torch.cuda.is_available():
            self.device = torch.device("cuda")
        elif is_torch_npu_available():
            self.device = torch.device("npu")
        else:
            self.device = torch.device("cpu")
        self.model = self.model.to(self.device)

        self.num_gpus = torch.cuda.device_count()
        if self.num_gpus > 1:
            self.model = torch.nn.DataParallel(self.model)

    def __str__(self) -> str:
        return self.name

    def encode_queries(
        self, queries: List[Union[Dict[str, str], str]], **kwargs
    ) -> np.ndarray:
        """
        This function will be used for retrieval task
        if there is a instruction for queries, we will add it to the query text
        """
        if isinstance(queries[0], dict):
            if self.query_instruction_for_retrieval is not None:
                input_texts = [
                    "{}{}".format(self.query_instruction_for_retrieval, q["text"])
                    for q in queries
                ]
            else:
                input_texts = [q["text"] for q in queries]
        else:
            if self.query_instruction_for_retrieval is not None:
                input_texts = [
                    "{}{}".format(self.query_instruction_for_retrieval, q)
                    for q in queries
                ]
            else:
                input_texts = queries
        return self.encode(
            input_texts, max_length=self.max_query_length, batch_size=self.batch_size
        )

    def encode_corpus(
        self, corpus: List[Union[Dict[str, str], str]], **kwargs
    ) -> np.ndarray:
        """
        This function will be used for retrieval task
        encode corpus for retrieval task
        """
        if isinstance(corpus[0], dict):
            if self.passage_instruction_for_retrieval is not None:
                input_texts = [
                    "{}{} {}".format(
                        self.passage_instruction_for_retrieval,
                        doc.get("title", ""),
                        doc["text"],
                    ).strip()
                    for doc in corpus
                ]
            else:
                input_texts = [
                    "{} {}".format(doc.get("title", ""), doc["text"]).strip()
                    for doc in corpus
                ]
        else:
            if self.passage_instruction_for_retrieval is not None:
                input_texts = self.passage_instruction_for_retrieval + corpus
            else:
                input_texts = corpus
        return self.encode(
            input_texts,
            max_length=self.max_passage_length,
            batch_size=self.corpus_batch_size,
        )

    @torch.no_grad()
    def encode(
        self,
        sentences: List[str],
        max_length: int = 512,
        batch_size: int = 16,
        **kwargs,
    ) -> np.ndarray:
        if self.num_gpus > 0:
            batch_size = batch_size * self.num_gpus
        self.model.eval()

        input_was_string = False
        if isinstance(sentences, str):
            sentences = [sentences]
            input_was_string = True

        dataset = datasets.Dataset.from_dict({"text": sentences})
        if self.pooling_method == "last":
            assert (
                self.tokenizer.eos_token_id != None
            ), "Setting `pooling_method='last'` require tokenizer.eos_token_id != None"
            dataset.set_transform(
                partial(
                    _transform_func_for_last_pooling,
                    tokenizer=self.tokenizer,
                    max_length=max_length,
                )
            )
        else:
            dataset.set_transform(
                partial(
                    _transform_func, tokenizer=self.tokenizer, max_length=max_length
                )
            )

        data_collator = DataCollatorWithPadding(self.tokenizer)
        data_loader = DataLoader(
            dataset,
            batch_size=batch_size,
            shuffle=False,
            drop_last=False,
            num_workers=4,
            collate_fn=data_collator,
            # pin_memory=True
        )

        all_embeddings = []
        for batch_data in tqdm(data_loader, desc="encoding", mininterval=10):
            batch_data = batch_data.to(self.device)
            last_hidden_state = self.model(
                **batch_data, return_dict=True
            ).last_hidden_state
            embeddings = self.pooling(
                last_hidden_state, batch_data["attention_mask"]
            ).float()
            if self.normalize_embeddings:
                embeddings = torch.nn.functional.normalize(embeddings, dim=-1)
            embeddings = cast(torch.Tensor, embeddings)
            all_embeddings.append(embeddings.cpu().numpy())

        all_embeddings = np.concatenate(all_embeddings, axis=0)
        if input_was_string:
            return all_embeddings[0]
        else:
            return all_embeddings

    def pooling(
        self, last_hidden_state: torch.Tensor, attention_mask: torch.Tensor = None
    ):
        if self.pooling_method == "cls":
            return last_hidden_state[:, 0]
        elif self.pooling_method == "mean":
            s = torch.sum(
                last_hidden_state * attention_mask.unsqueeze(-1).float(), dim=1
            )
            d = attention_mask.sum(dim=1, keepdim=True).float()
            return s / d
        elif self.pooling_method == "last":
            left_padding = attention_mask[:, -1].sum() == attention_mask.shape[0]
            if left_padding:
                return last_hidden_state[:, -1]
            else:
                sequence_lengths = attention_mask.sum(dim=1) - 1
                batch_size = last_hidden_state.shape[0]
                return last_hidden_state[
                    torch.arange(batch_size, device=last_hidden_state.device),
                    sequence_lengths,
                ]


class DRESReranker:
    """
    Dense Retrieval Exact Search Reranker
    """

    def __init__(
        self,
        model_name_or_path: str,
        use_fp16: bool = True,
        query_instruction_for_reranking: Optional[str] = None,
        passage_instruction_for_reranking: Optional[str] = None,
        max_length: int = 512,
        batch_size: int = 256,
        **kwargs,
    ):
        self.name = os.path.basename(model_name_or_path)

        self.tokenizer = AutoTokenizer.from_pretrained(model_name_or_path)

        if "jina" in model_name_or_path:
            self.model = AutoModelForSequenceClassification.from_pretrained(
                model_name_or_path, num_labels=1, trust_remote_code=True
            )
        else:
            self.model = AutoModelForSequenceClassification.from_pretrained(
                model_name_or_path
            )

        self.query_instruction_for_reranking = query_instruction_for_reranking
        self.passage_instruction_for_reranking = passage_instruction_for_reranking
        self.max_length = max_length
        self.batch_size = batch_size

        if use_fp16:
            self.model.half()
        if torch.cuda.is_available():
            self.device = torch.device("cuda")
        elif is_torch_npu_available():
            self.device = torch.device("npu")
        else:
            self.device = torch.device("cpu")
        self.model = self.model.to(self.device)

        self.model.eval()
        self.num_gpus = torch.cuda.device_count()
        if self.num_gpus > 1:
            self.model = torch.nn.DataParallel(self.model)

    def __str__(self) -> str:
        return self.name

    def add_instruction(self, sentence_pairs: List[Tuple[str, str]]):
        if self.query_instruction_for_reranking is not None:
            sentence_pairs = [
                (f"{self.query_instruction_for_reranking}{query}", passage)
                for query, passage in sentence_pairs
            ]
        if self.passage_instruction_for_reranking is not None:
            sentence_pairs = [
                (query, f"{self.passage_instruction_for_reranking}{passage}")
                for query, passage in sentence_pairs
            ]
        return sentence_pairs

    @torch.no_grad()
    def compute_score(
        self, sentence_pairs: Union[List[Tuple[str, str]], Tuple[str, str]], **kwargs
    ):
        if self.num_gpus > 0:
            batch_size = self.batch_size * self.num_gpus
        else:
            batch_size = self.batch_size

        assert isinstance(sentence_pairs, list)
        if isinstance(sentence_pairs[0], str):
            sentence_pairs = [sentence_pairs]

        sentence_pairs = self.add_instruction(sentence_pairs)

        all_scores = []
        for start_index in tqdm(
            range(0, len(sentence_pairs), batch_size),
            desc="Compute Scores",
            disable=len(sentence_pairs) < 128,
        ):
            sentences_batch = sentence_pairs[start_index : start_index + batch_size]
            inputs = self.tokenizer(
                sentences_batch,
                padding=True,
                truncation=True,
                return_tensors="pt",
                max_length=self.max_length,
            ).to(self.device)

            scores = (
                self.model(**inputs, return_dict=True)
                .logits.view(
                    -1,
                )
                .float()
            )
            all_scores.extend(scores.cpu().numpy().tolist())

        if len(all_scores) == 1:
            return all_scores[0]
        return all_scores
