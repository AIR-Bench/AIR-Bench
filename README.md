<h1 align="center"> AIR-Bench: Automated Heterogeneous Information Retrieval Benchmark </h1>

<h1 align="center">
<img style="vertical-align:middle" width="741" height="242" src="https://github.com/AIR-Bench/AIR-Bench/blob/eaee9fa1e9e5d989a04c9b074ab3df824e1c68da/docs/images/banner.png" />
</h1>

<h4 align="center">
    <p>
        <a href="#introduction">Introduction</a> |
        <a href="#documentation">Documentation</a> |
        <a href="https://huggingface.co/spaces/AIR-Bench/leaderboard">Leaderboard</a> |
        <a href="#citing">Citing</a>
    <p>
</h4>

<h3 align="center">
    <a href="https://huggingface.co/spaces/AIR-Bench/leaderboard"><img style="float: middle; padding: 10px 10px 10px 10px;" width="60" height="55" src="https://github.com/AIR-Bench/AIR-Bench/blob/main/docs/images/hf_logo.png" /></a>
</h3>

## Introduction

### Background & Motivation

Evaluation is crucial for the development of information retrieval models. In recent years, a series of milestone works have been introduced to the community, such as [MSMARCO](https://microsoft.github.io/msmarco/), [Natural Question](https://ai.google.com/research/NaturalQuestions), (open-domain QA), [MIRACL](https://github.com/project-miracl/miracl) (Milti-lingual retrieval), [BEIR](https://github.com/beir-cellar/beir/) and [MTEB](https://github.com/embeddings-benchmark/mteb) (general-domain zero-shot retrieval). However, the existing benchmarks are severely limited in the following perspectives.

- **Incapability of dealing with new domains**. All of the existing benchmarks are static, which means they are established for the pre-defined domains based on human labeled data. Therefore, they are incapable of dealing with new domains which are interested by the users. 
- **Potential risk of over-fitting and data leakage**. The existing retrievers are intensively fine-tuned in order to achieve strong performances on popular benchmarks, like BEIR and MTEB. Despite that these benchmarks are initially designed for zero-shot evaluation of O.O.D. Evaluation, the in-domain training data is widely used during the fine-tuning process. What is worse, given the public availability of the existing evaluation datasets, the testing data could be falsely mixed into the retrievers' training set by mistake. 

### Features of AIR-Bench

The new benchmark is highlighted for the following new features. 

- **Automated**. The testing data is automatically generated by large language models without human intervention. Therefore, it is able to instantly support the evaluation of new domains at a very small cost. Besides, the new testing data is almost impossible to be covered by the training sets of any existing retrievers.
- **Heterogeneous** **and Dynamic**: The testing data is generated w.r.t. diverse and constantly augmented domains and languages (i.e. Multi-domain, Multi-lingual). As a result, it is able to provide an increasingly comprehensive evaluation benchmark for the community developers.  
- **Retrieval and RAG-oriented**. The new benchmark is dedicated to the evaluation of retrieval performance. In addition to the typical evaluation scenarios, like open-domain question answering or paraphrase retrieval, the new benchmark also incorporates a new setting called inner-document retrieval which is closely related with today's LLM and RAG applications. In this new setting, the model is expected to retrieve the relevant chunks of a very long documents, which contain the critical information to answer the input question. 

## Results

We plan to release new test dataset on regular basis. The latest version of is `24.04`. You could check out the results at
[AIR-Bench Leaderboard](https://huggingface.co/spaces/AIR-Bench/leaderboard).

## Installation
This repo is used to maintain the codebases for running AIR-Bench evaluation. To run the evaluation, please install `air-benchmark`.

```bash
pip install air-benchmark
```

## Usage
1. Run evaluations
    - As for models that are compatible with standard architectures in HuggingFace Transformers and do not require `trust_remote_model=True`, use the python script at [scripts/run_air_benchmark.py](https://github.com/AIR-Bench/AIR-Bench/blob/main/scripts/run_air_benchmark.py)

   <details><summary>click to see details</summary>
   
    ```bash
    # Run a selected evaluation. Running all tasks will take about hours on a GPU machines.
    python run_air_benchmark.py \
    --output_dir ./search_results \
    --encoder BAAI/bge-small-en-v1.5 \
    --reranker BAAI/bge-reranker-base \
    --task_types long-doc \  # remove this line to run on all tasks
    --domains book \  # remove this line to run on all domains
    --languages en \  # remove this line to run on all languages
    --search_top_k 1000 \
    --rerank_top_k 100 \
    --max_query_length 512 \
    --max_passage_length 512 \
    --batch_size 512 \
    --pooling_method cls \
    --normalize_embeddings True \
    --use_fp16 True \  # set to False for running on CPUs
    --add_instruction False \
    --overwrite False
    ```
   
   </details>

    - As for models that are compatible with [SentenceTransformers](https://sbert.net/), please refer to the example at [examples/evaluate_sentence_transformers_reranker.py](https://github.com/AIR-Bench/AIR-Bench/blob/main/examples/evaluate_sentence_transformers_embeddings.py)

2. Submit search results
    - Package the output files
      - As for the results without reranking models,

      ```bash
      cd scripts
      python zip_results.py \
      --results_dir search_results \
      --model_name [YOUR_RETRIEVAL_MODEL] \
      --save_dir search_results/[YOUR_RETRIEVAL_MODEL]
      ```

      - As for the results with reranking models

      ```bash
      cd scripts
      python zip_results.py \
      --results_dir search_results \
      --model_name [YOUR_RETRIEVAL_MODEL] \
      --reranker_name [YOUR_RERANKING_MODEL] \
      --save_dir search_results/[YOUR_RETRIEVAL_MODEL]
      ```

    - Upload the output `.zip` and fill in the model information at [AIR-Bench Leaderboard](https://github.com/AIR-Bench/AIR-Bench)

## Documentation

| Documentation                                                |                                                           |
| ------------------------------------------------------------ | --------------------------------------------------------- |
| 🏭 [Pipeline](https://github.com/AIR-Bench/AIR-Bench/blob/main/docs/data_generation.md) | The data generation pipeline of AIR-Bench                 |
| 📋 [Tasks](https://github.com/AIR-Bench/AIR-Bench/blob/main/docs/available_tasks.md) | Overview of available tasks in AIR-Bench                  |
| 📈 [Leaderboard](https://huggingface.co/spaces/AIR-Bench/leaderboard) | The interactive leaderboard of AIR-Bench                  |
| 🚀 [Submit](https://github.com/AIR-Bench/AIR-Bench/blob/main/docs/submit_to_leaderboard.md) | Information related to how to submit a model to AIR-Bench |
| 🤝 [Contributing](https://github.com/AIR-Bench/AIR-Bench/blob/main/docs/community_contribution.md) | How to contribute to AIR-Bench                            |

## Available Evaluation Results

Detailed results are available [here](https://github.com/AIR-Bench/AIR-Bench/blob/main/docs/available_evaluation_results.md).


## Acknowledgement
This work is inspired by [MTEB](https://github.com/embeddings-benchmark/mteb) and [BEIR](https://github.com/beir-cellar/beir/). Many thanks for the early feedbacks from [@tomaarsen](https://github.com/tomaarsen), [@Muennighoff](https://github.com/Muennighoff), [@takatost](https://github.com/takatost), [@chtlp](https://github.com/chtlp).


## Citing
TBD
