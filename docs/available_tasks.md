## Available Tasks

- [Available Tasks](#available-tasks)
  - [AIR-Bench_24.05](#air-bench_2405)
  - [AIR-Bench_24.04](#air-bench_2404)

The AIR-Bench is **dynamic**, which means it will be updated with new tasks in the future.

Latest benchmark version: `AIR-Bench_24.05`

|      Version      | Release Date | # of domains | # of languages | # of datasets |                           Details                            |
| :---------------: | :----------: | :------: | :--------: | :-------: | :----------------------------------------------------------: |
| `AIR-Bench_24.05` | Oct 17, 2024 |    9 <sup>[1]</sup>   |     13 <sup>[2]</sup>    |    69     | [here](https://github.com/AIR-Bench/AIR-Bench/blob/main/docs/available_tasks.md#air-bench_2405) |
| `AIR-Bench_24.04` | May 21, 2024 |    8 <sup>[3]</sup>    |     2 <sup>[4]</sup>     |    28     | [here](https://github.com/AIR-Bench/AIR-Bench/blob/main/docs/available_tasks.md#air-bench_2404) |

> [1] wiki, web, news, healthcare, law, finance, arxiv, book, science.
>
> [2] en, zh, es, fr, de, ru, ja, ko, ar, fa, id, hi, bn (English, Chinese, Spanish, French, German, Russian, Japanese, Korean, Arabic, Persian, Indonesian, Hindi, Bengali).
>
> [3] wiki, web, news, healthcare, law, finance, arxiv, book.
>
> [4] en, zh (English, Chinese).

Differences between versions:
- `AIR-Bench_24.05`: 69 datasets; 9 domains; 13 languages; dev and test sets; trimmed corpus size (~1M documents).
- `AIR-Bench_24.04`: initial version; 28 datasets; 8 domains; 2 languages; only test set; no limit corpus size.

### AIR-Bench_24.05

| Task | Domain | Language | Dataset Name | Source | #corpus | Avg #token of corpus | Split | # of queries | Avg #token of queries | # of positives | # of hard negatives |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| QA | Arxiv | English | default | [ArXiv (abstracts)](https://github.com/armancohan/long-summarization) | 222877 | 334 | dev | 346 | 19 | 1091 | 1230 |
| QA | Arxiv | English | default | [ArXiv (abstracts)](https://github.com/armancohan/long-summarization) | 222877 | 334 | test | 1385 | 19 | 4249 | 5058 |
| QA | Finance | English | default | [Reuters-21578](https://huggingface.co/datasets/reuters21578) | 26266 | 202 | dev | 317 | 17 | 627 | 1122 |
| QA | Finance | English | default | [Reuters-21578](https://huggingface.co/datasets/reuters21578) | 26266 | 202 | test | 1268 | 17 | 2730 | 4473 |
| QA | Finance | Chinese | default | [FinCorpus (fin_articles)](https://huggingface.co/datasets/Duxiaoman-DI/FinCorpus) | 1014974 | 1613 | dev | 361 | 29 | 1516 | 1471 |
| QA | Finance | Chinese | default | [FinCorpus (fin_articles)](https://huggingface.co/datasets/Duxiaoman-DI/FinCorpus) | 1014974 | 1613 | test | 1444 | 29 | 6320 | 5740 |
| QA | Finance | French | default | [CoFiF](https://huggingface.co/datasets/FrancophonIA/CoFiF) | 1006801 | 92 | dev | 310 | 21 | 1841 | 1071 |
| QA | Finance | French | default | [CoFiF](https://huggingface.co/datasets/FrancophonIA/CoFiF) | 1006801 | 92 | test | 1243 | 20 | 7206 | 4362 |
| QA | Finance | Arabic | default | [financial_news](https://huggingface.co/datasets/asas-ai/financial_news) | 11235 | 397 | dev | 293 | 49 | 635 | 727 |
| QA | Finance | Arabic | default | [financial_news](https://huggingface.co/datasets/asas-ai/financial_news) | 11235 | 397 | test | 1175 | 46 | 2796 | 2959 |
| QA | Healthcare | English | default | [PubMedQA](https://huggingface.co/datasets/qiaojin/PubMedQA) | 847395 | 103 | dev | 341 | 20 | 1008 | 1382 |
| QA | Healthcare | English | default | [PubMedQA](https://huggingface.co/datasets/qiaojin/PubMedQA) | 847395 | 103 | test | 1366 | 19 | 4044 | 5641 |
| QA | Healthcare | Chinese | default | [Huatuo Encyclopedia QA](https://huggingface.co/datasets/FreedomIntelligence/huatuo_encyclopedia_qa) | 360218 | 751 | dev | 374 | 31 | 2030 | 1490 |
| QA | Healthcare | Chinese | default | [Huatuo Encyclopedia QA](https://huggingface.co/datasets/FreedomIntelligence/huatuo_encyclopedia_qa) | 360218 | 751 | test | 1500 | 31 | 7999 | 5846 |
| QA | Healthcare | Spanish | default | [Multilingual Medical Corpora](https://zenodo.org/records/3463379) | 1006093 | 60 | dev | 300 | 21 | 1210 | 930 |
| QA | Healthcare | Spanish | default | [Multilingual Medical Corpora](https://zenodo.org/records/3463379) | 1006093 | 60 | test | 1201 | 22 | 4695 | 3809 |
| QA | Healthcare | French | default | [Multilingual Medical Corpora](https://zenodo.org/records/3463379) | 972938 | 202 | dev | 331 | 23 | 1885 | 1261 |
| QA | Healthcare | French | default | [Multilingual Medical Corpora](https://zenodo.org/records/3463379) | 972938 | 202 | test | 1326 | 24 | 7460 | 5119 |
| QA | Healthcare | German | default | [GEM/mlsum](https://huggingface.co/datasets/GEM/mlsum) | 27934 | 909 | dev | 360 | 21 | 1102 | 1137 |
| QA | Healthcare | German | default | [GEM/mlsum](https://huggingface.co/datasets/GEM/mlsum) | 27934 | 909 | test | 1441 | 20 | 4667 | 4306 |
| QA | Law | English | default | [Pile of Law (EUR-Lex)](https://huggingface.co/datasets/pile-of-law/pile-of-law) | 141678 | 1509 | dev | 360 | 20 | 1080 | 1341 |
| QA | Law | English | default | [Pile of Law (EUR-Lex)](https://huggingface.co/datasets/pile-of-law/pile-of-law) | 141678 | 1509 | test | 1441 | 19 | 4292 | 5233 |
| QA | Law | French | default | [Multilingual Legal Pile](https://huggingface.co/datasets/joelniklaus/Multi_Legal_Pile) | 649017 | 2540 | dev | 348 | 23 | 1371 | 1206 |
| QA | Law | French | default | [Multilingual Legal Pile](https://huggingface.co/datasets/joelniklaus/Multi_Legal_Pile) | 649017 | 2540 | test | 1394 | 22 | 5535 | 4968 |
| QA | Law | German | default | [Multilingual Legal Pile](https://huggingface.co/datasets/joelniklaus/Multi_Legal_Pile) | 752913 | 3361 | dev | 345 | 24 | 1373 | 1099 |
| QA | Law | German | default | [Multilingual Legal Pile](https://huggingface.co/datasets/joelniklaus/Multi_Legal_Pile) | 752913 | 3361 | test | 1382 | 25 | 5500 | 4622 |
| QA | Science | Russian | default | [ruSciBench](https://huggingface.co/datasets/mlsa-iai-msu-lab/ru_sci_bench) | 200532 | 347 | dev | 345 | 34 | 1577 | 1160 |
| QA | Science | Russian | default | [ruSciBench](https://huggingface.co/datasets/mlsa-iai-msu-lab/ru_sci_bench) | 200532 | 347 | test | 1382 | 33 | 6018 | 4655 |
| QA | MSMARCO (Web) | English | default | [MS MARCO (dev)](https://huggingface.co/datasets/intfloat/simlm-msmarco) | 8872840 | 81 | dev | 6319 | 16 | 31447 | 26828 |
| QA | News | English | default | [CC-News](https://huggingface.co/datasets/cc_news) | 574417 | 531 | dev | 322 | 16 | 1206 | 1375 |
| QA | News | English | default | [CC-News](https://huggingface.co/datasets/cc_news) | 574417 | 531 | test | 1292 | 16 | 4592 | 5409 |
| QA | News | Chinese | default | [Multilingual CC-News](https://huggingface.co/datasets/intfloat/multilingual_cc_news) | 935162 | 1263 | dev | 339 | 32 | 1477 | 1354 |
| QA | News | Chinese | default | [Multilingual CC-News](https://huggingface.co/datasets/intfloat/multilingual_cc_news) | 935162 | 1263 | test | 1358 | 30 | 5904 | 5264 |
| QA | News | Spanish | default | [Multilingual CC-News](https://huggingface.co/datasets/intfloat/multilingual_cc_news) | 1007104 | 615 | dev | 337 | 23 | 1541 | 1240 |
| QA | News | Spanish | default | [Multilingual CC-News](https://huggingface.co/datasets/intfloat/multilingual_cc_news) | 1007104 | 615 | test | 1351 | 23 | 6246 | 5257 |
| QA | News | French | default | [Multilingual CC-News](https://huggingface.co/datasets/intfloat/multilingual_cc_news) | 1007592 | 641 | dev | 345 | 23 | 1548 | 1424 |
| QA | News | French | default | [Multilingual CC-News](https://huggingface.co/datasets/intfloat/multilingual_cc_news) | 1007592 | 641 | test | 1383 | 22 | 6224 | 5594 |
| QA | News | German | default | [Multilingual CC-News](https://huggingface.co/datasets/intfloat/multilingual_cc_news) | 1006876 | 659 | dev | 336 | 23 | 1448 | 1234 |
| QA | News | German | default | [Multilingual CC-News](https://huggingface.co/datasets/intfloat/multilingual_cc_news) | 1006876 | 659 | test | 1348 | 23 | 5990 | 5176 |
| QA | News | Russian | default | [Multilingual CC-News](https://huggingface.co/datasets/intfloat/multilingual_cc_news) | 1004550 | 776 | dev | 337 | 34 | 1676 | 1301 |
| QA | News | Russian | default | [Multilingual CC-News](https://huggingface.co/datasets/intfloat/multilingual_cc_news) | 1004550 | 776 | test | 1352 | 33 | 6689 | 5158 |
| QA | News | Japanese | default | [Multilingual CC-News](https://huggingface.co/datasets/intfloat/multilingual_cc_news) | 834364 | 1559 | dev | 344 | 35 | 1817 | 1334 |
| QA | News | Japanese | default | [Multilingual CC-News](https://huggingface.co/datasets/intfloat/multilingual_cc_news) | 834364 | 1559 | test | 1378 | 36 | 6590 | 5197 |
| QA | News | Korean | default | [Multilingual CC-News](https://huggingface.co/datasets/intfloat/multilingual_cc_news) | 1006798 | 1072 | dev | 361 | 34 | 1967 | 1413 |
| QA | News | Korean | default | [Multilingual CC-News](https://huggingface.co/datasets/intfloat/multilingual_cc_news) | 1006798 | 1072 | test | 1447 | 36 | 7908 | 5665 |
| QA | News | Arabic | default | [Multilingual CC-News](https://huggingface.co/datasets/intfloat/multilingual_cc_news) | 1006308 | 992 | dev | 349 | 42 | 1810 | 1307 |
| QA | News | Arabic | default | [Multilingual CC-News](https://huggingface.co/datasets/intfloat/multilingual_cc_news) | 1006308 | 992 | test | 1396 | 43 | 7169 | 5266 |
| QA | News | Persian | default | [Multilingual CC-News](https://huggingface.co/datasets/intfloat/multilingual_cc_news) | 1002797 | 1351 | dev | 346 | 50 | 1952 | 1341 |
| QA | News | Persian | default | [Multilingual CC-News](https://huggingface.co/datasets/intfloat/multilingual_cc_news) | 1002797 | 1351 | test | 1386 | 48 | 7885 | 5353 |
| QA | News | Indonesian | default | [Multilingual CC-News](https://huggingface.co/datasets/intfloat/multilingual_cc_news) | 1007724 | 548 | dev | 338 | 24 | 1799 | 1397 |
| QA | News | Indonesian | default | [Multilingual CC-News](https://huggingface.co/datasets/intfloat/multilingual_cc_news) | 1007724 | 548 | test | 1356 | 24 | 7485 | 5618 |
| QA | News | Hindi | default | [Multilingual CC-News](https://huggingface.co/datasets/intfloat/multilingual_cc_news) | 1006218 | 1465 | dev | 349 | 66 | 1716 | 1264 |
| QA | News | Hindi | default | [Multilingual CC-News](https://huggingface.co/datasets/intfloat/multilingual_cc_news) | 1006218 | 1465 | test | 1398 | 67 | 7039 | 5162 |
| QA | News | Bengali | default | [Multilingual CC-News](https://huggingface.co/datasets/intfloat/multilingual_cc_news) | 20681 | 912 | dev | 289 | 84 | 562 | 741 |
| QA | News | Bengali | default | [Multilingual CC-News](https://huggingface.co/datasets/intfloat/multilingual_cc_news) | 20681 | 912 | test | 1159 | 78 | 2269 | 3013 |
| QA | Web | English | default | [mC4](https://huggingface.co/datasets/mc4) | 1012910 | 838 | dev | 341 | 16 | 1087 | 1511 |
| QA | Web | English | default | [mC4](https://huggingface.co/datasets/mc4) | 1012910 | 838 | test | 1366 | 16 | 4456 | 5928 |
| QA | Web | Chinese | default | [mC4](https://huggingface.co/datasets/mc4) | 956699 | 1208 | dev | 336 | 30 | 1230 | 1366 |
| QA | Web | Chinese | default | [mC4](https://huggingface.co/datasets/mc4) | 956699 | 1208 | test | 1347 | 29 | 5020 | 5355 |
| QA | Web | Spanish | default | [mC4](https://huggingface.co/datasets/mc4) | 403020 | 912 | dev | 341 | 23 | 1317 | 1281 |
| QA | Web | Spanish | default | [mC4](https://huggingface.co/datasets/mc4) | 403020 | 912 | test | 1368 | 24 | 5317 | 5302 |
| QA | Web | French | default | [mC4](https://huggingface.co/datasets/mc4) | 387210 | 1076 | dev | 364 | 20 | 1444 | 1451 |
| QA | Web | French | default | [mC4](https://huggingface.co/datasets/mc4) | 387210 | 1076 | test | 1457 | 20 | 5572 | 5552 |
| QA | Web | German | default | [mC4](https://huggingface.co/datasets/mc4) | 441182 | 1025 | dev | 357 | 20 | 1320 | 1345 |
| QA | Web | German | default | [mC4](https://huggingface.co/datasets/mc4) | 441182 | 1025 | test | 1432 | 20 | 5539 | 5253 |
| QA | Web | Russian | default | [mC4](https://huggingface.co/datasets/mc4) | 490581 | 1266 | dev | 324 | 32 | 1330 | 1277 |
| QA | Web | Russian | default | [mC4](https://huggingface.co/datasets/mc4) | 490581 | 1266 | test | 1297 | 33 | 5096 | 5152 |
| QA | Web | Japanese | default | [mC4](https://huggingface.co/datasets/mc4) | 547419 | 1026 | dev | 323 | 35 | 1106 | 1253 |
| QA | Web | Japanese | default | [mC4](https://huggingface.co/datasets/mc4) | 547419 | 1026 | test | 1293 | 36 | 4473 | 4976 |
| QA | Web | Korean | default | [mC4](https://huggingface.co/datasets/mc4) | 250605 | 1137 | dev | 327 | 34 | 1156 | 1083 |
| QA | Web | Korean | default | [mC4](https://huggingface.co/datasets/mc4) | 250605 | 1137 | test | 1309 | 36 | 4239 | 4457 |
| QA | Web | Arabic | default | [mC4](https://huggingface.co/datasets/mc4) | 165902 | 1686 | dev | 334 | 42 | 1133 | 1119 |
| QA | Web | Arabic | default | [mC4](https://huggingface.co/datasets/mc4) | 165902 | 1686 | test | 1338 | 42 | 4782 | 4717 |
| QA | Web | Persian | default | [mC4](https://huggingface.co/datasets/mc4) | 181463 | 2114 | dev | 338 | 49 | 1389 | 1160 |
| QA | Web | Persian | default | [mC4](https://huggingface.co/datasets/mc4) | 181463 | 2114 | test | 1354 | 47 | 5532 | 4839 |
| QA | Web | Indonesian | default | [mC4](https://huggingface.co/datasets/mc4) | 245878 | 1059 | dev | 339 | 23 | 1395 | 1295 |
| QA | Web | Indonesian | default | [mC4](https://huggingface.co/datasets/mc4) | 245878 | 1059 | test | 1356 | 23 | 5605 | 5202 |
| QA | Web | Hindi | default | [mC4](https://huggingface.co/datasets/mc4) | 50501 | 2396 | dev | 355 | 68 | 1180 | 1180 |
| QA | Web | Hindi | default | [mC4](https://huggingface.co/datasets/mc4) | 50501 | 2396 | test | 1423 | 64 | 4706 | 4481 |
| QA | Web | Bengali | default | [mC4](https://huggingface.co/datasets/mc4) | 45375 | 2161 | dev | 362 | 73 | 1142 | 1073 |
| QA | Web | Bengali | default | [mC4](https://huggingface.co/datasets/mc4) | 45375 | 2161 | test | 1451 | 77 | 4759 | 4449 |
| QA | Wiki | English | default | [Wikipedia (20240101)](https://huggingface.co/datasets/NeuML/wikipedia-20240101) | 1012092 | 665 | dev | 345 | 18 | 863 | 1576 |
| QA | Wiki | English | default | [Wikipedia (20240101)](https://huggingface.co/datasets/NeuML/wikipedia-20240101) | 1012092 | 665 | test | 1382 | 17 | 3397 | 6306 |
| QA | Wiki | Chinese | default | [Wikipedia (20240401)](https://huggingface.co/datasets/wikipedia) | 1011604 | 557 | dev | 335 | 30 | 952 | 1301 |
| QA | Wiki | Chinese | default | [Wikipedia (20240401)](https://huggingface.co/datasets/wikipedia) | 1011604 | 557 | test | 1344 | 30 | 3793 | 5662 |
| QA | Wiki | Spanish | default | [Wikipedia (20240401)](https://huggingface.co/datasets/wikipedia) | 1008147 | 801 | dev | 345 | 22 | 879 | 1451 |
| QA | Wiki | Spanish | default | [Wikipedia (20240401)](https://huggingface.co/datasets/wikipedia) | 1008147 | 801 | test | 1380 | 23 | 3531 | 5767 |
| QA | Wiki | French | default | [Wikipedia (20240401)](https://huggingface.co/datasets/wikipedia) | 1008270 | 779 | dev | 356 | 20 | 768 | 1496 |
| QA | Wiki | French | default | [Wikipedia (20240401)](https://huggingface.co/datasets/wikipedia) | 1008270 | 779 | test | 1424 | 21 | 3429 | 5989 |
| QA | Wiki | German | default | [Wikipedia (20240401)](https://huggingface.co/datasets/wikipedia) | 1008186 | 891 | dev | 350 | 23 | 817 | 1481 |
| QA | Wiki | German | default | [Wikipedia (20240401)](https://huggingface.co/datasets/wikipedia) | 1008186 | 891 | test | 1404 | 22 | 3411 | 5881 |
| QA | Wiki | Russian | default | [Wikipedia (20240401)](https://huggingface.co/datasets/wikipedia) | 1008405 | 1211 | dev | 365 | 30 | 1154 | 1505 |
| QA | Wiki | Russian | default | [Wikipedia (20240401)](https://huggingface.co/datasets/wikipedia) | 1008405 | 1211 | test | 1463 | 30 | 4516 | 6283 |
| QA | Wiki | Japanese | default | [Wikipedia (20240401)](https://huggingface.co/datasets/wikipedia) | 1008365 | 1470 | dev | 358 | 30 | 1099 | 1537 |
| QA | Wiki | Japanese | default | [Wikipedia (20240401)](https://huggingface.co/datasets/wikipedia) | 1008365 | 1470 | test | 1432 | 32 | 4303 | 6101 |
| QA | Wiki | Korean | default | [Wikipedia (20240401)](https://huggingface.co/datasets/wikipedia) | 665227 | 775 | dev | 346 | 39 | 1109 | 1423 |
| QA | Wiki | Korean | default | [Wikipedia (20240401)](https://huggingface.co/datasets/wikipedia) | 665227 | 775 | test | 1384 | 35 | 4604 | 5810 |
| QA | Wiki | Arabic | default | [Wikipedia (20240401)](https://huggingface.co/datasets/wikipedia) | 1008232 | 787 | dev | 338 | 40 | 1112 | 1438 |
| QA | Wiki | Arabic | default | [Wikipedia (20240401)](https://huggingface.co/datasets/wikipedia) | 1008232 | 787 | test | 1355 | 38 | 4467 | 5778 |
| QA | Wiki | Persian | default | [Wikipedia (20240401)](https://huggingface.co/datasets/wikipedia) | 999223 | 627 | dev | 332 | 41 | 1179 | 1444 |
| QA | Wiki | Persian | default | [Wikipedia (20240401)](https://huggingface.co/datasets/wikipedia) | 999223 | 627 | test | 1328 | 45 | 4538 | 5581 |
| QA | Wiki | Indonesian | default | [Wikipedia (20240401)](https://huggingface.co/datasets/wikipedia) | 687513 | 451 | dev | 343 | 22 | 1003 | 1365 |
| QA | Wiki | Indonesian | default | [Wikipedia (20240401)](https://huggingface.co/datasets/wikipedia) | 687513 | 451 | test | 1373 | 21 | 4089 | 5486 |
| QA | Wiki | Hindi | default | [Wikipedia (20240401)](https://huggingface.co/datasets/wikipedia) | 162188 | 997 | dev | 340 | 59 | 995 | 1324 |
| QA | Wiki | Hindi | default | [Wikipedia (20240401)](https://huggingface.co/datasets/wikipedia) | 162188 | 997 | test | 1360 | 59 | 3911 | 5225 |
| QA | Wiki | Bengali | default | [Wikipedia (20240401)](https://huggingface.co/datasets/wikipedia) | 152064 | 2129 | dev | 364 | 69 | 1016 | 1542 |
| QA | Wiki | Bengali | default | [Wikipedia (20240401)](https://huggingface.co/datasets/wikipedia) | 152064 | 2129 | test | 1456 | 71 | 4203 | 5841 |
| Long-Doc | Arxiv | English | llama2 | [llama2](https://arxiv.org/pdf/2307.09288.pdf) | 566 | 136 | dev | 326 | 18 | 635 | 0 |
| Long-Doc | Arxiv | English | gemini | [gemini](https://arxiv.org/pdf/2312.11805.pdf) | 276 | 136 | test | 249 | 18 | 249 | 0 |
| Long-Doc | Arxiv | English | gpt3 | [gpt3](https://arxiv.org/pdf/2005.14165.pdf) | 515 | 137 | test | 337 | 16 | 496 | 0 |
| Long-Doc | Arxiv | English | llm-survey | [llm-survey](https://arxiv.org/pdf/2303.18223.pdf) | 1144 | 135 | test | 357 | 17 | 924 | 0 |
| Long-Doc | Book | English | a-brief-history-of-time_stephen-hawking | [a-brief-history-of-time_stephen-hawking](https://www.docdroid.net/GCLN82v/stephen-hawking-a-brief-history-of-time-pdf) | 778 | 127 | dev | 370 | 16 | 876 | 0 |
| Long-Doc | Book | English | origin-of-species_darwin | [origin-of-species_darwin](https://www.vliz.be/docs/Zeecijfers/Origin_of_Species.pdf) | 1758 | 126 | test | 366 | 16 | 1145 | 0 |
| Long-Doc | Healthcare | English | pubmed_100K-200K_3 | [pubmed_100K-200K_3](https://huggingface.co/datasets/lexlms/lex_files) | 873 | 133 | dev | 357 | 19 | 978 | 0 |
| Long-Doc | Healthcare | English | pubmed_100K-200K_1 | [pubmed_100K-200K_1](https://huggingface.co/datasets/lexlms/lex_files) | 899 | 133 | test | 372 | 20 | 1008 | 0 |
| Long-Doc | Healthcare | English | pubmed_100K-200K_2 | [pubmed_100K-200K_2](https://huggingface.co/datasets/lexlms/lex_files) | 872 | 136 | test | 355 | 18 | 980 | 0 |
| Long-Doc | Healthcare | English | pubmed_30K-40K_10-merged | [pubmed_30K-40K_10-merged](https://huggingface.co/datasets/lexlms/lex_files) | 2154 | 133 | test | 368 | 18 | 1485 | 0 |
| Long-Doc | Healthcare | English | pubmed_40K-50K_5-merged | [pubmed_40K-50K_5-merged](https://huggingface.co/datasets/lexlms/lex_files) | 1731 | 136 | test | 336 | 21 | 1046 | 0 |
| Long-Doc | Law | English | lex_files_300K-400K | [lex_files_300K-400K](https://huggingface.co/datasets/lexlms/lex_files) | 2797 | 137 | dev | 339 | 15 | 1307 | 0 |
| Long-Doc | Law | English | lex_files_400K-500K | [lex_files_400K-500K](https://huggingface.co/datasets/lexlms/lex_files) | 3320 | 137 | test | 333 | 17 | 1427 | 0 |
| Long-Doc | Law | English | lex_files_500K-600K | [lex_files_500K-600K](https://huggingface.co/datasets/lexlms/lex_files) | 4087 | 136 | test | 346 | 17 | 1324 | 0 |
| Long-Doc | Law | English | lex_files_600K-700K | [lex_files_600K-700K](https://huggingface.co/datasets/lexlms/lex_files) | 5049 | 138 | test | 338 | 18 | 1442 | 0 |


### AIR-Bench_24.04

| Task | Domain | Language | Dataset Name | Source | #corpus | Avg #token of corpus | Split | # of queries | Avg #token of queries | # of positives | # of hard negatives |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| QA | Arxiv | English | default | [ArXiv (abstracts)](https://github.com/armancohan/long-summarization) | 222877 | 334 | test | 1731 | 19 | 5340 | 6288 |
| QA | Finance | English | default | [Reuters-21578](https://huggingface.co/datasets/reuters21578) | 26266 | 202 | test | 1585 | 17 | 3357 | 5595 |
| QA | Finance | Chinese | default | [FinCorpus (fin_articles)](https://huggingface.co/datasets/Duxiaoman-DI/FinCorpus) | 2398095 | 1616 | test | 1805 | 29 | 7836 | 7211 |
| QA | Healthcare | English | default | [PubMedQA](https://huggingface.co/datasets/qiaojin/PubMedQA) | 847395 | 103 | test | 1707 | 19 | 5052 | 7023 |
| QA | Healthcare | Chinese | default | [Huatuo Encyclopedia QA](https://huggingface.co/datasets/FreedomIntelligence/huatuo_encyclopedia_qa) | 360218 | 751 | test | 1874 | 31 | 10029 | 7336 |
| QA | Law | English | default | [Pile of Law (EUR-Lex)](https://huggingface.co/datasets/pile-of-law/pile-of-law) | 141678 | 1509 | test | 1801 | 19 | 5372 | 6574 |
| QA | MSMARCO (Web) | English | default | [MS MARCO (dev)](https://huggingface.co/datasets/intfloat/simlm-msmarco) | 8872840 | 81 | test | 6319 | 16 | 31447 | 26828 |
| QA | News | English | default | [CC-News](https://huggingface.co/datasets/cc_news) | 574417 | 531 | test | 1614 | 16 | 5798 | 6784 |
| QA | News | Chinese | default | [Multilingual CC-News](https://huggingface.co/datasets/intfloat/multilingual_cc_news) | 935162 | 1263 | test | 1697 | 31 | 7381 | 6618 |
| QA | Web | English | default | [mC4](https://huggingface.co/datasets/mc4) | 2459587 | 840 | test | 1707 | 16 | 5543 | 7439 |
| QA | Web | Chinese | default | [mC4](https://huggingface.co/datasets/mc4) | 956699 | 1208 | test | 1683 | 29 | 6250 | 6721 |
| QA | Wiki | English | default | [Wikipedia (20240101)](https://huggingface.co/datasets/NeuML/wikipedia-20240101) | 6738498 | 667 | test | 1727 | 17 | 4260 | 7882 |
| QA | Wiki | Chinese | default | [Wikipedia (20240401)](https://huggingface.co/datasets/wikipedia) | 1161226 | 557 | test | 1679 | 30 | 4745 | 6963 |
| Long-Doc | Arxiv | English | gemini | [gemini](https://arxiv.org/pdf/2312.11805.pdf) | 276 | 136 | test | 249 | 18 | 249 | 0 |
| Long-Doc | Arxiv | English | gpt3 | [gpt3](https://arxiv.org/pdf/2005.14165.pdf) | 515 | 137 | test | 337 | 16 | 496 | 0 |
| Long-Doc | Arxiv | English | llama2 | [llama2](https://arxiv.org/pdf/2307.09288.pdf) | 566 | 136 | test | 326 | 18 | 635 | 0 |
| Long-Doc | Arxiv | English | llm-survey | [llm-survey](https://arxiv.org/pdf/2303.18223.pdf) | 1144 | 135 | test | 357 | 17 | 924 | 0 |
| Long-Doc | Book | English | a-brief-history-of-time_stephen-hawking | [a-brief-history-of-time_stephen-hawking](https://www.docdroid.net/GCLN82v/stephen-hawking-a-brief-history-of-time-pdf) | 778 | 127 | test | 370 | 16 | 876 | 0 |
| Long-Doc | Book | English | origin-of-species_darwin | [origin-of-species_darwin](https://www.vliz.be/docs/Zeecijfers/Origin_of_Species.pdf) | 1758 | 126 | test | 366 | 16 | 1145 | 0 |
| Long-Doc | Healthcare | English | pubmed_100K-200K_1 | [pubmed_100K-200K_1](https://huggingface.co/datasets/lexlms/lex_files) | 899 | 133 | test | 372 | 20 | 1008 | 0 |
| Long-Doc | Healthcare | English | pubmed_100K-200K_2 | [pubmed_100K-200K_2](https://huggingface.co/datasets/lexlms/lex_files) | 872 | 136 | test | 355 | 18 | 980 | 0 |
| Long-Doc | Healthcare | English | pubmed_100K-200K_3 | [pubmed_100K-200K_3](https://huggingface.co/datasets/lexlms/lex_files) | 873 | 133 | test | 357 | 19 | 978 | 0 |
| Long-Doc | Healthcare | English | pubmed_30K-40K_10-merged | [pubmed_30K-40K_10-merged](https://huggingface.co/datasets/lexlms/lex_files) | 2154 | 133 | test | 368 | 18 | 1485 | 0 |
| Long-Doc | Healthcare | English | pubmed_40K-50K_5-merged | [pubmed_40K-50K_5-merged](https://huggingface.co/datasets/lexlms/lex_files) | 1731 | 136 | test | 336 | 21 | 1046 | 0 |
| Long-Doc | Law | English | lex_files_300K-400K | [lex_files_300K-400K](https://huggingface.co/datasets/lexlms/lex_files) | 2797 | 137 | test | 339 | 15 | 1307 | 0 |
| Long-Doc | Law | English | lex_files_400K-500K | [lex_files_400K-500K](https://huggingface.co/datasets/lexlms/lex_files) | 3320 | 137 | test | 333 | 17 | 1427 | 0 |
| Long-Doc | Law | English | lex_files_500K-600K | [lex_files_500K-600K](https://huggingface.co/datasets/lexlms/lex_files) | 4087 | 136 | test | 346 | 17 | 1324 | 0 |
| Long-Doc | Law | English | lex_files_600K-700K | [lex_files_600K-700K](https://huggingface.co/datasets/lexlms/lex_files) | 5049 | 138 | test | 338 | 18 | 1442 | 0 |
