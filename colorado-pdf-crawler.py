import camelot
import json
from crawlerMap import coloradoMap
from elkCodes import elkCodes

# get all the tables that you want to crawl
coloradoDataTables = camelot.read_pdf(coloradoMap['drawStatsInput'], pages="3-10")

# global flags for tracking edge cases

def main(coDataTables):
    
    formattedDataRows = getFormattedDataRows(coDataTables)
    outputDataObj = getOutputDataObj(formattedDataRows)
        
        # elif 'Total Choice 1' in tableHeader:
        #     rawUnitDataObj[currentDrawCode]['totalChoice1'].append(table.data)
    with open("./output/colorado/2021-co-elk-draw-stats.json", "w") as outfile:
        json.dump(outputDataObj, outfile)

# get formatted data rows
def getFormattedDataRows(dataTables):
    unitIndex = 1
    rawUnitDataObj = {}
    currentDrawCode = ''

    for table in dataTables:
        tableHeader = table.data[0][0]
        tableData = table.data

        if 'Post-Draw Successful' in tableHeader:
            # since haing a negative index with throw an error
            # i want to ensure that i am always using the correct index as
            # 'Post-Draw successful will always be the first table of the
            # data that i want to get
            currentDrawCode = elkCodes[unitIndex-1]
            unitIndex += 1
            formattedPostDrawArr = formatDrawDataArr(tableData)

            rawUnitDataObj[currentDrawCode] = {
                'preDraw': [],
                'postDraw': [],
                'totalChoice1': []
            }
            rawUnitDataObj[currentDrawCode]['postDraw'].append(formattedPostDrawArr)
                
        elif 'Pre-Draw Applicants' in tableHeader:
            #rawUnitDataObj[currentDrawCode].preDraw = table.data
            formattedPostDrawArr = formatDrawDataArr(tableData)
            rawUnitDataObj[currentDrawCode]['preDraw'].append(formattedPostDrawArr)

    return rawUnitDataObj
    

# assign them to obj

def formatDrawDataArr(postDrawArr):
    rowIndex = 0
    returnArr = []
    for row in postDrawArr:
        # if rowIndex == 0:
        #     if row[1].isnumeric and len(row[1]) > 0:
        #         returnArr.append(row)
        if hasDrawData(row):
            returnArr.append(row)
            rowIndex += 1

    return returnArr

def formatPreDrawData(preDrawArr):
    rowIndex = 0

def formatTotalChoiceData(totalChoiceArr):
    rowIndex = 0

def hasDrawData(dataRow):
    if isHeader(dataRow):
        return False
    elif isEmpty(dataRow):
        return False
    else:
        return True
    

    # check if empty
    # check if header
def isHeader(dataRow):
    if 'Adult' in dataRow or "Res" in dataRow or "Res \n-" in dataRow:
        return True
    elif 'Pre-Draw' in dataRow[0] or 'Post-Draw' in dataRow[0]:
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

def getOutputDataObj(formattedDataArr):
    return formattedDataArr

main(coloradoDataTables)