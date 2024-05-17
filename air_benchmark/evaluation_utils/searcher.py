import json
import logging
import os
from typing import Any, Dict

from mteb.evaluation.evaluators import RetrievalEvaluator

from air_benchmark.model_utils import DRESModel, DRESReranker

logger = logging.getLogger(__name__)


class Searcher:
    def __init__(self, search_top_k: int = 1000):
        self.search_top_k = search_top_k

    def dense_search(
        self,
        model,
        corpus: Dict[str, Dict[str, Any]],
        queries: Dict[str, str],
        score_function: str = "cos_sim",
        **kwargs,
    ):
        retriever = RetrievalEvaluator(
            retriever=model,
            k_values=[self.search_top_k],
            score_function=score_function,
            **kwargs,
        )
        search_results = retriever(corpus=corpus, queries=queries)
        return search_results

    def rerank(
        self,
        reranker,
        search_results: Dict[str, Dict[str, float]],
        corpus: Dict[str, Dict[str, Any]],
        queries: Dict[str, str],
        rerank_top_k: int = 100,
    ):
        # truncate search results to top_k
        for qid in search_results:
            search_results[qid] = dict(
                sorted(search_results[qid].items(), key=lambda x: x[1], reverse=True)[
                    :rerank_top_k
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
        scores = reranker.compute_score(pairs)
        for i, score in enumerate(scores):
            sentence_pairs[i]["score"] = float(score)
        # rerank
        reranked_results = {qid: {} for qid in search_results}
        for pair in sentence_pairs:
            reranked_results[pair["qid"]][pair["docid"]] = pair["score"]
        return reranked_results

    def _bm25_save_corpus(
        self, corpus: Dict[str, Dict[str, Any]], corpus_save_dir: str
    ):
        os.makedirs(corpus_save_dir, exist_ok=True)

        corpus_list = [
            {"id": docid, "contents": corpus[docid]["text"]} for docid in corpus
        ]

        coprus_save_path = os.path.join(corpus_save_dir, "corpus.jsonl")
        with open(coprus_save_path, "w", encoding="utf-8") as f:
            for data in corpus_list:
                f.write(json.dumps(data, ensure_ascii=False) + "\n")

    def _bm25_build_index(
        self, corpus_save_dir: str, index_save_dir: str, language: str
    ):
        os.makedirs(index_save_dir, exist_ok=True)

        if "zh_" in language:
            language = "zh"
        cmd = f"python -m pyserini.index.lucene \
                --language {language} \
                --collection JsonCollection \
                --input {corpus_save_dir} \
                --index {index_save_dir} \
                --generator DefaultLuceneDocumentGenerator \
                --threads 1 --optimize \
            "
        os.system(cmd)

    def _bm25_save_queries(self, queries: Dict[str, str], queries_save_path: str):
        queries_list = [
            {"id": qid, "content": queries[qid].replace("\n", " ").replace("\t", " ")}
            for qid in queries
        ]
        with open(queries_save_path, "w", encoding="utf-8") as f:
            for query in queries_list:
                assert "\n" not in query["id"] and "\t" not in query["id"]
                line = f"{query['id']}\t{query['content']}"
                f.write(line + "\n")

    def _bm25_search(
        self,
        language: str,
        index_save_dir: str,
        queries_save_path: str,
        search_results_save_path: str,
        top_k: int = 1000,
    ):
        if "zh_" in language:
            language = "zh"
        cmd = f"python -m pyserini.search.lucene \
                --language {language} \
                --index {index_save_dir} \
                --topics {queries_save_path} \
                --output {search_results_save_path} \
                --bm25 \
                --hits {top_k} \
                --batch-size 128 \
                --threads 16 \
            "
        os.system(cmd)

    def _bm25_load_search_results(self, search_results_save_path: str, top_k: int):
        search_results = {}
        with open(search_results_save_path, "r", encoding="utf-8") as f:
            for line in f:
                qid, _, docid, rank, score, _ = line.strip().split(" ")
                if qid not in search_results:
                    search_results[qid] = {}

                if int(rank) <= top_k:
                    search_results[qid][docid] = float(score)
        return search_results

    def bm25_search(
        self,
        bm25_tmp_dir: str,
        corpus: Dict[str, Dict[str, Any]],
        queries: Dict[str, str],
        language: str,
        remove_bm25_tmp_dir: bool = False,
        **kwargs,
    ):
        corpus_save_dir = os.path.join(bm25_tmp_dir, "corpus")
        index_save_dir = os.path.join(bm25_tmp_dir, "index")
        queries_save_path = os.path.join(bm25_tmp_dir, f"{language}.tsv")

        self._bm25_save_corpus(corpus, corpus_save_dir)
        self._bm25_build_index(corpus_save_dir, index_save_dir, language)
        self._bm25_save_queries(queries, queries_save_path)

        search_results_save_path = os.path.join(bm25_tmp_dir, "bm25_search_results.txt")
        self._bm25_search(
            language,
            index_save_dir,
            queries_save_path,
            search_results_save_path,
            self.search_top_k,
        )

        search_results = self._bm25_load_search_results(
            search_results_save_path, self.search_top_k
        )

        if remove_bm25_tmp_dir:
            os.system(f"rm -rf {bm25_tmp_dir}")

        return search_results
