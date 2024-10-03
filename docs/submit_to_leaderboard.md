# Submit to Leaderboard

The initial version `AIR-Bench_24.04` is designed to be a closed-book benchmark, where the golden truth is kept private for users. We provide a leaderboard for participants to submit the top-k search results of their models and compare their performance with others. The leaderboard is hosted on the HuggingFace Hub.

However, according to the feedback from the community (refer to [issue #26](https://github.com/AIR-Bench/AIR-Bench/issues/26)), users could not know the evaluation results until they submit their models’ search results to the leaderboard. It is not user-friendly for users to iterate their models’ performance.

Therefore, for the latest version `AIR-Bench_24.05`, we **split the queries into test set and dev set**. The golden truth of the dev set is provided to users, so that users could evaluate their models’ performance on the dev set by themselves. The golden truth for the test set is still kept private for users to submit their models’ search results to the leaderboard.

To **evaluate your models on the dev set**, please refer to [here](https://github.com/AIR-Bench/AIR-Bench/blob/main/scripts#5-compute-metrics-for-dev-set-optional). *We will contribute the dev set to [MTEB](https://huggingface.co/spaces/mteb/leaderboard) to help the users compare their models with other models*.

To **submit your model to the leaderboard** for evaluating on the test set, please follow the steps below.

## Installation

```bash
pip install air-benchmark
```

## Run evaluations

We provide a set of scripts to run evaluations on AIR-Bench for models that are compatible with different frameworks, such HuggingFace Transformers, Sentence Transformers, etc.

See the [scripts](https://github.com/AIR-Bench/AIR-Bench/blob/main/scripts) to run evaluations on AIR-Bench for your models. If you have a model that is not compatible with the provided scripts, you should implement the evaluation script like the scripts provided.

After running the evaluation, you will get the search results in the `output_dir` that you specified in the evaluation script. The `output_dir` is set to `./search_results` by default. 

For example, if you run the evaluation script for the `bge-m3` retrieval model and the `bge-reranker-v2-m3` reranking model, the file structure of the search results will be like this:

<details><summary>air-benchmark>=0.1.0 (pypi version)</summary>

```shell
search_results/
├── bge-m3/
│   ├── NoReranker/
│   │   ├── qa
│   │   │   ├── arxiv
│   │   │   │   ├── en_default_dev.json
│   │   │   │   ├── en_default_test.json
│   │   │   ├── finance
│   │   │   │   ├── en_default_dev.json
│   │   │   │   ├── en_default_test.json
│   │   │   │   ├── zh_default_dev.json
│   │   │   │   ├── zh_default_test.json
│   │   │   │   ...
│   │   ├── long-doc
│   │   │   ├── book
│   │   │   │   ├── en_a-brief-history-of-time_stephen-hawking_dev.json
│   │   │   │   ├── en_origin-of-species_darwin_test.json
│   │   │   │   ...
│   ├── bge-reranker-v2-m3/
│   │   ├── qa
│   │   │   ├── arxiv
│   │   │   │   ├── en_default_dev.json
│   │   │   │   ├── en_default_test.json
│   │   │   ├── finance
│   │   │   │   ├── en_default_dev.json
│   │   │   │   ├── en_default_test.json
│   │   │   │   ├── zh_default_dev.json
│   │   │   │   ├── zh_default_test.json
│   │   │   │   ...
│   │   ├── long-doc
│   │   │   ├── book
│   │   │   │   ├── en_a-brief-history-of-time_stephen-hawking_dev.json
│   │   │   │   ├── en_origin-of-species_darwin_test.json
│   │   │   │   ...
```

</details>

<details><summary>air-benchmark<=0.0.4 (pypi version)</summary>

```shell
search_results/
├── bge-m3/
│   ├── NoReranker/
│   │   ├── qa
│   │   │   ├── arxiv
│   │   │   │   ├── en_default.json
│   │   │   ├── finance
│   │   │   │   ├── en_default.json
│   │   │   │   ├── zh_default.json
│   │   │   │   ...
│   │   ├── long-doc
│   │   │   ├── book
│   │   │   │   ├── en_a-brief-history-of-time_stephen-hawking.json
│   │   │   │   ├── en_origin-of-species_darwin.json
│   │   │   │   ...
│   ├── bge-reranker-v2-m3/
│   │   ├── qa
│   │   │   ├── arxiv
│   │   │   │   ├── en_default.json
│   │   │   ├── finance
│   │   │   │   ├── en_default.json
│   │   │   │   ├── zh_default.json
│   │   │   │   ...
│   │   ├── long-doc
│   │   │   ├── book
│   │   │   │   ├── en_a-brief-history-of-time_stephen-hawking.json
│   │   │   │   ├── en_origin-of-species_darwin.json
│   │   │   │   ...
```

</details>

## Submit search results

### Package the output files

You should package the output files into a `.zip` file before submitting the results to the leaderboard. Use the [zip_results.py](https://github.com/AIR-Bench/AIR-Bench/tree/main/scripts/zip_results.py) script to pack up the results.

- As for the results without reranking models

```bash
cd scripts

python zip_results.py \
  --results_dir ./search_results \
  --retriever_name [YOUR_RETRIEVER_NAME] \
  --save_dir ./search_results
```

<details> 
<summary> Output </summary>

For our example, the output will be like this:

```shell
=========================================
Zipping search results...
Zip search results in ./search_results/bge-m3/NoReranker to ./search_results/bge-m3_NoReranker.zip.

=========================================
Success! Now you can upload the zipped search results to https://huggingface.co/spaces/AIR-Bench/leaderboard !
```

</details>

- As for the results with reranking models

```bash
cd scripts

python zip_results.py \
  --results_dir ./search_results \
  --retriever_name [YOUR_RETRIEVAL_MODEL] \
  --reranker_name [YOUR_RERANKING_MODEL] \
  --save_dir ./search_results
```

<details> 
<summary> Output </summary>

For our example, the output will be like this:

```shell
=========================================
Zipping search results...
Zip search results in ./search_results/bge-m3/bge-reranker-v2-m3 to ./search_results/bge-m3_bge-reranker-v2-m3.zip.

=========================================
Success! Now you can upload the zipped search results to https://huggingface.co/spaces/AIR-Bench/leaderboard !
```

</details>

### Submit to Leaderboard

Go to [AIR-Bench leaderboard](https://huggingface.co/spaces/AIR-Bench/leaderboard) and upload the `.zip` file from the previous step at the `Submit here!` tab. Please provide the model name together with a valid URL of the model. 

We recommend to [create a model card on HuggingFace Hub](https://huggingface.co/new) and put your model card URL in the model URL field. So that we could display more details about your model. 

If your evaluation only uses retrieval models, you don't need to fill the `Reranking Model name` and `Reranking Model URL`.

### Submit anonymously
You could submit the results without giving valid model URLs. By default, we won't show up the anonymous submissions. You could still find your submission by selecting the `Show anonymous submissions` checkbox.


## Check Leaderboard
We run the evaluation scripts regularly. It will take up to one hour to see your model on the leaderboard. You could use the search bar to find your model. If you don't see your model, please open an issue [here](https://github.com/AIR-Bench/AIR-Bench/issues/new). 
