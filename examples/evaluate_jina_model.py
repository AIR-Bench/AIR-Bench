from mteb.evaluation.evaluators import RetrievalEvaluator
import os
from openai import OpenAI
from sentence_transformers import SentenceTransformer, CrossEncoder
from typing import Any, Dict

from air_benchmark import AIRBench, Retriever, Reranker


class JinaEmbeddingModel:
    def __init__(self, model_name_or_path: str='jinaai/jina-embeddings-v2-base-en', **kwargs):
        self.name = os.path.basename(model_name_or_path)
        
        self.model = SentenceTransformer(
            model_name_or_path,
            trust_remote_code=True,
        )
        
        self.model.max_seq_length = 512
    
    def __str__(self) -> str:
        return self.name
    
    def encode_corpus(self, corpus, **kwargs):
        input_texts = corpus
        if isinstance(corpus[0], dict):
            input_texts = [
                "{} {}".format(doc.get("title", ""), doc.get("text", "")).strip()
                for doc in corpus
            ]
        return self.model.encode(input_texts, **kwargs)
    
    def encode_queries(self, queries, **kwargs):
        input_texts = queries
        if isinstance(queries[0], dict):
            input_texts = [doc.get("text", "").strip() for doc in queries]
        return self.model.encode(input_texts, **kwargs)


class JinaRerankerModel:
    def __init__(self, model_name_or_path: str='jinaai/jina-reranker-v1-tiny-en') -> None:
        self.name = os.path.basename(model_name_or_path)
        
        self.model = CrossEncoder(
            model_name_or_path,
            max_length=512,
            trust_remote_code=True,
        )
    
    def __str__(self):
        return self.name
    
    def compute_score(self, sentence_pairs, **kwargs):
        if isinstance(sentence_pairs[0], str):
            sentence_pairs = [sentence_pairs]
        return self.model.predict(sentence_pairs, **kwargs)


class JinaRetriever(Retriever):
    def __init__(self, jina_embedding_model: JinaEmbeddingModel, search_top_k: int = 1000, **kwargs):
        self.jina_embedding_model = jina_embedding_model
        super().__init__(search_top_k)
        self.retriever = RetrievalEvaluator(
            retriever=self.jina_embedding_model,
            k_values=[self.search_top_k],
            **kwargs,
        )
    
    def __str__(self):
        return str(self.jina_embedding_model)
    
    def __call__(
        self,
        corpus: Dict[str, Dict[str, Any]],
        queries: Dict[str, str],
        **kwargs,
    ):
        search_results = self.retriever(corpus=corpus, queries=queries)
        return search_results


class JinaReranker(Reranker):
    def __init__(self, jina_reranker_model: JinaRerankerModel, rerank_top_k: int = 100, **kwargs):
        self.jina_reranker_model = jina_reranker_model
        super().__init__(rerank_top_k)
        self.reranker = RetrievalEvaluator(
            reranker=self.jina_reranker_model,
            k_values=[self.rerank_top_k],
            **kwargs,
        )
    
    def __str__(self):
        return str(self.jina_reranker_model)
    
    def __call__(
        self,
        corpus: Dict[str, Dict[str, Any]],
        queries: Dict[str, str],
        search_results: Dict[str, Dict[str, float]],
        **kwargs,
    ):
        # truncate search results to top_k
        for qid in search_results:
            search_results[qid] = dict(
                sorted(search_results[qid].items(), key=lambda x: x[1], reverse=True)[
                    :self.rerank_top_k
                ]
            )
        # generate sentence pairs
        sentence_pairs = []
        for qid in search_results:
            for docid in search_results[qid]:
                sentence_pairs.append(
                    {
                        "qid": qid,
                        "docid": docid,
                        "query": queries[qid],
                        "doc": corpus[docid]["text"],
                    }
                )
        pairs = [(e["query"], e["doc"]) for e in sentence_pairs]
        # compute scores
        scores = self.jina_reranker_model.compute_score(pairs)
        for i, score in enumerate(scores):
            sentence_pairs[i]["score"] = float(score)
        # rerank
        reranked_results = {qid: {} for qid in search_results}
        for pair in sentence_pairs:
            reranked_results[pair["qid"]][pair["docid"]] = pair["score"]
        return reranked_results


def main():
    jina_embedding_model = JinaEmbeddingModel('jinaai/jina-embeddings-v2-base-en')
    jina_reranker_model = JinaRerankerModel('jinaai/jina-reranker-v1-tiny-en')
    
    evaluation = AIRBench(
        benchmark_version="AIR-Bench_24.04",
        task_types=["long-doc"],    # choose a single task for demo purpose
        domains=["book"],           # choose a single domain for demo purpose
        languages=["en"],           # choose a single language for demo purpose
    )
    
    retriever = JinaRetriever(
        jina_embedding_model, 
        search_top_k=1000,
        corpus_chunk_size=10000,  # change to 10_000_000 when encoding the large corpus to avoid multiple tqdm bars
    )
    
    reranker = JinaReranker(
        jina_reranker_model,
        rerank_top_k=100,
    )
    
    evaluation.run(
        retriever,
        reranker=reranker,
        output_dir='./search_results',
        overwrite=True,
    )


if __name__ == "__main__":
    main()
