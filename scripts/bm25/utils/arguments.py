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


@dataclass
class RerankerArgs:
    model_name_or_path: str = field(
        default=None,
        metadata={
            "help": 'One or more reranker name or path. For example, "BAAI/bge-reranker-v2-m3" or "path/to/reranker".',
        },
    )
    add_instruction: bool = field(default=False, metadata={"help": "Add instruction for reranking?"})
    query_instruction_for_reranking: str = field(
        default=None, metadata={"help": "query instruction for reranking"}
    )
    passage_instruction_for_reranking: str = field(
        default=None, metadata={"help": "passage instruction for reranking"}
    )
    max_length: int = field(default=512, metadata={"help": "Max length for reranking."})
    batch_size: int = field(default=256, metadata={"help": "Inference batch size for reranking."})
    trust_remote_code: bool = field(
        default=False, metadata={"help": "Trust remote code or not."}
    )

    use_fp16: bool = field(default=True, metadata={"help": "Use fp16 for reranking."})
