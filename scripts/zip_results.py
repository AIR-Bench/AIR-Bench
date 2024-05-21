"""
# Zip "Retrieval Model + NoReranker" search results in <search_results>/<retriever_name>/NoReranker to <save_dir>/<retriever_name>_NoReranker.zip.
python zip_results.py \
--results_dir search_results \
--retriever_name bge-m3 \
--save_dir search_results/zipped_results

# Zip "Retrieval Model + Reranker" search results in <search_results>/<retriever_name>/<reranker_name> to <save_dir>/<retriever_name>_<reranker_name>.zip.
python zip_results.py \
--results_dir search_results \
--retriever_name bge-m3 \
--reranker_name bge-reranker-v2-m3 \
--save_dir search_results/zipped_results
"""

import argparse
import os
import zipfile

from air_benchmark.tasks.tasks import check_domains, check_task_types


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--results_dir",
        type=str,
        required=True,
        help="Path to the search results directory",
    )
    parser.add_argument(
        "--retriever_name", type=str, required=True, help="Model name used for the search"
    )
    parser.add_argument(
        "--reranker_name",
        type=str,
        default="NoReranker",
        help="Reranker name used for the search. Default: NoReranker",
    )
    parser.add_argument(
        "--save_dir",
        type=str,
        required=True,
        help="Path to the directory to save the zipped search results",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite the existing zipped file if it exists",
    )
    return parser.parse_args()


def check_results_path(results_path: str):
    if not os.path.exists(results_path):
        raise FileNotFoundError(f"Search results in {results_path} does not exist.")
    for task_type in os.listdir(results_path):
        check_task_types([task_type])
        task_type_dir = os.path.join(results_path, task_type)
        for domain in os.listdir(task_type_dir):
            check_domains([domain])


def zip_results(
    results_dir: str,
    save_dir: str,
    retriever_name: str,
    reranker_name: str = "NoReranker",
    overwrite: bool = False,
):
    results_path = os.path.join(results_dir, retriever_name, reranker_name)
    try:
        check_results_path(results_path)
    except Exception as e:
        print(f"Invalid file structure in {results_path}: {e}\n")
        return False

    os.makedirs(save_dir, exist_ok=True)
    zip_filename = os.path.join(save_dir, f"{retriever_name}_{reranker_name}.zip")
    if os.path.exists(zip_filename) and not overwrite:
        print(f"Zipped file {zip_filename} already exists.\n")
        return False

    try:
        print("Zipping search results...")
        with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
            for root, _, files in os.walk(results_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    zipf.write(file_path, os.path.relpath(file_path, results_path))
    except Exception as e:
        print(f"Failed to zip search results in {results_path}: {e}\n")
        return False

    print(f"Zip search results in {results_path} to {zip_filename}.\n")
    return True


def main():
    args = get_args()

    print("=========================================")
    success = zip_results(
        args.results_dir,
        args.save_dir,
        args.retriever_name,
        reranker_name=args.reranker_name,
        overwrite=args.overwrite,
    )
    print("=========================================")
    if success:
        print(
            "Success! Now you can upload the zipped search results to https://huggingface.co/spaces/AIR-Bench/leaderboard !"
        )
    else:
        print("Failed! Please check the error message and try again!")


if __name__ == "__main__":
    main()
