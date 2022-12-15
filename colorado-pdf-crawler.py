import camelot
import json
from crawlerMap import coloradoMap
from elkCodes import elkCodes

# get all the tables that you want to crawl
coloradoDataTables = camelot.read_pdf(coloradoMap['drawStatsInput'], pages="3-10")

# global flags for tracking edge cases

def main(coDataTables):
    unitIndex = 1

    orphanedData = False
    firstOrphanedData = False
    
    rawUnitDataObj = {}
    outputDataObj = {}

    for table in coDataTables:
        tableHeader = table.data[0][0]
        tableData = table.data

        if 'Post-Draw Successful' in tableHeader:
            # since haing a negative index with throw an error
            # i want to ensure that i am always using the correct index as
            # 'Post-Draw successful will always be the first table of the
            # data that i want to get
            orphanedData = False
            currentDrawCode = elkCodes[unitIndex-1]
            unitIndex += 1
            formattedPostDrawArr = formatPostDrawData(table.data)

            rawUnitDataObj[currentDrawCode] = {
                'preDraw': [],
                'postDraw': [],
                'totalChoice1': []
            }
            rawUnitDataObj[currentDrawCode]['postDraw'].append(formattedPostDrawArr)
            if len(table.data) > 27:
                orphanedData = True
            # write logic for really big tables that have orphan tables that start with '1'

        elif 'Pre-Draw Applicants' in tableHeader:
            #rawUnitDataObj[currentDrawCode].preDraw = table.data
            rawUnitDataObj[currentDrawCode]['preDraw'].append(table.data)
        
        # elif 'Total Choice 1' in tableHeader:
        #     rawUnitDataObj[currentDrawCode]['totalChoice1'].append(table.data)
    with open("./output/colorado/2021-co-elk-draw-stats.json", "w") as outfile:
        json.dump(rawUnitDataObj, outfile)

# assign them to obj

def formatPostDrawData(postDrawArr):
    rowIndex = 0
    returnArr = []
    for row in postDrawArr:
        if rowIndex == 0:
            if row[1].isnumeric and len(row[1]) > 0:
                returnArr.append(row)
        elif isRelevantData(row):
            returnArr.append(row)
            rowIndex += 1
    return returnArr

def formatPreDrawData(preDrawArr):
    rowIndex = 0

def formatTotalChoiceData(totalChoiceArr):
    rowIndex = 0

def isRelevantData(dataRow):
    print(dataRow)
    if isHeader(dataRow):
        return False
    if isEmpty(dataRow):
        return False
    return True
    

    # check if empty
    # check if header
def isHeader(dataRow):
    if 'Adult' in dataRow or "Res" in dataRow:
        return True
    return False

def isEmpty(dataRow):
    emptyRowNine =  ["","","","","","","","",""]
    emptyRowEight =  ["","","","","","","",""]
    emptyRowSeven =  ["","","","","","",""]
    emptyRowSix =  ["","","","","",""]
    if dataRow == emptyRowNine or dataRow == emptyRowEight or dataRow == emptyRowSeven or dataRow == emptyRowSix:
        return True
    return False

# def formatData():
    # data to omit
    # ['Post-Draw Successful', '', '', '', '', '', '', '']
    #  ['', '', 'Adult', '', 'Youth', '', 'Landowner (LPP)', '']
    #  ['Choice', 'Preference Points', 'Res', 'NonRes', 'Res', 'NonRes', 'Unrestricted', 'Restricted']
main(coloradoDataTables)