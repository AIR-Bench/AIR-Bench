# Avaliable Evaluation Results on AIR-Bench

- [Avaliable Evaluation Results on AIR-Bench](#avaliable-evaluation-results-on-air-bench)
  - [Consistency with MS MARCO](#consistency-with-ms-marco)
  - [Influence of Hard Negatives](#influence-of-hard-negatives)
  - [QA](#qa)
    - [nDCG@10 in arxiv](#ndcg10-in-arxiv)
    - [nDCG@10 in finance](#ndcg10-in-finance)
    - [nDCG@10 in healthcare](#ndcg10-in-healthcare)
    - [nDCG@10 in law](#ndcg10-in-law)
    - [nDCG@10 in msmarco](#ndcg10-in-msmarco)
    - [nDCG@10 in news](#ndcg10-in-news)
    - [nDCG@10 in web](#ndcg10-in-web)
    - [nDCG@10 in wiki](#ndcg10-in-wiki)
  - [Long-Doc](#long-doc)
    - [nDCG@10 in arxiv](#ndcg10-in-arxiv-1)
    - [nDCG@10 in book](#ndcg10-in-book)
    - [nDCG@10 in healthcare](#ndcg10-in-healthcare-1)
    - [nDCG@10 in law](#ndcg10-in-law-1)

## Consistency with MS MARCO

Selected Models: BM25, [multilingual-e5-large](https://huggingface.co/intfloat/multilingual-e5-large), [multilingual-e5-base](https://huggingface.co/intfloat/multilingual-e5-base), [multilingual-e5-small](https://huggingface.co/intfloat/multilingual-e5-small), [bge-large-en-v1.5](https://huggingface.co/BAAI/bge-large-en-v1.5), [bge-base-en-v1.5](https://huggingface.co/BAAI/bge-base-en-v1.5), [bge-small-en-v1.5](https://huggingface.co/BAAI/bge-small-en-v1.5), [e5-mistral-7b-instruct](https://huggingface.co/intfloat/e5-mistral-7b-instruct), [simlm-base-msmarco-finetuned](https://huggingface.co/intfloat/simlm-base-msmarco-finetuned), [jina-embeddings-v2-base-en](https://huggingface.co/jinaai/jina-embeddings-v2-base-en), [bge-m3](https://huggingface.co/BAAI/bge-m3), [msmarco-roberta-base-ance-firstp](https://huggingface.co/sentence-transformers/msmarco-roberta-base-ance-firstp).

nDCG@10 on the **original MS MARCO dev**:

| Rank | Model                            | Reranker   |  average   |     en     |
| ---- | :------------------------------- | :--------- | :--------: | :--------: |
| 1    | multilingual-e5-large            | NoReranker | **45.119** | **45.119** |
| 2    | multilingual-e5-base             | NoReranker |   44.130   |   44.130   |
| 3    | bge-large-en-v1.5                | NoReranker |   44.122   |   44.122   |
| 4    | e5-mistral-7b-instruct           | NoReranker |   43.787   |   43.787   |
| 5    | bge-small-en-v1.5                | NoReranker |   42.553   |   42.553   |
| 6    | bge-base-en-v1.5                 | NoReranker |   42.388   |   42.388   |
| 7    | multilingual-e5-small            | NoReranker |   42.253   |   42.253   |
| 8    | simlm-base-msmarco-finetuned     | NoReranker |   41.675   |   41.675   |
| 9    | jina-embeddings-v2-base-en       | NoReranker |   39.887   |   39.887   |
| 10   | bge-m3                           | NoReranker |   39.565   |   39.565   |
| 11   | msmarco-roberta-base-ance-firstp | NoReranker |   33.637   |   33.637   |
| 12   | BM25                             | NoReranker |   26.211   |   26.211   |

nDCG@10 on the **generated MS MARCO dev**:

| Rank | Model                            | Reranker   |  average   |     en     |
| ---- | :------------------------------- | :--------- | :--------: | :--------: |
| 1    | e5-mistral-7b-instruct           | NoReranker | **59.015** | **59.015** |
| 2    | bge-large-en-v1.5                | NoReranker |   55.513   |   55.513   |
| 3    | multilingual-e5-large            | NoReranker |   54.431   |   54.431   |
| 4    | bge-m3                           | NoReranker |   54.404   |   54.404   |
| 5    | bge-base-en-v1.5                 | NoReranker |   54.292   |   54.292   |
| 6    | multilingual-e5-base             | NoReranker |   52.581   |   52.581   |
| 7    | bge-small-en-v1.5                | NoReranker |   51.528   |   51.528   |
| 8    | jina-embeddings-v2-base-en       | NoReranker |   51.112   |   51.112   |
| 9    | simlm-base-msmarco-finetuned     | NoReranker |   48.102   |   48.102   |
| 10   | multilingual-e5-small            | NoReranker |   47.989   |   47.989   |
| 11   | msmarco-roberta-base-ance-firstp | NoReranker |   42.107   |   42.107   |
| 12   | BM25                             | NoReranker |   34.155   |   34.155   |

**Consistency Analysis**: `correlation = 0.7133` and `p_value (alpha=0.05) = 0.0092` indicate that the generated dataset maintains good consistency with the original dataset.

```python
from scipy.stats import spearmanr

original_msmarco_rankings  = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
generated_msmarco_rankings = [3, 6, 2, 1, 7, 5, 10, 9, 8, 4, 11, 12]

correlation, p_value = spearmanr(original_msmarco_rankings, generated_msmarco_rankings)
print(correlation, p_value)
# correlation = 0.7132867132867133
# p_value (alpha=0.05) = 0.009201779777634754
```

## Influence of Hard Negatives

nDCG@10 on the generated MS MARCO dev (**add** hard negatives):

| Rank | Model                            | Reranker   |  average   |     en     |
| ---- | :------------------------------- | :--------- | :--------: | :--------: |
| 1    | e5-mistral-7b-instruct           | NoReranker | **59.015** | **59.015** |
| 2    | bge-large-en-v1.5                | NoReranker |   55.513   |   55.513   |
| 3    | multilingual-e5-large            | NoReranker |   54.431   |   54.431   |
| 4    | bge-m3                           | NoReranker |   54.404   |   54.404   |
| 5    | bge-base-en-v1.5                 | NoReranker |   54.292   |   54.292   |
| 6    | multilingual-e5-base             | NoReranker |   52.581   |   52.581   |
| 7    | bge-small-en-v1.5                | NoReranker |   51.528   |   51.528   |
| 8    | jina-embeddings-v2-base-en       | NoReranker |   51.112   |   51.112   |
| 9    | simlm-base-msmarco-finetuned     | NoReranker |   48.102   |   48.102   |
| 10   | multilingual-e5-small            | NoReranker |   47.989   |   47.989   |
| 11   | msmarco-roberta-base-ance-firstp | NoReranker |   42.107   |   42.107   |
| 12   | BM25                             | NoReranker |   34.155   |   34.155   |

nDCG@10 on the generated MS MARCO dev (**remove** hard negatives):

| Rank | Model                            | Reranker   |  average   |     en     |
| ---- | :------------------------------- | :--------- | :--------: | :--------: |
| 1    | e5-mistral-7b-instruct           | NoReranker | **59.391** | **59.391** |
| 2    | bge-large-en-v1.5                | NoReranker |   56.975   |   56.975   |
| 3    | multilingual-e5-large            | NoReranker |   56.554   |   56.554   |
| 4    | bge-m3                           | NoReranker |   55.651   |   55.651   |
| 5    | bge-base-en-v1.5                 | NoReranker |   55.613   |   55.613   |
| 6    | multilingual-e5-base             | NoReranker |   54.597   |   54.597   |
| 7    | bge-small-en-v1.5                | NoReranker |   52.773   |   52.773   |
| 8    | jina-embeddings-v2-base-en       | NoReranker |   52.190   |   52.190   |
| 9    | multilingual-e5-small            | NoReranker |   49.919   |   49.919   |
| 10   | simlm-base-msmarco-finetuned     | NoReranker |   48.748   |   48.748   |
| 11   | msmarco-roberta-base-ance-firstp | NoReranker |   43.067   |   43.067   |
| 12   | BM25                             | NoReranker |   35.203   |   35.203   |

**Analysis**: The hard negatives will influence the difficulty of the benchmark.

## QA

#### nDCG@10 in arxiv

| Model                      | Reranker                     |  average   |     en     |
| :------------------------- | :--------------------------- | :--------: | :--------: |
| BM25                       | NoReranker                   |   32.842   |   32.842   |
| bge-base-en-v1.5           | NoReranker                   |   39.201   |   39.201   |
| bge-base-en-v1.5           | bce-reranker-base_v1         |   49.794   |   49.794   |
| bge-base-en-v1.5           | bge-reranker-large           |   50.584   |   50.584   |
| bge-base-en-v1.5           | bge-reranker-v2-m3           |   52.149   |   52.149   |
| bge-base-en-v1.5           | jina-reranker-v1-tiny-en     |   41.230   |   41.230   |
| bge-base-en-v1.5           | jina-reranker-v1-turbo-en    |   43.048   |   43.048   |
| bge-base-en-v1.5           | mmarco-mMiniLMv2-L12-H384-v1 |   37.193   |   37.193   |
| bge-large-en-v1.5          | NoReranker                   |   40.388   |   40.388   |
| bge-large-en-v1.5          | bce-reranker-base_v1         |   50.564   |   50.564   |
| bge-large-en-v1.5          | bge-reranker-large           |   50.789   |   50.789   |
| bge-large-en-v1.5          | bge-reranker-v2-m3           |   51.991   |   51.991   |
| bge-large-en-v1.5          | jina-reranker-v1-tiny-en     |   41.649   |   41.649   |
| bge-large-en-v1.5          | jina-reranker-v1-turbo-en    |   43.453   |   43.453   |
| bge-large-en-v1.5          | mmarco-mMiniLMv2-L12-H384-v1 |   36.728   |   36.728   |
| bge-m3                     | NoReranker                   |   40.802   |   40.802   |
| bge-m3                     | bce-reranker-base_v1         |   54.093   |   54.093   |
| bge-m3                     | bge-reranker-large           |   51.489   |   51.489   |
| bge-m3                     | bge-reranker-v2-m3           |   55.698   |   55.698   |
| bge-m3                     | jina-reranker-v1-tiny-en     |   49.034   |   49.034   |
| bge-m3                     | jina-reranker-v1-turbo-en    |   48.883   |   48.883   |
| bge-m3                     | mmarco-mMiniLMv2-L12-H384-v1 |   53.468   |   53.468   |
| bge-small-en-v1.5          | NoReranker                   |   36.314   |   36.314   |
| bge-small-en-v1.5          | bce-reranker-base_v1         |   48.454   |   48.454   |
| bge-small-en-v1.5          | bge-reranker-large           |   49.032   |   49.032   |
| bge-small-en-v1.5          | bge-reranker-v2-m3           |   50.539   |   50.539   |
| bge-small-en-v1.5          | jina-reranker-v1-tiny-en     |   40.607   |   40.607   |
| bge-small-en-v1.5          | jina-reranker-v1-turbo-en    |   41.777   |   41.777   |
| bge-small-en-v1.5          | mmarco-mMiniLMv2-L12-H384-v1 |   36.329   |   36.329   |
| e5-mistral-7b-instruct     | NoReranker                   |   44.780   |   44.780   |
| e5-mistral-7b-instruct     | bce-reranker-base_v1         |   48.715   |   48.715   |
| e5-mistral-7b-instruct     | bge-reranker-large           |   54.253   |   54.253   |
| e5-mistral-7b-instruct     | bge-reranker-v2-m3           | **56.512** | **56.512** |
| e5-mistral-7b-instruct     | jina-reranker-v1-tiny-en     |   44.922   |   44.922   |
| e5-mistral-7b-instruct     | jina-reranker-v1-turbo-en    |   46.845   |   46.845   |
| e5-mistral-7b-instruct     | mmarco-mMiniLMv2-L12-H384-v1 |   32.507   |   32.507   |
| jina-embeddings-v2-base-en | NoReranker                   |   36.851   |   36.851   |
| jina-embeddings-v2-base-en | bce-reranker-base_v1         |   50.811   |   50.811   |
| jina-embeddings-v2-base-en | bge-reranker-large           |   49.040   |   49.040   |
| jina-embeddings-v2-base-en | bge-reranker-v2-m3           |   52.612   |   52.612   |
| jina-embeddings-v2-base-en | jina-reranker-v1-tiny-en     |   47.263   |   47.263   |
| jina-embeddings-v2-base-en | jina-reranker-v1-turbo-en    |   46.936   |   46.936   |
| jina-embeddings-v2-base-en | mmarco-mMiniLMv2-L12-H384-v1 |   50.453   |   50.453   |
| multilingual-e5-base       | NoReranker                   |   33.291   |   33.291   |
| multilingual-e5-base       | bce-reranker-base_v1         |   49.397   |   49.397   |
| multilingual-e5-base       | bge-reranker-large           |   50.956   |   50.956   |
| multilingual-e5-base       | bge-reranker-v2-m3           |   51.486   |   51.486   |
| multilingual-e5-base       | jina-reranker-v1-tiny-en     |   45.081   |   45.081   |
| multilingual-e5-base       | jina-reranker-v1-turbo-en    |   46.018   |   46.018   |
| multilingual-e5-base       | mmarco-mMiniLMv2-L12-H384-v1 |   48.915   |   48.915   |
| multilingual-e5-large      | NoReranker                   |   36.926   |   36.926   |
| multilingual-e5-large      | bce-reranker-base_v1         |   51.533   |   51.533   |
| multilingual-e5-large      | bge-reranker-large           |   52.539   |   52.539   |
| multilingual-e5-large      | bge-reranker-v2-m3           |   54.399   |   54.399   |
| multilingual-e5-large      | jina-reranker-v1-tiny-en     |   47.122   |   47.122   |
| multilingual-e5-large      | jina-reranker-v1-turbo-en    |   47.842   |   47.842   |
| multilingual-e5-large      | mmarco-mMiniLMv2-L12-H384-v1 |   51.165   |   51.165   |
| multilingual-e5-small      | NoReranker                   |   32.384   |   32.384   |
| multilingual-e5-small      | bce-reranker-base_v1         |   49.460   |   49.460   |
| multilingual-e5-small      | bge-reranker-large           |   50.450   |   50.450   |
| multilingual-e5-small      | bge-reranker-v2-m3           |   51.165   |   51.165   |
| multilingual-e5-small      | jina-reranker-v1-tiny-en     |   44.152   |   44.152   |
| multilingual-e5-small      | jina-reranker-v1-turbo-en    |   45.482   |   45.482   |
| multilingual-e5-small      | mmarco-mMiniLMv2-L12-H384-v1 |   47.726   |   47.726   |

#### nDCG@10 in finance

| Model                      | Reranker                     |  average   |     en     |     zh     |
| :------------------------- | :--------------------------- | :--------: | :--------: | :--------: |
| BM25                       | NoReranker                   |   30.682   |   44.343   |   17.021   |
| bge-base-en-v1.5           | NoReranker                   |     -      |   48.085   |    nan     |
| bge-base-en-v1.5           | bce-reranker-base_v1         |     -      |   53.459   |    nan     |
| bge-base-en-v1.5           | bge-reranker-large           |     -      |   54.973   |    nan     |
| bge-base-en-v1.5           | bge-reranker-v2-m3           |     -      |   57.671   |    nan     |
| bge-base-en-v1.5           | jina-reranker-v1-tiny-en     |     -      |   49.352   |    nan     |
| bge-base-en-v1.5           | jina-reranker-v1-turbo-en    |     -      |   48.444   |    nan     |
| bge-base-en-v1.5           | mmarco-mMiniLMv2-L12-H384-v1 |     -      |   39.012   |    nan     |
| bge-large-en-v1.5          | NoReranker                   |     -      |   46.945   |    nan     |
| bge-large-en-v1.5          | bce-reranker-base_v1         |     -      |   53.089   |    nan     |
| bge-large-en-v1.5          | bge-reranker-large           |     -      |   54.941   |    nan     |
| bge-large-en-v1.5          | bge-reranker-v2-m3           |     -      |   57.339   |    nan     |
| bge-large-en-v1.5          | jina-reranker-v1-tiny-en     |     -      |   48.941   |    nan     |
| bge-large-en-v1.5          | jina-reranker-v1-turbo-en    |     -      |   48.133   |    nan     |
| bge-large-en-v1.5          | mmarco-mMiniLMv2-L12-H384-v1 |     -      |   37.950   |    nan     |
| bge-m3                     | NoReranker                   |   41.837   |   51.498   |   32.177   |
| bge-m3                     | bce-reranker-base_v1         | **53.922** |   59.322   |   48.523   |
| bge-m3                     | bge-reranker-large           |   51.354   |   50.109   | **52.598** |
| bge-m3                     | bge-reranker-v2-m3           |   53.741   |   59.138   |   48.343   |
| bge-m3                     | jina-reranker-v1-tiny-en     |     -      |   52.287   |    nan     |
| bge-m3                     | jina-reranker-v1-turbo-en    |     -      |   50.807   |    nan     |
| bge-m3                     | mmarco-mMiniLMv2-L12-H384-v1 |   49.641   |   54.980   |   44.303   |
| bge-small-en-v1.5          | NoReranker                   |     -      |   44.185   |    nan     |
| bge-small-en-v1.5          | bce-reranker-base_v1         |     -      |   53.017   |    nan     |
| bge-small-en-v1.5          | bge-reranker-large           |     -      |   54.225   |    nan     |
| bge-small-en-v1.5          | bge-reranker-v2-m3           |     -      |   56.464   |    nan     |
| bge-small-en-v1.5          | jina-reranker-v1-tiny-en     |     -      |   48.255   |    nan     |
| bge-small-en-v1.5          | jina-reranker-v1-turbo-en    |     -      |   47.516   |    nan     |
| bge-small-en-v1.5          | mmarco-mMiniLMv2-L12-H384-v1 |     -      |   38.081   |    nan     |
| e5-mistral-7b-instruct     | NoReranker                   |   40.441   |   54.781   |   26.101   |
| e5-mistral-7b-instruct     | bce-reranker-base_v1         |   43.581   |   51.507   |   35.656   |
| e5-mistral-7b-instruct     | bge-reranker-large           |   48.143   |   58.089   |   38.197   |
| e5-mistral-7b-instruct     | bge-reranker-v2-m3           |   48.652   |   59.675   |   37.629   |
| e5-mistral-7b-instruct     | jina-reranker-v1-tiny-en     |     -      |   50.953   |    nan     |
| e5-mistral-7b-instruct     | jina-reranker-v1-turbo-en    |     -      |   48.594   |    nan     |
| e5-mistral-7b-instruct     | mmarco-mMiniLMv2-L12-H384-v1 |   28.354   |   35.982   |   20.727   |
| jina-embeddings-v2-base-en | NoReranker                   |     -      |   41.414   |    nan     |
| jina-embeddings-v2-base-en | bce-reranker-base_v1         |     -      |   56.184   |    nan     |
| jina-embeddings-v2-base-en | bge-reranker-large           |     -      |   47.277   |    nan     |
| jina-embeddings-v2-base-en | bge-reranker-v2-m3           |     -      |   56.455   |    nan     |
| jina-embeddings-v2-base-en | jina-reranker-v1-tiny-en     |     -      |   50.335   |    nan     |
| jina-embeddings-v2-base-en | jina-reranker-v1-turbo-en    |     -      |   49.340   |    nan     |
| jina-embeddings-v2-base-en | mmarco-mMiniLMv2-L12-H384-v1 |     -      |   52.971   |    nan     |
| multilingual-e5-base       | NoReranker                   |   36.962   |   49.000   |   24.925   |
| multilingual-e5-base       | bce-reranker-base_v1         |   48.126   |   58.104   |   38.147   |
| multilingual-e5-base       | bge-reranker-large           |   50.459   |   57.599   |   43.319   |
| multilingual-e5-base       | bge-reranker-v2-m3           |   51.110   | **60.146** |   42.074   |
| multilingual-e5-base       | jina-reranker-v1-tiny-en     |   34.505   |   51.867   |   17.142   |
| multilingual-e5-base       | jina-reranker-v1-turbo-en    |   36.899   |   51.441   |   22.357   |
| multilingual-e5-base       | mmarco-mMiniLMv2-L12-H384-v1 |   44.998   |   53.540   |   36.457   |
| multilingual-e5-large      | NoReranker                   |   37.373   |   47.765   |   26.981   |
| multilingual-e5-large      | bce-reranker-base_v1         |   49.675   |   57.739   |   41.610   |
| multilingual-e5-large      | bge-reranker-large           |   51.092   |   56.917   |   45.266   |
| multilingual-e5-large      | bge-reranker-v2-m3           |   51.903   |   59.552   |   44.253   |
| multilingual-e5-large      | jina-reranker-v1-tiny-en     |     -      |   51.446   |    nan     |
| multilingual-e5-large      | jina-reranker-v1-turbo-en    |     -      |   50.879   |    nan     |
| multilingual-e5-large      | mmarco-mMiniLMv2-L12-H384-v1 |   46.273   |   53.913   |   38.632   |
| multilingual-e5-small      | NoReranker                   |   34.514   |   45.683   |   23.344   |
| multilingual-e5-small      | bce-reranker-base_v1         |   46.979   |   56.284   |   37.673   |
| multilingual-e5-small      | bge-reranker-large           |   49.297   |   56.375   |   42.220   |
| multilingual-e5-small      | bge-reranker-v2-m3           |   49.892   |   58.459   |   41.325   |
| multilingual-e5-small      | jina-reranker-v1-tiny-en     |   33.874   |   50.435   |   17.314   |
| multilingual-e5-small      | jina-reranker-v1-turbo-en    |   36.283   |   50.462   |   22.104   |
| multilingual-e5-small      | mmarco-mMiniLMv2-L12-H384-v1 |   44.139   |   52.418   |   35.859   |

#### nDCG@10 in healthcare

| Model                      | Reranker                     |  average   |     en     |     zh     |
| :------------------------- | :--------------------------- | :--------: | :--------: | :--------: |
| BM25                       | NoReranker                   |   26.841   |   35.596   |   18.087   |
| bge-base-en-v1.5           | NoReranker                   |     -      |   52.184   |    nan     |
| bge-base-en-v1.5           | bce-reranker-base_v1         |     -      |   54.467   |    nan     |
| bge-base-en-v1.5           | bge-reranker-large           |     -      |   53.881   |    nan     |
| bge-base-en-v1.5           | bge-reranker-v2-m3           |     -      |   60.910   |    nan     |
| bge-base-en-v1.5           | jina-reranker-v1-tiny-en     |     -      |   48.083   |    nan     |
| bge-base-en-v1.5           | jina-reranker-v1-turbo-en    |     -      |   46.528   |    nan     |
| bge-base-en-v1.5           | mmarco-mMiniLMv2-L12-H384-v1 |     -      |   46.245   |    nan     |
| bge-large-en-v1.5          | NoReranker                   |     -      |   52.808   |    nan     |
| bge-large-en-v1.5          | jina-reranker-v1-tiny-en     |     -      |   48.509   |    nan     |
| bge-large-en-v1.5          | jina-reranker-v1-turbo-en    |     -      |   48.075   |    nan     |
| bge-large-en-v1.5          | bce-reranker-base_v1         |     -      |   54.625   |    nan     |
| bge-large-en-v1.5          | bge-reranker-large           |     -      |   55.739   |    nan     |
| bge-large-en-v1.5          | bge-reranker-v2-m3           |     -      |   61.265   |    nan     |
| bge-large-en-v1.5          | mmarco-mMiniLMv2-L12-H384-v1 |     -      |   45.994   |    nan     |
| bge-m3                     | NoReranker                   |   45.733   |   49.084   |   42.383   |
| bge-m3                     | bce-reranker-base_v1         |   59.035   |   57.010   |   61.061   |
| bge-m3                     | bge-reranker-large           |   55.913   |   48.927   | **62.899** |
| bge-m3                     | bge-reranker-v2-m3           | **60.486** |   62.040   |   58.932   |
| bge-m3                     | jina-reranker-v1-tiny-en     |     -      |   54.678   |    nan     |
| bge-m3                     | jina-reranker-v1-turbo-en    |     -      |   52.998   |    nan     |
| bge-m3                     | mmarco-mMiniLMv2-L12-H384-v1 |   57.533   |   60.723   |   54.343   |
| bge-small-en-v1.5          | NoReranker                   |     -      |   48.469   |    nan     |
| bge-small-en-v1.5          | bce-reranker-base_v1         |     -      |   53.438   |    nan     |
| bge-small-en-v1.5          | bge-reranker-large           |     -      |   53.012   |    nan     |
| bge-small-en-v1.5          | bge-reranker-v2-m3           |     -      |   60.347   |    nan     |
| bge-small-en-v1.5          | jina-reranker-v1-tiny-en     |     -      |   47.261   |    nan     |
| bge-small-en-v1.5          | jina-reranker-v1-turbo-en    |     -      |   45.386   |    nan     |
| bge-small-en-v1.5          | mmarco-mMiniLMv2-L12-H384-v1 |     -      |   45.746   |    nan     |
| e5-mistral-7b-instruct     | NoReranker                   |   46.064   |   56.343   |   35.785   |
| e5-mistral-7b-instruct     | bce-reranker-base_v1         |   47.873   |   53.101   |   42.645   |
| e5-mistral-7b-instruct     | bge-reranker-large           |   54.916   |   59.473   |   50.360   |
| e5-mistral-7b-instruct     | bge-reranker-v2-m3           |   55.642   | **63.421** |   47.862   |
| e5-mistral-7b-instruct     | jina-reranker-v1-tiny-en     |     -      |   47.715   |    nan     |
| e5-mistral-7b-instruct     | jina-reranker-v1-turbo-en    |     -      |   48.919   |    nan     |
| e5-mistral-7b-instruct     | mmarco-mMiniLMv2-L12-H384-v1 |   34.434   |   39.053   |   29.815   |
| jina-embeddings-v2-base-en | NoReranker                   |     -      |   47.324   |    nan     |
| jina-embeddings-v2-base-en | bce-reranker-base_v1         |     -      |   55.374   |    nan     |
| jina-embeddings-v2-base-en | bge-reranker-large           |     -      |   48.954   |    nan     |
| jina-embeddings-v2-base-en | bge-reranker-v2-m3           |     -      |   61.088   |    nan     |
| jina-embeddings-v2-base-en | jina-reranker-v1-tiny-en     |     -      |   53.141   |    nan     |
| jina-embeddings-v2-base-en | jina-reranker-v1-turbo-en    |     -      |   52.344   |    nan     |
| jina-embeddings-v2-base-en | mmarco-mMiniLMv2-L12-H384-v1 |     -      |   59.331   |    nan     |
| multilingual-e5-base       | NoReranker                   |   38.740   |   49.311   |   28.169   |
| multilingual-e5-base       | bce-reranker-base_v1         |   55.180   |   58.026   |   52.333   |
| multilingual-e5-base       | bge-reranker-large           |   56.723   |   59.282   |   54.164   |
| multilingual-e5-base       | bge-reranker-v2-m3           |   57.672   |   61.927   |   53.417   |
| multilingual-e5-base       | jina-reranker-v1-tiny-en     |   35.078   |   52.854   |   17.301   |
| multilingual-e5-base       | jina-reranker-v1-turbo-en    |   38.645   |   50.699   |   26.592   |
| multilingual-e5-base       | mmarco-mMiniLMv2-L12-H384-v1 |   53.544   |   58.899   |   48.189   |
| multilingual-e5-large      | NoReranker                   |   42.182   |   50.623   |   33.742   |
| multilingual-e5-large      | bce-reranker-base_v1         |   56.175   |   57.684   |   54.667   |
| multilingual-e5-large      | bge-reranker-large           |   57.397   |   58.440   |   56.353   |
| multilingual-e5-large      | bge-reranker-v2-m3           |   58.420   |   61.871   |   54.970   |
| multilingual-e5-large      | jina-reranker-v1-tiny-en     |     -      |   52.823   |    nan     |
| multilingual-e5-large      | jina-reranker-v1-turbo-en    |     -      |   50.236   |    nan     |
| multilingual-e5-large      | mmarco-mMiniLMv2-L12-H384-v1 |   54.418   |   59.128   |   49.708   |
| multilingual-e5-small      | NoReranker                   |   36.992   |   44.664   |   29.319   |
| multilingual-e5-small      | bce-reranker-base_v1         |   54.052   |   56.197   |   51.908   |
| multilingual-e5-small      | bge-reranker-large           |   55.735   |   57.420   |   54.050   |
| multilingual-e5-small      | bge-reranker-v2-m3           |   56.428   |   59.914   |   52.941   |
| multilingual-e5-small      | jina-reranker-v1-tiny-en     |   33.985   |   51.429   |   16.540   |
| multilingual-e5-small      | jina-reranker-v1-turbo-en    |   37.441   |   49.396   |   25.486   |
| multilingual-e5-small      | mmarco-mMiniLMv2-L12-H384-v1 |   51.777   |   56.492   |   47.061   |

#### nDCG@10 in law

| Model                      | Reranker                     |  average   |     en     |     zh     |
| :------------------------- | :--------------------------- | :--------: | :--------: | :--------: |
| BM25                       | NoReranker                   |   28.604   |   19.273   |   37.935   |
| bge-base-en-v1.5           | NoReranker                   |     -      |   18.879   |    nan     |
| bge-base-en-v1.5           | bce-reranker-base_v1         |     -      |   30.352   |    nan     |
| bge-base-en-v1.5           | bge-reranker-large           |     -      |   33.224   |    nan     |
| bge-base-en-v1.5           | bge-reranker-v2-m3           |     -      |   33.598   |    nan     |
| bge-base-en-v1.5           | jina-reranker-v1-tiny-en     |     -      |   26.239   |    nan     |
| bge-base-en-v1.5           | jina-reranker-v1-turbo-en    |     -      |   26.876   |    nan     |
| bge-base-en-v1.5           | mmarco-mMiniLMv2-L12-H384-v1 |     -      |   21.783   |    nan     |
| bge-large-en-v1.5          | NoReranker                   |     -      |   26.422   |    nan     |
| bge-large-en-v1.5          | bce-reranker-base_v1         |     -      |   34.801   |    nan     |
| bge-large-en-v1.5          | bge-reranker-large           |     -      |   38.991   |    nan     |
| bge-large-en-v1.5          | bge-reranker-v2-m3           |     -      |   38.919   |    nan     |
| bge-large-en-v1.5          | jina-reranker-v1-tiny-en     |     -      |   30.135   |    nan     |
| bge-large-en-v1.5          | jina-reranker-v1-turbo-en    |     -      |   30.405   |    nan     |
| bge-large-en-v1.5          | mmarco-mMiniLMv2-L12-H384-v1 |     -      |   25.082   |    nan     |
| bge-m3                     | NoReranker                   |   47.592   |   26.687   |   68.497   |
| bge-m3                     | bce-reranker-base_v1         |   58.576   |   40.093   |   77.060   |
| bge-m3                     | bge-reranker-large           | **61.557** | **42.282** | **80.833** |
| bge-m3                     | bge-reranker-v2-m3           |   60.281   |   41.906   |   78.656   |
| bge-m3                     | jina-reranker-v1-tiny-en     |     -      |   32.476   |    nan     |
| bge-m3                     | jina-reranker-v1-turbo-en    |     -      |   32.405   |    nan     |
| bge-m3                     | mmarco-mMiniLMv2-L12-H384-v1 |   53.148   |   35.443   |   70.853   |
| bge-small-en-v1.5          | NoReranker                   |     -      |   18.189   |    nan     |
| bge-small-en-v1.5          | bce-reranker-base_v1         |     -      |   29.828   |    nan     |
| bge-small-en-v1.5          | bge-reranker-large           |     -      |   32.815   |    nan     |
| bge-small-en-v1.5          | bge-reranker-v2-m3           |     -      |   33.242   |    nan     |
| bge-small-en-v1.5          | jina-reranker-v1-tiny-en     |     -      |   25.508   |    nan     |
| bge-small-en-v1.5          | jina-reranker-v1-turbo-en    |     -      |   26.596   |    nan     |
| bge-small-en-v1.5          | mmarco-mMiniLMv2-L12-H384-v1 |     -      |   22.072   |    nan     |
| e5-mistral-7b-instruct     | NoReranker                   |   44.535   |   19.297   |   69.772   |
| e5-mistral-7b-instruct     | bce-reranker-base_v1         |   46.666   |   24.339   |   68.993   |
| e5-mistral-7b-instruct     | bge-reranker-large           |   52.918   |   30.145   |   75.691   |
| e5-mistral-7b-instruct     | bge-reranker-v2-m3           |   52.124   |   30.321   |   73.928   |
| e5-mistral-7b-instruct     | jina-reranker-v1-tiny-en     |     -      |   25.044   |    nan     |
| e5-mistral-7b-instruct     | jina-reranker-v1-turbo-en    |     -      |   24.557   |    nan     |
| e5-mistral-7b-instruct     | mmarco-mMiniLMv2-L12-H384-v1 |   30.553   |   14.533   |   46.574   |
| jina-embeddings-v2-base-en | NoReranker                   |     -      |   14.815   |    nan     |
| jina-embeddings-v2-base-en | bce-reranker-base_v1         |     -      |   28.749   |    nan     |
| jina-embeddings-v2-base-en | bge-reranker-large           |     -      |   28.241   |    nan     |
| jina-embeddings-v2-base-en | bge-reranker-v2-m3           |     -      |   28.659   |    nan     |
| jina-embeddings-v2-base-en | jina-reranker-v1-tiny-en     |     -      |   23.140   |    nan     |
| jina-embeddings-v2-base-en | jina-reranker-v1-turbo-en    |     -      |   23.244   |    nan     |
| jina-embeddings-v2-base-en | mmarco-mMiniLMv2-L12-H384-v1 |     -      |   25.426   |    nan     |
| multilingual-e5-base       | NoReranker                   |   39.400   |   15.654   |   63.146   |
| multilingual-e5-base       | bce-reranker-base_v1         |   51.517   |   30.032   |   73.002   |
| multilingual-e5-base       | bge-reranker-large           |   55.585   |   31.208   |   79.961   |
| multilingual-e5-base       | bge-reranker-v2-m3           |   55.060   |   31.598   |   78.522   |
| multilingual-e5-base       | jina-reranker-v1-tiny-en     |   24.240   |   25.449   |   23.031   |
| multilingual-e5-base       | jina-reranker-v1-turbo-en    |   30.040   |   26.109   |   33.971   |
| multilingual-e5-base       | mmarco-mMiniLMv2-L12-H384-v1 |   48.760   |   26.162   |   71.358   |
| multilingual-e5-large      | NoReranker                   |   43.261   |   19.678   |   66.845   |
| multilingual-e5-large      | bce-reranker-base_v1         |   54.036   |   34.486   |   73.587   |
| multilingual-e5-large      | bge-reranker-large           |   58.279   |   36.325   |   80.233   |
| multilingual-e5-large      | bge-reranker-v2-m3           |   57.758   |   36.657   |   78.860   |
| multilingual-e5-large      | jina-reranker-v1-tiny-en     |     -      |   28.916   |    nan     |
| multilingual-e5-large      | jina-reranker-v1-turbo-en    |     -      |   30.140   |    nan     |
| multilingual-e5-large      | mmarco-mMiniLMv2-L12-H384-v1 |   51.068   |   30.336   |   71.800   |
| multilingual-e5-small      | NoReranker                   |   36.499   |   14.607   |   58.391   |
| multilingual-e5-small      | bce-reranker-base_v1         |   50.823   |   29.581   |   72.066   |
| multilingual-e5-small      | bge-reranker-large           |   54.864   |   30.847   |   78.880   |
| multilingual-e5-small      | bge-reranker-v2-m3           |   54.394   |   31.227   |   77.561   |
| multilingual-e5-small      | jina-reranker-v1-tiny-en     |   23.911   |   24.948   |   22.873   |
| multilingual-e5-small      | jina-reranker-v1-turbo-en    |   29.403   |   26.603   |   32.204   |
| multilingual-e5-small      | mmarco-mMiniLMv2-L12-H384-v1 |   47.526   |   25.439   |   69.612   |

#### nDCG@10 in msmarco

| Model                      | Reranker                     |  average   |     en     |
| :------------------------- | :--------------------------- | :--------: | :--------: |
| BM25                       | NoReranker                   |   34.155   |   34.155   |
| bge-base-en-v1.5           | NoReranker                   |   54.292   |   54.292   |
| bge-base-en-v1.5           | bce-reranker-base_v1         |   57.923   |   57.923   |
| bge-base-en-v1.5           | bge-reranker-large           |   63.914   |   63.914   |
| bge-base-en-v1.5           | bge-reranker-v2-m3           |   64.083   |   64.083   |
| bge-base-en-v1.5           | jina-reranker-v1-tiny-en     |   44.070   |   44.070   |
| bge-base-en-v1.5           | jina-reranker-v1-turbo-en    |   47.537   |   47.537   |
| bge-base-en-v1.5           | mmarco-mMiniLMv2-L12-H384-v1 |   48.122   |   48.122   |
| bge-large-en-v1.5          | NoReranker                   |   55.513   |   55.513   |
| bge-large-en-v1.5          | bce-reranker-base_v1         |   58.409   |   58.409   |
| bge-large-en-v1.5          | bge-reranker-large           |   63.961   |   63.961   |
| bge-large-en-v1.5          | bge-reranker-v2-m3           |   64.253   |   64.253   |
| bge-large-en-v1.5          | jina-reranker-v1-tiny-en     |   44.334   |   44.334   |
| bge-large-en-v1.5          | jina-reranker-v1-turbo-en    |   48.146   |   48.146   |
| bge-large-en-v1.5          | mmarco-mMiniLMv2-L12-H384-v1 |   48.222   |   48.222   |
| bge-m3                     | NoReranker                   |   54.404   |   54.404   |
| bge-m3                     | bce-reranker-base_v1         |   62.571   |   62.571   |
| bge-m3                     | bge-reranker-large           | **71.318** | **71.318** |
| bge-m3                     | bge-reranker-v2-m3           |   70.369   |   70.369   |
| bge-m3                     | jina-reranker-v1-tiny-en     |   56.502   |   56.502   |
| bge-m3                     | jina-reranker-v1-turbo-en    |   55.981   |   55.981   |
| bge-m3                     | mmarco-mMiniLMv2-L12-H384-v1 |   69.305   |   69.305   |
| bge-small-en-v1.5          | NoReranker                   |   51.528   |   51.528   |
| bge-small-en-v1.5          | bce-reranker-base_v1         |   57.126   |   57.126   |
| bge-small-en-v1.5          | bge-reranker-large           |   63.141   |   63.141   |
| bge-small-en-v1.5          | bge-reranker-v2-m3           |   63.206   |   63.206   |
| bge-small-en-v1.5          | jina-reranker-v1-tiny-en     |   43.640   |   43.640   |
| bge-small-en-v1.5          | jina-reranker-v1-turbo-en    |   47.065   |   47.065   |
| bge-small-en-v1.5          | mmarco-mMiniLMv2-L12-H384-v1 |   47.587   |   47.587   |
| e5-mistral-7b-instruct     | NoReranker                   |   59.015   |   59.015   |
| e5-mistral-7b-instruct     | bce-reranker-base_v1         |   48.302   |   48.302   |
| e5-mistral-7b-instruct     | bge-reranker-large           |   65.692   |   65.692   |
| e5-mistral-7b-instruct     | bge-reranker-v2-m3           |   66.699   |   66.699   |
| e5-mistral-7b-instruct     | jina-reranker-v1-tiny-en     |   44.696   |   44.696   |
| e5-mistral-7b-instruct     | jina-reranker-v1-turbo-en    |   52.062   |   52.062   |
| e5-mistral-7b-instruct     | mmarco-mMiniLMv2-L12-H384-v1 |   36.391   |   36.391   |
| jina-embeddings-v2-base-en | NoReranker                   |   51.112   |   51.112   |
| jina-embeddings-v2-base-en | bce-reranker-base_v1         |   61.954   |   61.954   |
| jina-embeddings-v2-base-en | bge-reranker-large           |   70.256   |   70.256   |
| jina-embeddings-v2-base-en | bge-reranker-v2-m3           |   69.086   |   69.086   |
| jina-embeddings-v2-base-en | jina-reranker-v1-tiny-en     |   55.221   |   55.221   |
| jina-embeddings-v2-base-en | jina-reranker-v1-turbo-en    |   54.670   |   54.670   |
| jina-embeddings-v2-base-en | mmarco-mMiniLMv2-L12-H384-v1 |   68.029   |   68.029   |
| multilingual-e5-base       | NoReranker                   |   52.581   |   52.581   |
| multilingual-e5-base       | bce-reranker-base_v1         |   61.748   |   61.748   |
| multilingual-e5-base       | bge-reranker-large           |   69.668   |   69.668   |
| multilingual-e5-base       | bge-reranker-v2-m3           |   68.685   |   68.685   |
| multilingual-e5-base       | jina-reranker-v1-tiny-en     |   54.368   |   54.368   |
| multilingual-e5-base       | jina-reranker-v1-turbo-en    |   53.597   |   53.597   |
| multilingual-e5-base       | mmarco-mMiniLMv2-L12-H384-v1 |   65.390   |   65.390   |
| multilingual-e5-large      | NoReranker                   |   54.431   |   54.431   |
| multilingual-e5-large      | bce-reranker-base_v1         |   62.500   |   62.500   |
| multilingual-e5-large      | bge-reranker-large           |   69.977   |   69.977   |
| multilingual-e5-large      | bge-reranker-v2-m3           |   68.959   |   68.959   |
| multilingual-e5-large      | jina-reranker-v1-tiny-en     |   54.687   |   54.687   |
| multilingual-e5-large      | jina-reranker-v1-turbo-en    |   53.690   |   53.690   |
| multilingual-e5-large      | mmarco-mMiniLMv2-L12-H384-v1 |   65.774   |   65.774   |
| multilingual-e5-small      | NoReranker                   |   47.989   |   47.989   |
| multilingual-e5-small      | bce-reranker-base_v1         |   60.740   |   60.740   |
| multilingual-e5-small      | bge-reranker-large           |   68.422   |   68.422   |
| multilingual-e5-small      | bge-reranker-v2-m3           |   67.452   |   67.452   |
| multilingual-e5-small      | jina-reranker-v1-tiny-en     |   53.321   |   53.321   |
| multilingual-e5-small      | jina-reranker-v1-turbo-en    |   52.823   |   52.823   |
| multilingual-e5-small      | mmarco-mMiniLMv2-L12-H384-v1 |   63.954   |   63.954   |

#### nDCG@10 in news

| Model                      | Reranker                     |  average   |     en     |     zh     |
| :------------------------- | :--------------------------- | :--------: | :--------: | :--------: |
| BM25                       | NoReranker                   |   28.207   |   41.145   |   15.268   |
| bge-base-en-v1.5           | NoReranker                   |     -      |   44.098   |    nan     |
| bge-base-en-v1.5           | bce-reranker-base_v1         |     -      |   55.231   |    nan     |
| bge-base-en-v1.5           | bge-reranker-large           |     -      |   57.760   |    nan     |
| bge-base-en-v1.5           | bge-reranker-v2-m3           |     -      |   58.547   |    nan     |
| bge-base-en-v1.5           | jina-reranker-v1-tiny-en     |     -      |   48.138   |    nan     |
| bge-base-en-v1.5           | jina-reranker-v1-turbo-en    |     -      |   47.419   |    nan     |
| bge-base-en-v1.5           | mmarco-mMiniLMv2-L12-H384-v1 |     -      |   44.122   |    nan     |
| bge-large-en-v1.5          | NoReranker                   |     -      |   46.217   |    nan     |
| bge-large-en-v1.5          | bce-reranker-base_v1         |     -      |   55.833   |    nan     |
| bge-large-en-v1.5          | bge-reranker-large           |     -      |   57.917   |    nan     |
| bge-large-en-v1.5          | bge-reranker-v2-m3           |     -      |   58.748   |    nan     |
| bge-large-en-v1.5          | jina-reranker-v1-tiny-en     |     -      |   48.705   |    nan     |
| bge-large-en-v1.5          | jina-reranker-v1-turbo-en    |     -      |   48.115   |    nan     |
| bge-large-en-v1.5          | mmarco-mMiniLMv2-L12-H384-v1 |     -      |   43.905   |    nan     |
| bge-m3                     | NoReranker                   |   44.395   |   48.039   |   40.752   |
| bge-m3                     | bce-reranker-base_v1         | **62.147** |   62.551   |   61.743   |
| bge-m3                     | bge-reranker-large           |   61.565   |   59.875   | **63.254** |
| bge-m3                     | bge-reranker-v2-m3           |   61.432   | **63.787** |   59.077   |
| bge-m3                     | jina-reranker-v1-tiny-en     |     -      |   55.195   |    nan     |
| bge-m3                     | jina-reranker-v1-turbo-en    |     -      |   52.646   |    nan     |
| bge-m3                     | mmarco-mMiniLMv2-L12-H384-v1 |   56.522   |   59.596   |   53.448   |
| bge-small-en-v1.5          | NoReranker                   |     -      |   43.169   |    nan     |
| bge-small-en-v1.5          | bce-reranker-base_v1         |     -      |   54.538   |    nan     |
| bge-small-en-v1.5          | bge-reranker-large           |     -      |   56.251   |    nan     |
| bge-small-en-v1.5          | bge-reranker-v2-m3           |     -      |   57.391   |    nan     |
| bge-small-en-v1.5          | jina-reranker-v1-tiny-en     |     -      |   47.474   |    nan     |
| bge-small-en-v1.5          | jina-reranker-v1-turbo-en    |     -      |   46.642   |    nan     |
| bge-small-en-v1.5          | mmarco-mMiniLMv2-L12-H384-v1 |     -      |   43.066   |    nan     |
| e5-mistral-7b-instruct     | NoReranker                   |   42.081   |   48.176   |   35.986   |
| e5-mistral-7b-instruct     | bce-reranker-base_v1         |   46.467   |   45.662   |   47.272   |
| e5-mistral-7b-instruct     | bge-reranker-large           |   54.388   |   59.179   |   49.598   |
| e5-mistral-7b-instruct     | bge-reranker-v2-m3           |   55.961   |   60.287   |   51.635   |
| e5-mistral-7b-instruct     | jina-reranker-v1-tiny-en     |     -      |   48.766   |    nan     |
| e5-mistral-7b-instruct     | jina-reranker-v1-turbo-en    |     -      |   43.847   |    nan     |
| e5-mistral-7b-instruct     | mmarco-mMiniLMv2-L12-H384-v1 |   30.817   |   34.551   |   27.084   |
| jina-embeddings-v2-base-en | NoReranker                   |     -      |   33.736   |    nan     |
| jina-embeddings-v2-base-en | bce-reranker-base_v1         |     -      |   53.611   |    nan     |
| jina-embeddings-v2-base-en | bge-reranker-large           |     -      |   50.802   |    nan     |
| jina-embeddings-v2-base-en | bge-reranker-v2-m3           |     -      |   54.851   |    nan     |
| jina-embeddings-v2-base-en | jina-reranker-v1-tiny-en     |     -      |   48.311   |    nan     |
| jina-embeddings-v2-base-en | jina-reranker-v1-turbo-en    |     -      |   46.215   |    nan     |
| jina-embeddings-v2-base-en | mmarco-mMiniLMv2-L12-H384-v1 |     -      |   51.593   |    nan     |
| multilingual-e5-base       | NoReranker                   |   39.816   |   43.456   |   36.177   |
| multilingual-e5-base       | bce-reranker-base_v1         |   55.192   |   56.681   |   53.703   |
| multilingual-e5-base       | bge-reranker-large           |   58.554   |   59.825   |   57.284   |
| multilingual-e5-base       | bge-reranker-v2-m3           |   58.852   |   60.917   |   56.788   |
| multilingual-e5-base       | jina-reranker-v1-tiny-en     |   36.602   |   53.145   |   20.058   |
| multilingual-e5-base       | jina-reranker-v1-turbo-en    |   38.096   |   50.424   |   25.767   |
| multilingual-e5-base       | mmarco-mMiniLMv2-L12-H384-v1 |   52.004   |   55.498   |   48.510   |
| multilingual-e5-large      | NoReranker                   |   41.607   |   43.498   |   39.715   |
| multilingual-e5-large      | bce-reranker-base_v1         |   56.399   |   57.128   |   55.670   |
| multilingual-e5-large      | bge-reranker-large           |   59.028   |   59.447   |   58.610   |
| multilingual-e5-large      | bge-reranker-v2-m3           |   59.419   |   60.841   |   57.997   |
| multilingual-e5-large      | jina-reranker-v1-tiny-en     |     -      |   52.934   |    nan     |
| multilingual-e5-large      | jina-reranker-v1-turbo-en    |     -      |   50.073   |    nan     |
| multilingual-e5-large      | mmarco-mMiniLMv2-L12-H384-v1 |   52.738   |   55.723   |   49.752   |
| multilingual-e5-small      | NoReranker                   |   33.134   |   38.998   |   27.270   |
| multilingual-e5-small      | bce-reranker-base_v1         |   52.021   |   55.177   |   48.864   |
| multilingual-e5-small      | bge-reranker-large           |   54.724   |   57.982   |   51.467   |
| multilingual-e5-small      | bge-reranker-v2-m3           |   55.276   |   59.341   |   51.212   |
| multilingual-e5-small      | jina-reranker-v1-tiny-en     |   34.956   |   51.421   |   18.491   |
| multilingual-e5-small      | jina-reranker-v1-turbo-en    |   36.160   |   49.211   |   23.110   |
| multilingual-e5-small      | mmarco-mMiniLMv2-L12-H384-v1 |   49.228   |   53.842   |   44.615   |

#### nDCG@10 in web

| Model                      | Reranker                     |  average   |     en     |     zh     |
| :------------------------- | :--------------------------- | :--------: | :--------: | :--------: |
| BM25                       | NoReranker                   |   34.251   |   34.689   |   33.813   |
| bge-base-en-v1.5           | NoReranker                   |     -      |   43.962   |    nan     |
| bge-base-en-v1.5           | bce-reranker-base_v1         |     -      |   52.920   |    nan     |
| bge-base-en-v1.5           | bge-reranker-large           |     -      |   56.339   |    nan     |
| bge-base-en-v1.5           | bge-reranker-v2-m3           |     -      |   57.473   |    nan     |
| bge-base-en-v1.5           | jina-reranker-v1-tiny-en     |     -      |   46.635   |    nan     |
| bge-base-en-v1.5           | jina-reranker-v1-turbo-en    |     -      |   46.771   |    nan     |
| bge-base-en-v1.5           | mmarco-mMiniLMv2-L12-H384-v1 |     -      |   44.499   |    nan     |
| bge-large-en-v1.5          | NoReranker                   |     -      |   46.130   |    nan     |
| bge-large-en-v1.5          | bce-reranker-base_v1         |     -      |   54.547   |    nan     |
| bge-large-en-v1.5          | bge-reranker-large           |     -      |   57.657   |    nan     |
| bge-large-en-v1.5          | bge-reranker-v2-m3           |     -      |   58.817   |    nan     |
| bge-large-en-v1.5          | jina-reranker-v1-tiny-en     |     -      |   47.492   |    nan     |
| bge-large-en-v1.5          | jina-reranker-v1-turbo-en    |     -      |   47.962   |    nan     |
| bge-large-en-v1.5          | mmarco-mMiniLMv2-L12-H384-v1 |     -      |   44.889   |    nan     |
| bge-m3                     | NoReranker                   |   48.869   |   47.350   |   50.388   |
| bge-m3                     | bce-reranker-base_v1         |   62.182   |   59.502   |   64.862   |
| bge-m3                     | bge-reranker-large           |   63.050   |   58.315   | **67.786** |
| bge-m3                     | bge-reranker-v2-m3           | **64.784** | **63.665** |   65.903   |
| bge-m3                     | jina-reranker-v1-tiny-en     |     -      |   54.640   |    nan     |
| bge-m3                     | jina-reranker-v1-turbo-en    |     -      |   53.103   |    nan     |
| bge-m3                     | mmarco-mMiniLMv2-L12-H384-v1 |   56.871   |   57.833   |   55.909   |
| bge-small-en-v1.5          | NoReranker                   |     -      |   43.670   |    nan     |
| bge-small-en-v1.5          | bce-reranker-base_v1         |     -      |   52.493   |    nan     |
| bge-small-en-v1.5          | bge-reranker-large           |     -      |   55.737   |    nan     |
| bge-small-en-v1.5          | bge-reranker-v2-m3           |     -      |   57.184   |    nan     |
| bge-small-en-v1.5          | jina-reranker-v1-tiny-en     |     -      |   46.163   |    nan     |
| bge-small-en-v1.5          | jina-reranker-v1-turbo-en    |     -      |   46.192   |    nan     |
| bge-small-en-v1.5          | mmarco-mMiniLMv2-L12-H384-v1 |     -      |   44.127   |    nan     |
| e5-mistral-7b-instruct     | NoReranker                   |   45.187   |   44.412   |   45.962   |
| e5-mistral-7b-instruct     | bce-reranker-base_v1         |   47.158   |   43.231   |   51.085   |
| e5-mistral-7b-instruct     | bge-reranker-large           |   56.946   |   57.050   |   56.842   |
| e5-mistral-7b-instruct     | bge-reranker-v2-m3           |   58.603   |   59.545   |   57.661   |
| e5-mistral-7b-instruct     | jina-reranker-v1-tiny-en     |     -      |   47.543   |    nan     |
| e5-mistral-7b-instruct     | jina-reranker-v1-turbo-en    |     -      |   44.126   |    nan     |
| e5-mistral-7b-instruct     | mmarco-mMiniLMv2-L12-H384-v1 |   31.836   |   35.676   |   27.996   |
| jina-embeddings-v2-base-en | NoReranker                   |     -      |   35.439   |    nan     |
| jina-embeddings-v2-base-en | bce-reranker-base_v1         |     -      |   52.931   |    nan     |
| jina-embeddings-v2-base-en | bge-reranker-large           |     -      |   52.085   |    nan     |
| jina-embeddings-v2-base-en | bge-reranker-v2-m3           |     -      |   56.050   |    nan     |
| jina-embeddings-v2-base-en | jina-reranker-v1-tiny-en     |     -      |   48.769   |    nan     |
| jina-embeddings-v2-base-en | jina-reranker-v1-turbo-en    |     -      |   47.939   |    nan     |
| jina-embeddings-v2-base-en | mmarco-mMiniLMv2-L12-H384-v1 |     -      |   51.587   |    nan     |
| multilingual-e5-base       | NoReranker                   |   41.259   |   38.261   |   44.258   |
| multilingual-e5-base       | bce-reranker-base_v1         |   55.580   |   53.929   |   57.230   |
| multilingual-e5-base       | bge-reranker-large           |   57.197   |   53.085   |   61.310   |
| multilingual-e5-base       | bge-reranker-v2-m3           |   59.759   |   57.566   |   61.953   |
| multilingual-e5-base       | jina-reranker-v1-tiny-en     |   39.970   |   49.773   |   30.166   |
| multilingual-e5-base       | jina-reranker-v1-turbo-en    |   41.602   |   48.013   |   35.192   |
| multilingual-e5-base       | mmarco-mMiniLMv2-L12-H384-v1 |   51.524   |   50.967   |   52.082   |
| multilingual-e5-large      | NoReranker                   |   42.914   |   37.548   |   48.281   |
| multilingual-e5-large      | bce-reranker-base_v1         |   56.855   |   54.447   |   59.263   |
| multilingual-e5-large      | bge-reranker-large           |   58.596   |   54.515   |   62.677   |
| multilingual-e5-large      | bge-reranker-v2-m3           |   60.233   |   57.658   |   62.807   |
| multilingual-e5-large      | jina-reranker-v1-tiny-en     |     -      |   50.067   |    nan     |
| multilingual-e5-large      | jina-reranker-v1-turbo-en    |     -      |   48.353   |    nan     |
| multilingual-e5-large      | mmarco-mMiniLMv2-L12-H384-v1 |   52.392   |   52.055   |   52.730   |
| multilingual-e5-small      | NoReranker                   |   37.638   |   33.485   |   41.791   |
| multilingual-e5-small      | bce-reranker-base_v1         |   54.126   |   51.346   |   56.906   |
| multilingual-e5-small      | bge-reranker-large           |   54.672   |   48.955   |   60.389   |
| multilingual-e5-small      | bge-reranker-v2-m3           |   57.698   |   54.414   |   60.983   |
| multilingual-e5-small      | jina-reranker-v1-tiny-en     |   38.522   |   47.581   |   29.463   |
| multilingual-e5-small      | jina-reranker-v1-turbo-en    |   40.120   |   46.125   |   34.115   |
| multilingual-e5-small      | mmarco-mMiniLMv2-L12-H384-v1 |   49.389   |   48.500   |   50.278   |

#### nDCG@10 in wiki

| Model                      | Reranker                     |  average   |     en     |     zh     |
| :------------------------- | :--------------------------- | :--------: | :--------: | :--------: |
| BM25                       | NoReranker                   |   43.878   |   48.321   |   39.434   |
| bge-base-en-v1.5           | NoReranker                   |     -      |   57.175   |    nan     |
| bge-base-en-v1.5           | bce-reranker-base_v1         |     -      |   63.656   |    nan     |
| bge-base-en-v1.5           | bge-reranker-large           |     -      |   68.472   |    nan     |
| bge-base-en-v1.5           | bge-reranker-v2-m3           |     -      |   68.898   |    nan     |
| bge-base-en-v1.5           | jina-reranker-v1-tiny-en     |     -      |   59.364   |    nan     |
| bge-base-en-v1.5           | jina-reranker-v1-turbo-en    |     -      |   62.587   |    nan     |
| bge-base-en-v1.5           | mmarco-mMiniLMv2-L12-H384-v1 |     -      |   51.472   |    nan     |
| bge-large-en-v1.5          | NoReranker                   |     -      |   58.644   |    nan     |
| bge-large-en-v1.5          | bce-reranker-base_v1         |     -      |   64.504   |    nan     |
| bge-large-en-v1.5          | bge-reranker-large           |     -      |   68.708   |    nan     |
| bge-large-en-v1.5          | bge-reranker-v2-m3           |     -      |   69.337   |    nan     |
| bge-large-en-v1.5          | jina-reranker-v1-tiny-en     |     -      |   59.944   |    nan     |
| bge-large-en-v1.5          | jina-reranker-v1-turbo-en    |     -      |   62.805   |    nan     |
| bge-large-en-v1.5          | mmarco-mMiniLMv2-L12-H384-v1 |     -      |   51.756   |    nan     |
| bge-small-en-v1.5          | NoReranker                   |     -      |   56.160   |    nan     |
| bge-small-en-v1.5          | bce-reranker-base_v1         |     -      |   63.124   |    nan     |
| bge-small-en-v1.5          | bge-reranker-large           |     -      |   67.507   |    nan     |
| bge-small-en-v1.5          | bge-reranker-v2-m3           |     -      |   68.069   |    nan     |
| bge-small-en-v1.5          | jina-reranker-v1-tiny-en     |     -      |   58.443   |    nan     |
| bge-small-en-v1.5          | jina-reranker-v1-turbo-en    |     -      |   61.868   |    nan     |
| bge-small-en-v1.5          | mmarco-mMiniLMv2-L12-H384-v1 |     -      |   50.709   |    nan     |
| bge-m3                     | NoReranker                   |   61.431   |   60.487   |   62.374   |
| bge-m3                     | bce-reranker-base_v1         |   68.993   |   65.062   |   72.923   |
| bge-m3                     | bge-reranker-large           |   71.359   |   66.598   | **76.121** |
| bge-m3                     | bge-reranker-v2-m3           | **73.877** | **72.332** |   75.422   |
| bge-m3                     | jina-reranker-v1-tiny-en     |     -      |   66.034   |    nan     |
| bge-m3                     | jina-reranker-v1-turbo-en    |     -      |   66.338   |    nan     |
| bge-m3                     | mmarco-mMiniLMv2-L12-H384-v1 |   67.310   |   66.153   |   68.467   |
| e5-mistral-7b-instruct     | NoReranker                   |   58.804   |   61.664   |   55.945   |
| e5-mistral-7b-instruct     | bce-reranker-base_v1         |   65.532   |   64.424   |   66.639   |
| e5-mistral-7b-instruct     | bge-reranker-large           |   70.797   |   71.399   |   70.195   |
| e5-mistral-7b-instruct     | bge-reranker-v2-m3           |   70.587   |   71.481   |   69.692   |
| e5-mistral-7b-instruct     | jina-reranker-v1-tiny-en     |     -      |   61.628   |    nan     |
| e5-mistral-7b-instruct     | jina-reranker-v1-turbo-en    |     -      |   64.410   |    nan     |
| e5-mistral-7b-instruct     | mmarco-mMiniLMv2-L12-H384-v1 |   39.258   |   40.342   |   38.173   |
| jina-embeddings-v2-base-en | NoReranker                   |     -      |   53.552   |    nan     |
| jina-embeddings-v2-base-en | bce-reranker-base_v1         |     -      |   62.279   |    nan     |
| jina-embeddings-v2-base-en | bge-reranker-large           |     -      |   63.786   |    nan     |
| jina-embeddings-v2-base-en | bge-reranker-v2-m3           |     -      |   67.804   |    nan     |
| jina-embeddings-v2-base-en | jina-reranker-v1-tiny-en     |     -      |   62.295   |    nan     |
| jina-embeddings-v2-base-en | jina-reranker-v1-turbo-en    |     -      |   63.085   |    nan     |
| jina-embeddings-v2-base-en | mmarco-mMiniLMv2-L12-H384-v1 |     -      |   62.350   |    nan     |
| multilingual-e5-base       | NoReranker                   |   55.158   |   52.559   |   57.757   |
| multilingual-e5-base       | bce-reranker-base_v1         |   66.214   |   64.865   |   67.563   |
| multilingual-e5-base       | bge-reranker-large           |   69.668   |   67.899   |   71.437   |
| multilingual-e5-base       | bge-reranker-v2-m3           |   70.935   |   69.651   |   72.220   |
| multilingual-e5-base       | jina-reranker-v1-tiny-en     |   50.255   |   63.027   |   37.482   |
| multilingual-e5-base       | jina-reranker-v1-turbo-en    |   56.220   |   63.664   |   48.776   |
| multilingual-e5-base       | mmarco-mMiniLMv2-L12-H384-v1 |   62.648   |   62.092   |   63.205   |
| multilingual-e5-large      | NoReranker                   |   57.158   |   53.759   |   60.557   |
| multilingual-e5-large      | bce-reranker-base_v1         |   67.772   |   66.451   |   69.092   |
| multilingual-e5-large      | bge-reranker-large           |   71.095   |   69.565   |   72.625   |
| multilingual-e5-large      | bge-reranker-v2-m3           |   72.398   |   71.401   |   73.395   |
| multilingual-e5-large      | jina-reranker-v1-tiny-en     |     -      |   64.250   |    nan     |
| multilingual-e5-large      | jina-reranker-v1-turbo-en    |     -      |   65.030   |    nan     |
| multilingual-e5-large      | mmarco-mMiniLMv2-L12-H384-v1 |   63.823   |   64.256   |   63.390   |
| multilingual-e5-small      | NoReranker                   |   52.025   |   51.462   |   52.588   |
| multilingual-e5-small      | bce-reranker-base_v1         |   64.787   |   63.698   |   65.877   |
| multilingual-e5-small      | bge-reranker-large           |   67.395   |   66.182   |   68.609   |
| multilingual-e5-small      | bge-reranker-v2-m3           |   68.816   |   68.113   |   69.518   |
| multilingual-e5-small      | jina-reranker-v1-tiny-en     |   49.745   |   62.050   |   37.439   |
| multilingual-e5-small      | jina-reranker-v1-turbo-en    |   55.076   |   62.685   |   47.468   |
| multilingual-e5-small      | mmarco-mMiniLMv2-L12-H384-v1 |   61.041   |   61.107   |   60.976   |

## Long-Doc

#### nDCG@10 in arxiv

| Model                      | Reranker                     |  average   | en gemini  |  en gpt3   | en llama2  | en llm-survey |
| :------------------------- | :--------------------------- | :--------: | :--------: | :--------: | :--------: | :-----------: |
| BM25                       | NoReranker                   |   40.470   |   44.097   |   40.311   |   38.478   |    38.995     |
| bge-base-en-v1.5           | NoReranker                   |   49.413   |   55.375   |   48.819   |   49.089   |    44.367     |
| bge-base-en-v1.5           | bce-reranker-base_v1         |   54.453   |   56.835   |   54.548   |   56.763   |    49.665     |
| bge-base-en-v1.5           | bge-reranker-large           |   59.990   |   62.109   |   58.402   |   60.812   |    58.639     |
| bge-base-en-v1.5           | bge-reranker-v2-m3           |   61.550   |   63.490   |   59.436   |   63.949   |    59.327     |
| bge-base-en-v1.5           | jina-reranker-v1-tiny-en     |   47.526   |   53.118   |   45.153   |   49.392   |    42.441     |
| bge-base-en-v1.5           | jina-reranker-v1-turbo-en    |   49.980   |   55.406   |   45.759   |   50.414   |    48.342     |
| bge-base-en-v1.5           | mmarco-mMiniLMv2-L12-H384-v1 |   50.101   |   52.975   |   51.194   |   48.964   |    47.270     |
| bge-large-en-v1.5          | NoReranker                   |   51.704   |   58.953   |   49.084   |   50.788   |    47.990     |
| bge-large-en-v1.5          | bce-reranker-base_v1         |   53.653   |   56.206   |   54.515   |   56.706   |    47.186     |
| bge-large-en-v1.5          | bge-reranker-large           |   60.341   |   62.534   |   59.141   |   62.181   |    57.508     |
| bge-large-en-v1.5          | bge-reranker-v2-m3           |   61.697   |   63.623   |   59.317   |   64.915   |    58.932     |
| bge-large-en-v1.5          | jina-reranker-v1-tiny-en     |   47.105   |   52.803   |   44.817   |   48.541   |    42.260     |
| bge-large-en-v1.5          | jina-reranker-v1-turbo-en    |   49.892   |   55.853   |   46.064   |   50.621   |    47.032     |
| bge-large-en-v1.5          | mmarco-mMiniLMv2-L12-H384-v1 |   49.391   |   52.926   |   50.790   |   47.445   |    46.403     |
| bge-m3                     | NoReranker                   |   56.661   |   63.905   |   55.610   |   55.703   |    51.426     |
| bge-m3                     | bce-reranker-base_v1         |   57.809   |   57.835   |   57.446   |   59.566   |    56.388     |
| bge-m3                     | bge-reranker-large           |   57.324   |   60.883   |   53.360   |   61.724   |    53.328     |
| bge-m3                     | bge-reranker-v2-m3           |   64.669   |   68.046   |   61.676   |   65.830   |    63.126     |
| bge-m3                     | jina-reranker-v1-tiny-en     |   54.083   |   55.870   |   54.180   |   55.435   |    50.847     |
| bge-m3                     | jina-reranker-v1-turbo-en    |   55.504   |   60.974   |   53.258   |   54.925   |    52.860     |
| bge-m3                     | mmarco-mMiniLMv2-L12-H384-v1 |   61.522   |   64.086   |   58.471   |   62.024   |    61.508     |
| bge-small-en-v1.5          | NoReranker                   |   48.226   |   53.283   |   49.908   |   46.527   |    43.185     |
| bge-small-en-v1.5          | bce-reranker-base_v1         |   53.199   |   55.290   |   52.960   |   56.155   |    48.389     |
| bge-small-en-v1.5          | bge-reranker-large           |   59.559   |   61.892   |   58.407   |   60.463   |    57.476     |
| bge-small-en-v1.5          | bge-reranker-v2-m3           |   60.528   |   62.479   |   58.736   |   62.607   |    58.289     |
| bge-small-en-v1.5          | jina-reranker-v1-tiny-en     |   47.101   |   52.472   |   44.933   |   48.432   |    42.567     |
| bge-small-en-v1.5          | jina-reranker-v1-turbo-en    |   49.818   |   54.950   |   45.838   |   50.493   |    47.990     |
| bge-small-en-v1.5          | mmarco-mMiniLMv2-L12-H384-v1 |   48.951   |   52.348   |   49.466   |   47.848   |    46.142     |
| e5-mistral-7b-instruct     | NoReranker                   |   55.199   |   58.576   |   57.146   |   54.153   |    50.922     |
| e5-mistral-7b-instruct     | bce-reranker-base_v1         |   49.746   |   52.235   |   49.382   |   52.726   |    44.642     |
| e5-mistral-7b-instruct     | bge-reranker-large           |   59.396   |   61.414   |   58.921   |   60.848   |    56.400     |
| e5-mistral-7b-instruct     | bge-reranker-v2-m3           |   61.628   |   65.310   |   58.984   |   63.415   |    58.803     |
| e5-mistral-7b-instruct     | jina-reranker-v1-tiny-en     |   44.121   |   46.746   |   44.000   |   45.939   |    39.800     |
| e5-mistral-7b-instruct     | jina-reranker-v1-turbo-en    |   51.684   |   58.341   |   50.329   |   51.172   |    46.896     |
| e5-mistral-7b-instruct     | mmarco-mMiniLMv2-L12-H384-v1 |   34.802   |   36.663   |   36.285   |   32.707   |    33.551     |
| jina-embeddings-v2-base-en | NoReranker                   |   51.791   |   57.515   |   52.687   |   49.264   |    47.700     |
| jina-embeddings-v2-base-en | bce-reranker-base_v1         |   57.476   |   58.710   |   58.129   |   58.733   |    54.332     |
| jina-embeddings-v2-base-en | bge-reranker-large           |   56.771   |   60.728   |   52.747   |   61.311   |    52.299     |
| jina-embeddings-v2-base-en | bge-reranker-v2-m3           |   64.192   |   67.981   |   61.335   |   65.012   |    62.439     |
| jina-embeddings-v2-base-en | jina-reranker-v1-tiny-en     |   53.912   |   55.783   |   54.073   |   55.370   |    50.421     |
| jina-embeddings-v2-base-en | jina-reranker-v1-turbo-en    |   55.821   |   60.843   |   54.254   |   55.265   |    52.923     |
| jina-embeddings-v2-base-en | mmarco-mMiniLMv2-L12-H384-v1 |   61.226   |   63.614   |   58.935   |   61.388   |    60.966     |
| multilingual-e5-base       | NoReranker                   |   52.384   |   58.350   |   52.406   |   51.528   |    47.252     |
| multilingual-e5-base       | bce-reranker-base_v1         |   55.229   |   55.516   |   55.105   |   58.181   |    52.114     |
| multilingual-e5-base       | bge-reranker-large           |   62.981   |   64.923   |   60.480   |   65.507   |    61.015     |
| multilingual-e5-base       | bge-reranker-v2-m3           | **65.420** |   67.916   | **62.113** | **67.363** |  **64.288**   |
| multilingual-e5-base       | jina-reranker-v1-tiny-en     |   52.999   |   54.887   |   52.865   |   54.842   |    49.402     |
| multilingual-e5-base       | jina-reranker-v1-turbo-en    |   55.216   |   60.151   |   54.216   |   55.598   |    50.900     |
| multilingual-e5-base       | mmarco-mMiniLMv2-L12-H384-v1 |   59.271   |   63.139   |   55.440   |   59.488   |    59.019     |
| multilingual-e5-large      | NoReranker                   |   54.441   |   60.110   |   54.805   |   52.210   |    50.637     |
| multilingual-e5-large      | bce-reranker-base_v1         |   55.226   |   55.359   |   55.635   |   58.147   |    51.763     |
| multilingual-e5-large      | bge-reranker-large           |   63.068   |   65.357   |   60.329   |   65.335   |    61.250     |
| multilingual-e5-large      | bge-reranker-v2-m3           |   65.150   | **68.264** |   61.939   |   66.374   |    64.022     |
| multilingual-e5-large      | jina-reranker-v1-tiny-en     |   53.021   |   55.607   |   52.795   |   53.969   |    49.714     |
| multilingual-e5-large      | jina-reranker-v1-turbo-en    |   55.273   |   59.880   |   54.853   |   55.031   |    51.330     |
| multilingual-e5-large      | mmarco-mMiniLMv2-L12-H384-v1 |   59.496   |   63.689   |   56.466   |   59.196   |    58.633     |
| multilingual-e5-small      | NoReranker                   |   49.514   |   55.789   |   49.811   |   47.732   |    44.724     |
| multilingual-e5-small      | bce-reranker-base_v1         |   54.318   |   54.937   |   54.617   |   58.048   |    49.669     |
| multilingual-e5-small      | bge-reranker-large           |   62.830   |   65.150   |   59.946   |   65.259   |    60.966     |
| multilingual-e5-small      | bge-reranker-v2-m3           |   64.882   |   67.928   |   61.169   |   66.465   |    63.968     |
| multilingual-e5-small      | jina-reranker-v1-tiny-en     |   53.246   |   55.581   |   53.173   |   54.672   |    49.558     |
| multilingual-e5-small      | jina-reranker-v1-turbo-en    |   54.920   |   59.711   |   54.091   |   54.828   |    51.049     |
| multilingual-e5-small      | mmarco-mMiniLMv2-L12-H384-v1 |   59.218   |   63.277   |   56.047   |   59.228   |    58.319     |

#### nDCG@10 in book

| Model                      | Reranker                     |  average   | en a-brief-history-of-time_stephen-hawking | en origin-of-species_darwin |
| :------------------------- | :--------------------------- | :--------: | :----------------------------------------: | :-------------------------: |
| BM25                       | NoReranker                   |   41.405   |                   46.612                   |           36.198            |
| bge-base-en-v1.5           | NoReranker                   |   56.873   |                   62.089                   |           51.656            |
| bge-base-en-v1.5           | bce-reranker-base_v1         |   63.165   |                   66.538                   |           59.793            |
| bge-base-en-v1.5           | bge-reranker-large           |   61.113   |                   64.676                   |           57.550            |
| bge-base-en-v1.5           | bge-reranker-v2-m3           |   65.892   |                   70.164                   |           61.620            |
| bge-base-en-v1.5           | jina-reranker-v1-tiny-en     |   51.967   |                   57.270                   |           46.663            |
| bge-base-en-v1.5           | jina-reranker-v1-turbo-en    |   48.978   |                   55.861                   |           42.095            |
| bge-base-en-v1.5           | mmarco-mMiniLMv2-L12-H384-v1 |   56.200   |                   57.982                   |           54.419            |
| bge-large-en-v1.5          | NoReranker                   |   57.885   |                   62.407                   |           53.363            |
| bge-large-en-v1.5          | bce-reranker-base_v1         |   63.599   |                   66.796                   |           60.402            |
| bge-large-en-v1.5          | bge-reranker-large           |   61.810   |                   64.743                   |           58.877            |
| bge-large-en-v1.5          | bge-reranker-v2-m3           |   66.173   |                   69.921                   |           62.426            |
| bge-large-en-v1.5          | jina-reranker-v1-tiny-en     |   52.112   |                   57.034                   |           47.190            |
| bge-large-en-v1.5          | jina-reranker-v1-turbo-en    |   49.217   |                   55.622                   |           42.812            |
| bge-large-en-v1.5          | mmarco-mMiniLMv2-L12-H384-v1 |   56.681   |                   58.336                   |           55.026            |
| bge-m3                     | NoReranker                   |   59.788   |                   66.552                   |           53.025            |
| bge-m3                     | bce-reranker-base_v1         |   67.254   |                   68.229                   |           66.278            |
| bge-m3                     | bge-reranker-large           |   46.010   |                   50.817                   |           41.203            |
| bge-m3                     | bge-reranker-v2-m3           |   67.913   |                   72.050                   |           63.777            |
| bge-m3                     | jina-reranker-v1-tiny-en     |   57.685   |                   64.064                   |           51.305            |
| bge-m3                     | jina-reranker-v1-turbo-en    |   56.772   |                   62.972                   |           50.572            |
| bge-m3                     | mmarco-mMiniLMv2-L12-H384-v1 |   69.223   |                   71.828                   |           66.618            |
| bge-small-en-v1.5          | NoReranker                   |   53.514   |                   59.489                   |           47.540            |
| bge-small-en-v1.5          | bce-reranker-base_v1         |   63.041   |                   66.390                   |           59.692            |
| bge-small-en-v1.5          | bge-reranker-large           |   61.490   |                   64.663                   |           58.317            |
| bge-small-en-v1.5          | bge-reranker-v2-m3           |   65.793   |                   69.985                   |           61.602            |
| bge-small-en-v1.5          | jina-reranker-v1-tiny-en     |   52.246   |                   57.389                   |           47.103            |
| bge-small-en-v1.5          | jina-reranker-v1-turbo-en    |   48.762   |                   55.842                   |           41.683            |
| bge-small-en-v1.5          | mmarco-mMiniLMv2-L12-H384-v1 |   55.940   |                   57.497                   |           54.384            |
| e5-mistral-7b-instruct     | NoReranker                   |   61.643   |                   67.148                   |           56.139            |
| e5-mistral-7b-instruct     | bce-reranker-base_v1         |   56.435   |                   60.614                   |           52.256            |
| e5-mistral-7b-instruct     | bge-reranker-large           |   63.420   |                   67.552                   |           59.288            |
| e5-mistral-7b-instruct     | bge-reranker-v2-m3           |   65.552   |                   69.041                   |           62.064            |
| e5-mistral-7b-instruct     | jina-reranker-v1-tiny-en     |   51.258   |                   56.617                   |           45.898            |
| e5-mistral-7b-instruct     | jina-reranker-v1-turbo-en    |   51.840   |                   57.799                   |           45.881            |
| e5-mistral-7b-instruct     | mmarco-mMiniLMv2-L12-H384-v1 |   42.337   |                   44.268                   |           40.406            |
| jina-embeddings-v2-base-en | NoReranker                   |   56.766   |                   63.012                   |           50.520            |
| jina-embeddings-v2-base-en | bce-reranker-base_v1         |   67.388   |                   68.182                   |           66.593            |
| jina-embeddings-v2-base-en | bge-reranker-large           |   46.180   |                   50.342                   |           42.018            |
| jina-embeddings-v2-base-en | bge-reranker-v2-m3           |   68.289   |                   71.908                   |           64.670            |
| jina-embeddings-v2-base-en | jina-reranker-v1-tiny-en     |   57.697   |                   63.549                   |           51.845            |
| jina-embeddings-v2-base-en | jina-reranker-v1-turbo-en    |   57.737   |                   63.587                   |           51.888            |
| jina-embeddings-v2-base-en | mmarco-mMiniLMv2-L12-H384-v1 | **69.439** |                   71.571                   |         **67.308**          |
| multilingual-e5-base       | NoReranker                   |   55.595   |                   62.142                   |           49.048            |
| multilingual-e5-base       | bce-reranker-base_v1         |   65.203   |                   67.307                   |           63.098            |
| multilingual-e5-base       | bge-reranker-large           |   65.781   |                   70.132                   |           61.429            |
| multilingual-e5-base       | bge-reranker-v2-m3           |   68.552   |                 **73.087**                 |           64.018            |
| multilingual-e5-base       | jina-reranker-v1-tiny-en     |   57.117   |                   64.005                   |           50.230            |
| multilingual-e5-base       | jina-reranker-v1-turbo-en    |   56.786   |                   63.673                   |           49.899            |
| multilingual-e5-base       | mmarco-mMiniLMv2-L12-H384-v1 |   67.797   |                   70.923                   |           64.672            |
| multilingual-e5-large      | NoReranker                   |   58.527   |                   64.557                   |           52.497            |
| multilingual-e5-large      | bce-reranker-base_v1         |   65.380   |                   67.317                   |           63.444            |
| multilingual-e5-large      | bge-reranker-large           |   65.284   |                   69.839                   |           60.728            |
| multilingual-e5-large      | bge-reranker-v2-m3           |   68.499   |                   72.652                   |           64.347            |
| multilingual-e5-large      | jina-reranker-v1-tiny-en     |   57.054   |                   63.571                   |           50.537            |
| multilingual-e5-large      | jina-reranker-v1-turbo-en    |   56.867   |                   63.762                   |           49.972            |
| multilingual-e5-large      | mmarco-mMiniLMv2-L12-H384-v1 |   68.041   |                   70.686                   |           65.396            |
| multilingual-e5-small      | NoReranker                   |   50.362   |                   57.010                   |           43.714            |
| multilingual-e5-small      | bce-reranker-base_v1         |   64.308   |                   66.446                   |           62.170            |
| multilingual-e5-small      | bge-reranker-large           |   64.967   |                   69.477                   |           60.457            |
| multilingual-e5-small      | bge-reranker-v2-m3           |   67.721   |                   72.230                   |           63.212            |
| multilingual-e5-small      | jina-reranker-v1-tiny-en     |   55.695   |                   62.676                   |           48.714            |
| multilingual-e5-small      | jina-reranker-v1-turbo-en    |   55.513   |                   62.747                   |           48.279            |
| multilingual-e5-small      | mmarco-mMiniLMv2-L12-H384-v1 |   66.835   |                   70.152                   |           63.518            |

#### nDCG@10 in healthcare

| Model                      | Reranker                     |  average   | en pubmed_100K-200K_1 | en pubmed_100K-200K_2 | en pubmed_100K-200K_3 | en pubmed_30K-40K_10-merged | en pubmed_40K-50K_5-merged |
| :------------------------- | :--------------------------- | :--------: | :-------------------: | :-------------------: | :-------------------: | :-------------------------: | :------------------------: |
| BM25                       | NoReranker                   |   52.717   |        51.834         |        51.769         |        52.071         |           60.119            |           47.791           |
| bge-base-en-v1.5           | NoReranker                   |   58.825   |        56.595         |        57.196         |        58.861         |           66.618            |           54.856           |
| bge-base-en-v1.5           | bce-reranker-base_v1         |   67.906   |        66.459         |        67.025         |        65.508         |           77.239            |           63.298           |
| bge-base-en-v1.5           | bge-reranker-large           |   68.905   |        66.733         |        69.856         |        66.588         |           77.335            |           64.012           |
| bge-base-en-v1.5           | bge-reranker-v2-m3           |   70.931   |        71.461         |        71.100         |        68.137         |           78.118            |           65.840           |
| bge-base-en-v1.5           | jina-reranker-v1-tiny-en     |   59.490   |        57.006         |        61.185         |        57.087         |           66.857            |           55.317           |
| bge-base-en-v1.5           | jina-reranker-v1-turbo-en    |   61.500   |        62.574         |        61.773         |        59.736         |           67.846            |           55.571           |
| bge-base-en-v1.5           | mmarco-mMiniLMv2-L12-H384-v1 |   60.950   |        60.763         |        61.630         |        61.380         |           67.061            |           53.914           |
| bge-large-en-v1.5          | NoReranker                   |   59.060   |        58.532         |        58.142         |        59.172         |           66.316            |           53.136           |
| bge-large-en-v1.5          | bce-reranker-base_v1         |   67.992   |        66.240         |        67.599         |        65.193         |           77.487            |           63.443           |
| bge-large-en-v1.5          | bge-reranker-large           |   69.023   |        67.368         |        70.496         |        65.912         |           77.288            |           64.050           |
| bge-large-en-v1.5          | bge-reranker-v2-m3           |   70.886   |        71.308         |        71.998         |        67.088         |           77.923            |           66.112           |
| bge-large-en-v1.5          | jina-reranker-v1-tiny-en     |   59.737   |        57.474         |        61.287         |        57.331         |           66.965            |           55.629           |
| bge-large-en-v1.5          | jina-reranker-v1-turbo-en    |   61.736   |        63.745         |        62.035         |        59.859         |           67.745            |           55.298           |
| bge-large-en-v1.5          | mmarco-mMiniLMv2-L12-H384-v1 |   60.895   |        61.023         |        61.977         |        60.585         |           67.025            |           53.864           |
| bge-m3                     | NoReranker                   |   59.024   |        59.125         |        58.789         |        58.617         |           66.649            |           51.941           |
| bge-m3                     | bce-reranker-base_v1         |   71.273   |        70.055         |        70.119         |        69.900         |           80.104            |           66.188           |
| bge-m3                     | bge-reranker-large           |   62.350   |        64.123         |        64.964         |        61.652         |           65.352            |           55.658           |
| bge-m3                     | bge-reranker-v2-m3           |   73.591   |        73.918         |        73.535         |        72.598         |           81.656            |           66.248           |
| bge-m3                     | jina-reranker-v1-tiny-en     |   66.694   |        66.445         |        67.356         |        65.115         |           73.285            |           61.269           |
| bge-m3                     | jina-reranker-v1-turbo-en    |   66.460   |        66.891         |        67.144         |        65.862         |           73.236            |           59.169           |
| bge-m3                     | mmarco-mMiniLMv2-L12-H384-v1 |   73.630   |        74.450         |        73.293         |        73.583         |           80.681            |           66.145           |
| bge-small-en-v1.5          | NoReranker                   |   53.986   |        54.290         |        53.341         |        50.404         |           62.907            |           48.989           |
| bge-small-en-v1.5          | bce-reranker-base_v1         |   67.007   |        65.144         |        66.061         |        65.296         |           76.423            |           62.111           |
| bge-small-en-v1.5          | bge-reranker-large           |   67.894   |        65.671         |        68.716         |        66.152         |           76.777            |           62.152           |
| bge-small-en-v1.5          | bge-reranker-v2-m3           |   69.776   |        69.545         |        70.201         |        67.991         |           77.213            |           63.929           |
| bge-small-en-v1.5          | jina-reranker-v1-tiny-en     |   58.831   |        57.090         |        60.168         |        56.746         |           66.482            |           53.671           |
| bge-small-en-v1.5          | jina-reranker-v1-turbo-en    |   60.598   |        61.480         |        60.917         |        59.333         |           67.240            |           54.020           |
| bge-small-en-v1.5          | mmarco-mMiniLMv2-L12-H384-v1 |   60.121   |        58.372         |        60.513         |        61.767         |           66.612            |           53.342           |
| e5-mistral-7b-instruct     | NoReranker                   |   61.242   |        57.637         |        61.058         |        61.081         |           70.342            |           56.091           |
| e5-mistral-7b-instruct     | bce-reranker-base_v1         |   64.240   |        61.065         |        64.988         |        62.094         |           72.665            |           60.389           |
| e5-mistral-7b-instruct     | bge-reranker-large           |   69.165   |        66.804         |        70.280         |        67.081         |           77.999            |           63.660           |
| e5-mistral-7b-instruct     | bge-reranker-v2-m3           |   71.280   |        69.722         |        72.975         |        68.494         |           80.045            |           65.162           |
| e5-mistral-7b-instruct     | jina-reranker-v1-tiny-en     |   58.509   |        55.346         |        60.712         |        57.262         |           65.963            |           53.261           |
| e5-mistral-7b-instruct     | jina-reranker-v1-turbo-en    |   64.092   |        62.536         |        65.104         |        63.131         |           71.551            |           58.138           |
| e5-mistral-7b-instruct     | mmarco-mMiniLMv2-L12-H384-v1 |   49.205   |        46.237         |        51.053         |        47.740         |           56.511            |           44.485           |
| jina-embeddings-v2-base-en | NoReranker                   |   55.817   |        52.898         |        56.472         |        56.509         |           64.306            |           48.902           |
| jina-embeddings-v2-base-en | bce-reranker-base_v1         |   71.090   |        68.582         |        68.908         |        70.784         |           79.782            |           67.393           |
| jina-embeddings-v2-base-en | bge-reranker-large           |   62.517   |        62.820         |        63.772         |        62.309         |           66.331            |           57.355           |
| jina-embeddings-v2-base-en | bge-reranker-v2-m3           |   73.081   |        71.909         |        72.986         |        72.369         |           80.653            |           67.487           |
| jina-embeddings-v2-base-en | jina-reranker-v1-tiny-en     |   66.099   |        64.471         |        66.933         |        65.059         |           72.445            |           61.586           |
| jina-embeddings-v2-base-en | jina-reranker-v1-turbo-en    |   65.786   |        64.892         |        66.031         |        65.958         |           72.881            |           59.170           |
| jina-embeddings-v2-base-en | mmarco-mMiniLMv2-L12-H384-v1 |   73.152   |        72.209         |        71.923         |      **73.665**       |           80.372            |         **67.590**         |
| multilingual-e5-base       | NoReranker                   |   57.427   |        57.663         |        54.213         |        56.444         |           66.255            |           52.562           |
| multilingual-e5-base       | bce-reranker-base_v1         |   71.205   |        69.794         |        71.343         |        70.217         |           79.507            |           65.162           |
| multilingual-e5-base       | bge-reranker-large           |   72.342   |        71.816         |        72.979         |        71.910         |           80.743            |           64.264           |
| multilingual-e5-base       | bge-reranker-v2-m3           |   73.935   |      **74.857**       |        74.304         |        71.535         |         **82.550**          |           66.427           |
| multilingual-e5-base       | jina-reranker-v1-tiny-en     |   65.248   |        65.671         |        66.026         |        63.120         |           72.184            |           59.241           |
| multilingual-e5-base       | jina-reranker-v1-turbo-en    |   66.039   |        67.112         |        66.498         |        65.757         |           73.065            |           57.761           |
| multilingual-e5-base       | mmarco-mMiniLMv2-L12-H384-v1 |   72.230   |        73.338         |        71.119         |        71.735         |           79.725            |           65.233           |
| multilingual-e5-large      | NoReranker                   |   57.722   |        57.759         |        54.873         |        56.541         |           66.086            |           53.350           |
| multilingual-e5-large      | bce-reranker-base_v1         |   71.074   |        68.658         |        70.901         |        70.198         |           79.349            |           66.264           |
| multilingual-e5-large      | bge-reranker-large           |   72.612   |        71.544         |        73.482         |        72.145         |           80.859            |           65.028           |
| multilingual-e5-large      | bge-reranker-v2-m3           | **74.100** |        73.825         |      **75.020**       |        72.020         |           82.436            |           67.198           |
| multilingual-e5-large      | jina-reranker-v1-tiny-en     |   65.369   |        65.099         |        66.610         |        63.502         |           71.842            |           59.791           |
| multilingual-e5-large      | jina-reranker-v1-turbo-en    |   65.758   |        65.766         |        66.630         |        65.835         |           72.597            |           57.961           |
| multilingual-e5-large      | mmarco-mMiniLMv2-L12-H384-v1 |   72.040   |        72.206         |        71.101         |        72.102         |           79.240            |           65.553           |
| multilingual-e5-small      | NoReranker                   |   53.259   |        51.549         |        51.844         |        50.216         |           62.787            |           49.897           |
| multilingual-e5-small      | bce-reranker-base_v1         |   70.477   |        68.702         |        70.207         |        69.212         |           78.899            |           65.363           |
| multilingual-e5-small      | bge-reranker-large           |   71.839   |        71.029         |        72.273         |        71.048         |           80.054            |           64.792           |
| multilingual-e5-small      | bge-reranker-v2-m3           |   73.398   |        73.714         |        73.998         |        70.976         |           81.675            |           66.626           |
| multilingual-e5-small      | jina-reranker-v1-tiny-en     |   64.743   |        65.260         |        65.039         |        63.313         |           70.983            |           59.120           |
| multilingual-e5-small      | jina-reranker-v1-turbo-en    |   65.331   |        65.421         |        66.063         |        65.187         |           72.468            |           57.517           |
| multilingual-e5-small      | mmarco-mMiniLMv2-L12-H384-v1 |   71.346   |        71.890         |        70.496         |        71.365         |           78.787            |           64.190           |

#### nDCG@10 in law

| Model                      | Reranker                     |  average   | en lex_files_300K-400K | en lex_files_400K-500K | en lex_files_500K-600K | en lex_files_600K-700K |
| :------------------------- | :--------------------------- | :--------: | :--------------------: | :--------------------: | :--------------------: | :--------------------: |
| BM25                       | NoReranker                   |   40.581   |         44.496         |         37.604         |         36.844         |         43.382         |
| bge-base-en-v1.5           | NoReranker                   |   56.022   |         62.721         |         54.350         |         55.810         |         51.205         |
| bge-base-en-v1.5           | bce-reranker-base_v1         |   65.594   |         70.467         |         61.905         |         64.488         |         65.516         |
| bge-base-en-v1.5           | bge-reranker-large           |   67.887   |         71.740         |         65.134         |         65.881         |         68.791         |
| bge-base-en-v1.5           | bge-reranker-v2-m3           |   70.296   |         74.181         |         67.739         |         70.365         |         68.898         |
| bge-base-en-v1.5           | jina-reranker-v1-tiny-en     |   47.267   |         50.487         |         43.834         |         45.441         |         49.305         |
| bge-base-en-v1.5           | jina-reranker-v1-turbo-en    |   51.365   |         54.405         |         48.053         |         49.536         |         53.468         |
| bge-base-en-v1.5           | mmarco-mMiniLMv2-L12-H384-v1 |   58.665   |         62.809         |         54.742         |         57.837         |         59.273         |
| bge-large-en-v1.5          | NoReranker                   |   57.622   |         63.352         |         55.437         |         57.673         |         54.026         |
| bge-large-en-v1.5          | bce-reranker-base_v1         |   65.593   |         70.005         |         61.876         |         64.026         |         66.465         |
| bge-large-en-v1.5          | bge-reranker-large           |   68.242   |         72.289         |         66.875         |         65.272         |         68.530         |
| bge-large-en-v1.5          | bge-reranker-v2-m3           |   70.709   |         74.924         |         68.846         |         69.890         |         69.177         |
| bge-large-en-v1.5          | jina-reranker-v1-tiny-en     |   47.462   |         51.239         |         43.801         |         45.490         |         49.318         |
| bge-large-en-v1.5          | jina-reranker-v1-turbo-en    |   52.120   |         55.694         |         48.681         |         50.089         |         54.016         |
| bge-large-en-v1.5          | mmarco-mMiniLMv2-L12-H384-v1 |   58.793   |         62.811         |         54.859         |         57.860         |         59.641         |
| bge-m3                     | NoReranker                   |   59.876   |         65.151         |         59.222         |         58.091         |         57.041         |
| bge-m3                     | bce-reranker-base_v1         |   71.748   |         74.999         |         70.972         |         70.105         |         70.914         |
| bge-m3                     | bge-reranker-large           |   61.136   |         62.799         |         61.023         |         56.778         |         63.944         |
| bge-m3                     | bge-reranker-v2-m3           | **74.445** |       **78.798**       |       **72.082**       |       **73.359**       |         73.540         |
| bge-m3                     | jina-reranker-v1-tiny-en     |   56.650   |         60.474         |         53.798         |         55.159         |         57.170         |
| bge-m3                     | jina-reranker-v1-turbo-en    |   58.691   |         62.403         |         54.696         |         57.071         |         60.593         |
| bge-m3                     | mmarco-mMiniLMv2-L12-H384-v1 |   72.076   |         76.183         |         70.583         |         71.716         |         69.821         |
| bge-small-en-v1.5          | NoReranker                   |   51.715   |         59.502         |         50.332         |         49.408         |         47.619         |
| bge-small-en-v1.5          | bce-reranker-base_v1         |   65.025   |         70.078         |         61.831         |         63.407         |         64.784         |
| bge-small-en-v1.5          | bge-reranker-large           |   67.272   |         71.916         |         64.457         |         65.339         |         67.375         |
| bge-small-en-v1.5          | bge-reranker-v2-m3           |   69.573   |         73.722         |         67.489         |         69.656         |         67.426         |
| bge-small-en-v1.5          | jina-reranker-v1-tiny-en     |   47.053   |         49.863         |         43.781         |         45.970         |         48.599         |
| bge-small-en-v1.5          | jina-reranker-v1-turbo-en    |   50.853   |         54.326         |         47.495         |         49.625         |         51.966         |
| bge-small-en-v1.5          | mmarco-mMiniLMv2-L12-H384-v1 |   57.939   |         62.034         |         54.357         |         57.657         |         57.707         |
| e5-mistral-7b-instruct     | NoReranker                   |   57.457   |         64.791         |         53.489         |         56.662         |         54.886         |
| e5-mistral-7b-instruct     | bce-reranker-base_v1         |   60.348   |         65.742         |         57.516         |         58.213         |         59.921         |
| e5-mistral-7b-instruct     | bge-reranker-large           |   67.874   |         73.234         |         65.290         |         64.927         |         68.045         |
| e5-mistral-7b-instruct     | bge-reranker-v2-m3           |   70.412   |         75.794         |         67.424         |         69.513         |         68.916         |
| e5-mistral-7b-instruct     | jina-reranker-v1-tiny-en     |   44.803   |         49.566         |         41.877         |         42.386         |         45.385         |
| e5-mistral-7b-instruct     | jina-reranker-v1-turbo-en    |   52.708   |         56.895         |         48.207         |         51.181         |         54.549         |
| e5-mistral-7b-instruct     | mmarco-mMiniLMv2-L12-H384-v1 |   43.480   |         48.711         |         37.195         |         41.507         |         46.507         |
| jina-embeddings-v2-base-en | NoReranker                   |   54.762   |         61.818         |         52.040         |         53.990         |         51.200         |
| jina-embeddings-v2-base-en | bce-reranker-base_v1         |   70.785   |         73.868         |         69.387         |         69.146         |         70.738         |
| jina-embeddings-v2-base-en | bge-reranker-large           |   61.293   |         63.519         |         60.028         |         56.602         |         65.024         |
| jina-embeddings-v2-base-en | bge-reranker-v2-m3           |   73.643   |         78.219         |         70.338         |         71.572         |         74.444         |
| jina-embeddings-v2-base-en | jina-reranker-v1-tiny-en     |   56.215   |         60.165         |         52.857         |         53.842         |         57.996         |
| jina-embeddings-v2-base-en | jina-reranker-v1-turbo-en    |   57.984   |         61.873         |         53.553         |         55.122         |         61.388         |
| jina-embeddings-v2-base-en | mmarco-mMiniLMv2-L12-H384-v1 |   71.353   |         75.825         |         69.399         |         69.879         |         70.308         |
| multilingual-e5-base       | NoReranker                   |   56.212   |         62.280         |         53.207         |         55.292         |         54.070         |
| multilingual-e5-base       | bce-reranker-base_v1         |   68.304   |         71.826         |         65.436         |         67.152         |         68.803         |
| multilingual-e5-base       | bge-reranker-large           |   70.385   |         74.507         |         69.008         |         66.634         |         71.389         |
| multilingual-e5-base       | bge-reranker-v2-m3           |   73.869   |         77.297         |         71.696         |         72.231         |         74.253         |
| multilingual-e5-base       | jina-reranker-v1-tiny-en     |   55.245   |         59.313         |         52.129         |         52.707         |         56.833         |
| multilingual-e5-base       | jina-reranker-v1-turbo-en    |   57.230   |         61.093         |         52.813         |         55.387         |         59.628         |
| multilingual-e5-base       | mmarco-mMiniLMv2-L12-H384-v1 |   69.683   |         73.894         |         67.617         |         68.582         |         68.638         |
| multilingual-e5-large      | NoReranker                   |   60.472   |         64.715         |         58.407         |         60.329         |         58.439         |
| multilingual-e5-large      | bce-reranker-base_v1         |   68.613   |         72.057         |         66.311         |         67.240         |         68.844         |
| multilingual-e5-large      | bge-reranker-large           |   70.817   |         74.893         |         69.442         |         67.262         |         71.671         |
| multilingual-e5-large      | bge-reranker-v2-m3           |   74.386   |         77.840         |         71.997         |         73.122         |       **74.586**       |
| multilingual-e5-large      | jina-reranker-v1-tiny-en     |   55.769   |         60.058         |         52.455         |         53.222         |         57.340         |
| multilingual-e5-large      | jina-reranker-v1-turbo-en    |   57.661   |         61.389         |         53.125         |         56.093         |         60.036         |
| multilingual-e5-large      | mmarco-mMiniLMv2-L12-H384-v1 |   69.883   |         74.756         |         67.611         |         68.833         |         68.334         |
| multilingual-e5-small      | NoReranker                   |   50.357   |         57.788         |         46.643         |         48.704         |         48.295         |
| multilingual-e5-small      | bce-reranker-base_v1         |   67.258   |         70.962         |         64.814         |         66.741         |         66.516         |
| multilingual-e5-small      | bge-reranker-large           |   70.129   |         75.062         |         68.616         |         67.106         |         69.731         |
| multilingual-e5-small      | bge-reranker-v2-m3           |   72.806   |         76.511         |         70.836         |         72.014         |         71.865         |
| multilingual-e5-small      | jina-reranker-v1-tiny-en     |   55.053   |         59.180         |         51.912         |         53.377         |         55.745         |
| multilingual-e5-small      | jina-reranker-v1-turbo-en    |   56.654   |         60.996         |         52.142         |         54.989         |         58.490         |
| multilingual-e5-small      | mmarco-mMiniLMv2-L12-H384-v1 |   69.014   |         74.335         |         66.317         |         68.385         |         67.020         |

