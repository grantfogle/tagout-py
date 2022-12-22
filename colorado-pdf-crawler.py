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
    return formattedDataArr

def combinedDrawData(preDrawStats, postDrawStats):
    combinedDrawObj = {}
    # example data {
    # 28: {
        # res:
        #     applicants:
        #     success:
        # nonRes:
        #     applicants:
        #     success:
    #totalChoice1
    #totalChoice2
    #totalChoice3
    statsRowIndex = 0
    # passedFirstChoice = False

    for stats in preDrawStats:
        for data in stats:
            # type of row
                # preference point row
                # total choice row
                # grand total row
                # check if bad data row, ie \
            # check first row 
            # check last row, if it is a total
            dataRowIndex = 0
            preferencePoint = 0
            statsRowIndex += 1
            resApplicants = 0
            nonResApplicants = 0
            # all the data is in the first four or five items, 
            # let's get the reference index
            # find first data index
            # case 1st index

            # CHECK LENGTH OF DATA ROW
            # If LENGTH 8
            if (data.length == 8):
                preferencePoint = int(data[1])
                resApplicants = int(data[2])
                nonResApplicants = int(data[3])
            # If LENGTH 9
            elif (data.length == 9):
                preferencePoint = int(data[2])
                resApplicants = int(data[3])
                nonResApplicants = int(data[4])
            

            # If length 10



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