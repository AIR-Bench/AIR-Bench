# Evaluation Scripts

- [Overview](#overview)
- [Available Scripts](#available-scripts)
  - [HuggingFace Transformers](#huggingface-transformers)
  - [Sentence Transformers](#sentence-transformers)
  - [BM25](#bm25)


This document shows how to evaluate the performance of a model on AIR-Bench using the provided evaluation scripts.

## Overview

### 1. Print Benchmark Information

Use the following code to print the benchmark information, including the benchmark version, task types, domains, and languages.

```python
from air_benchmark import AIRBench

AIRBench.print_benchmark_table()
```

### 2. Implement a Retriever

You need to implement a retriever that takes a set of queries and a corpus and returns the relevant documents for each query.

```python
from air_benchmark import Retriever

class MyRetriever(Retriever):
    def __str__(self):
        """
        Return the name of the retriever
        """
        raise NotImplementedError("You need to implement this method")

    def __call__(
        self,
        corpus: Dict[str, Dict[str, Any]],
        queries: Dict[str, str],
        **kwargs,
    ) -> Dict[str, Dict[str, float]]:
        """
        Retrieve relevant documents for each query
        """
        raise NotImplementedError("You need to implement this method")
```

### 3. Implement a Reranker (Optional)

You need to implement a reranker that takes a set of queries, a corpus, and the search results and returns the reranked search results.

```python
from air_benchmark import Reranker

class MyReranker(Reranker):
    def __str__(self):
        """
        Return the name of the reranker
        """
        raise NotImplementedError("You need to implement this method")

    def __call__(
        self,
        corpus: Dict[str, Dict[str, Any]],
        queries: Dict[str, str],
        search_results: Dict[str, Dict[str, float]],
        **kwargs,
    ) -> Dict[str, Dict[str, float]]:
        """
        Rerank the search results for each query
        """
        raise NotImplementedError("You need to implement this method")
```

### 4. Evaluate the Model

After implementing the retriever and the reranker, you can evaluate the model on AIR-Bench using the following code.

> **Note**: You need to specify the cache directory to store the downloaded data. The full benchmark requires ~52GB of disk space.

```python
from air_benchmark import AIRBench, Retriever, Reranker

class MyRetriever(Retriever):
    pass

class MyReranker(Reranker):
    pass


retriever = MyRetriever(search_top_k=1000)
reranker = MyReranker(rerank_top_k=100)

evaluation = AIRBench(
    benchmark_version="AIR-Bench_24.04",
    task_types="long-doc",      # remove this line if you want to evaluate on all tasks
    domains="arxiv",            # remove this line if you want to evaluate on all domains
    languages="en",             # remove this line if you want to evaluate on all languages
    cache_dir="<CACHE_DIR>"     # path to the cache directory (**NEED ~52GB FOR FULL BENCHMARK**)
)

evaluation.run(
    retriever,
    reranker=reranker,          # remove this line if you don't have a reranker
    output_dir="<OUTPUT_DIR>"   # path to the output directory, default is "./search_results"
    overwrite=False             # set to True if you want to overwrite the existing results
)
```

## Available Scripts

### HuggingFace Transformers

As for models that are compatible with the [HuggingFace Transformers](https://huggingface.co/docs/transformers/index), you can use the scripts at [hf-transformers](https://github.com/AIR-Bench/AIR-Bench/blob/main/examples/hf-transformers/evaluate_hf_transformers.py) to evaluate the models on AIR-Bench.

```bash
pip install mteb transformers

cd scripts/hf-transformers
```

<details><summary>click to see details</summary>

- Run all tasks:

```bash
python evaluate_hf_transformers.py \
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
```

- Run the tasks in the specified task type, domains, and languages:

```bash
python evaluate_hf_transformers.py \
--task_types qa \
--domains finance law \
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
```

</details>


### Sentence Transformers

As for models that are compatible with [SentenceTransformers](https://sbert.net/), you can use the scripts at [sentence-transformers](https://github.com/AIR-Bench/AIR-Bench/blob/main/examples/hf-transformers/evaluate_sentence_transformers.py) to evaluate the models on AIR-Bench.

```bash
pip install mteb transformers sentence-transformers

cd scripts/sentence-transformers
```

<details><summary>click to see details</summary>

- Run all tasks:

```bash
python evaluate_sentence_transformers.py \
--output_dir ./search_results \
--encoder sentence-transformers/all-MiniLM-L6-v2 \
--search_top_k 1000 \
--max_query_length 512 \
--max_passage_length 512 \
--batch_size 512 \
--normalize_embeddings True \
--reranker BAAI/bge-reranker-base \
--rerank_top_k 100 \
--batch_size_for_reranking 512 \
--overwrite False
```

- Run the tasks in the specified task type, domains, and languages:

```bash
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
--reranker BAAI/bge-reranker-base \
--rerank_top_k 100 \
--batch_size_for_reranking 512 \
--overwrite False
```

</details>


### BM25

As for the BM25 method implemented in [Pyserini](https://github.com/castorini/pyserini), you can use the scripts at [bm25](https://github.com/AIR-Bench/AIR-Bench/blob/main/examples/hf-transformers/evaluate_bm25.py) to evaluate the BM25 method on AIR-Bench.

```bash
pip install pyserini transformers

cd scripts/bm25
```

<details><summary>click to see details</summary>

- Run all tasks:

```bash
python evaluate_bm25.py \
--output_dir ./search_results \
--bm25_tmp_dir ./bm25_tmp_dir \
--remove_bm25_tmp_dir True \
--overwrite False
```

- Run the tasks in the specified task type, domains, and languages:

```bash
python evaluate_bm25.py \
--task_types qa \
--domains finance law \
--languages en \
--output_dir ./search_results \
--bm25_tmp_dir ./bm25_tmp_dir \
--remove_bm25_tmp_dir True \
--overwrite False
```

</details>
