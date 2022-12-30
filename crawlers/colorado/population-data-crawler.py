import json
from crawlerMap import colorado
from pypdf import PdfReader

def main():
    index = 0
    reader = PdfReader(colorado['elk']['populationStatsInput'])
    page = reader.pages[0]
    pageText = page.extract_text()
    pageLines = pageText.splitlines()
    finalDataObj = {}

    for dataLine in pageLines:
        if (index > 4 and index < 47):
            dataObj = getFormattedData(dataLine)
            for unit in dataObj:
                finalDataObj[unit] = dataObj[unit]                
        index += 1

    print(finalDataObj)
    with open(colorado['elk']['populationStatsOutput'], "w") as outfile:
        json.dump(finalDataObj, outfile)

def getFormattedData(popLine):
    pop = popLine.split(' ')
    slicedPop = pop[1 : (len(pop) - 2)]
    finalObj = {}
    obj = {
        'dau': pop[0],
        'populationEstimate': pop[len(pop) - 2],
        'bullCowRatio': pop[len(pop) - 1],
        'dauUnits': []
    }
    for item in slicedPop:
        removedCommas = item.replace(',', '')
        if removedCommas.isnumeric():
            obj['dauUnits'].append(removedCommas)
    for unit in obj['dauUnits']:
        finalObj[unit] = obj

    return finalObj
    #  if 
    #
    #
    dataObj = {}
    # print(slicedPop)

# first number is dau
# if it's a string then it's herd name
# middle numbers are units
# second to last number is population estimate
# last number is bull cow ratio
# coloradoDataTables = camelot.read_pdf(colorado['elk']['populationStatsInput'], pages="all")

# for table in coloradoDataTables:
#     print(table)
#     print(table[0])
main()