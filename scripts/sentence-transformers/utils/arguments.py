from dataclasses import dataclass, field


@dataclass
class ModelArgs:
    encoder: str = field(
        metadata={
            "help": 'Encoder name or path. For example, "BAAI/bge-m3" or "path/to/encoder".',
            "required": True,
        }
    )
    normalize_embeddings: bool = field(
        default=True, metadata={"help": "Normalize embeddings or not"}
    )
    add_instruction: bool = field(default=False, metadata={"help": "Add instruction for retrieval?"})
    query_instruction: str = field(
        default=None, metadata={"help": "query instruction for retrieval"}
    )
    passage_instruction: str = field(
        default=None, metadata={"help": "passage instruction for retrieval"}
    )
    batch_size: int = field(default=256, metadata={"help": "Inference batch size for retrieval."})
    corpus_batch_size: int = field(
        default=0,
        metadata={
            "help": "Inference batch size for corpus. If 0, then use `batch_size`."
        },
    )
    
    reranker: str = field(
        default=None,
        metadata={
            "help": 'One or more reranker name or path. For example, "BAAI/bge-reranker-v2-m3" or "path/to/reranker".',
        },
    )
    max_length_for_reranking: int = field(default=512, metadata={"help": "Max length for reranking."})
    batch_size_for_reranking: int = field(default=256, metadata={"help": "Inference batch size for reranking."})
