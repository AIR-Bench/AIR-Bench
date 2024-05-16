# Usage of scripts

## [run_air_benchmark.py](https://github.com/AIR-Bench/AIR-Bench/blob/main/scripts/run_air_benchmark.py)
You can use this script to generate search results on AIR-Bench for your model.

- Run all tasks

You can evaluate all tasks following this command: 
```
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
```
The results will be saved to `output_dir`.


- Run the tasks in the specified task type, domains, and languages

You can pass argument `task_types`, `domains`, and `languages` to select a sub set of all tasks.

```
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
```




## [zip_results.py](https://github.com/AIR-Bench/AIR-Bench/blob/main/scripts/zip_results.py)
This script can compress your search results into zipfile, which can be submitted to AIR-Bench leaderboard.

- Embedding Model + NoReranker
```
# Zip "Embedding Model + NoReranker" search results in <search_results>/<model_name>/NoReranker to <save_dir>/<model_name>_NoReranker.zip.
python zip_results.py \
--results_dir search_results \
--model_name bge-m3 \
--save_dir search_results/zipped_results
```

- Embedding Model + DRESReranker
```
# Zip "Embedding Model + DRESReranker" search results in <search_results>/<model_name>/<reranker_name> to <save_dir>/<model_name>_<reranker_name>.zip.
python zip_results.py \
--results_dir search_results \
--model_name bge-m3 \
--reranker_name bge-reranker-v2-m3 \
--save_dir search_results/zipped_results
```

