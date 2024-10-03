import os
from typing import List, Optional, Tuple, Union

import torch
from tqdm import tqdm
from transformers import (
    AutoModelForSequenceClassification,
    AutoTokenizer,
    is_torch_npu_available,
)


class Reranker:
    def __init__(
        self,
        model_name_or_path: str,
        use_fp16: bool = True,
        query_instruction_for_reranking: Optional[str] = None,
        passage_instruction_for_reranking: Optional[str] = None,
        max_length: int = 512,
        batch_size: int = 256,
        trust_remote_code: bool = False,
        **kwargs,
    ):
        self.name = os.path.basename(model_name_or_path)

        self.tokenizer = AutoTokenizer.from_pretrained(
            model_name_or_path,
            trust_remote_code=trust_remote_code,
            **kwargs,
        )
        
        self.model = AutoModelForSequenceClassification.from_pretrained(
            model_name_or_path,
            trust_remote_code=trust_remote_code,
            **kwargs,
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
