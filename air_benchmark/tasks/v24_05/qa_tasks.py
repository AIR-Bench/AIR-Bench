QAWikiTask = {
    "en": {
        "default": {
            "name": "Wikipedia (20240101)",
            "source": "https://huggingface.co/datasets/NeuML/wikipedia-20240101",
            "splits": ["dev", "test"],
            "size": {
              "corpus": 1012092,
              "queries": {
                "dev": 345,
                "test": 1382
              }
            },
            "token_num": {
              "corpus": {
                "max_token_num": 15794,
                "min_token_num": 11,
                "avg_token_num": 665
              },
              "queries": {
                "dev": {
                  "max_token_num": 71,
                  "min_token_num": 4,
                  "avg_token_num": 18
                },
                "test": {
                  "max_token_num": 105,
                  "min_token_num": 3,
                  "avg_token_num": 17
                }
              }
            },
            "labels": {
              "dev": {
                "total_num": 2439,
                "pos_num": 863,
                "hard_neg_num": 1576
              },
              "test": {
                "total_num": 9703,
                "pos_num": 3397,
                "hard_neg_num": 6306
              }
            }
        }
    },
    "zh": {
        "default": {
            "name": "Wikipedia (20240401)",
            "source": "https://huggingface.co/datasets/wikipedia",
            "splits": ["dev", "test"],
            "size": {
              "corpus": 1011604,
              "queries": {
                "dev": 335,
                "test": 1344
              }
            },
            "token_num": {
              "corpus": {
                "max_token_num": 19407,
                "min_token_num": 11,
                "avg_token_num": 557
              },
              "queries": {
                "dev": {
                  "max_token_num": 145,
                  "min_token_num": 4,
                  "avg_token_num": 30
                },
                "test": {
                  "max_token_num": 188,
                  "min_token_num": 3,
                  "avg_token_num": 30
                }
              }
            },
            "labels": {
              "dev": {
                "total_num": 2253,
                "pos_num": 952,
                "hard_neg_num": 1301
              },
              "test": {
                "total_num": 9455,
                "pos_num": 3793,
                "hard_neg_num": 5662
              }
            }
        }
    },
    "ar": {
        "default": {
            "name": "Wikipedia (20240401)",
            "source": "https://huggingface.co/datasets/wikipedia",
            "splits": ["dev", "test"],
            "size": {
              "corpus": 1008232,
              "queries": {
                "dev": 338,
                "test": 1355
              }
            },
            "token_num": {
              "corpus": {
                "max_token_num": 9997,
                "min_token_num": 19,
                "avg_token_num": 787
              },
              "queries": {
                "dev": {
                  "max_token_num": 414,
                  "min_token_num": 5,
                  "avg_token_num": 40
                },
                "test": {
                  "max_token_num": 256,
                  "min_token_num": 7,
                  "avg_token_num": 38
                }
              }
            },
            "labels": {
              "dev": {
                "total_num": 2550,
                "pos_num": 1112,
                "hard_neg_num": 1438
              },
              "test": {
                "total_num": 10245,
                "pos_num": 4467,
                "hard_neg_num": 5778
              }
            }
        }
    },
    "bn": {
        "default": {
            "name": "Wikipedia (20240401)",
            "source": "https://huggingface.co/datasets/wikipedia",
            "splits": ["dev", "test"],
            "size": {
              "corpus": 152064,
              "queries": {
                "dev": 364,
                "test": 1456
              }
            },
            "token_num": {
              "corpus": {
                "max_token_num": 9998,
                "min_token_num": 40,
                "avg_token_num": 2129
              },
              "queries": {
                "dev": {
                  "max_token_num": 232,
                  "min_token_num": 15,
                  "avg_token_num": 69
                },
                "test": {
                  "max_token_num": 432,
                  "min_token_num": 11,
                  "avg_token_num": 71
                }
              }
            },
            "labels": {
              "dev": {
                "total_num": 2558,
                "pos_num": 1016,
                "hard_neg_num": 1542
              },
              "test": {
                "total_num": 10044,
                "pos_num": 4203,
                "hard_neg_num": 5841
              }
            }
        }
    },
    "de": {
        "default": {
            "name": "Wikipedia (20240401)",
            "source": "https://huggingface.co/datasets/wikipedia",
            "splits": ["dev", "test"],
            "size": {
              "corpus": 1008186,
              "queries": {
                "dev": 350,
                "test": 1404
              }
            },
            "token_num": {
              "corpus": {
                "max_token_num": 9999,
                "min_token_num": 16,
                "avg_token_num": 891
              },
              "queries": {
                "dev": {
                  "max_token_num": 101,
                  "min_token_num": 4,
                  "avg_token_num": 23
                },
                "test": {
                  "max_token_num": 179,
                  "min_token_num": 3,
                  "avg_token_num": 22
                }
              }
            },
            "labels": {
              "dev": {
                "total_num": 2298,
                "pos_num": 817,
                "hard_neg_num": 1481
              },
              "test": {
                "total_num": 9292,
                "pos_num": 3411,
                "hard_neg_num": 5881
              }
            }
        }
    },
    "es": {
        "default": {
            "name": "Wikipedia (20240401)",
            "source": "https://huggingface.co/datasets/wikipedia",
            "splits": ["dev", "test"],
            "size": {
              "corpus": 1008147,
              "queries": {
                "dev": 345,
                "test": 1380
              }
            },
            "token_num": {
              "corpus": {
                "max_token_num": 9999,
                "min_token_num": 16,
                "avg_token_num": 801
              },
              "queries": {
                "dev": {
                  "max_token_num": 83,
                  "min_token_num": 3,
                  "avg_token_num": 22
                },
                "test": {
                  "max_token_num": 125,
                  "min_token_num": 3,
                  "avg_token_num": 23
                }
              }
            },
            "labels": {
              "dev": {
                "total_num": 2330,
                "pos_num": 879,
                "hard_neg_num": 1451
              },
              "test": {
                "total_num": 9298,
                "pos_num": 3531,
                "hard_neg_num": 5767
              }
            }
        }
    },
    "fa": {
        "default": {
            "name": "Wikipedia (20240401)",
            "source": "https://huggingface.co/datasets/wikipedia",
            "splits": ["dev", "test"],
            "size": {
              "corpus": 999223,
              "queries": {
                "dev": 332,
                "test": 1328
              }
            },
            "token_num": {
              "corpus": {
                "max_token_num": 9999,
                "min_token_num": 21,
                "avg_token_num": 627
              },
              "queries": {
                "dev": {
                  "max_token_num": 271,
                  "min_token_num": 5,
                  "avg_token_num": 41
                },
                "test": {
                  "max_token_num": 449,
                  "min_token_num": 6,
                  "avg_token_num": 45
                }
              }
            },
            "labels": {
              "dev": {
                "total_num": 2623,
                "pos_num": 1179,
                "hard_neg_num": 1444
              },
              "test": {
                "total_num": 10119,
                "pos_num": 4538,
                "hard_neg_num": 5581
              }
            }
        }
    },
    "fr": {
        "default": {
            "name": "Wikipedia (20240401)",
            "source": "https://huggingface.co/datasets/wikipedia",
            "splits": ["dev", "test"],
            "size": {
              "corpus": 1008270,
              "queries": {
                "dev": 356,
                "test": 1424
              }
            },
            "token_num": {
              "corpus": {
                "max_token_num": 9999,
                "min_token_num": 16,
                "avg_token_num": 779
              },
              "queries": {
                "dev": {
                  "max_token_num": 86,
                  "min_token_num": 5,
                  "avg_token_num": 20
                },
                "test": {
                  "max_token_num": 89,
                  "min_token_num": 4,
                  "avg_token_num": 21
                }
              }
            },
            "labels": {
              "dev": {
                "total_num": 2264,
                "pos_num": 768,
                "hard_neg_num": 1496
              },
              "test": {
                "total_num": 9418,
                "pos_num": 3429,
                "hard_neg_num": 5989
              }
            }
        }
    },
    "hi": {
        "default": {
            "name": "Wikipedia (20240401)",
            "source": "https://huggingface.co/datasets/wikipedia",
            "splits": ["dev", "test"],
            "size": {
              "corpus": 162188,
              "queries": {
                "dev": 340,
                "test": 1360
              }
            },
            "token_num": {
              "corpus": {
                "max_token_num": 9999,
                "min_token_num": 16,
                "avg_token_num": 997
              },
              "queries": {
                "dev": {
                  "max_token_num": 259,
                  "min_token_num": 11,
                  "avg_token_num": 59
                },
                "test": {
                  "max_token_num": 402,
                  "min_token_num": 7,
                  "avg_token_num": 59
                }
              }
            },
            "labels": {
              "dev": {
                "total_num": 2319,
                "pos_num": 995,
                "hard_neg_num": 1324
              },
              "test": {
                "total_num": 9136,
                "pos_num": 3911,
                "hard_neg_num": 5225
              }
            }
        }
    },
    "id": {
        "default": {
            "name": "Wikipedia (20240401)",
            "source": "https://huggingface.co/datasets/wikipedia",
            "splits": ["dev", "test"],
            "size": {
              "corpus": 687513,
              "queries": {
                "dev": 343,
                "test": 1373
              }
            },
            "token_num": {
              "corpus": {
                "max_token_num": 9996,
                "min_token_num": 16,
                "avg_token_num": 451
              },
              "queries": {
                "dev": {
                  "max_token_num": 106,
                  "min_token_num": 5,
                  "avg_token_num": 22
                },
                "test": {
                  "max_token_num": 196,
                  "min_token_num": 3,
                  "avg_token_num": 21
                }
              }
            },
            "labels": {
              "dev": {
                "total_num": 2368,
                "pos_num": 1003,
                "hard_neg_num": 1365
              },
              "test": {
                "total_num": 9575,
                "pos_num": 4089,
                "hard_neg_num": 5486
              }
            }
        }
    },
    "ja": {
        "default": {
            "name": "Wikipedia (20240401)",
            "source": "https://huggingface.co/datasets/wikipedia",
            "splits": ["dev", "test"],
            "size": {
              "corpus": 1008365,
              "queries": {
                "dev": 358,
                "test": 1432
              }
            },
            "token_num": {
              "corpus": {
                "max_token_num": 9999,
                "min_token_num": 16,
                "avg_token_num": 1470
              },
              "queries": {
                "dev": {
                  "max_token_num": 84,
                  "min_token_num": 5,
                  "avg_token_num": 30
                },
                "test": {
                  "max_token_num": 135,
                  "min_token_num": 4,
                  "avg_token_num": 32
                }
              }
            },
            "labels": {
              "dev": {
                "total_num": 2636,
                "pos_num": 1099,
                "hard_neg_num": 1537
              },
              "test": {
                "total_num": 10404,
                "pos_num": 4303,
                "hard_neg_num": 6101
              }
            }
        }
    },
    "ko": {
        "default": {
            "name": "Wikipedia (20240401)",
            "source": "https://huggingface.co/datasets/wikipedia",
            "splits": ["dev", "test"],
            "size": {
              "corpus": 665227,
              "queries": {
                "dev": 346,
                "test": 1384
              }
            },
            "token_num": {
              "corpus": {
                "max_token_num": 9999,
                "min_token_num": 16,
                "avg_token_num": 775
              },
              "queries": {
                "dev": {
                  "max_token_num": 298,
                  "min_token_num": 6,
                  "avg_token_num": 39
                },
                "test": {
                  "max_token_num": 295,
                  "min_token_num": 4,
                  "avg_token_num": 35
                }
              }
            },
            "labels": {
              "dev": {
                "total_num": 2532,
                "pos_num": 1109,
                "hard_neg_num": 1423
              },
              "test": {
                "total_num": 10414,
                "pos_num": 4604,
                "hard_neg_num": 5810
              }
            }
        }
    },
    "ru": {
        "default": {
            "name": "Wikipedia (20240401)",
            "source": "https://huggingface.co/datasets/wikipedia",
            "splits": ["dev", "test"],
            "size": {
              "corpus": 1008405,
              "queries": {
                "dev": 365,
                "test": 1463
              }
            },
            "token_num": {
              "corpus": {
                "max_token_num": 9999,
                "min_token_num": 17,
                "avg_token_num": 1211
              },
              "queries": {
                "dev": {
                  "max_token_num": 146,
                  "min_token_num": 6,
                  "avg_token_num": 30
                },
                "test": {
                  "max_token_num": 170,
                  "min_token_num": 5,
                  "avg_token_num": 30
                }
              }
            },
            "labels": {
              "dev": {
                "total_num": 2659,
                "pos_num": 1154,
                "hard_neg_num": 1505
              },
              "test": {
                "total_num": 10799,
                "pos_num": 4516,
                "hard_neg_num": 6283
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
            "splits": ["dev", "test"],
            "size": {
              "corpus": 1012910,
              "queries": {
                "dev": 341,
                "test": 1366
              }
            },
            "token_num": {
              "corpus": {
                "max_token_num": 13157,
                "min_token_num": 8,
                "avg_token_num": 838
              },
              "queries": {
                "dev": {
                  "max_token_num": 75,
                  "min_token_num": 4,
                  "avg_token_num": 16
                },
                "test": {
                  "max_token_num": 153,
                  "min_token_num": 3,
                  "avg_token_num": 16
                }
              }
            },
            "labels": {
              "dev": {
                "total_num": 2598,
                "pos_num": 1087,
                "hard_neg_num": 1511
              },
              "test": {
                "total_num": 10384,
                "pos_num": 4456,
                "hard_neg_num": 5928
              }
            }
        }
    },
    "zh": {
        "default": {
            "name": "mC4",
            "source": "https://huggingface.co/datasets/mc4",
            "splits": ["dev", "test"],
            "size": {
              "corpus": 956699,
              "queries": {
                "dev": 336,
                "test": 1347
              }
            },
            "token_num": {
              "corpus": {
                "max_token_num": 21442,
                "min_token_num": 8,
                "avg_token_num": 1208
              },
              "queries": {
                "dev": {
                  "max_token_num": 164,
                  "min_token_num": 5,
                  "avg_token_num": 30
                },
                "test": {
                  "max_token_num": 176,
                  "min_token_num": 4,
                  "avg_token_num": 29
                }
              }
            },
            "labels": {
              "dev": {
                "total_num": 2596,
                "pos_num": 1230,
                "hard_neg_num": 1366
              },
              "test": {
                "total_num": 10375,
                "pos_num": 5020,
                "hard_neg_num": 5355
              }
            }
        }
    },
    "ar": {
        "default": {
            "name": "mC4",
            "source": "https://huggingface.co/datasets/mc4",
            "splits": ["dev", "test"],
            "size": {
              "corpus": 165902,
              "queries": {
                "dev": 334,
                "test": 1338
              }
            },
            "token_num": {
              "corpus": {
                "max_token_num": 9999,
                "min_token_num": 16,
                "avg_token_num": 1686
              },
              "queries": {
                "dev": {
                  "max_token_num": 182,
                  "min_token_num": 7,
                  "avg_token_num": 42
                },
                "test": {
                  "max_token_num": 381,
                  "min_token_num": 7,
                  "avg_token_num": 42
                }
              }
            },
            "labels": {
              "dev": {
                "total_num": 2252,
                "pos_num": 1133,
                "hard_neg_num": 1119
              },
              "test": {
                "total_num": 9499,
                "pos_num": 4782,
                "hard_neg_num": 4717
              }
            }
        }
    },
    "bn": {
        "default": {
            "name": "mC4",
            "source": "https://huggingface.co/datasets/mc4",
            "splits": ["dev", "test"],
            "size": {
              "corpus": 45375,
              "queries": {
                "dev": 362,
                "test": 1451
              }
            },
            "token_num": {
              "corpus": {
                "max_token_num": 9991,
                "min_token_num": 16,
                "avg_token_num": 2161
              },
              "queries": {
                "dev": {
                  "max_token_num": 424,
                  "min_token_num": 13,
                  "avg_token_num": 73
                },
                "test": {
                  "max_token_num": 406,
                  "min_token_num": 9,
                  "avg_token_num": 77
                }
              }
            },
            "labels": {
              "dev": {
                "total_num": 2215,
                "pos_num": 1142,
                "hard_neg_num": 1073
              },
              "test": {
                "total_num": 9208,
                "pos_num": 4759,
                "hard_neg_num": 4449
              }
            }
        }
    },
    "de": {
        "default": {
            "name": "mC4",
            "source": "https://huggingface.co/datasets/mc4",
            "splits": ["dev", "test"],
            "size": {
              "corpus": 441182,
              "queries": {
                "dev": 357,
                "test": 1432
              }
            },
            "token_num": {
              "corpus": {
                "max_token_num": 9996,
                "min_token_num": 16,
                "avg_token_num": 1025
              },
              "queries": {
                "dev": {
                  "max_token_num": 74,
                  "min_token_num": 5,
                  "avg_token_num": 20
                },
                "test": {
                  "max_token_num": 91,
                  "min_token_num": 5,
                  "avg_token_num": 20
                }
              }
            },
            "labels": {
              "dev": {
                "total_num": 2665,
                "pos_num": 1320,
                "hard_neg_num": 1345
              },
              "test": {
                "total_num": 10792,
                "pos_num": 5539,
                "hard_neg_num": 5253
              }
            }
        }
    },
    "es": {
        "default": {
            "name": "mC4",
            "source": "https://huggingface.co/datasets/mc4",
            "splits": ["dev", "test"],
            "size": {
              "corpus": 403020,
              "queries": {
                "dev": 341,
                "test": 1368
              }
            },
            "token_num": {
              "corpus": {
                "max_token_num": 9990,
                "min_token_num": 16,
                "avg_token_num": 912
              },
              "queries": {
                "dev": {
                  "max_token_num": 114,
                  "min_token_num": 4,
                  "avg_token_num": 23
                },
                "test": {
                  "max_token_num": 128,
                  "min_token_num": 2,
                  "avg_token_num": 24
                }
              }
            },
            "labels": {
              "dev": {
                "total_num": 2598,
                "pos_num": 1317,
                "hard_neg_num": 1281
              },
              "test": {
                "total_num": 10619,
                "pos_num": 5317,
                "hard_neg_num": 5302
              }
            }
        }
    },
    "fa": {
        "default": {
            "name": "mC4",
            "source": "https://huggingface.co/datasets/mc4",
            "splits": ["dev", "test"],
            "size": {
              "corpus": 181463,
              "queries": {
                "dev": 338,
                "test": 1354
              }
            },
            "token_num": {
              "corpus": {
                "max_token_num": 9999,
                "min_token_num": 16,
                "avg_token_num": 2114
              },
              "queries": {
                "dev": {
                  "max_token_num": 232,
                  "min_token_num": 7,
                  "avg_token_num": 49
                },
                "test": {
                  "max_token_num": 386,
                  "min_token_num": 4,
                  "avg_token_num": 47
                }
              }
            },
            "labels": {
              "dev": {
                "total_num": 2549,
                "pos_num": 1389,
                "hard_neg_num": 1160
              },
              "test": {
                "total_num": 10371,
                "pos_num": 5532,
                "hard_neg_num": 4839
              }
            }
        }
    },
    "fr": {
        "default": {
            "name": "mC4",
            "source": "https://huggingface.co/datasets/mc4",
            "splits": ["dev", "test"],
            "size": {
              "corpus": 387210,
              "queries": {
                "dev": 364,
                "test": 1457
              }
            },
            "token_num": {
              "corpus": {
                "max_token_num": 9999,
                "min_token_num": 16,
                "avg_token_num": 1076
              },
              "queries": {
                "dev": {
                  "max_token_num": 67,
                  "min_token_num": 5,
                  "avg_token_num": 20
                },
                "test": {
                  "max_token_num": 71,
                  "min_token_num": 2,
                  "avg_token_num": 20
                }
              }
            },
            "labels": {
              "dev": {
                "total_num": 2895,
                "pos_num": 1444,
                "hard_neg_num": 1451
              },
              "test": {
                "total_num": 11124,
                "pos_num": 5572,
                "hard_neg_num": 5552
              }
            }
        }
    },
    "hi": {
        "default": {
            "name": "mC4",
            "source": "https://huggingface.co/datasets/mc4",
            "splits": ["dev", "test"],
            "size": {
              "corpus": 50501,
              "queries": {
                "dev": 355,
                "test": 1423
              }
            },
            "token_num": {
              "corpus": {
                "max_token_num": 9998,
                "min_token_num": 16,
                "avg_token_num": 2396
              },
              "queries": {
                "dev": {
                  "max_token_num": 417,
                  "min_token_num": 9,
                  "avg_token_num": 68
                },
                "test": {
                  "max_token_num": 515,
                  "min_token_num": 9,
                  "avg_token_num": 64
                }
              }
            },
            "labels": {
              "dev": {
                "total_num": 2360,
                "pos_num": 1180,
                "hard_neg_num": 1180
              },
              "test": {
                "total_num": 9187,
                "pos_num": 4706,
                "hard_neg_num": 4481
              }
            }
        }
    },
    "id": {
        "default": {
            "name": "mC4",
            "source": "https://huggingface.co/datasets/mc4",
            "splits": ["dev", "test"],
            "size": {
              "corpus": 245878,
              "queries": {
                "dev": 339,
                "test": 1356
              }
            },
            "token_num": {
              "corpus": {
                "max_token_num": 9978,
                "min_token_num": 16,
                "avg_token_num": 1059
              },
              "queries": {
                "dev": {
                  "max_token_num": 91,
                  "min_token_num": 4,
                  "avg_token_num": 23
                },
                "test": {
                  "max_token_num": 139,
                  "min_token_num": 4,
                  "avg_token_num": 23
                }
              }
            },
            "labels": {
              "dev": {
                "total_num": 2690,
                "pos_num": 1395,
                "hard_neg_num": 1295
              },
              "test": {
                "total_num": 10807,
                "pos_num": 5605,
                "hard_neg_num": 5202
              }
            }
        }
    },
    "ja": {
        "default": {
            "name": "mC4",
            "source": "https://huggingface.co/datasets/mc4",
            "splits": ["dev", "test"],
            "size": {
              "corpus": 547419,
              "queries": {
                "dev": 323,
                "test": 1293
              }
            },
            "token_num": {
              "corpus": {
                "max_token_num": 9997,
                "min_token_num": 16,
                "avg_token_num": 1026
              },
              "queries": {
                "dev": {
                  "max_token_num": 186,
                  "min_token_num": 4,
                  "avg_token_num": 35
                },
                "test": {
                  "max_token_num": 289,
                  "min_token_num": 4,
                  "avg_token_num": 36
                }
              }
            },
            "labels": {
              "dev": {
                "total_num": 2359,
                "pos_num": 1106,
                "hard_neg_num": 1253
              },
              "test": {
                "total_num": 9449,
                "pos_num": 4473,
                "hard_neg_num": 4976
              }
            }
        }
    },
    "ko": {
        "default": {
            "name": "mC4",
            "source": "https://huggingface.co/datasets/mc4",
            "splits": ["dev", "test"],
            "size": {
              "corpus": 250605,
              "queries": {
                "dev": 327,
                "test": 1309
              }
            },
            "token_num": {
              "corpus": {
                "max_token_num": 9999,
                "min_token_num": 16,
                "avg_token_num": 1137
              },
              "queries": {
                "dev": {
                  "max_token_num": 186,
                  "min_token_num": 5,
                  "avg_token_num": 34
                },
                "test": {
                  "max_token_num": 288,
                  "min_token_num": 5,
                  "avg_token_num": 36
                }
              }
            },
            "labels": {
              "dev": {
                "total_num": 2239,
                "pos_num": 1156,
                "hard_neg_num": 1083
              },
              "test": {
                "total_num": 8696,
                "pos_num": 4239,
                "hard_neg_num": 4457
              }
            }
        }
    },
    "ru": {
        "default": {
            "name": "mC4",
            "source": "https://huggingface.co/datasets/mc4",
            "splits": ["dev", "test"],
            "size": {
              "corpus": 490581,
              "queries": {
                "dev": 324,
                "test": 1297
              }
            },
            "token_num": {
              "corpus": {
                "max_token_num": 9999,
                "min_token_num": 16,
                "avg_token_num": 1266
              },
              "queries": {
                "dev": {
                  "max_token_num": 134,
                  "min_token_num": 5,
                  "avg_token_num": 32
                },
                "test": {
                  "max_token_num": 301,
                  "min_token_num": 4,
                  "avg_token_num": 33
                }
              }
            },
            "labels": {
              "dev": {
                "total_num": 2607,
                "pos_num": 1330,
                "hard_neg_num": 1277
              },
              "test": {
                "total_num": 10248,
                "pos_num": 5096,
                "hard_neg_num": 5152
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
            "splits": ["dev", "test"],
            "size": {
              "corpus": 847395,
              "queries": {
                "dev": 341,
                "test": 1366
              }
            },
            "token_num": {
              "corpus": {
                "max_token_num": 1271,
                "min_token_num": 8,
                "avg_token_num": 103
              },
              "queries": {
                "dev": {
                  "max_token_num": 64,
                  "min_token_num": 4,
                  "avg_token_num": 20
                },
                "test": {
                  "max_token_num": 93,
                  "min_token_num": 3,
                  "avg_token_num": 19
                }
              }
            },
            "labels": {
              "dev": {
                "total_num": 2390,
                "pos_num": 1008,
                "hard_neg_num": 1382
              },
              "test": {
                "total_num": 9685,
                "pos_num": 4044,
                "hard_neg_num": 5641
              }
            }
        }
    },
    "zh": {
        "default": {
            "name": "Huatuo Encyclopedia QA",
            "source": "https://huggingface.co/datasets/FreedomIntelligence/huatuo_encyclopedia_qa",
            "splits": ["dev", "test"],
            "size": {
              "corpus": 360218,
              "queries": {
                "dev": 374,
                "test": 1500
              }
            },
            "token_num": {
              "corpus": {
                "max_token_num": 16020,
                "min_token_num": 13,
                "avg_token_num": 751
              },
              "queries": {
                "dev": {
                  "max_token_num": 186,
                  "min_token_num": 5,
                  "avg_token_num": 31
                },
                "test": {
                  "max_token_num": 383,
                  "min_token_num": 3,
                  "avg_token_num": 31
                }
              }
            },
            "labels": {
              "dev": {
                "total_num": 3520,
                "pos_num": 2030,
                "hard_neg_num": 1490
              },
              "test": {
                "total_num": 13845,
                "pos_num": 7999,
                "hard_neg_num": 5846
              }
            }
        }
    },
    "de": {
        "default": {
            "name": "GEM/mlsum",
            "source": "https://huggingface.co/datasets/GEM/mlsum",
            "splits": ["dev", "test"],
            "size": {
              "corpus": 27934,
              "queries": {
                "dev": 360,
                "test": 1441
              }
            },
            "token_num": {
              "corpus": {
                "max_token_num": 7474,
                "min_token_num": 60,
                "avg_token_num": 909
              },
              "queries": {
                "dev": {
                  "max_token_num": 98,
                  "min_token_num": 4,
                  "avg_token_num": 21
                },
                "test": {
                  "max_token_num": 77,
                  "min_token_num": 4,
                  "avg_token_num": 20
                }
              }
            },
            "labels": {
              "dev": {
                "total_num": 2239,
                "pos_num": 1102,
                "hard_neg_num": 1137
              },
              "test": {
                "total_num": 8973,
                "pos_num": 4667,
                "hard_neg_num": 4306
              }
            }
        }
    },
    "es": {
        "default": {
            "name": "Multilingual Medical Corpora",
            "source": "https://zenodo.org/records/3463379",
            "splits": ["dev", "test"],
            "size": {
              "corpus": 1006093,
              "queries": {
                "dev": 300,
                "test": 1201
              }
            },
            "token_num": {
              "corpus": {
                "max_token_num": 6654,
                "min_token_num": 17,
                "avg_token_num": 60
              },
              "queries": {
                "dev": {
                  "max_token_num": 94,
                  "min_token_num": 6,
                  "avg_token_num": 21
                },
                "test": {
                  "max_token_num": 91,
                  "min_token_num": 2,
                  "avg_token_num": 22
                }
              }
            },
            "labels": {
              "dev": {
                "total_num": 2140,
                "pos_num": 1210,
                "hard_neg_num": 930
              },
              "test": {
                "total_num": 8504,
                "pos_num": 4695,
                "hard_neg_num": 3809
              }
            }
        }
    },
    "fr": {
        "default": {
            "name": "Multilingual Medical Corpora",
            "source": "https://zenodo.org/records/3463379",
            "splits": ["dev", "test"],
            "size": {
              "corpus": 972938,
              "queries": {
                "dev": 331,
                "test": 1326
              }
            },
            "token_num": {
              "corpus": {
                "max_token_num": 6777,
                "min_token_num": 16,
                "avg_token_num": 202
              },
              "queries": {
                "dev": {
                  "max_token_num": 126,
                  "min_token_num": 4,
                  "avg_token_num": 23
                },
                "test": {
                  "max_token_num": 144,
                  "min_token_num": 4,
                  "avg_token_num": 24
                }
              }
            },
            "labels": {
              "dev": {
                "total_num": 3146,
                "pos_num": 1885,
                "hard_neg_num": 1261
              },
              "test": {
                "total_num": 12579,
                "pos_num": 7460,
                "hard_neg_num": 5119
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
            "splits": ["dev", "test"],
            "size": {
              "corpus": 141678,
              "queries": {
                "dev": 360,
                "test": 1441
              }
            },
            "token_num": {
              "corpus": {
                "max_token_num": 14530,
                "min_token_num": 13,
                "avg_token_num": 1509
              },
              "queries": {
                "dev": {
                  "max_token_num": 110,
                  "min_token_num": 4,
                  "avg_token_num": 20
                },
                "test": {
                  "max_token_num": 105,
                  "min_token_num": 2,
                  "avg_token_num": 19
                }
              }
            },
            "labels": {
              "dev": {
                "total_num": 2421,
                "pos_num": 1080,
                "hard_neg_num": 1341
              },
              "test": {
                "total_num": 9525,
                "pos_num": 4292,
                "hard_neg_num": 5233
              }
            }
        }
    },
    "de": {
        "default": {
            "name": "Multilingual Legal Pile",
            "source": "https://huggingface.co/datasets/joelniklaus/Multi_Legal_Pile",
            "splits": ["dev", "test"],
            "size": {
              "corpus": 752913,
              "queries": {
                "dev": 345,
                "test": 1382
              }
            },
            "token_num": {
              "corpus": {
                "max_token_num": 9999,
                "min_token_num": 22,
                "avg_token_num": 3361
              },
              "queries": {
                "dev": {
                  "max_token_num": 121,
                  "min_token_num": 5,
                  "avg_token_num": 24
                },
                "test": {
                  "max_token_num": 159,
                  "min_token_num": 4,
                  "avg_token_num": 25
                }
              }
            },
            "labels": {
              "dev": {
                "total_num": 2472,
                "pos_num": 1373,
                "hard_neg_num": 1099
              },
              "test": {
                "total_num": 10122,
                "pos_num": 5500,
                "hard_neg_num": 4622
              }
            }
        }
    },
    "fr": {
        "default": {
            "name": "Multilingual Legal Pile",
            "source": "https://huggingface.co/datasets/joelniklaus/Multi_Legal_Pile",
            "splits": ["dev", "test"],
            "size": {
              "corpus": 649017,
              "queries": {
                "dev": 348,
                "test": 1394
              }
            },
            "token_num": {
              "corpus": {
                "max_token_num": 9999,
                "min_token_num": 28,
                "avg_token_num": 2540
              },
              "queries": {
                "dev": {
                  "max_token_num": 74,
                  "min_token_num": 5,
                  "avg_token_num": 23
                },
                "test": {
                  "max_token_num": 87,
                  "min_token_num": 2,
                  "avg_token_num": 22
                }
              }
            },
            "labels": {
              "dev": {
                "total_num": 2577,
                "pos_num": 1371,
                "hard_neg_num": 1206
              },
              "test": {
                "total_num": 10503,
                "pos_num": 5535,
                "hard_neg_num": 4968
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
            "splits": ["dev", "test"],
            "size": {
              "corpus": 222877,
              "queries": {
                "dev": 346,
                "test": 1385
              }
            },
            "token_num": {
              "corpus": {
                "max_token_num": 9654,
                "min_token_num": 11,
                "avg_token_num": 334
              },
              "queries": {
                "dev": {
                  "max_token_num": 91,
                  "min_token_num": 4,
                  "avg_token_num": 19
                },
                "test": {
                  "max_token_num": 82,
                  "min_token_num": 4,
                  "avg_token_num": 19
                }
              }
            },
            "labels": {
              "dev": {
                "total_num": 2321,
                "pos_num": 1091,
                "hard_neg_num": 1230
              },
              "test": {
                "total_num": 9307,
                "pos_num": 4249,
                "hard_neg_num": 5058
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
            "splits": ["dev", "test"],
            "size": {
              "corpus": 574417,
              "queries": {
                "dev": 322,
                "test": 1292
              }
            },
            "token_num": {
              "corpus": {
                "max_token_num": 14119,
                "min_token_num": 15,
                "avg_token_num": 531
              },
              "queries": {
                "dev": {
                  "max_token_num": 74,
                  "min_token_num": 4,
                  "avg_token_num": 16
                },
                "test": {
                  "max_token_num": 137,
                  "min_token_num": 3,
                  "avg_token_num": 16
                }
              }
            },
            "labels": {
              "dev": {
                "total_num": 2581,
                "pos_num": 1206,
                "hard_neg_num": 1375
              },
              "test": {
                "total_num": 10001,
                "pos_num": 4592,
                "hard_neg_num": 5409
              }
            }
        }
    },
    "zh": {
        "default": {
            "name": "Multilingual CC-News",
            "source": "https://huggingface.co/datasets/intfloat/multilingual_cc_news",
            "splits": ["dev", "test"],
            "size": {
              "corpus": 935162,
              "queries": {
                "dev": 339,
                "test": 1358
              }
            },
            "token_num": {
              "corpus": {
                "max_token_num": 44111,
                "min_token_num": 17,
                "avg_token_num": 1263
              },
              "queries": {
                "dev": {
                  "max_token_num": 348,
                  "min_token_num": 6,
                  "avg_token_num": 32
                },
                "test": {
                  "max_token_num": 223,
                  "min_token_num": 2,
                  "avg_token_num": 30
                }
              }
            },
            "labels": {
              "dev": {
                "total_num": 2831,
                "pos_num": 1477,
                "hard_neg_num": 1354
              },
              "test": {
                "total_num": 11168,
                "pos_num": 5904,
                "hard_neg_num": 5264
              }
            }
        }
    },
    "ar": {
        "default": {
            "name": "Multilingual CC-News",
            "source": "https://huggingface.co/datasets/intfloat/multilingual_cc_news",
            "splits": ["dev", "test"],
            "size": {
              "corpus": 1006308,
              "queries": {
                "dev": 349,
                "test": 1396
              }
            },
            "token_num": {
              "corpus": {
                "max_token_num": 9996,
                "min_token_num": 16,
                "avg_token_num": 992
              },
              "queries": {
                "dev": {
                  "max_token_num": 252,
                  "min_token_num": 10,
                  "avg_token_num": 42
                },
                "test": {
                  "max_token_num": 278,
                  "min_token_num": 7,
                  "avg_token_num": 43
                }
              }
            },
            "labels": {
              "dev": {
                "total_num": 3117,
                "pos_num": 1810,
                "hard_neg_num": 1307
              },
              "test": {
                "total_num": 12435,
                "pos_num": 7169,
                "hard_neg_num": 5266
              }
            }
        }
    },
    "bn": {
        "default": {
            "name": "Multilingual CC-News",
            "source": "https://huggingface.co/datasets/intfloat/multilingual_cc_news",
            "splits": ["dev", "test"],
            "size": {
              "corpus": 20681,
              "queries": {
                "dev": 289,
                "test": 1159
              }
            },
            "token_num": {
              "corpus": {
                "max_token_num": 9984,
                "min_token_num": 16,
                "avg_token_num": 912
              },
              "queries": {
                "dev": {
                  "max_token_num": 431,
                  "min_token_num": 6,
                  "avg_token_num": 84
                },
                "test": {
                  "max_token_num": 600,
                  "min_token_num": 6,
                  "avg_token_num": 78
                }
              }
            },
            "labels": {
              "dev": {
                "total_num": 1303,
                "pos_num": 562,
                "hard_neg_num": 741
              },
              "test": {
                "total_num": 5282,
                "pos_num": 2269,
                "hard_neg_num": 3013
              }
            }
        }
    },
    "de": {
        "default": {
            "name": "Multilingual CC-News",
            "source": "https://huggingface.co/datasets/intfloat/multilingual_cc_news",
            "splits": ["dev", "test"],
            "size": {
              "corpus": 1006876,
              "queries": {
                "dev": 336,
                "test": 1348
              }
            },
            "token_num": {
              "corpus": {
                "max_token_num": 9985,
                "min_token_num": 17,
                "avg_token_num": 659
              },
              "queries": {
                "dev": {
                  "max_token_num": 127,
                  "min_token_num": 2,
                  "avg_token_num": 23
                },
                "test": {
                  "max_token_num": 144,
                  "min_token_num": 2,
                  "avg_token_num": 23
                }
              }
            },
            "labels": {
              "dev": {
                "total_num": 2682,
                "pos_num": 1448,
                "hard_neg_num": 1234
              },
              "test": {
                "total_num": 11166,
                "pos_num": 5990,
                "hard_neg_num": 5176
              }
            }
        }
    },
    "es": {
        "default": {
            "name": "Multilingual CC-News",
            "source": "https://huggingface.co/datasets/intfloat/multilingual_cc_news",
            "splits": ["dev", "test"],
            "size": {
              "corpus": 1007104,
              "queries": {
                "dev": 337,
                "test": 1351
              }
            },
            "token_num": {
              "corpus": {
                "max_token_num": 9985,
                "min_token_num": 16,
                "avg_token_num": 615
              },
              "queries": {
                "dev": {
                  "max_token_num": 160,
                  "min_token_num": 4,
                  "avg_token_num": 23
                },
                "test": {
                  "max_token_num": 169,
                  "min_token_num": 3,
                  "avg_token_num": 23
                }
              }
            },
            "labels": {
              "dev": {
                "total_num": 2781,
                "pos_num": 1541,
                "hard_neg_num": 1240
              },
              "test": {
                "total_num": 11503,
                "pos_num": 6246,
                "hard_neg_num": 5257
              }
            }
        }
    },
    "fa": {
        "default": {
            "name": "Multilingual CC-News",
            "source": "https://huggingface.co/datasets/intfloat/multilingual_cc_news",
            "splits": ["dev", "test"],
            "size": {
              "corpus": 1002797,
              "queries": {
                "dev": 346,
                "test": 1386
              }
            },
            "token_num": {
              "corpus": {
                "max_token_num": 9999,
                "min_token_num": 16,
                "avg_token_num": 1351
              },
              "queries": {
                "dev": {
                  "max_token_num": 340,
                  "min_token_num": 6,
                  "avg_token_num": 50
                },
                "test": {
                  "max_token_num": 380,
                  "min_token_num": 5,
                  "avg_token_num": 48
                }
              }
            },
            "labels": {
              "dev": {
                "total_num": 3293,
                "pos_num": 1952,
                "hard_neg_num": 1341
              },
              "test": {
                "total_num": 13238,
                "pos_num": 7885,
                "hard_neg_num": 5353
              }
            }
        }
    },
    "fr": {
        "default": {
            "name": "Multilingual CC-News",
            "source": "https://huggingface.co/datasets/intfloat/multilingual_cc_news",
            "splits": ["dev", "test"],
            "size": {
              "corpus": 1007592,
              "queries": {
                "dev": 345,
                "test": 1383
              }
            },
            "token_num": {
              "corpus": {
                "max_token_num": 9967,
                "min_token_num": 16,
                "avg_token_num": 641
              },
              "queries": {
                "dev": {
                  "max_token_num": 108,
                  "min_token_num": 2,
                  "avg_token_num": 23
                },
                "test": {
                  "max_token_num": 163,
                  "min_token_num": 3,
                  "avg_token_num": 22
                }
              }
            },
            "labels": {
              "dev": {
                "total_num": 2972,
                "pos_num": 1548,
                "hard_neg_num": 1424
              },
              "test": {
                "total_num": 11818,
                "pos_num": 6224,
                "hard_neg_num": 5594
              }
            }
        }
    },
    "hi": {
        "default": {
            "name": "Multilingual CC-News",
            "source": "https://huggingface.co/datasets/intfloat/multilingual_cc_news",
            "splits": ["dev", "test"],
            "size": {
              "corpus": 1006218,
              "queries": {
                "dev": 349,
                "test": 1398
              }
            },
            "token_num": {
              "corpus": {
                "max_token_num": 9999,
                "min_token_num": 16,
                "avg_token_num": 1465
              },
              "queries": {
                "dev": {
                  "max_token_num": 381,
                  "min_token_num": 8,
                  "avg_token_num": 66
                },
                "test": {
                  "max_token_num": 630,
                  "min_token_num": 7,
                  "avg_token_num": 67
                }
              }
            },
            "labels": {
              "dev": {
                "total_num": 2980,
                "pos_num": 1716,
                "hard_neg_num": 1264
              },
              "test": {
                "total_num": 12201,
                "pos_num": 7039,
                "hard_neg_num": 5162
              }
            }
        }
    },
    "id": {
        "default": {
            "name": "Multilingual CC-News",
            "source": "https://huggingface.co/datasets/intfloat/multilingual_cc_news",
            "splits": ["dev", "test"],
            "size": {
              "corpus": 1007724,
              "queries": {
                "dev": 338,
                "test": 1356
              }
            },
            "token_num": {
              "corpus": {
                "max_token_num": 9789,
                "min_token_num": 16,
                "avg_token_num": 548
              },
              "queries": {
                "dev": {
                  "max_token_num": 208,
                  "min_token_num": 6,
                  "avg_token_num": 24
                },
                "test": {
                  "max_token_num": 228,
                  "min_token_num": 4,
                  "avg_token_num": 24
                }
              }
            },
            "labels": {
              "dev": {
                "total_num": 3196,
                "pos_num": 1799,
                "hard_neg_num": 1397
              },
              "test": {
                "total_num": 13103,
                "pos_num": 7485,
                "hard_neg_num": 5618
              }
            }
        }
    },
    "ja": {
        "default": {
            "name": "Multilingual CC-News",
            "source": "https://huggingface.co/datasets/intfloat/multilingual_cc_news",
            "splits": ["dev", "test"],
            "size": {
              "corpus": 834364,
              "queries": {
                "dev": 344,
                "test": 1378
              }
            },
            "token_num": {
              "corpus": {
                "max_token_num": 9999,
                "min_token_num": 17,
                "avg_token_num": 1559
              },
              "queries": {
                "dev": {
                  "max_token_num": 296,
                  "min_token_num": 6,
                  "avg_token_num": 35
                },
                "test": {
                  "max_token_num": 185,
                  "min_token_num": 4,
                  "avg_token_num": 36
                }
              }
            },
            "labels": {
              "dev": {
                "total_num": 3151,
                "pos_num": 1817,
                "hard_neg_num": 1334
              },
              "test": {
                "total_num": 11787,
                "pos_num": 6590,
                "hard_neg_num": 5197
              }
            }
        }
    },
    "ko": {
        "default": {
            "name": "Multilingual CC-News",
            "source": "https://huggingface.co/datasets/intfloat/multilingual_cc_news",
            "splits": ["dev", "test"],
            "size": {
              "corpus": 1006798,
              "queries": {
                "dev": 361,
                "test": 1447
              }
            },
            "token_num": {
              "corpus": {
                "max_token_num": 9998,
                "min_token_num": 21,
                "avg_token_num": 1072
              },
              "queries": {
                "dev": {
                  "max_token_num": 136,
                  "min_token_num": 6,
                  "avg_token_num": 34
                },
                "test": {
                  "max_token_num": 239,
                  "min_token_num": 4,
                  "avg_token_num": 36
                }
              }
            },
            "labels": {
              "dev": {
                "total_num": 3380,
                "pos_num": 1967,
                "hard_neg_num": 1413
              },
              "test": {
                "total_num": 13573,
                "pos_num": 7908,
                "hard_neg_num": 5665
              }
            }
        }
    },
    "ru": {
        "default": {
            "name": "Multilingual CC-News",
            "source": "https://huggingface.co/datasets/intfloat/multilingual_cc_news",
            "splits": ["dev", "test"],
            "size": {
              "corpus": 1004550,
              "queries": {
                "dev": 337,
                "test": 1352
              }
            },
            "token_num": {
              "corpus": {
                "max_token_num": 9999,
                "min_token_num": 17,
                "avg_token_num": 776
              },
              "queries": {
                "dev": {
                  "max_token_num": 200,
                  "min_token_num": 6,
                  "avg_token_num": 34
                },
                "test": {
                  "max_token_num": 236,
                  "min_token_num": 5,
                  "avg_token_num": 33
                }
              }
            },
            "labels": {
              "dev": {
                "total_num": 2977,
                "pos_num": 1676,
                "hard_neg_num": 1301
              },
              "test": {
                "total_num": 11847,
                "pos_num": 6689,
                "hard_neg_num": 5158
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
            "splits": ["dev", "test"],
            "size": {
              "corpus": 26266,
              "queries": {
                "dev": 317,
                "test": 1268
              }
            },
            "token_num": {
              "corpus": {
                "max_token_num": 5632,
                "min_token_num": 18,
                "avg_token_num": 202
              },
              "queries": {
                "dev": {
                  "max_token_num": 77,
                  "min_token_num": 3,
                  "avg_token_num": 17
                },
                "test": {
                  "max_token_num": 107,
                  "min_token_num": 2,
                  "avg_token_num": 17
                }
              }
            },
            "labels": {
              "dev": {
                "total_num": 1749,
                "pos_num": 627,
                "hard_neg_num": 1122
              },
              "test": {
                "total_num": 7203,
                "pos_num": 2730,
                "hard_neg_num": 4473
              }
            }
        }
    },
    "zh": {
        "default": {
            "name": "FinCorpus (fin_articles)",
            "source": "https://huggingface.co/datasets/Duxiaoman-DI/FinCorpus",
            "splits": ["dev", "test"],
            "size": {
              "corpus": 1014974,
              "queries": {
                "dev": 361,
                "test": 1444
              }
            },
            "token_num": {
              "corpus": {
                "max_token_num": 19686,
                "min_token_num": 28,
                "avg_token_num": 1613
              },
              "queries": {
                "dev": {
                  "max_token_num": 211,
                  "min_token_num": 5,
                  "avg_token_num": 29
                },
                "test": {
                  "max_token_num": 193,
                  "min_token_num": 3,
                  "avg_token_num": 29
                }
              }
            },
            "labels": {
              "dev": {
                "total_num": 2987,
                "pos_num": 1516,
                "hard_neg_num": 1471
              },
              "test": {
                "total_num": 12060,
                "pos_num": 6320,
                "hard_neg_num": 5740
              }
            }
        }
    },
    "ar": {
        "default": {
            "name": "financial_news",
            "source": "https://huggingface.co/datasets/asas-ai/financial_news",
            "splits": ["dev", "test"],
            "size": {
              "corpus": 11235,
              "queries": {
                "dev": 293,
                "test": 1175
              }
            },
            "token_num": {
              "corpus": {
                "max_token_num": 8639,
                "min_token_num": 16,
                "avg_token_num": 397
              },
              "queries": {
                "dev": {
                  "max_token_num": 306,
                  "min_token_num": 7,
                  "avg_token_num": 49
                },
                "test": {
                  "max_token_num": 397,
                  "min_token_num": 7,
                  "avg_token_num": 46
                }
              }
            },
            "labels": {
              "dev": {
                "total_num": 1362,
                "pos_num": 635,
                "hard_neg_num": 727
              },
              "test": {
                "total_num": 5755,
                "pos_num": 2796,
                "hard_neg_num": 2959
              }
            }
        }
    },
    "fr": {
        "default": {
            "name": "CoFiF",
            "source": "https://huggingface.co/datasets/FrancophonIA/CoFiF",
            "splits": ["dev", "test"],
            "size": {
              "corpus": 1006801,
              "queries": {
                "dev": 310,
                "test": 1243
              }
            },
            "token_num": {
              "corpus": {
                "max_token_num": 6008,
                "min_token_num": 16,
                "avg_token_num": 92
              },
              "queries": {
                "dev": {
                  "max_token_num": 65,
                  "min_token_num": 3,
                  "avg_token_num": 21
                },
                "test": {
                  "max_token_num": 85,
                  "min_token_num": 4,
                  "avg_token_num": 20
                }
              }
            },
            "labels": {
              "dev": {
                "total_num": 2912,
                "pos_num": 1841,
                "hard_neg_num": 1071
              },
              "test": {
                "total_num": 11568,
                "pos_num": 7206,
                "hard_neg_num": 4362
              }
            }
        }
    },
}

QAScienceTask = {
    "ru": {
        "default": {
            "name": "ruSciBench",
            "source": "https://huggingface.co/datasets/mlsa-iai-msu-lab/ru_sci_bench",
            "splits": ["dev", "test"],
            "size": {
              "corpus": 200532,
              "queries": {
                "dev": 345,
                "test": 1382
              }
            },
            "token_num": {
              "corpus": {
                "max_token_num": 6318,
                "min_token_num": 16,
                "avg_token_num": 347
              },
              "queries": {
                "dev": {
                  "max_token_num": 198,
                  "min_token_num": 4,
                  "avg_token_num": 34
                },
                "test": {
                  "max_token_num": 191,
                  "min_token_num": 6,
                  "avg_token_num": 33
                }
              }
            },
            "labels": {
              "dev": {
                "total_num": 2737,
                "pos_num": 1577,
                "hard_neg_num": 1160
              },
              "test": {
                "total_num": 10673,
                "pos_num": 6018,
                "hard_neg_num": 4655
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
            "splits": ["dev"],
            "size": {
              "corpus": 8872840,
              "queries": {
                "dev": 6319
              }
            },
            "token_num": {
              "corpus": {
                "max_token_num": 50888,
                "min_token_num": 2,
                "avg_token_num": 81
              },
              "queries": {
                "dev": {
                  "max_token_num": 92,
                  "min_token_num": 2,
                  "avg_token_num": 16
                }
              }
            },
            "labels": {
              "dev": {
                "total_num": 58275,
                "pos_num": 31447,
                "hard_neg_num": 26828
              }
            }
        }
    },
}
