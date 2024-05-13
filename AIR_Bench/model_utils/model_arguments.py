from dataclasses import dataclass, field


@dataclass
class ModelArgs:
    encoder: str = field(
        metadata={'help': 'Encoder name or path. For example, "BAAI/bge-m3" or "path/to/encoder".',
                  'required': True}
    )
    reranker: str = field(
        default=None,
        metadata={'help': 'One or more reranker name or path. For example, "BAAI/bge-reranker-v2-m3" or "path/to/reranker".',
                  'nargs': '+'}
    )
    pooling_method: str = field(
        default='cls',
        metadata={'help': "Pooling method. Avaliable methods: 'cls', 'mean', 'last'"}
    )
    normalize_embeddings: bool = field(
        default=True,
        metadata={'help': "Normalize embeddings or not"}
    )
    use_fp16: bool = field(
        default=True,
        metadata={'help': 'Use fp16 for inference.'}
    )
    add_instruction: bool = field(
        default=False,
        metadata={'help': 'Add instruction?'}
    )
    query_instruction_for_retrieval: str = field(
        default=None,
        metadata={'help': 'query instruction for retrieval'}
    )
    passage_instruction_for_retrieval: str = field(
        default=None,
        metadata={'help': 'passage instruction for retrieval'}
    )
    max_query_length: int = field(
        default=512,
        metadata={'help': 'Max query length.'}
    )
    max_passage_length: int = field(
        default=512,
        metadata={'help': 'Max passage length.'}
    )
    batch_size: int = field(
        default=256,
        metadata={'help': 'Inference batch size.'}
    )
    corpus_batch_size: int = field(
        default=0,
        metadata={'help': 'Inference batch size for corpus. If 0, then use `batch_size`.'}
    )
