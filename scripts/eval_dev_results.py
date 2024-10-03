"""
python eval_dev_results.py \
--benchmark_version AIR-Bench_24.05 \
--search_results_save_dir ./hf-transformers/search_results \
--cache_dir ~/.cache \
--output_method markdown \
--output_path ./24.05_eval_dev_results.md \
--metrics ndcg_at_10 recall_at_10
"""
import argparse
from air_benchmark import AIRBench
from air_benchmark.tasks import LATEST_BENCHMARK_VERSION


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--benchmark_version", 
        type=str, default=LATEST_BENCHMARK_VERSION,
        help="The version of the benchmark to evaluate against. Default is the latest version."
    )
    parser.add_argument(
        "--search_results_save_dir",
        type=str, required=True, 
        help="The directory where the search results are saved."
    )
    parser.add_argument(
        "--cache_dir",
        type=str, default=None,
        help="The directory where the cache is stored."
    )
    parser.add_argument(
        "--output_method",
        type=str, default="markdown", choices=["markdown", "json"],
        help="The method to output the evaluation results. Default is markdown."
    )
    parser.add_argument(
        "--output_path",
        type=str, default="./eval_results.md", 
        help="The path to save the evaluation results. Default is ./eval_results.md."
    )
    parser.add_argument(
        "--metrics",
        type=str, default=["ndcg_at_10", "recall_at_10"],
        nargs="+"
    )
    return parser.parse_args()


def main():
    args = get_args()
    AIRBench.evaluate_dev(
        benchmark_version=args.benchmark_version,
        search_results_save_dir=args.search_results_save_dir,
        cache_dir=args.cache_dir,
        output_method=args.output_method,
        output_path=args.output_path,
        metrics=args.metrics if isinstance(args.metrics, list) else [args.metrics],
    )


if __name__ == "__main__":
    main()
