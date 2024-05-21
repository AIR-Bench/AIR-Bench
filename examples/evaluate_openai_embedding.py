from mteb.evaluation.evaluators import RetrievalEvaluator
import os
from openai import OpenAI
from typing import Any, Dict

from air_benchmark import AIRBench, Retriever


class OpenAIEmbeddingModel:
    def __init__(self, model_name: str='text-embedding-ada-002', **kwargs):
        self.model = model_name
        self.client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))
    
    def __str__(self) -> str:
        return self.model
    
    def encode_corpus(self, corpus, **kwargs):
        input_texts = corpus
        if isinstance(corpus[0], dict):
            input_texts = [
                "{} {}".format(doc.get("title", ""), doc.get("text", "")).strip()
                for doc in corpus
            ]
        return self.encode(input_texts, **kwargs)
    
    def encode_queries(self, queries, **kwargs):
        input_texts = queries
        if isinstance(queries[0], dict):
            input_texts = [doc.get("text", "").strip() for doc in queries]
        return self.encode(input_texts, **kwargs)

    def encode(self, sentences, **kwargs):
        output = self.client.embeddings.create(
            input=sentences,
            model=self.model,
            **kwargs
        )
        embeddings = [x.embedding for x in output.data]
        return embeddings


class OpenAIEmbeddingModelRetriever(Retriever):
    def __init__(self, openai_embedding_model: OpenAIEmbeddingModel, search_top_k: int = 1000, **kwargs):
        self.openai_embedding_model = openai_embedding_model
        super().__init__(search_top_k)
        self.retriever = RetrievalEvaluator(
            retriever=self.openai_embedding_model,
            k_values=[self.search_top_k],
            **kwargs,
        )
    
    def __str__(self):
        return str(self.openai_embedding_model)
    
    def __call__(
        self,
        corpus: Dict[str, Dict[str, Any]],
        queries: Dict[str, str],
        **kwargs,
    ):
        search_results = self.retriever(corpus=corpus, queries=queries)
        return search_results


def main():
    openai_embedding_model = OpenAIEmbeddingModel('text-embedding-ada-002')
    
    evaluation = AIRBench(
        benchmark_version="AIR-Bench_24.04",
        task_types=["long-doc"],    # choose a single task for demo purpose
        domains=["book"],           # choose a single domain for demo purpose
        languages=["en"],           # choose a single language for demo purpose
    )
    
    retriever = OpenAIEmbeddingModelRetriever(
        openai_embedding_model, 
        search_top_k=1000,
        corpus_chunk_size=10000,  # change to 10_000_000 when encoding the large corpus to avoid multiple tqdm bars
    )
    
    evaluation.run(
        retriever,
        output_dir='./search_results',
        overwrite=True,
    )


if __name__ == "__main__":
    main()
