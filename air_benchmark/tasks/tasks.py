from itertools import chain
from typing import List, Optional, Tuple

from air_benchmark.tasks.long_doc_tasks import (
    LongDocArxivTask,
    LongDocBookTask,
    LongDocHealthcareTask,
    LongDocLawTask,
)
from air_benchmark.tasks.qa_tasks import (
    QAArxivTask,
    QAFinanceTask,
    QAHealthcareTask,
    QALawTask,
    QAMSMARCOTask,
    QANewsTask,
    QAWebTask,
    QAWikiTask,
)

LATEST_BENCHMARK_VERSION = "AIR-Bench_24.04"


QATaskTable = {
    "wiki": QAWikiTask,
    "web": QAWebTask,
    "healthcare": QAHealthcareTask,
    "law": QALawTask,
    "arxiv": QAArxivTask,
    "news": QANewsTask,
    "finance": QAFinanceTask,
    "msmarco": QAMSMARCOTask,
}


LongDocTaskTable = {
    "healthcare": LongDocHealthcareTask,
    "arxiv": LongDocArxivTask,
    "law": LongDocLawTask,
    "book": LongDocBookTask,
}


TaskTable = {
    "qa": QATaskTable,
    "long-doc": LongDocTaskTable,
}


BenchmarkTable = {
    "AIR-Bench_24.04": TaskTable,
}


def get_available_benchmark_versions() -> List[str]:
    return sorted(list(BenchmarkTable.keys()))


def get_available_task_types() -> List[str]:
    return sorted(list(TaskTable.keys()))


def get_available_domains() -> List[str]:
    return sorted(list(frozenset(chain(QATaskTable, LongDocTaskTable))))


def get_available_languages() -> List[str]:
    languages = set()
    for task in QATaskTable.values():
        for lang in task.keys():
            languages.add(lang)
    for task in LongDocTaskTable.values():
        for lang in task.keys():
            languages.add(lang)

    return sorted(list(languages))


def check_benchmark_version(benchmark_version: Optional[str]) -> str:
    if benchmark_version is None:
        benchmark_version = LATEST_BENCHMARK_VERSION
    else:
        available_benchmark_versions = get_available_benchmark_versions()

        if benchmark_version not in available_benchmark_versions:
            raise ValueError(
                f"Invalid benchmark version: {benchmark_version}. Available versions: {', '.join(available_benchmark_versions)}"
            )

    return benchmark_version


def check_task_types(task_types: Optional[List[str]]) -> List[str]:
    available_task_types = get_available_task_types()
    if task_types is None:
        task_types = available_task_types
    else:
        if isinstance(task_types, str):
            task_types = [task_types]
        task_types = list(set(task_types))
        task_types = [task_type.lower() for task_type in task_types]
        for task_type in task_types:
            if task_type not in available_task_types:
                raise ValueError(
                    f"Invalid task type: {task_type}. Available task types: {', '.join(available_task_types)}"
                )
    return task_types


def check_domains(domains: Optional[List[str]]) -> List[str]:
    available_domains = get_available_domains()
    if domains is None:
        domains = available_domains
    else:
        if isinstance(domains, str):
            domains = [domains]
        domains = list(set(domains))
        domains = [domain.lower() for domain in domains]
        for domain in domains:
            if domain not in available_domains:
                raise ValueError(
                    f"Invalid domain: {domain}. Available domains: {', '.join(available_domains)}"
                )
    return domains


def check_languages(languages: Optional[List[str]]) -> List[str]:
    available_languages = get_available_languages()
    if languages is None:
        languages = available_languages
    else:
        if isinstance(languages, str):
            languages = [languages]
        languages = list(set(languages))
        languages = [language.lower() for language in languages]
        for language in languages:
            if language not in available_languages:
                raise ValueError(
                    f"Invalid language: {language}. Available languages: {', '.join(available_languages)}"
                )
    return languages


def get_task_name_list(
    benchmark_version: str, task_type: str, domain: str, language: str
) -> Tuple[bool, str]:
    if benchmark_version not in BenchmarkTable:
        return False, None
    task_table = BenchmarkTable[benchmark_version]
    if task_type not in task_table:
        return False, None
    if domain not in task_table[task_type]:
        return False, None
    if language not in task_table[task_type][domain]:
        return False, None
    return True, list(task_table[task_type][domain][language].keys())
