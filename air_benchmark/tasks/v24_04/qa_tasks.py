QAWikiTask = {
    "en": {
        "default": {
            "name": "Wikipedia (20240101)",
            "source": "https://huggingface.co/datasets/NeuML/wikipedia-20240101",
            "splits": ["test"],
            "size": {
                "corpus": 6738498,
                "queries": {
                    "test": 1727
                }
            },
            "token_num": {
                "corpus": {
                    "max_token_num": 17806,
                    "min_token_num": 9,
                    "avg_token_num": 667
                },
                "queries": {
                    "test": {
                        "max_token_num": 105,
                        "min_token_num": 3,
                        "avg_token_num": 17
                    }
                }
            },
            "labels": {
                "test": {
                    "total_num": 12142,
                    "pos_num": 4260,
                    "hard_neg_num": 7882
                }
            }
        }
    },
    "zh": {
        "default": {
            "name": "Wikipedia (20240401)",
            "source": "https://huggingface.co/datasets/wikipedia",
            "splits": ["test"],
            "size": {
                "corpus": 1161226,
                "queries": {
                    "test": 1679
                }
            },
            "token_num": {
                "corpus": {
                    "max_token_num": 19407,
                    "min_token_num": 11,
                    "avg_token_num": 557
                },
                "queries": {
                    "test": {
                        "max_token_num": 188,
                        "min_token_num": 3,
                        "avg_token_num": 30
                    }
                }
            },
            "labels": {
                "test": {
                    "total_num": 11708,
                    "pos_num": 4745,
                    "hard_neg_num": 6963
                }
            }
        }
    },
}

QAWebTask = {
    "en": {
        "default": {
            "name": "mC4",
            "source": "https://huggingface.co/datasets/mc4",
            "splits": ["test"],
            "size": {
                "corpus": 2459587,
                "queries": {
                    "test": 1707
                }
            },
            "token_num": {
                "corpus": {
                    "max_token_num": 16848,
                    "min_token_num": 8,
                    "avg_token_num": 840
                },
                "queries": {
                    "test": {
                        "max_token_num": 153,
                        "min_token_num": 3,
                        "avg_token_num": 16
                    }
                }
            },
            "labels": {
                "test": {
                    "total_num": 12982,
                    "pos_num": 5543,
                    "hard_neg_num": 7439
                }
            }
        }
    },
    "zh": {
        "default": {
            "name": "mC4",
            "source": "https://huggingface.co/datasets/mc4",
            "splits": ["test"],
            "size": {
                "corpus": 956699,
                "queries": {
                    "test": 1683
                }
            },
            "token_num": {
                "corpus": {
                    "max_token_num": 21442,
                    "min_token_num": 8,
                    "avg_token_num": 1208
                },
                "queries": {
                    "test": {
                        "max_token_num": 176,
                        "min_token_num": 4,
                        "avg_token_num": 29
                    }
                }
            },
            "labels": {
                "test": {
                    "total_num": 12971,
                    "pos_num": 6250,
                    "hard_neg_num": 6721
                }
            }
        }
    },
}

QAHealthcareTask = {
    "en": {
        "default": {
            "name": "PubMedQA",
            "source": "https://huggingface.co/datasets/qiaojin/PubMedQA",
            "splits": ["test"],
            "size": {
                "corpus": 847395,
                "queries": {
                    "test": 1707
                }
            },
            "token_num": {
                "corpus": {
                    "max_token_num": 1271,
                    "min_token_num": 8,
                    "avg_token_num": 103
                },
                "queries": {
                    "test": {
                        "max_token_num": 93,
                        "min_token_num": 3,
                        "avg_token_num": 19
                    }
                }
            },
            "labels": {
                "test": {
                    "total_num": 12075,
                    "pos_num": 5052,
                    "hard_neg_num": 7023
                }
            }
        }
    },
    "zh": {
        "default": {
            "name": "Huatuo Encyclopedia QA",
            "source": "https://huggingface.co/datasets/FreedomIntelligence/huatuo_encyclopedia_qa",
            "splits": ["test"],
            "size": {
                "corpus": 360218,
                "queries": {
                    "test": 1874
                }
            },
            "token_num": {
                "corpus": {
                    "max_token_num": 16020,
                    "min_token_num": 13,
                    "avg_token_num": 751
                },
                "queries": {
                    "test": {
                        "max_token_num": 383,
                        "min_token_num": 3,
                        "avg_token_num": 31
                    }
                }
            },
            "labels": {
                "test": {
                    "total_num": 17365,
                    "pos_num": 10029,
                    "hard_neg_num": 7336
                }
            }
        }
    },
}

