from dataclasses import dataclass, field


@dataclass
class EvalArgs:
    benchmark_version: str = field(
        default=None, metadata={"help": "Benchmark version."}
    )
    output_dir: str = field(
        default="./search_results", metadata={"help": "Path to save results."}
    )
    task_types: str = field(
        default=None, metadata={"help": "Task types.", "nargs": "+"}
    )
    domains: str = field(
        default=None, metadata={"help": "Domains to evaluate.", "nargs": "+"}
    )
    languages: str = field(
        default=None, metadata={"help": "Languages to evaluate.", "nargs": "+"}
    )
    search_top_k: int = field(
        default=1000, metadata={"help": "Top k values for evaluation."}
    )
    rerank_top_k: int = field(default=100, metadata={"help": "Top k for reranking."})
    cache_dir: str = field(
        default=None, metadata={"help": "Cache directory for datasets."}
    )
    bm25_tmp_dir: str = field(
        default="./bm25_tmp_dir",
        metadata={"help": "Cache directory for evaluating BM25."},
    )
    remove_bm25_tmp_dir: bool = field(
        default=True, metadata={"help": "Remove BM25 tmp dir or not."}
    )
    overwrite: bool = field(
        default=False, metadata={"help": "whether to overwrite evaluation results"}
    )
