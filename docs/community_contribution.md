## Community Contribution

We welcome contributions such as corpus in more domains and more languages to AIR-Bench! You can upload the corpus you provide to Huggingface Hub and then open an issue in our repo. In the issue, you should provide:

- The source of the new corpus, such as link or citing.
- The domain and language of the new corpus.
- The huggingface link to download the new corpus.

The file format of the new corpus should be a jsonl file, where each line is a dict like this:

```python
{"text": str}
```