QALawTask = {
    "en": {
        "default": {
            "name": "Pile of Law (EUR-Lex)",
            "source": "https://huggingface.co/datasets/pile-of-law/pile-of-law",
            "splits": ["test"],
            "size": {
                "corpus": 141678,
                "queries": {
                    "test": 1801
                }
            },
            "token_num": {
                "corpus": {
                    "max_token_num": 14530,
                    "min_token_num": 13,
                    "avg_token_num": 1509
                },
                "queries": {
                    "test": {
                        "max_token_num": 110,
                        "min_token_num": 2,
                        "avg_token_num": 19
                    }
                }
            },
            "labels": {
                "test": {
                    "total_num": 11946,
                    "pos_num": 5372,
                    "hard_neg_num": 6574
                }
            }
        }
    },
}

QAArxivTask = {
    "en": {
        "default": {
            "name": "ArXiv (abstracts)",
            "source": "https://github.com/armancohan/long-summarization",
            "splits": ["test"],
            "size": {
                "corpus": 222877,
                "queries": {
                    "test": 1731
                }
            },
            "token_num": {
                "corpus": {
                    "max_token_num": 9654,
                    "min_token_num": 11,
                    "avg_token_num": 334
                },
                "queries": {
                    "test": {
                        "max_token_num": 91,
                        "min_token_num": 4,
                        "avg_token_num": 19
                    }
                }
            },
            "labels": {
                "test": {
                    "total_num": 11628,
                    "pos_num": 5340,
                    "hard_neg_num": 6288
                }
            }
        }
    },
}

QANewsTask = {
    "en": {
        "default": {
            "name": "CC-News",
            "source": "https://huggingface.co/datasets/cc_news",
            "splits": ["test"],
            "size": {
                "corpus": 574417,
                "queries": {
                    "test": 1614
                }
            },
            "token_num": {
                "corpus": {
                    "max_token_num": 14119,
                    "min_token_num": 15,
                    "avg_token_num": 531
                },
                "queries": {
                    "test": {
                        "max_token_num": 137,
                        "min_token_num": 3,
                        "avg_token_num": 16
                    }
                }
            },
            "labels": {
                "test": {
                    "total_num": 12582,
                    "pos_num": 5798,
                    "hard_neg_num": 6784
                }
            }
        }
    },
    "zh": {
        "default": {
            "name": "Multilingual CC-News",
            "source": "https://huggingface.co/datasets/intfloat/multilingual_cc_news",
            "splits": ["test"],
            "size": {
                "corpus": 935162,
                "queries": {
                    "test": 1697
                }
            },
            "token_num": {
                "corpus": {
                    "max_token_num": 44111,
                    "min_token_num": 17,
                    "avg_token_num": 1263
                },
                "queries": {
                    "test": {
                        "max_token_num": 348,
                        "min_token_num": 2,
                        "avg_token_num": 31
                    }
                }
            },
            "labels": {
                "test": {
                    "total_num": 13999,
                    "pos_num": 7381,
                    "hard_neg_num": 6618
                }
            }
        }
    },
}

QAFinanceTask = {
    "en": {
        "default": {
            "name": "Reuters-21578",
            "source": "https://huggingface.co/datasets/reuters21578",
            "splits": ["test"],
            "size": {
                "corpus": 26266,
                "queries": {
                    "test": 1585
                }
            },
            "token_num": {
                "corpus": {
                    "max_token_num": 5632,
                    "min_token_num": 18,
                    "avg_token_num": 202
                },
                "queries": {
                    "test": {
                        "max_token_num": 107,
                        "min_token_num": 2,
                        "avg_token_num": 17
                    }
                }
            },
            "labels": {
                "test": {
                    "total_num": 8952,
                    "pos_num": 3357,
                    "hard_neg_num": 5595
                }
            }
        }
    },
    "zh": {
        "default": {
            "name": "FinCorpus (fin_articles)",
            "source": "https://huggingface.co/datasets/Duxiaoman-DI/FinCorpus",
            "splits": ["test"],
            "size": {
                "corpus": 2398095,
                "queries": {
                    "test": 1805
                }
            },
            "token_num": {
                "corpus": {
                    "max_token_num": 19801,
                    "min_token_num": 27,
                    "avg_token_num": 1616
                },
                "queries": {
                    "test": {
                        "max_token_num": 211,
                        "min_token_num": 3,
                        "avg_token_num": 29
                    }
                }
            },
            "labels": {
                "test": {
                    "total_num": 15047,
                    "pos_num": 7836,
                    "hard_neg_num": 7211
                }
            }
        }
    },
}

QAMSMARCOTask = {
    "en": {
        "default": {
            "name": "MS MARCO (dev)",
            "source": "https://huggingface.co/datasets/intfloat/simlm-msmarco",
            "splits": ["test"],
            "size": {
                "corpus": 8872840,
                "queries": {
                    "test": 6319
                }
            },
            "token_num": {
                "corpus": {
                    "max_token_num": 50888,
                    "min_token_num": 2,
                    "avg_token_num": 81
                },
                "queries": {
                    "test": {
                        "max_token_num": 92,
                        "min_token_num": 2,
                        "avg_token_num": 16
                    }
                }
            },
            "labels": {
                "test": {
                    "total_num": 58275,
                    "pos_num": 31447,
                    "hard_neg_num": 26828
                }
            }
        }
    },
}
