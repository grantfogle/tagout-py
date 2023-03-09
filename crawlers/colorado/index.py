import json
from crawler_map import colorado
# from draw_stats_crawler_pypdf import getDrawStats
# from harvest_data_crawler import getHarvestData
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
# get draw stats for all species
for species in colorado:
    # get population stats
    if species != 'bear':
        populationData = getPopulationData(colorado[species]['populationStats']['input'])
        finalObj['colorado'][species]['populationStats'] = populationData
    # harvestData = getHarvestData()
    # drawStatsData = getDrawStatsData()

    print(species)
    print(colorado[species]['drawStats'])
    # finalObj['colorado'][species]['populationStats']
    # finalObj['colorado'][species]['harvestStats']
    # finalObj['colorado'][species]['drawStats']

# get population stats for all species
with open(firebaseUploadJsonPath, "w") as outfile:
         json.dump(finalObj, outfile)

# get harvest stats for all species

# write to the json file...
# create three different upload files


# write to firebase upload