## Available Tasks

- [Available Tasks](#available-tasks)
  - [AIR-Bench_24.04](#air-bench_2404)

The AIR-Bench is **dynamic**, which means it will be updated with new tasks in the future.

Latest benchmark version: `AIR-Bench_24.04`

### AIR-Bench_24.04

The following table gives you an overview of the tasks in `AIR-Bench_24.04`.

| Task Type | Domain     | Language | Source                                                       | #Query | Avg Char Len of Query | #Pos   | #Corpus   | #Hard Neg |
| --------- | ---------- | -------- | ------------------------------------------------------------ | ------ | --------------------- | ------ | --------- | --------- |
| QA        | Wiki       | English  | [Wikipedia](https://huggingface.co/datasets/NeuML/wikipedia-20240101) (20240101) | 1,727  | 79                    | 4,260  | 6,738,498 | 7,882     |
| QA        | Wiki       | Chinese  | [Wikipedia](https://huggingface.co/datasets/wikipedia) (20240401) | 1,679  | 24                    | 4,745  | 1,161,226 | 6,963     |
| QA        | Web        | English  | [mC4](https://huggingface.co/datasets/mc4)                   | 1,707  | 81                    | 5,543  | 2,459,587 | 7,439     |
| QA        | Web        | Chinese  | [mC4](https://huggingface.co/datasets/mc4)                   | 1,683  | 24                    | 6,250  | 956,699   | 6,721     |
| QA        | News       | English  | [CC-News](https://huggingface.co/datasets/cc_news)           | 1,614  | 83                    | 5,798  | 574,417   | 6,784     |
| QA        | News       | Chinese  | [Multilingual CC-News](https://huggingface.co/datasets/intfloat/multilingual_cc_news) | 1,697  | 25                    | 7,381  | 935,162   | 6,618     |
| QA        | Healthcare | English  | [PubMedQA](https://huggingface.co/datasets/qiaojin/PubMedQA) | 1,707  | 96                    | 5,052  | 847,395   | 7,023     |
| QA        | Healthcare | Chinese  | [Huatuo-26M](https://huggingface.co/datasets/FreedomIntelligence/huatuo_encyclopedia_qa) (Encyclopedia QA) | 1,874  | 22                    | 10,029 | 360,218   | 7,336     |
| QA        | Law        | English  | [pile-of-law](https://huggingface.co/datasets/pile-of-law/pile-of-law) (EUR-Lex) | 1,801  | 91                    | 5,372  | 141,678   | 6,574     |
| QA        | Finance    | English  | [Reuters-21578](https://huggingface.co/datasets/reuters21578) | 1,585  | 87                    | 3,357  | 26,266    | 5,595     |
| QA        | Finance    | Chinese  | [FinCorpus](https://huggingface.co/datasets/Duxiaoman-DI/FinCorpus) (fin_articles) | 1,805  | 24                    | 7,836  | 2,398,095 | 7,211     |
| QA        | Arxiv      | English  | [Arxiv](https://github.com/armancohan/long-summarization) (abstract) | 1,731  | 98                    | 5,340  | 222,877   | 6,288     |
| QA        | Web        | English  | [MS MARCO](https://huggingface.co/datasets/intfloat/simlm-msmarco) (dev) | 6,319  | 78                    | 31,447 | 8,872,840 | 26,828    |
| Long-Doc  | Arxiv      | English  | [gpt3](https://arxiv.org/pdf/2005.14165.pdf)                 | 337    | 81                    | 496    | 515       | -         |
| Long-Doc  | Arxiv      | English  | [llama2](https://arxiv.org/pdf/2307.09288.pdf)               | 326    | 93                    | 635    | 566       | -         |
| Long-Doc  | Arxiv      | English  | [llm-survey](https://arxiv.org/pdf/2303.18223.pdf)           | 357    | 94                    | 924    | 1,144     | -         |
| Long-Doc  | Arxiv      | English  | [gemini](https://arxiv.org/pdf/2312.11805.pdf)               | 249    | 95                    | 249    | 276       | -         |
| Long-Doc  | Book       | English  | [origin-of-species_darwin](https://www.vliz.be/docs/Zeecijfers/Origin_of_Species.pdf) | 366    | 89                    | 1,145  | 1,758     | -         |
| Long-Doc  | Book       | English  | [a-brief-history-of-time_stephen-hawking](https://www.docdroid.net/GCLN82v/stephen-hawking-a-brief-history-of-time-pdf) | 370    | 87                    | 876    | 778       | -         |
| Long-Doc  | Healthcare | English  | [pubmed_100K-200K_1](https://github.com/armancohan/long-summarization) | 372    | 94                    | 1,008  | 899       | -         |
| Long-Doc  | Healthcare | English  | [pubmed_100K-200K_2](https://github.com/armancohan/long-summarization) | 355    | 92                    | 980    | 872       | -         |
| Long-Doc  | Healthcare | English  | [pubmed_100K-200K_3](https://github.com/armancohan/long-summarization) | 357    | 93                    | 978    | 873       | -         |
| Long-Doc  | Healthcare | English  | [pubmed_40K-50K_5-merged](https://github.com/armancohan/long-summarization) | 336    | 95                    | 1,046  | 1,731     | -         |
| Long-Doc  | Healthcare | English  | [pubmed_30K-40K_10-merged](https://github.com/armancohan/long-summarization) | 368    | 94                    | 1,485  | 2,154     | -         |
| Long-Doc  | Law        | English  | [lex_files_300K-400K](https://huggingface.co/datasets/lexlms/lex_files) | 339    | 86                    | 1,307  | 2,797     | -         |
| Long-Doc  | Law        | English  | [lex_files_400K-500K](https://huggingface.co/datasets/lexlms/lex_files) | 333    | 87                    | 1,427  | 3,320     | -         |
| Long-Doc  | Law        | English  | [lex_files_500K-600K](https://huggingface.co/datasets/lexlms/lex_files) | 346    | 93                    | 1,324  | 4,087     | -         |
| Long-Doc  | Law        | English  | [lex_files_600K-700K](https://huggingface.co/datasets/lexlms/lex_files) | 338    | 96                    | 1,442  | 5,049     | -         |
