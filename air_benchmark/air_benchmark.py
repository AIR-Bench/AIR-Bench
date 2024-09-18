import os
import logging
from typing import List, Optional, Union

from air_benchmark.console import console, style_head, style_row
from air_benchmark.evaluation_utils.data_loader import DataLoader
from air_benchmark.evaluation_utils.evaluator import Evaluator
from air_benchmark.evaluation_utils.searcher import Retriever, Reranker
from air_benchmark.tasks.tasks import (
    BenchmarkTable,
    check_benchmark_version,
    check_task_types,
    check_domains,
    check_languages,
    check_splits,
    get_dataset_name_list,
    get_task_splits,
)

logger = logging.getLogger(__name__)


class AIRBench:
    def __init__(
        self,
        benchmark_version: Optional[str] = None,
        task_types: Optional[List[str]] = None,
        domains: Optional[List[str]] = None,
        languages: Optional[List[str]] = None,
        splits: Optional[List[str]] = None,
        cache_dir: Optional[str] = None,
    ):
        self.benchmark_version = check_benchmark_version(benchmark_version)
        self.task_types = check_task_types(task_types, self.benchmark_version)
        self.domains = check_domains(domains, self.benchmark_version)
        self.languages = check_languages(languages, self.benchmark_version)
        self.splits = check_splits(splits, self.benchmark_version)
        self.cache_dir = cache_dir

        self.data_loader = DataLoader(self.benchmark_version, cache_dir=self.cache_dir)

    @staticmethod
    def print_benchmark_table():
        for benchmark_version in BenchmarkTable:

            console.print(
                f"Benchmark Dataset Version: {benchmark_version}",
                style=style_head,
                justify="center",
            )

            for task_type in BenchmarkTable[benchmark_version]:
                console.print(
                    f"Task Type: {task_type}", style=style_head, justify="center"
                )
                for domain in BenchmarkTable[benchmark_version][task_type]:
                    console.print(
                        f"Domain: {domain}", style=style_head, justify="center"
                    )
                    for language in BenchmarkTable[benchmark_version][task_type][
                        domain
                    ]:
                        console.print(
                            f"Language: {language}", style=style_head, justify="center"
                        )
                        for dataset_name in BenchmarkTable[benchmark_version][task_type][
                            domain
                        ][language]:
                            console.print(
                                f"Dataset Name: {dataset_name}",
                                style=style_row,
                                justify="center",
                            )
                            console.print(
                                f"Source: {BenchmarkTable[benchmark_version][task_type][domain][language][dataset_name]['source']}",
                                style=style_row,
                                justify="center",
                            )
                            console.print(
                                f"Splits: {BenchmarkTable[benchmark_version][task_type][domain][language][dataset_name]['splits']}",
                                style=style_row,
                                justify="center",
                            )

    @staticmethod
    def check_retriever(retriever):
        for method in ["__str__", "__call__"]:
            if not hasattr(retriever, method) or not callable(
                getattr(retriever, method, None)
            ):
                raise ValueError(f"Retriever should have `{method}` method.")

    @staticmethod
    def check_reranker(reranker):
        for method in ["__str__", "__call__"]:
            if not hasattr(reranker, method) or not callable(
                getattr(reranker, method, None)
            ):
                raise ValueError(f"Reranker should have `{method}` method.")

    def run(
        self,
        retriever: Retriever,
        reranker: Optional[Reranker] = None,
        output_dir: str = "./search_results",
        overwrite: bool = False,
        **kwargs,
    ):
        console.print(f"Benchmark Dataset Version: {self.benchmark_version}", style=style_head, justify="center")
        
        evaluator = Evaluator(self.data_loader, overwrite=overwrite)
        
        for task_type in self.task_types:
            for domain in self.domains:
                for language in self.languages:
                    success, dataset_name_list = get_dataset_name_list(
                        self.benchmark_version, task_type, domain, language
                    )
                    if not success:
                        logger.info(
                            f"No task found for {task_type} in {domain} domain with {language} language, Benchmark version: {self.benchmark_version}. Skipping..."
                        )
                        continue
                    
                    for dataset_name in dataset_name_list:
                        task_splits = get_task_splits(
                            self.benchmark_version, task_type, domain, language, dataset_name
                        )
                        splits = [split for split in self.splits if split in task_splits]
                        if splits == []:
                            logger.info(
                                f"Not found {self.splits} splits for {task_type}/{domain}/{language}/{dataset_name} dataset, Benchmark version: {self.benchmark_version}. Skipping..."
                            )
                            continue
                        
                        console.print(
                            f"Task Type: {task_type} | Domain: {domain} | Language: {language} | Dataset Name: {dataset_name} | Splits: {splits}",
                            style=style_head,
                            justify="center",
                        )
                        
                        evaluator(
                            task_type=task_type,
                            domain=domain,
                            language=language,
                            dataset_name=dataset_name,
                            splits=splits,
                            search_results_save_dir=output_dir,
                            retriever=retriever,
                            reranker=reranker,
                            **kwargs,
                        )
        console.rule("[bold red]Evaluation Summary")
        console.print(f"Retriever: {retriever}", style=style_row, justify="center")
        console.print(
            f"Search Top K: {retriever.search_top_k}", style=style_row, justify="center"
        )
        if reranker is not None:
            console.print(f"Reranker: {reranker}", style=style_row, justify="center")
            console.print(
                f"Rerank Top K: {reranker.rerank_top_k}", style=style_row, justify="center"
            )
        console.print(
            f"Output directory: {output_dir}", style=style_row, justify="center"
        )

    @staticmethod
    def evaluate_dev(
        benchmark_version: str,
        search_results_save_dir: str,
        k_values: List[int] = [1, 3, 5, 10, 50, 100, 1000],
        cache_dir: Optional[str] = None,
        output_method: str = "markdown",
        output_path: str = "./eval_dev_results.md",
        metrics: Union[List[str], str] = ["ndcg_at_10", "recall_at_10"],
    ):
        data_loader = DataLoader(benchmark_version, cache_dir=cache_dir)
        evaluator = Evaluator(data_loader)
        
        eval_results_dict = {}
        for model_name in sorted(os.listdir(search_results_save_dir)):
            model_search_results_save_dir = os.path.join(search_results_save_dir, model_name)
            if not os.path.isdir(model_search_results_save_dir):
                continue
            for reranker_name in sorted(os.listdir(model_search_results_save_dir)):
                reranker_search_results_save_dir = os.path.join(model_search_results_save_dir, reranker_name)
                if not os.path.isdir(reranker_search_results_save_dir):
                    continue
                eval_results = evaluator.evaluate_results(
                    reranker_search_results_save_dir,
                    k_values=k_values,
                    split="dev",
                )
                if model_name not in eval_results_dict:
                    eval_results_dict[model_name] = {}
                eval_results_dict[model_name][reranker_name] = eval_results
        
        if output_method == "json":
            Evaluator.output_eval_results_to_json(eval_results_dict, output_path)
        elif output_method == "markdown":
            Evaluator.output_eval_results_to_markdown(eval_results_dict, output_path, metrics=metrics)
        else:
            raise ValueError(f"Invalid output method: {output_method}. Available methods: ['json', 'markdown']")
