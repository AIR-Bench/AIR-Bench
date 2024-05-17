# Community Contribution

## Contribute to this repo
This repo is used to maintain the codebase for running evaluations. If you find any issues and want to contribute to solve any existing issues, please follow the [Code of Conduct](https://github.com/AIR-Bench/AIR-Bench/blob/main/CODE_OF_CONDUCT.md)

Please refer to the [CONTRIBUTING](https://github.com/AIR-Bench/AIR-Bench/blob/main/CONTRIBUTING.md) page for more details.


## Contribute Corpus
You are more than welcomed to contribute corpus in more domains and more languages! 

If ...
- you want to know the models' performance on the domains and languages you care about
- you have public corpus in this domain and language, 

please follow the steps below to contribute the corpus.

### Prepare the corpus 
The file format of the new corpus should be a jsonl file, where each line is a dict like this:

```python
{"text": str}
```

### Upload the corpus to HuggingFace Hub

Create a new dataset at [HuggingFace Hub](https://huggingface.co/new-dataset) and follow the instructions to upload the corpus file you've created in the last step.

### Open an issue in this repo
Create an issue [here](https://github.com/AIR-Bench/AIR-Bench/issues/new) and describe the basic information about the new corpus including,

- task: `qa` or `long-doc`. Check the available tasks at [here](https://github.com/AIR-Bench/AIR-Bench/blob/main/docs/data_generation.md#task-type)
- domain: check the available domains at [here](https://github.com/AIR-Bench/AIR-Bench/blob/main/docs/data_generation.md#domain--language)
- language: check the available languages at [here](https://github.com/AIR-Bench/AIR-Bench/blob/main/docs/data_generation.md#domain--language)
- HuggingFace dataset url: the url of the dataset you've uploaded in the previous step

