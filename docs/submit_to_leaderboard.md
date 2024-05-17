# Submit to Leaderboard

The AIR-Bench is designed to be a closed-book benchmark. The golden truth is kept private. In this repo 

To submit your model to the leaderboard, please follow the steps below.

## Run Evaluation

### Use Transformers standard models
If your model uses the standard model architecture defined in huggingface transformers and is publicly available on Huggingface Hub or locally, you could use 
 [this script](https://github.com/AIR-Bench/AIR-Bench/tree/main/scripts/README.md#run_air_benchmarkpy) to evaluate your model.

<details>
<summary> Scripts for checking models </summary>>

A simple way to check is to run the following codes and make sure you don't see any warnings.

```python
from transformers import AutoModel, AutoTokenizer

model_name_or_path = "BAAI/bge-small-en-v1.5"
model = AutoModel.from_pretrained(model_name_or_path)
tokenizer = AutoTokenizer.from_pretrained(model_name_or_path)
```
</details>

<details>
  <summary> Example usage (click to unfold) </summary>

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

## Pack up Results
Run [this script](https://github.com/AIR-Bench/AIR-Bench/tree/main/scripts/README.md#zip_resultspy) to pack up the results into a `.zip` file.

### Submit results without reranking models

```bash
cd scripts
python zip_results.py \
--results_dir search_results \
--model_name [YOUR_RETRIEVAL_MODEL] \
--save_dir .
```

<details> 
<summary> Output </summary>

```shell
=========================================
Zipping search results...
Zip search results in search_results/all-MiniLM-L6-v2/NoReranker to ./all-MiniLM-L6-v2_NoReranker.zip.

=========================================
Success! Now you can upload the zipped search results to https://huggingface.co/spaces/AIR-Bench/leaderboard !
```

</details>

### Submit results with reranking models

```bash
cd scripts
python zip_results.py \
--results_dir search_results \
--model_name [YOUR_RETRIEVAL_MODEL] \
--reranker_name [YOUR_RERANKING_MODEL] \
--save_dir .
```

<details> 
<summary> Output </summary>

```shell
=========================================
Zipping search results...
Zip search results in search_results/jina-embeddings-v2-small-en/jina-reranker-v1-tiny-en to ./jina-embeddings-v2-small-en_jina-reranker-v1-tiny-en.zip.

=========================================
Success! Now you can upload the zipped search results to https://huggingface.co/spaces/AIR-Bench/leaderboard !
```

</details>

## Submit Results
Go to [AIR-Bench leaderboard](https://huggingface.co/spaces/AIR-Bench/leaderboard) and upload the `.zip` file from the previous step at the `Submit here!` tab. Please provide the model name together with a valid URL of the model. 

We recommend to [create a model card on HuggingFace Hub](https://huggingface.co/new) and put your model card URL in the model URL field. So that we could display more details about your model. 

If your evaluation only uses retrieval models, you don't need to fill the `Reranking Model name` and `Reranking Model URL`.

### Submit anonymously
You could submit the results without giving valid model URLs. By default, we won't show up the anonymous submissions. You could still find your submission by selecting the `Show anonymous submissions` checkbox.


## Check Leaderboard
We run the evaluation scripts regularly. It will take up to one hour to see your model on the leaderboard. You could use the search bar to find your model. If you don't see your model, please open an issue [here](https://github.com/AIR-Bench/AIR-Bench/issues/new). 
