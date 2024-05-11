## Data Generation

- [Data Generation](#data-generation)
  - [Task Type & Domain & Language](#task-type--domain--language)
  - [Pipeline](#pipeline)
    - [Corpus Preparation](#corpus-preparation)
    - [Query Generation](#query-generation)
    - [Hard Negative Generation](#hard-negative-generation)
    - [Quality Control](#quality-control)

### Task Type & Domain & Language

Task Types: QA, Long-Doc

Domains: Wiki, Web, Healthcare, Law, Arxiv, News, Finance, Book

Languages: 

- Current: English, Chinese

- Future: Other languages

### Pipeline

In the whole pipeline, we use `gpt-4-1106-preview` as the LLM.

```python
def generate_dataset(corpus, num_queries, task_type):
    # Generate Triplets
    triplets = []
    documents = sample(corpus, n=num_queries)
    for d in documents:
        # Generate Query
        q = generate_query(d)
        # Generate Hard Negative
        if task_type == 'QA':
            hn = generate_hard_negative(q, d)
        else:
            hn = None
        # Add New Triplet
        triplets.append((q, d, hn))

    # Build Dataset
    dataset = build_dataset(corpus, triplets)

    # Quality Control
    new_dataset = quality_control(dataset)
    return new_dataset

def generate_query(document):
    pass

def generate_hard_negative(query, document):
    pass

def quality_control(dataset):
    pass
```

#### Corpus Preparation

For QA task, we use the real-world datasets as the corpus, such as Wikipedia, mC4, etc.

For Long-Doc task, we firstly select the long documents, such as ArXiv papers, books, etc. Then we use the `SimpleNodeParser` from the [LlamaIndex](https://github.com/run-llama/llama_index/tree/main) to split the long document to fixed-size chunks (`chunk_size=200`, `chunk_overlap=50`) as the corpus.

#### Query Generation

Given a document, the pipeline generates a query as follows:

1. Let the LLM generate the characters who will find the document useful.
2. Let the LLM generate the scenarios in which the character may find the document useful.
3. Let the LLM generate the query based on the specific character and scenario.
4. Let the LLM rewrite the query 1~3 times to generate the final query.

#### Hard Negative Generation

Given a query and the positive document, the pipeline generates the hard negatives as follows:

1. Let the LLM generate 3~7 hard negatives for the given query and positive document.

#### Quality Control

Given a dataset, the pipeline will control the quality as follows:

1. Use the embedding model to search top-1000 relevant documents from the corpus for each query.
2. Use multiple rerankers to rerank the top-1000 relevant documents for each query. Then set the rank threshold to filter possible false negatives for each query.
3. Use the LLM as labeler to label the positive and possible false negatives for each query. Filter the queries with false positives, discard false hard negatives. and label the other false negatives as positives. Then the final new dataset comes out.
