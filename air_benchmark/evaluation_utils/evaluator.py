import json
import logging
import os
from typing import Dict, List, Optional

from air_benchmark.evaluation_utils.data_loader import DataLoader
from air_benchmark.evaluation_utils.searcher import Retriever, Reranker

logger = logging.getLogger(__name__)


class Evaluator:
    def __init__(
        self,
        data_loader: DataLoader,
        overwrite: bool = False,
    ):
        self.data_loader = data_loader
        self.overwrite = overwrite
        self.benchmark_version = data_loader.benchmark_version

    def check_data_info(
        self,
        data_info: Dict[str, str],
        model_name: str,
        reranker_name: str,
        domain: str,
        language: str,
        task_name: str,
    ):
        if data_info["benchmark_version"] != self.benchmark_version:
            raise ValueError(
                f'benchmark_version mismatch: {data_info["benchmark_version"]} vs {self.benchmark_version}'
            )
        if (
            data_info["model_name"] != model_name
            or data_info["reranker_name"] != reranker_name
        ):
            raise ValueError(
                f'model_name or reranker_name mismatch: {data_info["model_name"]} vs {model_name} or {data_info["reranker_name"]} vs {reranker_name}'
            )
        if (
            data_info["domain"] != domain
            or data_info["language"] != language
            or data_info["task_name"] != task_name
        ):
            raise ValueError(
                f'domain or language or task_name mismatch: {data_info["domain"]} vs {domain} or {data_info["language"]} vs {language} or {data_info["task_name"]} vs {task_name}'
            )
    
    def __call__(
        self,
        task_type: str,
        domain: str,
        language: str,
        task_name: str,
        search_results_save_dir: str,
        retriever: Retriever,
        reranker: Optional[Reranker] = None,
        **kwargs,
    ):
        # Retrieval Stage
        no_reranker_search_results_save_dir = os.path.join(
            search_results_save_dir, str(retriever), "NoReranker", task_type
        )
        os.makedirs(no_reranker_search_results_save_dir, exist_ok=True)
        
        no_reranker_search_results_save_path = os.path.join(
            no_reranker_search_results_save_dir, domain, f"{language}_{task_name}.json"
        )

        if os.path.exists(no_reranker_search_results_save_path) and not self.overwrite:
            data_info, no_reranker_search_results = self.load_search_results(
                no_reranker_search_results_save_path
            )

            self.check_data_info(
                data_info, str(retriever), "NoReranker", domain, language, task_name
            )
        else:
            corpus, queries = self.data_loader.load_data(
                task_type=task_type,
                domain=domain,
                language=language,
                task_name=task_name,
            )

            no_reranker_search_results = retriever(
                corpus=corpus,
                queries=queries,
                language=language,  # for language-specific retrievers, such as BM25Retriever
                **kwargs,
            )
            self.save_search_results(
                model_name=str(retriever),
                reranker_name="NoReranker",
                search_results=no_reranker_search_results,
                output_path=no_reranker_search_results_save_path,
                task_type=task_type,
                domain=domain,
                language=language,
                task_name=task_name,
                benchmark_version=self.benchmark_version,
            )
        
        # Reranking Stage
        if reranker is not None:
            reranker_search_results_save_dir = os.path.join(
                search_results_save_dir, str(retriever), str(reranker), task_type
            )
            os.makedirs(reranker_search_results_save_dir, exist_ok=True)
            
            rerank_search_results_save_path = os.path.join(
                reranker_search_results_save_dir, domain, f"{language}_{task_name}.json"
            )
            
            if os.path.exists(rerank_search_results_save_path) and not self.overwrite:
                return
            
            corpus, queries = self.data_loader.load_data(
                task_type=task_type,
                domain=domain,
                language=language,
                task_name=task_name,
            )
            
            rerank_search_results = reranker(
                corpus=corpus,
                queries=queries,
                search_results=no_reranker_search_results,
                **kwargs,
            )
            
            self.save_search_results(
                model_name=str(retriever),
                reranker_name=str(reranker),
                search_results=rerank_search_results,
                output_path=rerank_search_results_save_path,
                task_type=task_type,
                domain=domain,
                language=language,
                task_name=task_name,
                benchmark_version=self.benchmark_version,
            )
    
    @staticmethod
    def save_search_results(
        model_name: str,
        reranker_name: str,
        search_results: Dict[str, Dict[str, float]],
        output_path: str,
        task_type: str,
        domain: str,
        language: str,
        task_name: str,
        benchmark_version: str,
    ):
        data = {
            "model_name": model_name,
            "reranker_name": reranker_name,
            "benchmark_version": benchmark_version,
            "task_type": task_type,
            "domain": domain,
            "language": language,
            "task_name": task_name,
            "search_results": search_results,
        }

        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    @staticmethod
    def load_search_results(input_path: str):
        with open(input_path, "r", encoding="utf-8") as f:
            data_info = json.load(f)

        search_results = data_info.pop("search_results")
        return data_info, search_results
