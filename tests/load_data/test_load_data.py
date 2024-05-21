from air_benchmark.evaluation_utils.data_loader import DataLoader
from air_benchmark.tasks.tasks import get_task_name_list, LATEST_BENCHMARK_VERSION

def test_load_data():
    benchmark_version = LATEST_BENCHMARK_VERSION
    task_type = "long-doc"
    domain = "book"
    language = "en"
    _, task_name_list = get_task_name_list(
        benchmark_version=benchmark_version,
        task_type=task_type,
        domain=domain,
        language=language
    )

    data_loader = DataLoader(benchmark_version=LATEST_BENCHMARK_VERSION)
    
    for task_name in task_name_list:
        corpus, queries = data_loader.load_data(
            task_type=task_type,
            domain=domain,
            language=language,
            task_name=task_name
        )
        print("task_name:", task_name)


if __name__ == "__main__":
    test_load_data()
