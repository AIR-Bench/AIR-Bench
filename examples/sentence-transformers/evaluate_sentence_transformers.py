"""
# Run all tasks
python run_air_benchmark.py \
--output_dir ./search_results \
--encoder sentence-transformers/all-MiniLM-L6-v2 \
--search_top_k 1000 \
--batch_size 512 \
--normalize_embeddings True \
--reranker jinaai/jina-reranker-v1-tiny-en \
--rerank_top_k 100 \
--batch_size_for_reranking 512 \
--overwrite False

# Run the tasks in the specified task type, domains, and languages

python run_air_benchmark.py \
--task_types qa \
--domains healthcare web \
--languages en \
--output_dir ./search_results \
--encoder sentence-transformers/all-MiniLM-L6-v2 \
--search_top_k 1000 \
--batch_size 512 \
--normalize_embeddings True \
--reranker jinaai/jina-reranker-v1-tiny-en \
--rerank_top_k 100 \
--batch_size_for_reranking 512 \
--overwrite False
"""
from transformers import HfArgumentParser

from air_benchmark.air_benchmark import AIRBench
from air_benchmark.evaluation_utils.evaluation_arguments import EvalArgs

from utils.arguments import ModelArgs
from utils.models import SentenceTransformerEncoder, SentenceTransformerReranker
from utils.searcher import EmbeddingModelRetriever, CrossEncoderReranker


def get_models(model_args: ModelArgs):
    embedding_model = SentenceTransformerEncoder(
        model_args.encoder,
        normalize_embeddings=model_args.normalize_embeddings,
        query_instruction_for_retrieval=model_args.query_instruction_for_retrieval if model_args.add_instruction_for_retrieval else None,
        passage_instruction_for_retrieval=model_args.passage_instruction_for_retrieval if model_args.add_instruction_for_retrieval else None,
        batch_size=model_args.batch_size,
        corpus_batch_size=model_args.corpus_batch_size
    )
    cross_encoder = None
    if model_args.reranker is not None:
        cross_encoder = SentenceTransformerReranker(
            model_args.reranker,
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
