import os
import logging
import datasets

logger = logging.getLogger(__name__)


class DataLoader:
    def __init__(self, benchmark_version: str, cache_dir: str = None):
        self.benchmark_version = benchmark_version
        self.cache_dir = cache_dir

    def load_data(self, task_type: str, domain: str, language: str, task_name: str):
        task_name = task_name.replace("-", "_")
        corpus_data = datasets.load_dataset(
            f"AIR-Bench/{task_type}_{domain}_{language}",
            self.benchmark_version,
            split=f"corpus_{task_name}",
            cache_dir=self.cache_dir,
        )
        queries_data = datasets.load_dataset(
            f"AIR-Bench/{task_type}_{domain}_{language}",
            self.benchmark_version,
            split=f"queries_{task_name}",
            cache_dir=self.cache_dir,
        )

        corpus = {e["id"]: {"text": e["text"]} for e in corpus_data}
        queries = {e["id"]: e["text"] for e in queries_data}

        corpus = datasets.DatasetDict(corpus)
        queries = datasets.DatasetDict(queries)
        return corpus, queries

    def load_qrels(self, task_type: str, domain: str, language: str, task_name: str):
        task_name = task_name.replace('-', '_')
        qrels_data = datasets.load_dataset(
            f'AIR-Bench/qrels-{task_type}_{domain}_{language}',
            self.benchmark_version,
            split=f"qrels_{task_name}",
            cache_dir=self.cache_dir,
            token=os.getenv('HF_TOKEN', None),
        )
        
        qrels = {}
        for data in qrels_data:
            qid = data['qid']
            if qid not in qrels:
                qrels[qid] = {}
            qrels[qid][data['docid']] = data['relevance']
        
        return datasets.DatasetDict(qrels)
