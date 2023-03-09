import json
from pypdf import PdfReader

finalObj = {
    'O1A': {},
    'O1R': {},
    'O2R': {},
    'O3R': {},
    'O4R': {},
    'L1R': {},
    'E1R': {},
    'O1M': {}
}

def breakdownData(input, huntCode, startPage, pageCount, species):
    reader = PdfReader(input)

    for i in range(pageCount):
        archeryIndex = i + startPage
        page = reader.pages[archeryIndex]
        pageText = page.extract_text()
        pageLines = pageText.splitlines()
        lastHeaderIndex = 6
        
        for j in range(lastHeaderIndex, len(pageLines) - 2, 1):
            dataStr = pageLines[j]
            dataStr = dataStr.replace('sum ', '')
        
            dataArr = dataStr.split(' ')
            if species == 'pronghorn':
                print(dataArr)
            if 'Total' not in dataArr and 'Days' not in dataArr and 'ntler' and len(dataArr) > 7:
                if species == 'elk':
                    finalObj[huntCode][dataArr[0]] = {
                        'bulls': dataArr[1],
                        'cows': dataArr[2],
                        'calves': dataArr[3],
                        'total': dataArr[4],
                        'hunters': dataArr[5],
                        'successPercent': dataArr[6],
                        'recDays': dataArr[7]
                    }
                else:
                    finalObj[huntCode][dataArr[0]] = {
                        'bucks': dataArr[1],
                        'does': dataArr[2],
                        'fawns': dataArr[3],
                        'total': dataArr[4],
                        'hunters': dataArr[5],
                        'successPercent': dataArr[6],
                        'recDays': dataArr[7]
                    }


def getHarvestData(harvestInput, harvestMap, species):

    for key in harvestMap:
        breakdownData(harvestInput, key, harvestMap[key]['startIndex'], harvestMap[key]['totalPages'], species)
    

    return finalObj

    # with open("../../outputs/colorado/co-elk-harvest-stats.json", "w") as outfile:
    #     json.dump(finalObj, outfile)
