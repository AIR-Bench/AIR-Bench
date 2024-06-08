import os
from sentence_transformers import CrossEncoder, SentenceTransformer
from typing import Optional


class SentenceTransformerEncoder:
    def __init__(
        self,
        model_name_or_path: str,
        normalize_embeddings: bool = True,
        query_instruction_for_retrieval: Optional[str] = None,
        passage_instruction_for_retrieval: Optional[str] = None,
        max_query_length: int = 512,
        max_passage_length: int = 8192,
        batch_size: int = 256,
        corpus_batch_size: int = 0,
        **kwargs
    ):
        self.name = os.path.basename(model_name_or_path)

        self.model = SentenceTransformer(model_name_or_path, **kwargs)
        self.query_instruction_for_retrieval = query_instruction_for_retrieval
        self.passage_instruction_for_retrieval = passage_instruction_for_retrieval
        self.max_query_length = max_query_length
        self.max_passage_length = max_passage_length
        self.normalize_embeddings = normalize_embeddings
        self.batch_size = batch_size
        self.corpus_batch_size = (
            corpus_batch_size if corpus_batch_size > 0 else batch_size
        )

    def encode_corpus(self, corpus, **kwargs):
        input_texts = corpus
        if isinstance(corpus[0], dict):
            input_texts = [
                "{} {}".format(doc.get("title", ""), doc.get("text", "")).strip()
                for doc in corpus
            ]
        self.model.max_seq_length = self.max_passage_length
        return self.model.encode(
            input_texts,
            prompt=self.passage_instruction_for_retrieval,
            batch_size=self.corpus_batch_size,
            normalize_embeddings=self.normalize_embeddings,
            show_progress_bar=True,
        )

    def encode_queries(self, queries, **kwargs):
        input_texts = queries
        if isinstance(queries[0], dict):
            input_texts = [doc.get("text", "").strip() for doc in queries]
        self.model.max_seq_length = self.max_query_length
        return self.model.encode(
            input_texts,
            prompt=self.query_instruction_for_retrieval,
            batch_size=self.batch_size,
            normalize_embeddings=self.normalize_embeddings,
            show_progress_bar=True,
        )

    def __str__(self):
        return self.name


class SentenceTransformerReranker:
    def __init__(
        self,
        model_name_or_path: str,
        max_length: int = 512,
        batch_size: int = 256,
        **kwargs
    ):
        self.name = os.path.basename(model_name_or_path)
        
        self.model = CrossEncoder(
            model_name_or_path,
            max_length=max_length,
            **kwargs
        )
        self.batch_size = batch_size

    def compute_score(self, sentence_pairs: list):
        if isinstance(sentence_pairs[0], str):
            sentence_pairs = [sentence_pairs]
        return self.model.predict(sentence_pairs, batch_size=self.batch_size)

    def __str__(self):
        return self.name
