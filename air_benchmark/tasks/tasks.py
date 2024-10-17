from typing import List, Optional, Tuple
from air_benchmark.tasks.v24_04.tasks import TaskTable as TaskTable_v24_04
from air_benchmark.tasks.v24_05.tasks import TaskTable as TaskTable_v24_05

LATEST_BENCHMARK_VERSION = "AIR-Bench_24.05"


BenchmarkTable = {
    "AIR-Bench_24.05": TaskTable_v24_05,
    "AIR-Bench_24.04": TaskTable_v24_04,
}


def get_available_benchmark_versions() -> List[str]:
    return sorted(list(BenchmarkTable.keys()))


def get_available_task_types(benchmark_version: str = LATEST_BENCHMARK_VERSION) -> List[str]:
    task_table = BenchmarkTable[benchmark_version]
    return sorted(list(task_table.keys()))


def get_available_domains(benchmark_version: str = LATEST_BENCHMARK_VERSION) -> List[str]:
    domains = set()
    for task_table in BenchmarkTable[benchmark_version].values():
        for domain in task_table.keys():
            domains.add(domain)
    return sorted(list(domains))


def get_available_languages(benchmark_version: str = LATEST_BENCHMARK_VERSION) -> List[str]:
    languages = set()
    for task_table in BenchmarkTable[benchmark_version].values():
        for task in task_table.values():
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


def check_task_types(
    task_types: Optional[List[str]],
    benchmark_version: str = LATEST_BENCHMARK_VERSION,
) -> List[str]:
    available_task_types = get_available_task_types(benchmark_version)
    if task_types is None:
        task_types = available_task_types
    else:
        if isinstance(task_types, str):
            task_types = [task_types]
        task_types = sorted(list(set(task_types)))
        task_types = [task_type.lower() for task_type in task_types]
        for task_type in task_types:
            if task_type not in available_task_types:
                raise ValueError(
                    f"{benchmark_version} | Invalid task type: {task_type}. Available task types: {', '.join(available_task_types)}"
                )
    return task_types


def check_domains(
    domains: Optional[List[str]],
    benchmark_version: str = LATEST_BENCHMARK_VERSION,
) -> List[str]:
    available_domains = get_available_domains(benchmark_version)
    if domains is None:
        domains = available_domains
    else:
        if isinstance(domains, str):
            domains = [domains]
        domains = sorted(list(set(domains)))
        domains = [domain.lower() for domain in domains]
        for domain in domains:
            if domain not in available_domains:
                raise ValueError(
                    f"{benchmark_version} | Invalid domain: {domain}. Available domains: {', '.join(available_domains)}"
                )
    return domains


def check_languages(
    languages: Optional[List[str]],
    benchmark_version: str = LATEST_BENCHMARK_VERSION,
) -> List[str]:
    available_languages = get_available_languages(benchmark_version)
    if languages is None:
        languages = available_languages
    else:
        if isinstance(languages, str):
            languages = [languages]
        languages = sorted(list(set(languages)))
        languages = [language.lower() for language in languages]
        for language in languages:
            if language not in available_languages:
                raise ValueError(
                    f"{benchmark_version} | Invalid language: {language}. Available languages: {', '.join(available_languages)}"
                )
    return languages


def check_splits(
    splits: Optional[List[str]],
    benchmark_version: str = LATEST_BENCHMARK_VERSION,
) -> List[str]:
    if benchmark_version == "AIR-Bench_24.04":
        available_splits = ["test"]
    else:
        available_splits = ["dev", "test"]
    if splits is None:
        splits = available_splits
    else:
        if isinstance(splits, str):
            splits = [splits]
        splits = sorted(list(set(splits)))
        splits = [split.lower() for split in splits]
    for split in splits:
        if split not in available_splits:
            raise ValueError(f"{benchmark_version} | Invalid split: {split}. Available splits: {', '.join(available_splits)}")
    return splits


def get_dataset_name_list(
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


def get_task_splits(
    benchmark_version: str, task_type: str, domain: str, language: str, dataset_name: str
) -> List[str]:
    if benchmark_version not in BenchmarkTable:
        return []
    task_table = BenchmarkTable[benchmark_version]
    if task_type not in task_table:
        return []
    if domain not in task_table[task_type]:
        return []
    if language not in task_table[task_type][domain]:
        return []
    if dataset_name not in task_table[task_type][domain][language]:
        return []
    return task_table[task_type][domain][language][dataset_name]['splits']
