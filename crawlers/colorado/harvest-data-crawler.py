import json
from crawlerMap import colorado
from pypdf import PdfReader

iterableObj = {
    'O1A': {
        'startIndex': 55,
        'totalPages': 4,
    },
    'O1M': {
        'startIndex': 59,
        'totalPages': 4,
    },
    'O1R': {
        'startIndex': 21,
        'totalPages': 4,
    },
    'O2R': {
        'startIndex': 25,
        'totalPages': 4,
    },
    'O3R': {
        'startIndex': 29,
        'totalPages': 4,
    },
    'O4R': {
        'startIndex': 33,
        'totalPages': 4,
    }
}
finalObj = {
    'O1A': {},
    'O1M': {},
    'O1R': {},
    'O2R': {},
    'O3R': {},
    'O4R': {}
}

reader = PdfReader(colorado['elk']['harvestStatsInput'])

# paramaters: huntCode, startIndex, pages
def getHarvestData(huntCode, startPage, pageCount):
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
            if 'Total' not in dataArr and 'Days' not in dataArr:
                finalObj[huntCode][dataArr[0]] = {
                    'bulls': dataArr[1],
                    'cows': dataArr[2],
                    'calves': dataArr[3],
                    'total': dataArr[4],
                    'hunters': dataArr[5],
                    'successPercent': dataArr[6],
                    'recDays': dataArr[7]
                }
                
    # print(finalObj)
        ## if row has total
        ## remove sum sum sum from 
        # remove last 
        # if length is too short
        # print(pageLines)

# def cleanUpData(dataRow):
#     if dataRow.length > 1


def main():
    for key in iterableObj:
        getHarvestData(key, iterableObj[key]['startIndex'], iterableObj[key]['totalPages'])
    # getHarvestData('O1A', 55, 4)
    # getHarvestData('O1A', 55, 4)
    # getHarvestData('O1A', 55, 4)
    # getHarvestData('O1A', 55, 4)

    with open("../../outputs/colorado/co-elk-harvest-stats.json", "w") as outfile:
        json.dump(finalObj, outfile)

    

main()