import os
import logging
import datasets


logger = logging.getLogger(__name__)


class DataLoader:
    def __init__(self, benchmark_version: str, cache_dir: str = None):
        self.benchmark_version = benchmark_version
        self.cache_dir = cache_dir

    def load_qrels(self, task_type: str, domain: str, language: str, dataset_name: str, split: str = 'dev'):
        dataset_name = dataset_name.replace('-', '_')
        if split == 'test':
            qrels_data = datasets.load_dataset(
                f'AIR-Bench/qrels-{task_type}_{domain}_{language}',
                self.benchmark_version,
                split=f"qrels_{dataset_name}_{split}" if self.benchmark_version != 'AIR-Bench_24.04' else f"qrels_{dataset_name}",        # To be compatible with the AIR-Bench_24.04 version
                cache_dir=self.cache_dir,
                token=os.getenv('HF_TOKEN', None),
            )
        else:
            qrels_data = datasets.load_dataset(
                f'AIR-Bench/{task_type}_{domain}_{language}',
                self.benchmark_version,
                split=f"qrels_{dataset_name}_{split}",
                cache_dir=self.cache_dir,
            )
        
        qrels = {}
        for data in qrels_data:
            qid = data['qid']
            if qid not in qrels:
                qrels[qid] = {}
            qrels[qid][data['docid']] = data['relevance']
        
        return datasets.DatasetDict(qrels)
    
    def load_corpus(self, task_type: str, domain: str, language: str, dataset_name: str):
        dataset_name = dataset_name.replace('-', '_')
        corpus_data = datasets.load_dataset(
            f'AIR-Bench/{task_type}_{domain}_{language}',
            self.benchmark_version,
            split=f"corpus_{dataset_name}",
            cache_dir=self.cache_dir,
        )
        
        corpus = {e['id']: {'text': e['text']} for e in corpus_data}
        return datasets.DatasetDict(corpus)
    
    def load_queries(self, task_type: str, domain: str, language: str, dataset_name: str, split: str = 'test'):
        dataset_name = dataset_name.replace('-', '_')
        queries_data = datasets.load_dataset(
            f'AIR-Bench/{task_type}_{domain}_{language}',
            self.benchmark_version,
            split=f"queries_{dataset_name}_{split}" if self.benchmark_version != 'AIR-Bench_24.04' else f"queries_{dataset_name}",    # To be compatible with the AIR-Bench_24.04 version
            cache_dir=self.cache_dir,
        )
        
        queries = {e['id']: e['text'] for e in queries_data}
        return datasets.DatasetDict(queries)
