import json
from crawler_map import colorado
from draw_stats_crawler_pypdf import getDrawStats
from harvest_data_crawler import getHarvestData
from population_data_crawler import getPopulationData

firebaseUploadJsonPath = '../../outputs/colorado/firebase-upload/firebase-upload.json'
finalObj = {
    'colorado': {
        'elk': {
            'populationStats': {},
            'harvestStats': {},
            'drawStats': {}
        },
        'pronghorn': {
            'populationStats': {},
            'harvestStats': {},
            'drawStats': {}
        },
        'deer': {
            'populationStats': {},
            'harvestStats': {},
            'drawStats': {}},
        'bear': {
            'populationStats': {},
            'harvestStats': {},
            'drawStats': {}
        }
    }
}

for species in colorado:

    if species != 'bear':
        drawStatsInput = colorado[species]['drawStats']['input']
        popInput = colorado[species]['populationStats']['input']
        harvestInput = colorado[species]['harvestStats']['input']
        harvestDataMap = colorado[species]['harvestStats']['harvestMap']
        drawStatsStart = colorado[species]['drawStats']['drawStatsMap']['startIndex']
        drawStatsEnd = colorado[species]['drawStats']['drawStatsMap']['endIndex']

        drawStatsData = getDrawStats(drawStatsInput, drawStatsStart, drawStatsEnd)
        populationData = getPopulationData(popInput)
        harvestData = getHarvestData(colorado[species]['harvestStats']['input'], harvestDataMap, species)
        
        finalObj['colorado'][species]['populationStats'] = populationData
        finalObj['colorado'][species]['harvestStats'] = harvestData
        finalObj['colorado'][species]['drawStats'] = drawStatsData    
    

with open(firebaseUploadJsonPath, "w") as outfile:
         json.dump(finalObj, outfile)
