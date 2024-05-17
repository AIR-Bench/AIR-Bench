import os

from sentence_transformers import SentenceTransformer

from air_benchmark.air_benchmark import AIRBench


class SentenceTransformerEncoder:
    def __init__(self, model_name_or_path: str, **kwargs):
        self.model = SentenceTransformer(model_name_or_path)
        self.name = os.path.basename(model_name_or_path)

    def encode_corpus(self, corpus, **kwargs):
        input_texts = corpus
        if isinstance(corpus[0], dict):
            input_texts = [
                "{} {}".format(doc.get("title", ""), doc.get("text", "")).strip()
                for doc in corpus
            ]
        return self.model.encode(input_texts)

    def encode_queries(self, queries, **kwargs):
        input_texts = queries
        if isinstance(queries[0], dict):
            input_texts = [doc.get("text", "").strip() for doc in queries]
        return self.model.encode(input_texts)

    def __str__(self):
        return self.name


def main():
    encoder = SentenceTransformerEncoder("sentence-transformers/all-MiniLM-L6-v2")

    evaluation = AIRBench(
        benchmark_version="AIR-Bench_24.04",
        task_types=["long-doc"],
        domains=["book"],
        languages=["en"],
    )

    evaluation.run(
        encoder,
        output_dir="./search_results",
        search_top_k=20,  # change to 1000 for proper evaluations
        rerank_top_k=10,  # change  to 100 for proper evaluations
        overwrite=True,
        corpus_chunk_size=10_000_000,
    )


if __name__ == '__main__':
    main()
