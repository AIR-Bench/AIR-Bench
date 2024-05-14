"""
# Run all tasks
python run_air_benchmark.py \
--output_dir ./search_results \
--encoder BAAI/bge-m3 \
--reranker BAAI/bge-reranker-v2-m3 \
--search_top_k 1000 \
--rerank_top_k 100 \
--max_query_length 512 \
--max_passage_length 512 \
--batch_size 512 \
--pooling_method cls \
--normalize_embeddings True \
--use_fp16 True \
--add_instruction False \
--overwrite False

# Run the tasks in the specified task type
python run_air_benchmark.py \
--task_types long-doc \
--output_dir ./search_results \
--encoder BAAI/bge-m3 \
--reranker BAAI/bge-reranker-v2-m3 \
--search_top_k 1000 \
--rerank_top_k 100 \
--max_query_length 512 \
--max_passage_length 512 \
--batch_size 512 \
--pooling_method cls \
--normalize_embeddings True \
--use_fp16 True \
--add_instruction False \
--overwrite False

# Run the tasks in the specified task type and domains
python run_air_benchmark.py \
--task_types long-doc \
--domains arxiv book \
--output_dir ./search_results \
--encoder BAAI/bge-m3 \
--reranker BAAI/bge-reranker-v2-m3 \
--search_top_k 1000 \
--rerank_top_k 100 \
--max_query_length 512 \
--max_passage_length 512 \
--batch_size 512 \
--pooling_method cls \
--normalize_embeddings True \
--use_fp16 True \
--add_instruction False \
--overwrite False

# Run the tasks in the specified languages
python run_air_benchmark.py \
--languages en \
--output_dir ./search_results \
--encoder BAAI/bge-m3 \
--reranker BAAI/bge-reranker-v2-m3 \
--search_top_k 1000 \
--rerank_top_k 100 \
--max_query_length 512 \
--max_passage_length 512 \
--batch_size 512 \
--pooling_method cls \
--normalize_embeddings True \
--use_fp16 True \
--add_instruction False \
--overwrite False

# Run the tasks in the specified task type, domains, and languages
python run_air_benchmark.py \
--task_types qa \
--domains wiki web \
--languages en \
--output_dir ./search_results \
--encoder BAAI/bge-m3 \
--reranker BAAI/bge-reranker-v2-m3 \
--search_top_k 1000 \
--rerank_top_k 100 \
--max_query_length 512 \
--max_passage_length 512 \
--batch_size 512 \
--pooling_method cls \
--normalize_embeddings True \
--use_fp16 True \
--add_instruction False \
--overwrite False
"""

import logging

from transformers import HfArgumentParser

from air_benchmark.air_benchmark import AIRBench
from air_benchmark.evaluation_utils.evaluation_arguments import EvalArgs
from air_benchmark.model_utils.flag_dres_model import (FlagDRESModel,
                                                       FlagDRESReranker)
from air_benchmark.model_utils.model_arguments import ModelArgs

logger = logging.getLogger(__name__)


def get_models(model_args: ModelArgs):
    if model_args.encoder.lower() == "bm25":
        return "BM25", []
    encoder = FlagDRESModel(
        model_name_or_path=model_args.encoder,
        pooling_method=model_args.pooling_method,
        normalize_embeddings=model_args.normalize_embeddings,
        use_fp16=model_args.use_fp16,
        query_instruction_for_retrieval=(
            model_args.query_instruction_for_retrieval
            if model_args.add_instruction
            else None
        ),
        passage_instruction_for_retrieval=(
            model_args.passage_instruction_for_retrieval
            if model_args.add_instruction
            else None
        ),
        max_query_length=model_args.max_query_length,
        max_passage_length=model_args.max_passage_length,
        batch_size=model_args.batch_size,
        corpus_batch_size=model_args.corpus_batch_size,
    )
    reranker_list = []
    if model_args.reranker is not None:
        for i in range(len(model_args.reranker)):
            reranker = model_args.reranker[i]
        for reranker in model_args.reranker:
            if reranker is None or reranker.lower() == "none" or reranker == "":
                continue
            reranker_list.append(
                FlagDRESReranker(
                    model_name_or_path=reranker,
                    use_fp16=model_args.use_fp16,
                    query_instruction_for_retrieval=(
                        model_args.query_instruction_for_retrieval
                        if model_args.add_instruction
                        else None
                    ),
                    passage_instruction_for_retrieval=(
                        model_args.passage_instruction_for_retrieval
                        if model_args.add_instruction
                        else None
                    ),
                    max_length=max(
                        model_args.max_query_length, model_args.max_passage_length
                    ),
                    batch_size=model_args.batch_size,
                )
            )
    return encoder, reranker_list


def main():
    parser = HfArgumentParser([ModelArgs, EvalArgs])
    model_args, eval_args = parser.parse_args_into_dataclasses()
    model_args: ModelArgs
    eval_args: EvalArgs

    encoder, reranker_list = get_models(model_args)

    evaluation = AIRBench(
        benchmark_version=eval_args.benchmark_version,
        task_types=eval_args.task_types,
        domains=eval_args.domains,
        languages=eval_args.languages,
        cache_dir=eval_args.cache_dir,
    )

    evaluation.run(
        encoder,
        output_dir=eval_args.output_dir,
        search_top_k=eval_args.search_top_k,
        reranker_list=reranker_list,
        rerank_top_k=eval_args.rerank_top_k,
        overwrite=eval_args.overwrite,
        corpus_chunk_size=10000000,  # 10M chunk size when encoding the corpus to avoid multiple tqdm bars
    )


if __name__ == "__main__":
    main()
