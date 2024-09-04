import json
import os
import shutil
import random
from typing import Dict, Any

from air_benchmark import Retriever


class BM25Retriever(Retriever):
    def __init__(
        self,
        bm25_tmp_dir: str,
        remove_bm25_tmp_dir: bool = False,
        search_top_k: int = 1000,
    ):
        super().__init__(search_top_k)
        self.bm25_tmp_dir = bm25_tmp_dir
        self.remove_bm25_tmp_dir = remove_bm25_tmp_dir
    
    def __str__(self):
        return "BM25"
    
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
                assert "\n" not in query["content"] and "\t" not in query["content"]
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

    def _fill_empty_search_results(
        self,
        search_results: Dict[str, Dict[str, float]],
        queries: Dict[str, str],
        corpus: Dict[str, Dict[str, Any]],
    ):
        """Randomly fill empty search results with 0.0 score."""
        random.seed(42)
        random_docid = random.sample(list(corpus.keys()), min(self.search_top_k, len(corpus)))
        count = 0
        for qid in queries:
            if qid not in search_results:
                count += 1
                search_results[qid] = {
                    docid: 0.0
                    for docid in random_docid
                }
        print(f"Warning: {count} queries have empty search results.")
        return search_results

    def __call__(
        self,
        corpus: Dict[str, Dict[str, Any]],
        queries: Dict[str, str],
        language: str,
        **kwargs,
    ):
        corpus_save_dir = os.path.join(self.bm25_tmp_dir, "corpus")
        index_save_dir = os.path.join(self.bm25_tmp_dir, "index")
        queries_save_path = os.path.join(self.bm25_tmp_dir, f"{language}.tsv")

        self._bm25_save_corpus(corpus, corpus_save_dir)
        self._bm25_build_index(corpus_save_dir, index_save_dir, language)
        self._bm25_save_queries(queries, queries_save_path)

        search_results_save_path = os.path.join(self.bm25_tmp_dir, "bm25_search_results.txt")
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

        # Top-k retrieval from bm25 maybe empty: https://github.com/castorini/pyserini/discussions/1252
        search_results = self._fill_empty_search_results(search_results, queries, corpus)

        if self.remove_bm25_tmp_dir:
            shutil.rmtree(self.bm25_tmp_dir)

        return search_results
