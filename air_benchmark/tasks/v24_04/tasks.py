from air_benchmark.tasks.v24_04.long_doc_tasks import (
    LongDocArxivTask,
    LongDocBookTask,
    LongDocHealthcareTask,
    LongDocLawTask,
)
from air_benchmark.tasks.v24_04.qa_tasks import (
    QAArxivTask,
    QAFinanceTask,
    QAHealthcareTask,
    QALawTask,
    QAMSMARCOTask,
    QANewsTask,
    QAWebTask,
    QAWikiTask,
)

QATaskTable = {
    "wiki": QAWikiTask,
    "web": QAWebTask,
    "healthcare": QAHealthcareTask,
    "law": QALawTask,
    "arxiv": QAArxivTask,
    "news": QANewsTask,
    "finance": QAFinanceTask,
    "msmarco": QAMSMARCOTask,
}


LongDocTaskTable = {
    "healthcare": LongDocHealthcareTask,
    "arxiv": LongDocArxivTask,
    "law": LongDocLawTask,
    "book": LongDocBookTask,
}


TaskTable = {
    "qa": QATaskTable,
    "long-doc": LongDocTaskTable,
}
