import json
from pdf2image import convert_from_path
import pytesseract

def extract_text_from_pdf(pdf_path):
    # Convert PDF to images
    pages = convert_from_path(pdf_path)

    # Process each page
    text = ""
    for page in pages:
        text += pytesseract.image_to_string(page) + "\n"

    return text


pdf_path = '../../data/colorado/population_estimates/2022ElkPopulationEstimates.pdf'
extracted_text = extract_text_from_pdf(pdf_path)
# print(extracted_text)

def getHerdNameAndUnits(textArr):
    herdName = ''
    units = []
    for item in textArr:
        itemRemovedComma = item.replace(',', '')
        if itemRemovedComma.isnumeric():
            units.append(itemRemovedComma)
        else:
            herdName += itemRemovedComma + ' '
    
    return (herdName, units)

extractedTextArr =  extracted_text.split('\n')

startIndex = 6
endIndex = len(extractedTextArr) - 10
state = 'colorado'
species = 'elk'
year = 2022
# example arr Item = [{
#   state: 'co',
#   species: 'elk',
#   year: 2022,
#   unit: 2,
#   dau: 1,
#   otherUnitsInDau: [1,2,3],
#   populationEstimate: 100,
#   maleFemaleRatio: 22
# }]
unitPopulationStatsArr = []

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
    
    print(dau, herdName, units, populationEstimate, maleFemaleRatio)

print(unitPopulationStatsArr)

output_path = '../../data/colorado/population_estimates/outputs/2022_elk_pop_est.json'

with open(output_path, 'w') as file:
    json.dump(unitPopulationStatsArr, file, indent=4)
