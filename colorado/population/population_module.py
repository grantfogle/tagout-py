import json
from extract_text_from_pdf import extract_text_from_pdf

input_path = '../../data/colorado/population_estimates/2022ElkPopulationEstimates.pdf'
output_path = '../../data/colorado/population_estimates/outputs/2022_elk_pop_est.json'

extracted_text = extract_text_from_pdf(input_path)
extractedTextArr =  extracted_text.split('\n')
# beginning of text you want to extract
startIndex = 6
# end of text you want to extract
endIndex = len(extractedTextArr) - 10

state = 'colorado'
species = 'elk'
year = 2022
# current return object
unitPopulationStatsArr = []
# example of object = [{
#   state: 'co',
#   species: 'elk',
#   year: 2022,
#   unit: 2,
#   dau: 1,
#   herdName,
#   otherUnitsInDau: [1,2,3],
#   populationEstimate: 100,
#   maleFemaleRatio: 22
# }]

def getHerdNameAndUnits(textArr):
    herdName = ''
    units = []
    for item in textArr:
        itemRemovedComma = item.replace(',', '')
        if itemRemovedComma.isnumeric():
            units.append(itemRemovedComma)
        else:
            herdName += itemRemovedComma + ' '
    
    return (herdName.strip(), units)

for i in range(startIndex, endIndex):
    splitTextArr = extractedTextArr[i].split(' ')
    dau = splitTextArr[0]
    populationEstimate = splitTextArr[-2]
    maleFemaleRatio = splitTextArr[-1]
    (herdName, units) = getHerdNameAndUnits(splitTextArr[1:-2])

    for unit in units:
        additonalUnitsInDau = [item for item in units if item != unit]
        unitPopulationStatsArr.append({
            'state': state,
            'species': species,
            'year': year,
            'unit': unit,
            'dau': dau,
            'herd_name': herdName,
            'additonal_units_in_dau': additonalUnitsInDau,
            'population_estimate': populationEstimate,
            'male_female_ratio': maleFemaleRatio,
        })

with open(output_path, 'w') as file:
    json.dump(unitPopulationStatsArr, file, indent=4)
