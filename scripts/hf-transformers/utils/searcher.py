from mteb.evaluation.evaluators import RetrievalEvaluator
from typing import Any, Dict

from air_benchmark import Retriever, Reranker

from utils.models import DRESModel, DRESReranker


class EmbeddingModelRetriever(Retriever):
    def __init__(self, embedding_model: DRESModel, search_top_k: int = 1000, **kwargs):
        super().__init__(search_top_k)
        self.embedding_model = embedding_model
        self.retriever = RetrievalEvaluator(
            retriever=embedding_model,
            k_values=[self.search_top_k],
            **kwargs,
        )
    
    def __str__(self):
        return str(self.embedding_model)
    
    def __call__(
        self,
        corpus: Dict[str, Dict[str, Any]],
        queries: Dict[str, str],
        **kwargs,
    ):
        search_results = self.retriever(corpus=corpus, queries=queries)
        return search_results


class CrossEncoderReranker(Reranker):
    def __init__(self, cross_encoder: DRESReranker, rerank_top_k: int = 100, **kwargs):
        super().__init__(rerank_top_k)
        self.cross_encoder = cross_encoder
    
    def __str__(self):
        return str(self.cross_encoder)
    
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
        scores = self.cross_encoder.compute_score(pairs)
        for i, score in enumerate(scores):
            sentence_pairs[i]["score"] = float(score)
        # rerank
        reranked_results = {qid: {} for qid in search_results}
        for pair in sentence_pairs:
            reranked_results[pair["qid"]][pair["docid"]] = pair["score"]
        return reranked_results
