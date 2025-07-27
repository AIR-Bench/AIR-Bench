from typing import Any, Dict

from air_benchmark import Retriever, Reranker

from utils.models import SentenceTransformerEncoder, SentenceTransformerReranker
from utils.utils import index, search


class EmbeddingModelRetriever(Retriever):
    def __init__(self, embedding_model: SentenceTransformerEncoder, search_top_k: int = 1000, **kwargs):
        super().__init__(search_top_k)
        self.embedding_model = embedding_model
    
    def __str__(self):
        return str(self.embedding_model)
    
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
        corpus_emb = self.embedding_model.encode_corpus(corpus_texts, **kwargs)
        queries_emb = self.embedding_model.encode_queries(queries_texts, **kwargs)

        faiss_index = index(corpus_embeddings=corpus_emb)
        all_scores, all_indices = search(query_embeddings=queries_emb, faiss_index=faiss_index, k=self.search_top_k)

        search_results = {}
        for idx, (scores, indices) in enumerate(zip(all_scores, all_indices)):
            search_results[queries_ids[idx]] = {}
            for score, indice in zip(scores, indices):
                if indice != -1:
                    search_results[queries_ids[idx]][corpus_ids[indice]] = float(score)

        return search_results


class CrossEncoderReranker(Reranker):
    def __init__(self, cross_encoder: SentenceTransformerReranker, rerank_top_k: int = 100, **kwargs):
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
