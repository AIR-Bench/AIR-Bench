from typing import List, Tuple

from air_benchmark.tasks.long_doc_tasks import (LongDocArxivTask,
                                                LongDocBookTask,
                                                LongDocHealthcareTask,
                                                LongDocLawTask)
from air_benchmark.tasks.qa_tasks import (QAArxivTask, QAFinanceTask,
                                          QAHealthcareTask, QALawTask,
                                          QAMSMARCOTask, QANewsTask, QAWebTask,
                                          QAWikiTask)

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


def get_avaliable_benchmark_versions() -> List[str]:
    return sorted(list(BenchmarkTable.keys()))


def get_avaliable_task_types() -> List[str]:
    return sorted(list(TaskTable.keys()))


def get_available_domains() -> List[str]:
    return sorted(list(QATaskTable.keys() | LongDocTaskTable.keys()))


def get_avaliable_languages() -> List[str]:
    languages = set()
    for task in QATaskTable.values():
        for lang in task.keys():
            languages.add(lang)
    for task in LongDocTaskTable.values():
        for lang in task.keys():
            languages.add(lang)

    return sorted(list(languages))


def check_benchmark_version(benchmark_version: str | None) -> str:
    if benchmark_version is None:
        benchmark_version = LATEST_BENCHMARK_VERSION
    else:
        avaliable_benchmark_versions = get_avaliable_benchmark_versions()

        if benchmark_version not in avaliable_benchmark_versions:
            raise ValueError(
                f"Invalid benchmark version: {benchmark_version}. Avaliable versions: {', '.join(avaliable_benchmark_versions)}"
            )

    return benchmark_version


def check_task_types(task_types: List[str] | None) -> List[str]:
    avaliable_task_types = get_avaliable_task_types()
    if task_types is None:
        task_types = avaliable_task_types
    else:
        task_types = list(set(task_types))
        task_types = [task_type.lower() for task_type in task_types]
        for task_type in task_types:
            if task_type not in avaliable_task_types:
                raise ValueError(
                    f"Invalid task type: {task_type}. Avaliable task types: {', '.join(avaliable_task_types)}"
                )
    return task_types


def check_domains(domains: List[str] | None) -> List[str]:
    avaliable_domains = get_available_domains()
    if domains is None:
        domains = avaliable_domains
    else:
        domains = list(set(domains))
        domains = [domain.lower() for domain in domains]
        for domain in domains:
            if domain not in avaliable_domains:
                raise ValueError(
                    f"Invalid domain: {domain}. Avaliable domains: {', '.join(avaliable_domains)}"
                )
    return domains


def check_languages(languages: List[str] | None) -> List[str]:
    avaliable_languages = get_avaliable_languages()
    if languages is None:
        languages = avaliable_languages
    else:
        languages = list(set(languages))
        languages = [language.lower() for language in languages]
        for language in languages:
            if language not in avaliable_languages:
                raise ValueError(
                    f"Invalid language: {language}. Avaliable languages: {', '.join(avaliable_languages)}"
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
