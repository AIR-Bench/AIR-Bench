from air_benchmark.tasks.v24_05.long_doc_tasks import (
    LongDocArxivTask,
    LongDocBookTask,
    LongDocHealthcareTask,
    LongDocLawTask,
)
from air_benchmark.tasks.v24_05.qa_tasks import (
    QAArxivTask,
    QAFinanceTask,
    QAHealthcareTask,
    QALawTask,
    QAMSMARCOTask,
    QANewsTask,
    QAScienceTask,
    QAWebTask,
    QAWikiTask,
)

QATaskTable = {
    "wiki": QAWikiTask,
    "web": QAWebTask,
    "healthcare": QAHealthcareTask,
    "law": QALawTask,
    "arxiv": QAArxivTask,
    "science": QAScienceTask,
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
