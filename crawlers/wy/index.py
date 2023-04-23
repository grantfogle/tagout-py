from data_map import wyoming
from draw_stats import getDrawStats

finalObj = {
    'wyoming': {
        'elk': {
            'populationStats': {},
            'harvestStats': {},
            'drawStats': {
                'random': {},
                'preferencePoint': {},
                'other': {}
            }
        },
        'pronghorn': {
            'populationStats': {},
            'harvestStats': {},
            'drawStats': {}
        },
        'deer': {
            'populationStats': {},
            'harvestStats': {},
            'drawStats': {}
        },
    }
}

for species in wyoming:
    # getDrawStats()
    print('cats')


def getDrawStats(drawStatsSource):

    getRandomDrawStats('E', 'NR', 'Random')
    for drawType in drawStatsSource:
        getWyomingDrawStats(drawType['input'])
