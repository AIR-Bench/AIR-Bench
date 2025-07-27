import faiss
import torch
import logging
import numpy as np
from tqdm import tqdm
from typing import Optional

logger = logging.getLogger(__name__)


"""
Copied from https://github.com/FlagOpen/FlagEmbedding/blob/v1.3.5/FlagEmbedding/abc/evaluation/utils.py#L111
"""
def index(
    index_factory: str = "Flat", 
    corpus_embeddings: Optional[np.ndarray] = None, 
    load_path: Optional[str] = None,
    device: Optional[str] = None
):
    """Create and add embeddings into a Faiss index.

    Args:
        index_factory (str, optional): Type of Faiss index to create. Defaults to "Flat".
        corpus_embeddings (Optional[np.ndarray], optional): The embedding vectors of the corpus. Defaults to None.
        load_path (Optional[str], optional): Path to load embeddings from. Defaults to None.
        device (Optional[str], optional): Device to hold Faiss index. Defaults to None.

    Returns:
        faiss.Index: The Faiss index that contains all the corpus embeddings.
    """
    if corpus_embeddings is None:
        corpus_embeddings = np.load(load_path)
    
    logger.info(f"Shape of embeddings: {corpus_embeddings.shape}")
    # create faiss index
    logger.info(f'Indexing {corpus_embeddings.shape[0]} documents...')
    faiss_index = faiss.index_factory(corpus_embeddings.shape[-1], index_factory, faiss.METRIC_INNER_PRODUCT)
    
    if device is None and torch.cuda.is_available():
        try:
            co = faiss.GpuMultipleClonerOptions()
            co.shard = True
            co.useFloat16 = True
            faiss_index = faiss.index_cpu_to_all_gpus(faiss_index, co)
        except:
            print('faiss do not support GPU, please uninstall faiss-cpu, faiss-gpu and install faiss-gpu again.')

    logger.info('Adding embeddings ...')
    corpus_embeddings = corpus_embeddings.astype(np.float32)
    faiss_index.train(corpus_embeddings)
    faiss_index.add(corpus_embeddings)
    logger.info('Embeddings add over...')
    return faiss_index


"""
Copied from https://github.com/FlagOpen/FlagEmbedding/blob/v1.3.5/FlagEmbedding/abc/evaluation/utils.py#L153
"""
def search(
    faiss_index: faiss.Index, 
    k: int = 100, 
    query_embeddings: Optional[np.ndarray] = None,
    load_path: Optional[str] = None
):
    """
    1. Encode queries into dense embeddings;
    2. Search through faiss index

    Args:
        faiss_index (faiss.Index): The Faiss index that contains all the corpus embeddings.
        k (int, optional): Top k numbers of closest neighbours. Defaults to :data:`100`.
        query_embeddings (Optional[np.ndarray], optional): The embedding vectors of queries. Defaults to :data:`None`.
        load_path (Optional[str], optional): Path to load embeddings from. Defaults to :data:`None`.

    Returns:
        Tuple[np.ndarray, np.ndarray]: The scores of search results and their corresponding indices.
    """
    if query_embeddings is None:
        query_embeddings = np.load(load_path)

    query_size = len(query_embeddings)

    all_scores = []
    all_indices = []

    for i in tqdm(range(0, query_size, 32), desc="Searching"):
        j = min(i + 32, query_size)
        query_embedding = query_embeddings[i: j]
        score, indice = faiss_index.search(query_embedding.astype(np.float32), k=k)
        all_scores.append(score)
        all_indices.append(indice)

    all_scores = np.concatenate(all_scores, axis=0)
    all_indices = np.concatenate(all_indices, axis=0)
    return all_scores, all_indices
