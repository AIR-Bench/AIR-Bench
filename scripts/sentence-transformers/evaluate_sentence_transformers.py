"""
Requirements:
    mteb>=1.7.17
    torch>=1.6.0
    transformers>=4.33.0
    sentence_transformers>=2.2.0

# Run all tasks
python evaluate_sentence_transformers.py \
--output_dir ./search_results \
--encoder sentence-transformers/all-MiniLM-L6-v2 \
--search_top_k 1000 \
--max_query_length 512 \
--max_passage_length 512 \
--batch_size 512 \
--normalize_embeddings True \
--reranker jinaai/jina-reranker-v1-tiny-en \
--rerank_top_k 100 \
--batch_size_for_reranking 512 \
--corpus_chunk_size 50000 \     # set to 10M if you have enough memory and want to avoid multiple tqdm bars
--overwrite False

# Run the tasks in the specified task type, domains, and languages
python evaluate_sentence_transformers.py \
--task_types qa \
--domains finance law \
--languages en \
--output_dir ./search_results \
--encoder sentence-transformers/all-MiniLM-L6-v2 \
--search_top_k 1000 \
--max_query_length 512 \
--max_passage_length 512 \
--batch_size 512 \
--normalize_embeddings True \
--reranker jinaai/jina-reranker-v1-tiny-en \
--rerank_top_k 100 \
--batch_size_for_reranking 512 \
--corpus_chunk_size 50000 \     # set to 10M if you have enough memory and want to avoid multiple tqdm bars
--overwrite False
"""
from transformers import HfArgumentParser

from air_benchmark import EvalArgs, AIRBench

from utils.arguments import ModelArgs
from utils.models import SentenceTransformerEncoder, SentenceTransformerReranker
from utils.searcher import EmbeddingModelRetriever, CrossEncoderReranker


def get_models(model_args: ModelArgs):
    embedding_model = SentenceTransformerEncoder(
        model_args.encoder,
        normalize_embeddings=model_args.normalize_embeddings,
        query_instruction_for_retrieval=model_args.query_instruction if model_args.add_instruction else None,
        passage_instruction_for_retrieval=model_args.passage_instruction if model_args.add_instruction else None,
        max_query_length=model_args.max_query_length,
        max_passage_length=model_args.max_passage_length,
        batch_size=model_args.batch_size,
        corpus_batch_size=model_args.corpus_batch_size,
        trust_remote_code=model_args.trust_remote_code,
    )
    cross_encoder = None
    if model_args.reranker is not None:
        cross_encoder = SentenceTransformerReranker(
            model_args.reranker,
            max_length=model_args.max_length_for_reranking,
            batch_size=model_args.batch_size_for_reranking,
            trust_remote_code=model_args.reranker_trust_remote_code,
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
        corpus_chunk_size=model_args.corpus_chunk_size,
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
