import pytest
from transformers import AutoTokenizer

from air_benchmark.model_utils.models import DRESModel, _transform_func_for_last_pooling


@pytest.fixture()
def model():
    return DRESModel("sentence-transformers/all-MiniLM-L6-v2", use_fp16=False)


@pytest.fixture()
def queries():
    return ["hello, world!", "AIR-Bench is awesome."]


@pytest.mark.parametrize("pooling_mtd", ["cls", "mean"])
def test_encode(model, queries, pooling_mtd):
    model.pooling_method = pooling_mtd
    results = model.encode(queries)
    assert results.shape == (2, 384)


def test_encode_queries_dict(model):
    queries = [{"text": f"this is corpus {i}"} for i in range(2)]
    results = model.encode_queries(queries)
    assert results.shape == (2, 384)


def test_encode_corpus(model):
    corpus = [
        {"title": f"this is title {i}", "text": f"this is corpus {i}"} for i in range(2)
    ]
    results = model.encode_corpus(corpus)
    assert results.shape == (2, 384)


def test__transform_func_for_last_pooling():
    examples = {
        "text": [
            "here is the loooooong text",
            "short text",
        ]
    }
    tokenizer = AutoTokenizer.from_pretrained('sentence-transformers/all-MiniLM-L6-v2')
    # last pooling using requires
    tokenizer.eos_token_id = tokenizer.sep_token_id
    results = _transform_func_for_last_pooling(examples, tokenizer)
    assert results["input_ids"].shape[0] == 2
    assert results["input_ids"][0][-1] == tokenizer.eos_token_id
    assert results["input_ids"][1][-1] == tokenizer.pad_token_id
