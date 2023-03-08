# future implementation of automating these crawls

colorado = {
    'elk': {
        # 'unitRegex': 'E[A-Z]\d\d\d[A-Z]\d[A-Z]',
        'drawStats': {
            'input': '../../inputs/colorado/2022ElkDrawRecap.pdf',
            'output': '../../outputs/colorado/2022-co-elk-draw-stats.json',
        },
        'populationStats': {
            'input': '../../inputs/colorado/2021ElkPopulationEstimates.pdf',
            'output': '../../outputs/colorado/co-elk-populations.json',
        },
        'harvestStats': {
            'input': '../../inputs/colorado/2021StatewideElkHarvest.pdf',
            'output': '../../outputs/colorado/co-elk-populations.json',
        }
    },
    'pronghorn': {
        'drawStats': {
            'input': '../../inputs/colorado/pronghorn/2022PronghornDrawRecap.pdf',
            'output': '../../outputs/colorado/pronghorn/pronghorn-draw-stats.json',
        },
        'populationStats': {
            'input': '../../inputs/colorado/pronghorn/2021PronghornPopulationEstimates.pdf',
            'output': '../../outputs/colorado/pronghorn/pronghorn-population-stats.json',
        },
        'harvestStats': {
            'input': '../../inputs/colorado/pronghorn/2021StatewidePronghornHarvest.pdf',
            'output': '../../outputs/colorado/pronghorn/pronghorn-harvest-stats.json',
        }
    },
    'deer': {
        'drawStats': {
            'input': '../../inputs/colorado/deer/2022DeerDrawRecap.pdf',
            'output': '../../outputs/colorado/deer/deer-draw-stats.json',
        },
        'populationStats': {
            'input': '../../inputs/colorado/deer/2021DeerPopulationEstimates.pdf',
            'output': '../../outputs/colorado/deer/deer-population-stats.json',
        },
        'harvestStats': {
            'input': '../../inputs/colorado/deer/2021StatewideDeerHarvest.pdf',
            'output': '../../outputs/colorado/deer/deer-harvest-stats.json',
        }
    },
    'bear': {
        'drawStats': {
            'input': '../../inputs/colorado/bear/2022BearDrawRecap.pdf',
            'output': '../../outputs/colorado/bear/bear-draw-stats.json',
        },
        'populationStats': {
            'input': '../../inputs/colorado/bear/2021BearPopulationEstimates.pdf',
            'output': '../../outputs/colorado/bear/bear-population-stats.json',
        },
        'harvestStats': {
            'input': '../../inputs/colorado/bear/2021StatewideBearHarvest.pdf',
            'output': '../../outputs/colorado/bear/bear-harvest-stats.json',
        }
    }
}