from dataclasses import dataclass, field


@dataclass
class BM25Args:
    bm25_tmp_dir: str = field(
        default="./bm25_tmp_dir",
        metadata={"help": "Cache directory for evaluating BM25."},
    )
    remove_bm25_tmp_dir: bool = field(
        default=True, metadata={"help": "Remove BM25 tmp dir or not."}
    )
