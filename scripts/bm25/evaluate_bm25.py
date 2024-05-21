"""
# Run all tasks
python evaluate_bm25.py \
--output_dir ./search_results \
--bm25_tmp_dir ./bm25_tmp_dir \
--remove_bm25_tmp_dir True \
--overwrite False

# Run the tasks in the specified task type, domains, and languages
python evaluate_bm25.py \
--task_types qa \
--domains finance law \
--languages en \
--output_dir ./search_results \
--bm25_tmp_dir ./bm25_tmp_dir \
--remove_bm25_tmp_dir True \
--overwrite False
"""
from transformers import HfArgumentParser

from air_benchmark import EvalArgs, AIRBench

from utils.searcher import BM25Retriever
from utils.arguments import BM25Args


def main():
    parser = HfArgumentParser([BM25Args, EvalArgs])
    bm25_args, eval_args = parser.parse_args_into_dataclasses()
    bm25_args: BM25Args
    eval_args: EvalArgs
    
    evaluation = AIRBench(
        benchmark_version=eval_args.benchmark_version,
        task_types=eval_args.task_types,
        domains=eval_args.domains,
        languages=eval_args.languages,
        cache_dir=eval_args.cache_dir,
    )
    
    retriever = BM25Retriever(
        bm25_tmp_dir=bm25_args.bm25_tmp_dir,
        remove_bm25_tmp_dir=bm25_args.remove_bm25_tmp_dir,
        search_top_k=eval_args.search_top_k,
    )
    
    evaluation.run(
        retriever,
        output_dir=eval_args.output_dir,
        overwrite=eval_args.overwrite,
    )


if __name__ == "__main__":
    main()
