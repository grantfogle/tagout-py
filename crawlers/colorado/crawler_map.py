colorado = {
    'elk': {
        # 'unitRegex': 'E[A-Z]\d\d\d[A-Z]\d[A-Z]',
        'drawStats': {
            'input': '../../inputs/colorado/elk/2021ElkDrawRecap.pdf',
            'output': '../../outputs/colorado/elk/2022-co-elk-draw-stats.json',
            'drawStatsMap': {
                'startIndex': 2,
                'endIndex': 963
            }
        },
        'populationStats': {
            'input': '../../inputs/colorado/elk/2021ElkPopulationEstimates.pdf',
            'output': '../../outputs/colorado/elk/co-elk-populations.json',
        },
        'harvestStats': {
            'input': '../../inputs/colorado/elk/2021StatewideElkHarvest.pdf',
            'output': '../../outputs/colorado/elk/co-elk-populations.json',
            'harvestMap': {
                'O1A': {
                    'startIndex': 55,
                    'totalPages': 4,
                },
                'O1M': {
                    'startIndex': 59,
                    'totalPages': 4,
                },
                'O1R': {
                    'startIndex': 21,
                    'totalPages': 4,
                },
                'O2R': {
                    'startIndex': 25,
                    'totalPages': 4,
                },
                'O3R': {
                    'startIndex': 29,
                    'totalPages': 4,
                },
                'O4R': {
                    'startIndex': 33,
                    'totalPages': 4,
                }
            }
        }
    },
    'pronghorn': {
        'drawStats': {
            'input': '../../inputs/colorado/pronghorn/2021PronghornDrawRecap.pdf',
            'output': '../../outputs/colorado/pronghorn/pronghorn-draw-stats.json',
            'drawStatsMap': {
                'startIndex': 2,
                'endIndex': 357
            }
        },
        'populationStats': {
            'input': '../../inputs/colorado/pronghorn/2021PronghornPopulationEstimates.pdf',
            'output': '../../outputs/colorado/pronghorn/pronghorn-population-stats.json',
        },
        'harvestStats': {
            'input': '../../inputs/colorado/pronghorn/2021StatewidePronghornHarvest.pdf',
            'output': '../../outputs/colorado/pronghorn/pronghorn-harvest-stats.json',
            'harvestMap': {
                'O1A': {
                    'startIndex': 15,
                    'totalPages': 3,
                },
                'O1M': {
                    'startIndex': 18,
                    'totalPages': 3,
                },
                'O1R': {
                    'startIndex': 10,
                    'totalPages': 3,
                },
                'L1R': {
                    'startIndex': 13,
                    'totalPages': 2,
                }
            }
        }
    },
    'deer': {
        'drawStats': {
            'input': '../../inputs/colorado/deer/2021DeerDrawRecap.pdf',
            'output': '../../outputs/colorado/deer/deer-draw-stats.json',
            'drawStatsMap': {
                'startIndex': 2,
                'endIndex': 1049
            }
        },
        'populationStats': {
            'input': '../../inputs/colorado/deer/2021DeerPopulationEstimates.pdf',
            'output': '../../outputs/colorado/deer/deer-population-stats.json',
        },
        'harvestStats': {
            'input': '../../inputs/colorado/deer/2021StatewideDeerHarvest.pdf',
            'output': '../../outputs/colorado/deer/deer-harvest-stats.json',
            'harvestMap': {
                'O1A': {
                    'startIndex': 32,
                    'totalPages': 5,
                },
                'O1M': {
                    'startIndex': 42,
                    'totalPages': 5,
                },
                'E1R': {
                    'startIndex': 20,
                    'totalPages': 3,
                },
                'L1R': {
                    'startIndex': 20,
                    'totalPages': 3,
                },
                'O2R': {
                    'startIndex': 23,
                    'totalPages': 3,
                },
                'O3R': {
                    'startIndex': 26,
                    'totalPages': 3,
                },
                'O4R': {
                    'startIndex': 29,
                    'totalPages': 3,
                }
            }
        }
    },
    # 'bear': {
    #     'drawStats': {
    #         'input': '../../inputs/colorado/bear/2022BearDrawRecap.pdf',
    #         'output': '../../outputs/colorado/bear/bear-draw-stats.json',
    #     },
        # 'populationStats': {
        #     'input': '../../inputs/colorado/bear/2021BearPopulationEstimates.pdf',
        #     'output': '../../outputs/colorado/bear/bear-population-stats.json',
        # },
    #     'harvestStats': {
    #         'input': '../../inputs/colorado/bear/2021StatewideBearHarvest.pdf',
    #         'output': '../../outputs/colorado/bear/bear-harvest-stats.json',
    #         'harvestMap': {}
    #     }
    # }
}