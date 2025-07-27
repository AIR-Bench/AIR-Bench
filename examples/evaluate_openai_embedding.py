import os
from openai import OpenAI
from typing import Any, Dict
from FlagEmbedding.abc.evaluation.utils import index, search

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
    
    def __str__(self):
        return str(self.openai_embedding_model)
    
    def __call__(
        self,
        corpus: Dict[str, Dict[str, Any]],
        queries: Dict[str, str],
        **kwargs,
    ):
        corpus_ids = []
        corpus_texts = []
        for docid, doc in corpus.items():
            corpus_ids.append(docid)
            corpus_texts.append(
                doc["text"]
            )
        queries_ids = []
        queries_texts = []
        for qid, query in queries.items():
            queries_ids.append(qid)
            queries_texts.append(query)

        # encode corpus and queries
        corpus_emb = self.openai_embedding_model.encode_corpus(corpus_texts, **kwargs)
        queries_emb = self.openai_embedding_model.encode_queries(queries_texts, **kwargs)

        faiss_index = index(corpus_embeddings=corpus_emb)
        all_scores, all_indices = search(query_embeddings=queries_emb, faiss_index=faiss_index, k=self.search_top_k)

        search_results = {}
        for idx, (scores, indices) in enumerate(zip(all_scores, all_indices)):
            search_results[queries_ids[idx]] = {}
            for score, indice in zip(scores, indices):
                if indice != -1:
                    search_results[queries_ids[idx]][corpus_ids[indice]] = float(score)

        return search_results


def main():
    openai_embedding_model = OpenAIEmbeddingModel('text-embedding-ada-002')
    
    evaluation = AIRBench(
        benchmark_version="AIR-Bench_24.04",
        task_types=["long-doc"],    # choose a single task for demo purpose
        domains=["book"],           # choose a single domain for demo purpose
        languages=["en"],           # choose a single language for demo purpose
        splits=["dev"],            # choose a single split for demo purpose
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
    
    # compute metrics for dev set
    evaluation.evaluate_dev(
        benchmark_version="AIR-Bench_24.05",
        search_results_save_dir='./search_results',
        output_method="markdown",
        output_path='./eval_dev_results.md',
        metrics=["ndcg_at_10", "recall_at_10"],
    )


if __name__ == "__main__":
    main()
