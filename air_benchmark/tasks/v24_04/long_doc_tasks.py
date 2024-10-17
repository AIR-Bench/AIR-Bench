LongDocHealthcareTask = {
    "en": {
        "pubmed_100K-200K_1": {
            "name": "pubmed_100K-200K_1",
            "source": "https://huggingface.co/datasets/lexlms/lex_files",
            "splits": ["test"],
            "size": {
                "corpus": 899,
                "queries": {
                    "test": 372
                }
            },
            "token_num": {
                "corpus": {
                    "max_token_num": 181,
                    "min_token_num": 58,
                    "avg_token_num": 133
                },
                "queries": {
                    "test": {
                        "max_token_num": 89,
                        "min_token_num": 4,
                        "avg_token_num": 20
                    }
                }
            },
            "labels": {
                "test": {
                    "total_num": 1008,
                    "pos_num": 1008,
                    "hard_neg_num": 0
                }
            }
        },
        "pubmed_100K-200K_2": {
            "name": "pubmed_100K-200K_2",
            "source": "https://huggingface.co/datasets/lexlms/lex_files",
            "splits": ["test"],
            "size": {
                "corpus": 872,
                "queries": {
                    "test": 355
                }
            },
            "token_num": {
                "corpus": {
                    "max_token_num": 194,
                    "min_token_num": 29,
                    "avg_token_num": 136
                },
                "queries": {
                    "test": {
                        "max_token_num": 114,
                        "min_token_num": 3,
                        "avg_token_num": 18
                    }
                }
            },
            "labels": {
                "test": {
                    "total_num": 980,
                    "pos_num": 980,
                    "hard_neg_num": 0
                }
            }
        },
        "pubmed_100K-200K_3": {
            "name": "pubmed_100K-200K_3",
            "source": "https://huggingface.co/datasets/lexlms/lex_files",
            "splits": ["test"],
            "size": {
                "corpus": 873,
                "queries": {
                    "test": 357
                }
            },
            "token_num": {
                "corpus": {
                    "max_token_num": 188,
                    "min_token_num": 22,
                    "avg_token_num": 133
                },
                "queries": {
                    "test": {
                        "max_token_num": 109,
                        "min_token_num": 4,
                        "avg_token_num": 19
                    }
                }
            },
            "labels": {
                "test": {
                    "total_num": 978,
                    "pos_num": 978,
                    "hard_neg_num": 0
                }
            }
        },
        "pubmed_40K-50K_5-merged": {
            "name": "pubmed_40K-50K_5-merged",
            "source": "https://huggingface.co/datasets/lexlms/lex_files",
            "splits": ["test"],
            "size": {
                "corpus": 1731,
                "queries": {
                    "test": 336
                }
            },
            "token_num": {
                "corpus": {
                    "max_token_num": 205,
                    "min_token_num": 36,
                    "avg_token_num": 136
                },
                "queries": {
                    "test": {
                        "max_token_num": 90,
                        "min_token_num": 4,
                        "avg_token_num": 21
                    }
                }
            },
            "labels": {
                "test": {
                    "total_num": 1046,
                    "pos_num": 1046,
                    "hard_neg_num": 0
                }
            }
        },
        "pubmed_30K-40K_10-merged": {
            "name": "pubmed_30K-40K_10-merged",
            "source": "https://huggingface.co/datasets/lexlms/lex_files",
            "splits": ["test"],
            "size": {
                "corpus": 2154,
                "queries": {
                    "test": 368
                }
            },
            "token_num": {
                "corpus": {
                    "max_token_num": 206,
                    "min_token_num": 25,
                    "avg_token_num": 133
                },
                "queries": {
                    "test": {
                        "max_token_num": 66,
                        "min_token_num": 4,
                        "avg_token_num": 18
                    }
                }
            },
            "labels": {
                "test": {
                    "total_num": 1485,
                    "pos_num": 1485,
                    "hard_neg_num": 0
                }
            }
        },
    },
}

LongDocArxivTask = {
    "en": {
        "gpt3": {
            "name": "gpt3",
            "source": "https://arxiv.org/pdf/2005.14165.pdf",
            "splits": ["test"],
            "size": {
                "corpus": 515,
                "queries": {
                    "test": 337
                }
            },
            "token_num": {
                "corpus": {
                    "max_token_num": 191,
                    "min_token_num": 10,
                    "avg_token_num": 137
                },
                "queries": {
                    "test": {
                        "max_token_num": 88,
                        "min_token_num": 4,
                        "avg_token_num": 16
                    }
                }
            },
            "labels": {
                "test": {
                    "total_num": 496,
                    "pos_num": 496,
                    "hard_neg_num": 0
                }
            }
        },
        "llama2": {
            "name": "llama2",
            "source": "https://arxiv.org/pdf/2307.09288.pdf",
            "splits": ["test"],
            "size": {
                "corpus": 566,
                "queries": {
                    "test": 326
                }
            },
            "token_num": {
                "corpus": {
                    "max_token_num": 202,
                    "min_token_num": 24,
                    "avg_token_num": 136
                },
                "queries": {
                    "test": {
                        "max_token_num": 108,
                        "min_token_num": 5,
                        "avg_token_num": 18
                    }
                }
            },
            "labels": {
                "test": {
                    "total_num": 635,
                    "pos_num": 635,
                    "hard_neg_num": 0
                }
            }
        },
        "gemini": {
            "name": "gemini",
            "source": "https://arxiv.org/pdf/2312.11805.pdf",
            "splits": ["test"],
            "size": {
                "corpus": 276,
                "queries": {
                    "test": 249
                }
            },
            "token_num": {
                "corpus": {
                    "max_token_num": 201,
                    "min_token_num": 34,
                    "avg_token_num": 136
                },
                "queries": {
                    "test": {
                        "max_token_num": 168,
                        "min_token_num": 3,
                        "avg_token_num": 18
                    }
                }
            },
            "labels": {
                "test": {
                    "total_num": 249,
                    "pos_num": 249,
                    "hard_neg_num": 0
                }
            }
        },
        "llm-survey": {
            "name": "llm-survey",
            "source": "https://arxiv.org/pdf/2303.18223.pdf",
            "splits": ["test"],
            "size": {
                "corpus": 1144,
                "queries": {
                    "test": 357
                }
            },
            "token_num": {
                "corpus": {
                    "max_token_num": 193,
                    "min_token_num": 39,
                    "avg_token_num": 135
                },
                "queries": {
                    "test": {
                        "max_token_num": 57,
                        "min_token_num": 4,
                        "avg_token_num": 17
                    }
                }
            },
            "labels": {
                "test": {
                    "total_num": 924,
                    "pos_num": 924,
                    "hard_neg_num": 0
                }
            }
        },
    },
}

