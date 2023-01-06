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
        'startIndex': 59,
        'totalPages': 4,
    },
    'O2R': {
        'startIndex': 59,
        'totalPages': 4,
    },
    'O3R': {
        'startIndex': 59,
        'totalPages': 4,
    },
    'O4R': {
        'startIndex': 59,
        'totalPages': 4,
    }
}
archeryPages = [55, 4]
muzzleLoaderPages = [59, 62]
riflePages = [22,36]
finalObj = {
    'O1A': {},
    'O1M': {},
    'O1R': {},
    'O2R': {},
    'O3R': {},
    'O4R': {}
}

index = 0
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
            if (j == 6):
                dataStr = dataStr.replace('sum ', '')
        
            dataArr = dataStr.split(' ')
            if 'Total' not in dataArr:
                # HUNT CODE
                finalObj[huntCode][dataArr[0]] = {
                    'bulls': dataArr[1],
                    'cows': dataArr[2],
                    'calves': dataArr[3],
                    'total': dataArr[4],
                    'hunters': dataArr[5],
                    'successPercent': dataArr[6],
                    'recDays': dataArr[7]
                }
                
    print(finalObj)
        ## if row has total
        ## remove sum sum sum from 
        # remove last 
        # if length is too short
        # print(pageLines)

# def cleanUpData(dataRow):
#     if dataRow.length > 1


def main():
    getHarvestData('O1A', 55, 4)
    

main()