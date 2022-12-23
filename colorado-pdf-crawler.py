import camelot
import json
from crawlerMap import coloradoMap
from elkCodes import elkCodes

# get all the tables that you want to crawl
coloradoDataTables = camelot.read_pdf(coloradoMap['drawStatsInput'], pages="3-20")

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
                'postDraw': []
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
    finalDrawData = {}
    for unit in formattedDataArr:
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
                    if dataLength == 8 and data[1] != '' and int(data[1]) >= 0:
                        resApps = data[2].replace('\n', '')
                        resApps = resApps.replace('-', '')
                        nonResApps = data[3].replace('\n', '')
                        nonResApps = nonResApps.replace('-', '')
    
                        tempObj['res']['apps'] = int(resApps) if resApps != '' else 0
                        tempObj['nonRes']['apps'] = int(nonResApps) if nonResApps != '' else 0
                        combinedDrawObj[data[1]] = tempObj
                    elif dataLength == 9 and data[2] != '' and int(data[2]) >= 0:
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
                    print('this is the problem right here: ', data)
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
                    # elif dataLength == 9:
                     # CHECK LENGTH OF DATA ROW
                    # If LENGTH 8
                    # if (data.length == 8):
                    #     preferencePoint = int(data[1])
                    #     resApplicants = int(data[2])
                    #     nonResApplicants = int(data[3])
                    # If LENGTH 9
                    # elif (data.length == 9):
                    #     preferencePoint = int(data[2])
                    #     resApplicants = int(data[3])
                    #     nonResApplicants = int(data[4])
                # preference point row
                # total choice row
                # grand total row
                # check if bad data row, ie \
            # check first row 
            # check last row, if it is a total
            # all the data is in the first four or five items, 
            # let's get the reference index
            # find first data index
            # case 1st index
            
            # If length 10
            # combinedDrawObj[preferencePoint] = {
            #     res:
            # }



            # if (data[0] != '' and data[0].isnumeric()):
            #     preferencePointIndex = 0
            #     preferencePoint = int(data[0])
            # elif (data[1] != '' and data[1].isnumeric()):
            #     preferencePointIndex = 1
            #     preferencePoint = int(data[1])
            # elif (data[2] != '' and data[2].isnumeric()):
            #     preferencePointIndex = 2
            #     preferencePoint = int(data[2])
            
            # if (preferencePoint == 1 and stats[statsRowIndex+1][dataRowIndex] != ''):

                # check next data row
            # if data === 1, let's check next row and same index
            # if data is greater than previous preference point
            # then it's probably not the correct index
            # case total choice 1 2 3 4
    # for stats in postDrawStats:
    
    #print('post draw stats', postDrawStats)




main(coloradoDataTables)