LongDocLawTask = {
    "en": {
        "lex_files_300K-400K": {
            "name": "lex_files_300K-400K",
            "source": "https://huggingface.co/datasets/lexlms/lex_files",
            "splits": ["test"],
            "size": {
                "corpus": 2797,
                "queries": {
                    "test": 339
                }
            },
            "token_num": {
                "corpus": {
                    "max_token_num": 210,
                    "min_token_num": 11,
                    "avg_token_num": 137
                },
                "queries": {
                    "test": {
                        "max_token_num": 80,
                        "min_token_num": 4,
                        "avg_token_num": 15
                    }
                }
            },
            "labels": {
                "test": {
                    "total_num": 1307,
                    "pos_num": 1307,
                    "hard_neg_num": 0
                }
            }
        },
        "lex_files_400K-500K": {
            "name": "lex_files_400K-500K",
            "source": "https://huggingface.co/datasets/lexlms/lex_files",
            "splits": ["test"],
            "size": {
                "corpus": 3320,
                "queries": {
                    "test": 333
                }
            },
            "token_num": {
                "corpus": {
                    "max_token_num": 213,
                    "min_token_num": 13,
                    "avg_token_num": 137
                },
                "queries": {
                    "test": {
                    "max_token_num": 69,
                    "min_token_num": 3,
                    "avg_token_num": 17
                    }
                }
            },
            "labels": {
                "test": {
                    "total_num": 1427,
                    "pos_num": 1427,
                    "hard_neg_num": 0
                }
            }
        },
        "lex_files_500K-600K": {
            "name": "lex_files_500K-600K",
            "source": "https://huggingface.co/datasets/lexlms/lex_files",
            "splits": ["test"],
            "size": {
                "corpus": 4087,
                "queries": {
                    "test": 346
                }
            },
            "token_num": {
                "corpus": {
                    "max_token_num": 211,
                    "min_token_num": 11,
                    "avg_token_num": 136
                },
                "queries": {
                    "test": {
                        "max_token_num": 72,
                        "min_token_num": 4,
                        "avg_token_num": 17
                    }
                }
            },
            "labels": {
                "test": {
                    "total_num": 1324,
                    "pos_num": 1324,
                    "hard_neg_num": 0
                }
            }
        },
        "lex_files_600K-700K": {
            "name": "lex_files_600K-700K",
            "source": "https://huggingface.co/datasets/lexlms/lex_files",
            "splits": ["test"],
            "size": {
                "corpus": 5049,
                "queries": {
                    "test": 338
                }
            },
            "token_num": {
                "corpus": {
                    "max_token_num": 209,
                    "min_token_num": 13,
                    "avg_token_num": 138
                },
                "queries": {
                    "test": {
                        "max_token_num": 108,
                        "min_token_num": 3,
                        "avg_token_num": 18
                    }
                }
            },
            "labels": {
                "test": {
                    "total_num": 1442,
                    "pos_num": 1442,
                    "hard_neg_num": 0
                }
            }
        },
    },
}

LongDocBookTask = {
    "en": {
        "origin-of-species_darwin": {
            "name": "origin-of-species_darwin",
            "source": "https://www.vliz.be/docs/Zeecijfers/Origin_of_Species.pdf",
            "splits": ["test"],
            "size": {
                "corpus": 1758,
                "queries": {
                    "test": 366
                }
            },
            "token_num": {
                "corpus": {
                    "max_token_num": 198,
                    "min_token_num": 15,
                    "avg_token_num": 126
                },
                "queries": {
                    "test": {
                        "max_token_num": 57,
                        "min_token_num": 4,
                        "avg_token_num": 16
                    }
                }
            },
            "labels": {
                "test": {
                    "total_num": 1145,
                    "pos_num": 1145,
                    "hard_neg_num": 0
                }
            }
        },
        "a-brief-history-of-time_stephen-hawking": {
            "name": "a-brief-history-of-time_stephen-hawking",
            "source": "https://www.docdroid.net/GCLN82v/stephen-hawking-a-brief-history-of-time-pdf",
            "splits": ["test"],
            "size": {
                "corpus": 778,
                "queries": {
                    "test": 370
                }
            },
            "token_num": {
                "corpus": {
                    "max_token_num": 193,
                    "min_token_num": 57,
                    "avg_token_num": 127
                },
                "queries": {
                    "test": {
                        "max_token_num": 65,
                        "min_token_num": 4,
                        "avg_token_num": 16
                    }
                }
            },
            "labels": {
                "test": {
                    "total_num": 876,
                    "pos_num": 876,
                    "hard_neg_num": 0
                }
            }
        },
    },
}
