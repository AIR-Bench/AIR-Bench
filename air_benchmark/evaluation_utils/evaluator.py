import json
import logging
import os
import json
import pandas as pd
from typing import Dict, Optional, List, Union
from mteb.evaluation.evaluators import RetrievalEvaluator

from air_benchmark.evaluation_utils.data_loader import DataLoader
from air_benchmark.evaluation_utils.searcher import Retriever, Reranker

logger = logging.getLogger(__name__)


class Evaluator:
    def __init__(
        self,
        data_loader: DataLoader,
        overwrite: bool = False,
    ):
        self.data_loader = data_loader
        self.overwrite = overwrite
        self.benchmark_version = data_loader.benchmark_version

    def check_data_info(
        self,
        data_info: Dict[str, str],
        model_name: str,
        reranker_name: str,
        domain: str,
        language: str,
        dataset_name: str,
        split: str,
    ):
        if data_info["benchmark_version"] != self.benchmark_version:
            raise ValueError(
                f'benchmark_version mismatch: {data_info["benchmark_version"]} vs {self.benchmark_version}'
            )
        if (
            data_info["model_name"] != model_name
            or data_info["reranker_name"] != reranker_name
        ):
            raise ValueError(
                f'model_name or reranker_name mismatch: {data_info["model_name"]} vs {model_name} or {data_info["reranker_name"]} vs {reranker_name}'
            )
        if (
            data_info["domain"] != domain
            or data_info["language"] != language
            or data_info["dataset_name"] != dataset_name
            or data_info["split"] != split
        ):
            raise ValueError(
                f'domain or language or dataset_name mismatch: {data_info["domain"]} vs {domain} or {data_info["language"]} vs {language} or {data_info["dataset_name"]} vs {dataset_name} or {data_info["split"]} vs {split}'
            )
    
    def __call__(
        self,
        task_type: str,
        domain: str,
        language: str,
        dataset_name: str,
        splits: List[str],
        search_results_save_dir: str,
        retriever: Retriever,
        reranker: Optional[Reranker] = None,
        **kwargs,
    ):
        # Retrieval Stage
        no_reranker_search_results_save_dir = os.path.join(
            search_results_save_dir, str(retriever), "NoReranker", task_type
        )
        os.makedirs(no_reranker_search_results_save_dir, exist_ok=True)
        
        flag = False
        for split in splits:
            split_no_reranker_search_results_save_path = os.path.join(
                no_reranker_search_results_save_dir, domain, f"{language}_{dataset_name}_{split}.json"
            )
            if not os.path.exists(split_no_reranker_search_results_save_path) or self.overwrite:
                flag = True
                break
        
        no_reranker_search_results_dict = {}
        if flag:
            corpus = self.data_loader.load_corpus(
                task_type=task_type,
                domain=domain,
                language=language,
                dataset_name=dataset_name,
            )
            
            queries_dict = {
                split: self.data_loader.load_queries(
                    task_type=task_type,
                    domain=domain,
                    language=language,
                    dataset_name=dataset_name,
                    split=split,
                ) for split in splits
            }
            
            all_queries = {}
            for _, split_queries in queries_dict.items():
                all_queries.update(split_queries)

            all_no_reranker_search_results = retriever(
                corpus=corpus,
                queries=all_queries,
                language=language,  # for language-specific retrievers, such as BM25Retriever
                **kwargs,
            )
            
            for split in splits:
                split_queries = queries_dict[split]
                no_reranker_search_results_dict[split] = {
                    qid: all_no_reranker_search_results[qid] for qid in split_queries
                }
                split_no_reranker_search_results_save_path = os.path.join(
                    no_reranker_search_results_save_dir, domain, f"{language}_{dataset_name}_{split}.json"
                )
                
                self.save_search_results(
                    model_name=str(retriever),
                    reranker_name="NoReranker",
                    search_results=no_reranker_search_results_dict[split],
                    output_path=split_no_reranker_search_results_save_path,
                    task_type=task_type,
                    domain=domain,
                    language=language,
                    dataset_name=dataset_name,
                    split=split,
                    benchmark_version=self.benchmark_version,
                )
        else:
            for split in splits:
                split_no_reranker_search_results_save_path = os.path.join(
                    no_reranker_search_results_save_dir, domain, f"{language}_{dataset_name}_{split}.json"
                )
                data_info, search_results = self.load_search_results(split_no_reranker_search_results_save_path)
                if 'dataset_name' not in data_info:
                    data_info['dataset_name'] = data_info['task_name']     # To be compatible with the AIR-Bench_24.04 version
                self.check_data_info(
                    data_info=data_info,
                    model_name=str(retriever),
                    reranker_name="NoReranker",
                    domain=domain,
                    language=language,
                    dataset_name=dataset_name,
                    split=split,
                )
                no_reranker_search_results_dict[split] = search_results
        
        # Reranking Stage
        if reranker is not None:
            reranker_search_results_save_dir = os.path.join(
                search_results_save_dir, str(retriever), str(reranker), task_type
            )
            os.makedirs(reranker_search_results_save_dir, exist_ok=True)
            
            corpus = self.data_loader.load_corpus(
                task_type=task_type,
                domain=domain,
                language=language,
                dataset_name=dataset_name,
            )
            
            queries_dict = {
                split: self.data_loader.load_queries(
                    task_type=task_type,
                    domain=domain,
                    language=language,
                    dataset_name=dataset_name,
                    split=split,
                ) for split in splits
            }
            
            for split in splits:
                rerank_search_results_save_path = os.path.join(
                    reranker_search_results_save_dir, domain, f"{language}_{dataset_name}_{split}.json"
                )
                
                if os.path.exists(rerank_search_results_save_path) and not self.overwrite:
                    return
                
                rerank_search_results = reranker(
                    corpus=corpus,
                    queries=queries_dict[split],
                    search_results=no_reranker_search_results_dict[split],
                    **kwargs,
                )
                
                self.save_search_results(
                    model_name=str(retriever),
                    reranker_name=str(reranker),
                    search_results=rerank_search_results,
                    output_path=rerank_search_results_save_path,
                    task_type=task_type,
                    domain=domain,
                    language=language,
                    dataset_name=dataset_name,
                    split=split,
                    benchmark_version=self.benchmark_version,
                )
    
    @staticmethod
    def save_search_results(
        model_name: str,
        reranker_name: str,
        search_results: Dict[str, Dict[str, float]],
        output_path: str,
        task_type: str,
        domain: str,
        language: str,
        dataset_name: str,
        split: str,
        benchmark_version: str,
    ):
        data = {
            "model_name": model_name,
            "reranker_name": reranker_name,
            "benchmark_version": benchmark_version,
            "task_type": task_type,
            "domain": domain,
            "language": language,
            "dataset_name": dataset_name,
            "split": split,
            "search_results": search_results,
        }

        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    @staticmethod
    def load_search_results(input_path: str):
        with open(input_path, "r", encoding="utf-8") as f:
            data_info = json.load(f)

        search_results = data_info.pop("search_results")
        return data_info, search_results

    @staticmethod
    def compute_metrics(
        qrels: Dict[str, Dict[str, int]],
        search_results: Dict[str, Dict[str, float]],
        k_values: List[int],
    ):
        ndcg, _map, recall, precision, _ = RetrievalEvaluator.evaluate(
            qrels=qrels,
            results=search_results,
            k_values=k_values,
            ignore_identical_ids=True,
        )
        mrr, _ = RetrievalEvaluator.evaluate_custom(
            qrels=qrels,
            results=search_results,
            k_values=k_values,
            metric='mrr',
        )
        scores = {
            **{f"ndcg_at_{k.split('@')[1]}": v for (k, v) in ndcg.items()},
            **{f"map_at_{k.split('@')[1]}": v for (k, v) in _map.items()},
            **{f"recall_at_{k.split('@')[1]}": v for (k, v) in recall.items()},
            **{f"precision_at_{k.split('@')[1]}": v for (k, v) in precision.items()},
            **{f"mrr_at_{k.split('@')[1]}": v for (k, v) in mrr.items()},
        }
        return scores
    
    def evaluate_results(
        self,
        search_results_save_dir: str,
        k_values: List[int] = [1, 3, 5, 10, 100, 1000],
        split: str = 'test',
    ):
        eval_results_dict = {}
        
        for task_type in os.listdir(search_results_save_dir):
            task_type_dir = os.path.join(search_results_save_dir, task_type)
            if not os.path.isdir(task_type_dir):
                continue
            for domain in os.listdir(task_type_dir):
                domain_dir = os.path.join(task_type_dir, domain)
                for file in os.listdir(domain_dir):
                    if not file.endswith('.json'):
                        continue
                    
                    file_path = os.path.join(domain_dir, file)
                    data_info, search_results = self.load_search_results(file_path)
                    if 'dataset_name' not in data_info:
                        data_info['dataset_name'] = data_info['task_name']     # To be compatible with the AIR-Bench_24.04 version
                    
                    _benchmark_version = data_info['benchmark_version']
                    assert _benchmark_version == self.benchmark_version, f'Mismatch benchmark_version: {_benchmark_version} vs {self.benchmark_version} in {file_path}'
                    
                    _split = data_info.get('split', 'test')     # To be compatible with the AIR-Bench_24.04 version
                    _task_type = data_info['task_type']
                    _domain = data_info['domain']
                    
                    if _split != split:
                        continue
                    
                    assert task_type == _task_type, f'Mismatch task_type: {task_type} vs {_task_type} in {file_path}'
                    assert domain == _domain, f'Mismatch domain: {domain} vs {_domain} in {file_path}'
                    
                    language = data_info['language']
                    
                    if task_type not in eval_results_dict:
                        eval_results_dict[task_type] = {}
                    if domain not in eval_results_dict[task_type]:
                        eval_results_dict[task_type][domain] = {}
                    if language not in eval_results_dict[task_type][domain]:
                        eval_results_dict[task_type][domain][language] = {}
                    
                    dataset_name = data_info['dataset_name']
                    
                    qrels = self.data_loader.load_qrels(
                        task_type=task_type,
                        domain=domain,
                        language=language,
                        dataset_name=dataset_name,
                        split=_split,
                    )
                    
                    eval_results = self.compute_metrics(
                        qrels=qrels,
                        search_results=search_results,
                        k_values=k_values
                    )
                    
                    eval_results_dict[task_type][domain][language][dataset_name] = eval_results
        
        return eval_results_dict

    @staticmethod
    def output_eval_results_to_json(eval_results_dict: dict, output_path: str):
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(eval_results_dict, f, indent=4)
        print(f"Results saved to {output_path}")

    @staticmethod
    def get_results_df_dict(metric: str, eval_results_dict: dict):
        task_type_results_dict = {}
        
        for model_name, model_results in eval_results_dict.items():
            for reranker_name, reranker_results in model_results.items():
                for task_type, task_results in reranker_results.items():
                    if task_type not in task_type_results_dict:
                        task_type_results_dict[task_type] = {}
                    for domain, domain_results in task_results.items():
                        if domain not in task_type_results_dict[task_type]:
                            task_type_results_dict[task_type][domain] = {}
                        
                        if model_name not in task_type_results_dict[task_type][domain]:
                            task_type_results_dict[task_type][domain][model_name] = {}
                        if reranker_name not in task_type_results_dict[task_type][domain][model_name]:
                            task_type_results_dict[task_type][domain][model_name][reranker_name] = {}
                        
                        for lang, lang_results in domain_results.items():
                            if metric in lang_results:
                                task_type_results_dict[task_type][domain][model_name][reranker_name][lang] = lang_results[metric]
                            else:
                                for dataset_name, dataset_name_results in lang_results.items():
                                    task = f"{lang} {dataset_name}"
                                    task_type_results_dict[task_type][domain][model_name][reranker_name][task] = dataset_name_results[metric]
        
        results_df_dict = {}
        for task_type, results_dict in task_type_results_dict.items():
            domains = sorted(list(results_dict.keys()))
            model_reranker_pairs = set()
            for domain in domains:
                for model_name, model_results in results_dict[domain].items():
                    for reranker_name, reranker_results in model_results.items():
                        model_reranker_pairs.add((model_name, reranker_name))
            model_reranker_pairs = sorted(list(model_reranker_pairs))
            
            domain_tasks = {domain: set() for domain in domains}
            for domain in domains:
                for model_name, model_results in results_dict[domain].items():
                    for reranker_name, reranker_results in model_results.items():
                        for task in reranker_results:
                            domain_tasks[domain].add(task)
            domain_tasks = {k: sorted(list(v)) for k, v in domain_tasks.items()}
            
            results_df_dict[task_type] = {
                'overall': None
            }
            index = [(model, reranker) for model, reranker in model_reranker_pairs]
            multi_index = pd.MultiIndex.from_tuples(index, names=['Model', 'Reranker'])
            
            overall_tasks = [
                f"{_domain} {_task}"
                for _domain in domains for _task in domain_tasks[_domain]
            ]
            overall_columns = ['average'] + overall_tasks
            overall_df = pd.DataFrame(index=multi_index, columns=overall_columns)
            for domain in domains:
                tasks = domain_tasks[domain]
                columns = ['average'] + tasks
                df = pd.DataFrame(index=multi_index, columns=columns)
                
                for model, reranker in model_reranker_pairs:
                    for task in tasks:
                        if model in results_dict[domain] \
                           and reranker in results_dict[domain][model] \
                           and task in results_dict[domain][model][reranker]:
                            df.loc[(model, reranker), task] = results_dict[domain][model][reranker][task]
                            overall_df.loc[(model, reranker), f"{domain} {task}"] = results_dict[domain][model][reranker][task]
                    if df.loc[(model, reranker), tasks].isnull().any():
                        df.loc[(model, reranker), 'average'] = None
                    else:
                        df.loc[(model, reranker), 'average'] = df.loc[(model, reranker), tasks].mean()
            
                results_df_dict[task_type][domain] = df
            
            # compute overall average
            for model, reranker in model_reranker_pairs:
                if overall_df.loc[(model, reranker), overall_tasks].isnull().any():
                    overall_df.loc[(model, reranker), 'average'] = None
                else:
                    overall_df.loc[(model, reranker), 'average'] = overall_df.loc[(model, reranker), overall_tasks].mean()
            results_df_dict[task_type]['overall'] = overall_df
        return results_df_dict
    
    @staticmethod
    def output_eval_results_to_markdown(eval_results_dict: dict, output_path: str, metrics: Union[List[str], str]):
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        if isinstance(metrics, str):
            metrics = [metrics]
        
        with open(output_path, 'w', encoding='utf-8') as f:
            for metric in metrics:
                f.write(f"## {metric}\n\n")
                results_df_dict = Evaluator.get_results_df_dict(metric, eval_results_dict)
                for task_type, task_results_df_dict in results_df_dict.items():
                    f.write(f"### {task_type}\n\n")
                    for domain, results_df in task_results_df_dict.items():
                        f.write(f"#### {domain}\n\n")
                        max_index = dict(results_df.idxmax(axis=0))
                        tasks = results_df.columns
                        f.write(f"| Model | Reranker | {' | '.join(tasks)} |\n")
                        f.write(f"| :---- | :---- | {' | '.join([':---:' for _ in tasks])} |\n")
                        for i, row in results_df.iterrows():
                            line = f"| {i[0]} | {i[1]} | "
                            for d, v in row.items():
                                if v is None:
                                    line += "- | "
                                else:
                                    if i != max_index[d]:
                                        line += f'{v*100:.3f} | '
                                    else:
                                        line += f'**{v*100:.3f}** | '
                            f.write(line + "\n")
                        f.write("\n")
                    f.write("\n")
                f.write("\n")
        print(f"Results saved to {output_path}")
