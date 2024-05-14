## Data Generation

- [Data Generation](#data-generation)
  - [Task Type](#task-type)
  - [Domain & Language](#domain--language)
  - [Pipeline](#pipeline)
    - [Corpus Preparation](#corpus-preparation)
    - [Candidate Generation](#candidate-generation)
    - [Quality Control](#quality-control)

### Task Type

As AIR-Bench focuses on the retrieval and RAG benchmarks, we include two tasks. 
- Question-Answering (QA) is the classic task of finding answers for a given question.
- Inner-Document retrieval (Inner-Doc) is the task we proposed to evaluate the models' performance in the RAG scenario. The task is to find the related document chunk (which are usually long-text) from the whole corpus given a question.

### Domain & Language
AIR-Bench is targeting at automatically generating testing data without human intervention. Therefore, it is able to instantly support the evaluation of new domains at a very small cost with the help of LLMs.

As for the initial version `AIR-Bench_24.04`, we've covered 8 domains (including Wiki, Web, Healthcare, Law, Arxiv, News, Finance, Book) and 2 languages (including English and Chinese). 


### Pipeline

Note that we use `gpt-4-1106-preview` as the LLM through the generation pipeline.


#### Corpus Preparation

For QA task, we use the real-world datasets as the corpus, such as Wikipedia, mC4, etc.

For Long-Doc task, we firstly select the long documents, such as ArXiv papers, books, etc. Then we use the `SimpleNodeParser` from the [LlamaIndex](https://github.com/run-llama/llama_index/tree/main) to split the long document to fixed-size chunks (`chunk_size=200`, `chunk_overlap=50`) as the corpus.

#### Candidate Generation 

We use LLMs to generate query and documents following the procedure below.

![Generate Query Pipeline](images/generate_query.png)

1. Select one document from the raw corpus
2. Generate the characters who will find the document useful.
3. Generate the scenarios in which the character may find the document useful.
4. Generate the query based on the specific character and scenario.
5. Rewrite the query for multiple times to avoid the duplicated texts as in the raw corpus.
6. Generate hard negative documents based on the given query and the positive document.
7. Repeat Step 1-6

#### Quality Control

![Quality Control Pipeline](images/quality_control.png)

Given a candidate data, we run the following steps to control the quality:

1. Use the embedding model to search top-1000 relevant documents from the corpus for each query.
2. Use multiple rerankers to rerank the top-1000 relevant documents. Based on the raw label from the previous candidate generation process and the prediction results from the reranker. We categorize the documents into three groups. 
    - Type 0 are the documents that are labeled as relevant to the query. We don't filter these documents by either embedding or reranking model.
    - Type 1 are the documents that are labeled as relevant but are generated as hard negative documents. 
    - Type 2 are the documents that are generated as positive documents for other queries but labeled by the models as relevant.
    - For the other documents, we skip them and don't take any action because the models' predictions are consistent with our expectation.

    |                | `relevance` = 1 | `relevance` = 0 | `relevance` = `N/A` |
    | -------------- |-----------------|---------------|-------------------|
    | pred = `pos`   | Type 0          | Type 1        | Type 2            |
    | pred = `neg`   | Type 0          | Skip          | Skip              |
3. Use the LLM as labeler to label the documents of the three types.
    - Type 0: when the LLM prediction is negative, it means the generated query does not match the relevant document candidate well and therefore we drop the generated query. When the prediction is positive, which is the same as our expectation, we don't need to take any action. 
    - Type 1: when the LLM prediction is positive, it means the generated hard negative sample is relevant to the query and therefore we remove the document from the corpus. When the prediction is negative, which is the same as the expectation, we keep it as it is.
    - Type 2: when the LLM prediction is positive, it means there are the document is relevant to the query although it is used to generate the another query. In this case, we change the golden truth to `relevance`=1. If the prediction is negative, it meets our expectation and we keep it as it is. 

    |                | Type 0        | Type 1           | Type 2                    |
    | -------------- |---------------|------------------|---------------------------|
    | pred = `pos`   | Skip          | discard document | Change to `relevance` = 1 |
    | pred = `neg`   | discard query | Skip             | Skip                      |
4. Repeat step 1-3 for each query.

[//]: # (### Codes)

[//]: # ()
[//]: # (Here is the sample code snippet for generating the datasets)

[//]: # ()
[//]: # (```python)

[//]: # (def generate_dataset&#40;corpus, num_queries, task_type&#41;:)

[//]: # (    # Generate Triplets)

[//]: # (    triplets = [])

[//]: # (    documents = sample&#40;corpus, n=num_queries&#41;)

[//]: # (    for d in documents:)

[//]: # (        # Generate Query)

[//]: # (        q = generate_query&#40;d&#41;)

[//]: # (        # Generate Hard Negative)

[//]: # (        if task_type == 'QA':)

[//]: # (            hn = generate_hard_negative&#40;q, d&#41;)

[//]: # (        else:)

[//]: # (            hn = None)

[//]: # (        # Add New Triplet)

[//]: # (        triplets.append&#40;&#40;q, d, hn&#41;&#41;)

[//]: # ()
[//]: # (    # Build Dataset)

[//]: # (    dataset = build_dataset&#40;corpus, triplets&#41;)

[//]: # ()
[//]: # (    # Quality Control)

[//]: # (    new_dataset = quality_control&#40;dataset&#41;)

[//]: # (    return new_dataset)

[//]: # ()
[//]: # (def generate_query&#40;document&#41;:)

[//]: # (    pass)

[//]: # ()
[//]: # (def generate_hard_negative&#40;query, document&#41;:)

[//]: # (    pass)

[//]: # ()
[//]: # (def quality_control&#40;dataset&#41;:)

[//]: # (    pass)

[//]: # (```)