from data_map import wyoming
from draw_stats import getWyomingDrawStats

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
    for drawType in drawStatsSource:
        getWyomingDrawStats(drawType['input'])