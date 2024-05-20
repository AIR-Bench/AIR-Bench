import json
import logging
import os
from typing import Any, Dict
from abc import ABC, abstractmethod

from mteb.evaluation.evaluators import RetrievalEvaluator

from air_benchmark.model_utils import DRESModel, DRESReranker

logger = logging.getLogger(__name__)


class Retriever(ABC):
    """
    Base class for retrievers.
    Extend this class and implement __call__ for custom retrievers.
    """
    def __init__(self, search_top_k: int = 1000):
        self.search_top_k = search_top_k
    
    @abstractmethod
    def __str__(self) -> str:
        """
        Returns: str: Name of the retriever.
        """
        pass
    
    @abstractmethod
    def __call__(
        self,
        corpus: Dict[str, Dict[str, Any]],
        queries: Dict[str, str],
        **kwargs,
    ) -> Dict[str, Dict[str, float]]:
        """
        This is called during the retrieval process.
        
        Parameters:
            corpus: Dict[str, Dict[str, Any]]: Corpus of documents. 
                Structure: {<docid>: {"text": <text>}}.
                Example: {"doc-0": {"text": "This is a document."}}
            queries: Dict[str, str]: Queries to search for.
                Structure: {<qid>: <query>}.
                Example: {"q-0": "This is a query."}
            **kwargs: Any: Additional arguments.
        
        Returns: Dict[str, Dict[str, float]]: Top-k search results for each query. k is specified by search_top_k.
            Structure: {qid: {docid: score}}. The higher is the score, the more relevant is the document.
            Example: {"q-0": {"doc-0": 0.9}}
        """
        pass

class Reranker(ABC):
    """
    Base class for rerankers.
    Extend this class and implement __call__ for custom rerankers.
    """
    def __init__(self, rerank_top_k: int = 100):
        self.rerank_top_k = rerank_top_k
    
    @abstractmethod
    def __str__(self) -> str:
        """
        Returns: str: Name of the reranker.
        """
        pass
    
    @abstractmethod
    def __call__(
        self,
        corpus: Dict[str, Dict[str, Any]],
        queries: Dict[str, str],
        search_results: Dict[str, Dict[str, float]],
        **kwargs,
    ) -> Dict[str, Dict[str, float]]:
        """
        This is called during the reranking process.
        
        Parameters:
            corpus: Dict[str, Dict[str, Any]]: Corpus of documents. 
                Structure: {<docid>: {"text": <text>}}.
                Example: {"doc-0": {"text": "This is a document."}}
            queries: Dict[str, str]: Queries to search for.
                Structure: {<qid>: <query>}.
                Example: {"q-0": "This is a query."}
            search_results: Dict[str, Dict[str, float]]: Search results for each query.
                Structure: {qid: {docid: score}}. The higher is the score, the more relevant is the document.
                Example: {"q-0": {"doc-0": 0.9}}
            **kwargs: Any: Additional arguments.
        
        Returns: Dict[str, Dict[str, float]]: Reranked search results for each query. k is specified by rerank_top_k.
            Structure: {qid: {docid: score}}. The higher is the score, the more relevant is the document.
            Example: {"q-0": {"doc-0": 0.9}}
        """
        pass


class EmbeddingModelRetriever(Retriever):
    def __init__(self, model: DRESModel, search_top_k: int = 1000, **kwargs):
        super().__init__(search_top_k)
        self.model = model
        self.retriever = RetrievalEvaluator(
            retriever=model,
            k_values=[self.search_top_k],
            **kwargs,
        )
    
    def __str__(self):
        return str(self.model)
    
    def __call__(
        self,
        corpus: Dict[str, Dict[str, Any]],
        queries: Dict[str, str],
        **kwargs,
    ):
        search_results = self.retriever(corpus=corpus, queries=queries)
        return search_results


class CrossEncoderReranker(Reranker):
    def __init__(self, reranker: DRESReranker, rerank_top_k: int = 100, **kwargs):
        super().__init__(rerank_top_k)
        self.reranker = reranker
    
    def __str__(self):
        return str(self.reranker)
    
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
        scores = self.reranker.compute_score(pairs)
        for i, score in enumerate(scores):
            sentence_pairs[i]["score"] = float(score)
        # rerank
        reranked_results = {qid: {} for qid in search_results}
        for pair in sentence_pairs:
            reranked_results[pair["qid"]][pair["docid"]] = pair["score"]
        return reranked_results
