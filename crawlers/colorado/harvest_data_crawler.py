import json
from pypdf import PdfReader

def breakdownData(input, huntCode, startPage, pageCount, species):
    if species == 'pronghorn':
        return getPronghornData(input, startPage, pageCount)
    elif species == 'elk':
        return getElkData(input, startPage, pageCount)
    elif species == 'deer':
        return getDeerData(input, startPage, pageCount, huntCode)
                    

def getElkData(input, startPage, pageCount):
    returnObj = {}
    reader = PdfReader(input)
    for i in range(pageCount):
        pageIndex = i + startPage
        page = reader.pages[pageIndex]
        pageText = page.extract_text()
        pageLines = pageText.splitlines()
        lastHeaderIndex = 6
        
        for j in range(lastHeaderIndex, len(pageLines) - 2, 1):
            dataStr = pageLines[j]
            dataStr = dataStr.replace('sum ', '')
            dataArr = dataStr.split(' ')

            if 'Total' not in dataArr and 'Days' not in dataArr and 'ntler' and len(dataArr) > 7 and 'GMU' not in dataArr:
                returnObj[dataArr[0]] = {
                    'bulls': dataArr[1],
                    'cows': dataArr[2],
                    'calves': dataArr[3],
                    'total': dataArr[4],
                    'hunters': dataArr[5],
                    'successPercent': dataArr[6],
                    'recDays': dataArr[7]
                }
    return returnObj

def getDeerData(input, startPage, pageCount, huntCode):
    reader = PdfReader(input)
    returnObj = {}
    for i in range(pageCount):
        pageIndex = i + startPage
        page = reader.pages[pageIndex]
        pageText = page.extract_text()
        pageLines = pageText.splitlines()
        lastHeaderIndex = 6

        ## Problem pulling muzzle loader data, will have to revisit

        for j in range(lastHeaderIndex, len(pageLines) - 2, 1):
            dataStr = pageLines[j]
            dataStr = dataStr.replace('sum ', '')
            dataArr = dataStr.split(' ')

            if 'Total' not in dataArr and 'Days' not in dataArr and 'ntler' and len(dataArr) > 7 and 'GMU' not in dataArr:
                returnObj[dataArr[0]] = {
                    'bucks': dataArr[1],
                    'does': dataArr[2],
                    'fawns': dataArr[3],
                    'total': dataArr[4],
                    'hunters': dataArr[5],
                    'successPercent': dataArr[6],
                    'recDays': dataArr[7]
                }
    return returnObj

def getPronghornData(input, startPage, pageCount):
    reader = PdfReader(input)
    returnObj = {}
    for i in range(pageCount):
        pageIndex = i + startPage
        page = reader.pages[pageIndex]
        pageText = page.extract_text()
        pageLines = pageText.splitlines()
        lastHeaderIndex = 7

        for j in range(lastHeaderIndex, len(pageLines) - 2, 1):
            dataStr = pageLines[j]
            dataStr = dataStr.replace('sum ', '')    
            dataArr = dataStr.split(' ')

            if 'Total' not in dataArr and 'Days' not in dataArr and 'ntler' and len(dataArr) > 7 and 'GMU' not in dataArr:
                returnObj[dataArr[0]] = {
                    'bucks': dataArr[1],
                    'does': dataArr[2],
                    'fawns': dataArr[3],
                    'total': dataArr[4],
                    'hunters': dataArr[5],
                    'successPercent': dataArr[6],
                    'recDays': dataArr[7]
                }
    return returnObj


def getHarvestData(harvestInput, harvestMap, species):
    finalObj = {}

    for key in harvestMap:
        finalObj[key] = {}

    for key in harvestMap:
        finalObj[key] = breakdownData(harvestInput, key, harvestMap[key]['startIndex'], harvestMap[key]['totalPages'], species)

    return finalObj
