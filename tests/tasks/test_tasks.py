from air_benchmark.tasks.tasks import (
    LongDocTaskTable,
    QATaskTable,
    get_available_domains,
)


def test_get_available_domains():
    domains = get_available_domains()
    target = frozenset([k for k in QATaskTable] + [k for k in LongDocTaskTable])
    assert domains == sorted(target)
