import json
from data_map import wyoming
from draw_stats import getDrawStats

firebaseUploadJsonPath = '/Users/grantfogle/Desktop/workspace/startups/tagout/tagout-py/outputs/wyoming/firebase-upload.json'
finalObj = {
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


def fetchDrawStats(drawStatsSource, species):

    # getRandomDrawStats('E', 'NR', 'Random')
    for drawType in drawStatsSource:

        # print(drawStatsSource[drawType])
        for resident in drawStatsSource[drawType]:
            inputPdf = drawStatsSource[drawType][resident]['input']
            if inputPdf:

                drawStats = getDrawStats(
                    inputPdf, species, resident, drawType)
                finalObj[species]['drawStats'][drawType][resident] = drawStats
                print('=====', finalObj)
            # getDrawStats()
            # print('=============', finalObj)


for species in wyoming:
    # print(species)
    fetchDrawStats(wyoming[species]['drawStats'], species)

with open(firebaseUploadJsonPath, "w") as outfile:
    json.dump(finalObj, outfile)
