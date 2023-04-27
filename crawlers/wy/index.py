import json
from data_map import wyoming
from draw_stats import getDrawStats
from harvest_stats import getHarvestStats

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


def fetchHarvestStats(input, startIndex, endIndex):
    populationStats = getHarvestStats(input, startIndex, endIndex)


for species in wyoming:
    popStatsObj = wyoming[species]['harvestStats']
    # print(species)
    # fetchDrawStats(wyoming[species]['drawStats'], species)
    fetchHarvestStats(
        popStatsObj['input'], popStatsObj['startIndex'], popStatsObj['endIndex'])

with open(firebaseUploadJsonPath, "w") as outfile:
    json.dump(finalObj, outfile)
