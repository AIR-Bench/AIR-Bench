import logging
from typing import List

from air_bench.console import console, style_head, style_row
from air_bench.evaluation_utils import DataLoader, Evaluator, Searcher
from air_bench.model_utils import FlagDRESModel, FlagDRESReranker
from air_bench.tasks.tasks import (BenchmarkTable, check_benchmark_version,
                                   check_domains, check_languages,
                                   check_task_types, get_task_name_list)

logger = logging.getLogger(__name__)


class AIRBench:
    def __init__(
        self,
        benchmark_version: str | None = None,
        task_types: List[str] | None = None,
        domains: List[str] | None = None,
        languages: List[str] | None = None,
        cache_dir: str | None = None,
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
            print(
                f"==================== Benchmark Version: {benchmark_version} ===================="
            )
            for task_type in BenchmarkTable[benchmark_version]:
                print(
                    f"  ******************* Task Type: {task_type} *******************"
                )
                for domain in BenchmarkTable[benchmark_version][task_type]:
                    print(
                        f"    +++++++++++++++++++ Domain: {domain} +++++++++++++++++++"
                    )
                    for language in BenchmarkTable[benchmark_version][task_type][
                        domain
                    ]:
                        print(
                            f"      ------------------- Language: {language} -------------------"
                        )
                        for task_name in BenchmarkTable[benchmark_version][task_type][
                            domain
                        ][language]:
                            print(f"        Task Name: {task_name}")
                            print(
                                f"        Source: {BenchmarkTable[benchmark_version][task_type][domain][language][task_name]['source']}"
                            )

    @staticmethod
    def check_encoder(encoder):
        for method in ["__str__", "encode_queries", "encode_corpus"]:
            if not hasattr(encoder, method) or not callable(
                getattr(encoder, method, None)
            ):
                raise ValueError(f"Encoder should have `{method}` method.")

    @staticmethod
    def check_reranker(reranker):
        for method in ["__str__", "compute_score"]:
            if not hasattr(reranker, method) or not callable(
                getattr(reranker, method, None)
            ):
                raise ValueError(f"Reranker should have `{method}` method.")

    def run(
        self,
        encoder: FlagDRESModel,
        output_dir: str = "search_results",
        search_top_k: int = 1000,
        reranker_list: List[FlagDRESReranker] | None = None,
        rerank_top_k: int = 100,
        overwrite: bool = False,
        **kwargs,
    ):
        self.check_encoder(encoder)
        if reranker_list is not None:
            for reranker in reranker_list:
                self.check_reranker(reranker)

        searcher = Searcher(search_top_k)
        evaluator = Evaluator(
            self.data_loader,
            searcher,
            rerank_top_k=rerank_top_k,
            k_values=[search_top_k],
            overwrite=overwrite,
        )

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

                        evaluator.generate_search_results(
                            model=encoder,
                            reranker_list=reranker_list,
                            search_results_save_dir=output_dir,
                            task_type=task_type,
                            domain=domain,
                            language=language,
                            task_name=task_name,
                            **kwargs,
                        )
        console.rule("[bold red]Evaluation Summary")
        console.print(f"Encoder: {encoder}", style=style_row, justify="center")
        reranker_names = [item.name for item in reranker_list]
        console.print(
            f"Rerankers: {*reranker_names,}", style=style_row, justify="center"
        )
        console.print(
            f"Output directory: {output_dir}", style=style_row, justify="center"
        )
        console.print(
            f"Search Top K: {search_top_k}", style=style_row, justify="center"
        )
        console.print(
            f"Rerank Top K: {rerank_top_k}", style=style_row, justify="center"
        )
