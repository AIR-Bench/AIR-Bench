# Community Contribution

## Contribute to this repo
This repo is used to maintain the codebase for running evaluations. If you find any issues and want to contribute to solve any existing issues, please follow the [Code of Conduct](https://github.com/AIR-Bench/AIR-Bench/blob/main/CODE_OF_CONDUCT.md)

Please refer to the [CONTRIBUTING](https://github.com/AIR-Bench/AIR-Bench/blob/main/CONTRIBUTING.md) page for more details.



## Contribute Corpus
We welcome contributions such as corpus in more domains and more languages to AIR-Bench! You can upload the corpus you provide to Huggingface Hub and then open an issue in our repo. In the issue, you should provide:

- The source of the new corpus, such as link or citing.
- The domain and language of the new corpus.
- The huggingface link to download the new corpus.

The file format of the new corpus should be a jsonl file, where each line is a dict like this:

```python
{"text": str}
```
