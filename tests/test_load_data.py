from air_benchmark.evaluation_utils.data_loader import DataLoader
from air_benchmark.tasks import get_dataset_name_list, get_task_splits, LATEST_BENCHMARK_VERSION

def test_load_data(
    benchmark_version: str,
    task_type: str,
    domain: str,
    language: str
):
    success, dataset_name_list = get_dataset_name_list(
        benchmark_version=benchmark_version,
        task_type=task_type,
        domain=domain,
        language=language
    )
    
    if not success:
        print("No task found for the given configuration.")
        return

    data_loader = DataLoader(benchmark_version=benchmark_version)
    
    for dataset_name in dataset_name_list:
        corpus = data_loader.load_corpus(
            task_type=task_type,
            domain=domain,
            language=language,
            dataset_name=dataset_name
        )
        print(f"Load {len(corpus)} documents from {task_type}/{domain}/{language}/{dataset_name} dataset. Benchmark version: {benchmark_version}.")
        splits = get_task_splits(
            benchmark_version=benchmark_version,
            task_type=task_type,
            domain=domain,
            language=language,
            dataset_name=dataset_name
        )
        for split in splits:
            queries = data_loader.load_queries(
                task_type=task_type,
                domain=domain,
                language=language,
                dataset_name=dataset_name,
                split=split
            )
            print(f"Load {len(queries)} queries from {split} set in {task_type}/{domain}/{language}/{dataset_name} dataset. Benchmark version: {benchmark_version}.")


if __name__ == "__main__":
    benchmark_version = LATEST_BENCHMARK_VERSION
    task_type = "long-doc"
    domain = "book"
    language = "en"
    test_load_data(
        benchmark_version=benchmark_version,
        task_type=task_type,
        domain=domain,
        language=language
    )
