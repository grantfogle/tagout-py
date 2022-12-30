import camelot
import json
from crawlerMap import coloradoMap
from output.colorado.elkCodes import elkCodes

coloradoDataTables = camelot.read_pdf(coloradoMap['drawStatsInput'], pages="801-960")

def main(coDataTables):
    
    formattedDataRows = getFormattedDataRows(coDataTables)
    outputDataObj = getOutputDataObj(formattedDataRows)
        
    with open("./output/colorado/2021-co-elk-draw-stats.json", "w") as outfile:
        json.dump(outputDataObj, outfile)

def getFormattedDataRows(dataTables):
    # unitIndex = 1
    # unitIndex = 38
    # # unitIndex = 83
    # unitIndex = 166
    # unitIndex = 257
    unitIndex = 743
    rawUnitDataObj = {}
    currentDrawCode = ''

    for table in dataTables:
        tableHeader = table.data[0][0]
        tableData = table.data

        if 'Post-Draw Successful' in tableHeader:
            currentDrawCode = elkCodes[unitIndex-1]
            unitIndex += 1
            formattedPostDrawArr = formatDrawDataArr(tableData)

            rawUnitDataObj[currentDrawCode] = {
                'preDraw': [],
                'postDraw': []
            }
            rawUnitDataObj[currentDrawCode]['postDraw'].append(formattedPostDrawArr)
                
        elif 'Pre-Draw Applicants' in tableHeader:
            #rawUnitDataObj[currentDrawCode].preDraw = table.data
            formattedPostDrawArr = formatDrawDataArr(tableData)
            rawUnitDataObj[currentDrawCode]['preDraw'].append(formattedPostDrawArr)

    print(unitIndex)
    return rawUnitDataObj
    

# assign them to obj

def formatDrawDataArr(postDrawArr):
    rowIndex = 0
    returnArr = []
    for row in postDrawArr:
        if hasDrawData(row):
            returnArr.append(row)
            rowIndex += 1

    return returnArr

def hasDrawData(dataRow):
    if isHeader(dataRow):
        return False
    elif isEmpty(dataRow):
        return False
    else:
        return True
    
def isHeader(dataRow):
    if 'Adult' in dataRow or "Res" in dataRow or "Res \n-" in dataRow or 'Choice\nPreference Points' in dataRow:
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
    finalDrawData = {}
    for unit in formattedDataArr:
        print(unit)
        finalDrawData[unit] = combinedDrawData(formattedDataArr[unit]['preDraw'], formattedDataArr[unit]['postDraw'])
    return finalDrawData

def totalChoiceRow(dataRow):
    if 'Total Choice 2' in dataRow or 'Total Choice 3' in dataRow or 'Total Choice 4' in dataRow:
        return True
    return False

def drawDataRow(dataRow):
    if ('Grand Total' in dataRow):
        return False
    if ('Total Choice 1' in dataRow):
        return False
    if (dataRow[1].isnumeric or dataRow[2].isnumeric()):
        return True
    return False

def combinedDrawData(preDrawStats, postDrawStats):
    combinedDrawObj = {}
    statsRowIndex = 0

    for stats in preDrawStats:
        for data in stats:
                tempObj = {
                    'res': {
                        'apps': 0,
                        'success': 0
                    },
                    'nonRes': {
                        'apps': 0,
                        'success': 0
                    }
                }
                statsRowIndex += 1
                resApps = 0
                nonResApps = 0
                dataLength = len(data)
                totalChoiceBool = totalChoiceRow(data)
                drawDataBool = drawDataRow(data)
                
                if (totalChoiceBool):
                    tempObj['res']['apps'] = int(data[3]) if data[3] != '-' else 0
                    tempObj['nonRes']['apps'] = int(data[4]) if data[4] != '-' else 0
                    combinedDrawObj[data[1]] = tempObj
                if (drawDataBool and not totalChoiceBool):
                    preferencePoint = data[1].replace('1\n', '') if dataLength == 8 else data[2].replace('1\n', '')
                    if dataLength == 8 and preferencePoint != '' and int(preferencePoint) >= 0:
                        resApps = data[2].replace('\n', '')
                        resApps = resApps.replace('-', '')
                        nonResApps = data[3].replace('\n', '')
                        nonResApps = nonResApps.replace('-', '')
    
                        tempObj['res']['apps'] = int(resApps) if resApps != '' else 0
                        tempObj['nonRes']['apps'] = int(nonResApps) if nonResApps != '' else 0
                        combinedDrawObj[preferencePoint] = tempObj
                    if dataLength == 9 and preferencePoint != '' and int(preferencePoint) >= 0:
                        resApps = data[3].replace('\n', '')
                        resApps = resApps.replace('-', '')
                        nonResApps = data[4].replace('\n', '')
                        nonResApps = nonResApps.replace('-', '')
    
                        tempObj['res']['apps'] = int(resApps) if resApps != '' else 0
                        tempObj['nonRes']['apps'] = int(nonResApps) if nonResApps != '' else 0
                        combinedDrawObj[data[2]] = tempObj


    for stats in postDrawStats:
        for data in stats:
                statsRowIndex += 1
                resApps = 0
                nonResApps = 0
                dataLength = len(data)
                totalChoiceBool = totalChoiceRow(data)
                drawDataBool = drawDataRow(data)
                if (totalChoiceBool):
                    totalChoiceStr = ''
                    if ('Total Choice' in data[0]):
                        totalChoiceStr = data[0]
                    elif ('Total Choice' in data[1]):
                        totalChoiceStr = data[1]
                    combinedDrawObj[totalChoiceStr]['res']['success'] = int(data[3]) if data[3] != '-' else 0
                    combinedDrawObj[totalChoiceStr]['nonRes']['success'] = int(data[4]) if data[4] != '-' else 0
                if (drawDataBool and not totalChoiceBool):
                    if dataLength == 8 and data[1] != '' and int(data[1]) >= 0:
                        resApps = data[2].replace('\n', '')
                        resApps = resApps.replace('-', '')
                        nonResApps = data[3].replace('\n', '')
                        nonResApps = nonResApps.replace('-', '')
    
                        combinedDrawObj[data[1]]['res']['success'] = int(resApps) if resApps != '' else 0
                        combinedDrawObj[data[1]]['nonRes']['success'] = int(nonResApps) if nonResApps != '' else 0

                    elif dataLength == 9 and data[2] != '' and int(data[2]) >= 0:
                        resApps = data[3].replace('\n', '')
                        resApps = resApps.replace('-', '')
                        nonResApps = data[4].replace('\n', '')
                        nonResApps = nonResApps.replace('-', '')
    
                        combinedDrawObj[data[2]]['res']['success'] = int(resApps) if resApps != '' else 0
                        combinedDrawObj[data[2]]['nonRes']['success'] = int(nonResApps) if nonResApps != '' else 0

    return combinedDrawObj

main(coloradoDataTables)