"""
# Run all tasks
python run_air_benchmark.py \
--output_dir ./search_results \
--encoder BAAI/bge-m3 \
--search_top_k 1000 \
--max_query_length 512 \
--max_passage_length 512 \
--batch_size 512 \
--pooling_method cls \
--normalize_embeddings True \
--reranker BAAI/bge-reranker-v2-m3 \
--rerank_top_k 100 \
--max_length_for_reranking 512 \
--batch_size_for_reranking 512 \
--use_fp16 True \
--overwrite False

# Run the tasks in the specified task type, domains, and languages
python run_air_benchmark.py \
--task_types qa \
--domains healthcare web \
--languages en \
--output_dir ./search_results \
--encoder BAAI/bge-m3 \
--search_top_k 1000 \
--max_query_length 512 \
--max_passage_length 512 \
--batch_size 512 \
--pooling_method cls \
--normalize_embeddings True \
--reranker BAAI/bge-reranker-v2-m3 \
--rerank_top_k 100 \
--batch_size_for_reranking 512 \
--use_fp16 True \
--overwrite False
"""
from transformers import HfArgumentParser

from air_benchmark.air_benchmark import AIRBench
from air_benchmark.evaluation_utils.evaluation_arguments import EvalArgs

from utils.arguments import ModelArgs
from utils.models import DRESModel, DRESReranker
from utils.searcher import EmbeddingModelRetriever, CrossEncoderReranker


def get_models(model_args: ModelArgs):
    embedding_model = DRESModel(
        model_args.encoder,
        pooling_method=model_args.pooling_method,
        normalize_embeddings=model_args.normalize_embeddings,
        use_fp16=model_args.use_fp16,
        query_instruction_for_retrieval=(
            model_args.query_instruction_for_retrieval
            if model_args.add_instruction_for_retrieval
            else None
        ),
        passage_instruction_for_retrieval=(
            model_args.passage_instruction_for_retrieval
            if model_args.add_instruction_for_retrieval
            else None
        ),
        max_query_length=model_args.max_query_length_for_retrieval,
        max_passage_length=model_args.max_passage_length_for_retrieval,
        batch_size=model_args.batch_size,
        corpus_batch_size=model_args.corpus_batch_size,
    )
    cross_encoder = None
    if model_args.reranker is not None:
        cross_encoder = DRESReranker(
            model_args.reranker,
            use_fp16=model_args.use_fp16,
            query_instruction_for_reranking=(
                model_args.query_instruction_for_reranking
                if model_args.add_instruction_for_reranking
                else None
            ),
            passage_instruction_for_reranking=(
                model_args.passage_instruction_for_reranking
                if model_args.add_instruction_for_reranking
                else None
            ),
            max_length=model_args.max_length_for_reranking,
            batch_size=model_args.batch_size_for_reranking,
        )
    return embedding_model, cross_encoder


def main():
    parser = HfArgumentParser([ModelArgs, EvalArgs])
    model_args, eval_args = parser.parse_args_into_dataclasses()
    model_args: ModelArgs
    eval_args: EvalArgs

    embedding_model, cross_encoder = get_models(model_args)
    
    evaluation = AIRBench(
        benchmark_version=eval_args.benchmark_version,
        task_types=eval_args.task_types,
        domains=eval_args.domains,
        languages=eval_args.languages,
        cache_dir=eval_args.cache_dir,
    )
    
    retriever = EmbeddingModelRetriever(
        embedding_model, 
        search_top_k=eval_args.search_top_k,
        corpus_chunk_size=10000000,  # 10M chunk size when encoding the corpus to avoid multiple tqdm bars
    )
    
    if cross_encoder is not None:
        reranker = CrossEncoderReranker(
            cross_encoder,
            rerank_top_k=eval_args.rerank_top_k,
        )
    else:
        reranker = None
    
    evaluation.run(
        retriever,
        reranker=reranker,
        output_dir=eval_args.output_dir,
        overwrite=eval_args.overwrite,
    )


if __name__ == "__main__":
    main()
