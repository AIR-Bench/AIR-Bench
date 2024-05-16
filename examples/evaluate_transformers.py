from air_benchmark.air_benchmark import AIRBench
from air_benchmark.model_utils.models import DRESModel, DRESReranker

encoder = DRESModel(
    "jinaai/jina-embeddings-v2-small-en",
    "mean",
    True,
    use_fp16=False,
    max_query_length=512,
    max_passage_length=512,
    batch_size=512,
)

reranker = DRESReranker(
    "jinaai/jina-reranker-v1-tiny-en",
    use_fp16=False,
    max_length=512,
    batch_size=512,
)

airb = AIRBench(
    benchmark_version="AIR-Bench_24.04",
    task_types=["long-doc"],
    domains=["arxiv"],
    languages=["en"],
)

airb.run(
    encoder,
    reranker_list=[
        reranker,
    ],
    output_dir="./search_results",
    search_top_k=1000,
    rerank_top_k=100,
    overwrite=True,
    corpus_chunk=10_000_000,
)
