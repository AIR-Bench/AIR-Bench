import logging
from typing import List, Optional

from air_benchmark.console import console, style_head, style_row
from air_benchmark.evaluation_utils.data_loader import DataLoader
from air_benchmark.evaluation_utils.evaluator import Evaluator
from air_benchmark.evaluation_utils.searcher import Retriever, Reranker
from air_benchmark.tasks.tasks import (
    BenchmarkTable,
    check_benchmark_version,
    check_domains,
    check_languages,
    check_task_types,
    get_task_name_list,
)

logger = logging.getLogger(__name__)


class AIRBench:
    def __init__(
        self,
        benchmark_version: Optional[str] = None,
        task_types: Optional[List[str]] = None,
        domains: Optional[List[str]] = None,
        languages: Optional[List[str]] = None,
        cache_dir: Optional[str] = None,
    ):
        self.benchmark_version = check_benchmark_version(benchmark_version)
        self.task_types = check_task_types(task_types)
        self.domains = check_domains(domains)
        self.languages = check_languages(languages)
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
                        for task_name in BenchmarkTable[benchmark_version][task_type][
                            domain
                        ][language]:
                            console.print(
                                f"Task Name: {task_name}",
                                style=style_row,
                                justify="center",
                            )
                            console.print(
                                f"Source: {BenchmarkTable[benchmark_version][task_type][domain][language][task_name]['source']}",
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
        evaluator = Evaluator(self.data_loader, overwrite=overwrite)
        
        for task_type in self.task_types:
            console.print(f"Task Type: {task_type}", style=style_head, justify="center")
            for domain in self.domains:
                console.print(f"Domain: {domain}", style=style_head, justify="center")
                for language in self.languages:
                    success, task_name_list = get_task_name_list(
                        self.benchmark_version, task_type, domain, language
                    )

                    if not success:
                        logger.info(
                            f"No task found for {task_type} in {domain} domain with {language} language, Benchmark version: {self.benchmark_version}. Skipping..."
                        )
                        continue

                    console.print(
                        f"Language: {language}", style=style_head, justify="center"
                    )

                    for task_name in task_name_list:
                        console.print(
                            f"Task Name: {task_name}",
                            style=style_head,
                            justify="center",
                        )
                        
                        evaluator(
                            task_type=task_type,
                            domain=domain,
                            language=language,
                            task_name=task_name,
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
