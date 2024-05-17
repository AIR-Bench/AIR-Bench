import os
from typing import Optional

import torch
from transformers import AutoModel, AutoTokenizer, is_torch_npu_available

from air_benchmark.air_benchmark import AIRBench
from air_benchmark.model_utils.models import (
    AutoModelForSequenceClassification,
    DRESModel,
    DRESReranker,
)


# jina-embeddings-v2 uses ALiBi which is not support by transformers by default and therefore requires `trust_remote_code=True`
class JinaEmbeddingsV2:
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

        self.tokenizer = AutoTokenizer.from_pretrained(model_name_or_path)
        self.model = AutoModel.from_pretrained(
            model_name_or_path, trust_remote_code=True
        )

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


class JinaRerankerV1(DRESReranker):
    def __init__(
        self,
        model_name_or_path: str,
        use_fp16: bool = True,
        query_instruction_for_retrieval: Optional[str] = None,
        passage_instruction_for_retrieval: Optional[str] = None,
        max_length: int = 512,
        batch_size: int = 256,
        **kwargs,
    ):
        self.name = os.path.basename(model_name_or_path)
        self.tokenizer = AutoTokenizer.from_pretrained(model_name_or_path)

        self.model = AutoModelForSequenceClassification.from_pretrained(
            model_name_or_path, num_labels=1, trust_remote_code=True
        )

        self.query_instruction_for_retrieval = query_instruction_for_retrieval
        self.passage_instruction_for_retrieval = passage_instruction_for_retrieval
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


def main():
    encoder = JinaEmbeddingsV2(
        "jinaai/jina-embeddings-v2-small-en",
        "mean",
        True,
        use_fp16=False,
        max_query_length=512,
        max_passage_length=512,
        batch_size=512,
    )

    reranker = JinaRerankerV1(
        "jinaai/jina-reranker-v1-tiny-en",
        use_fp16=False,
        max_length=512,
        batch_size=512,
    )

    evaluation = AIRBench(
        benchmark_version="AIR-Bench_24.04",
        task_types=["long-doc"],  # choose a single task for demo purpose
        domains=["book"],  # choose a single domain for demo purpose
        languages=["en"],  # choose a single language for demo purpose
    )

    evaluation.run(
        encoder,
        output_dir="./search_results",
        search_top_k=20,  # change to 1000 for proper evaluations
        reranker_list=[
            reranker,
        ],
        rerank_top_k=10,  # change to 100 for proper evaluations
        overwrite=True,
        corpus_chunk_size=10000,  # change 10_000_000 when encoding the large corpus to avoid multiple tqdm bars
    )


if __name__ == '__main__':
    main()
