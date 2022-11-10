import camelot
import tkinter
print('cats')
allTables = camelot.read_pdf("../../../../2021ElkDrawRecap-1.pdf", pages="1,2,3")

def breakoutPreferencePointsObj(tableData):
    print('table data', tableData)
    finalDict = {}
    totalCountArr = list()

    for row in tableData:
        if checkIfNotRelevantData(row):
            totalCountArr.append(row)

    print('totalCountArr', totalCountArr)

    # for row in totalCountArr:
    #     rangeCounter = len(tableData)
    #     for i in range(len(row)):

    #         if row[i] and row[i].isnumeric() and (row[i] != 1 and i < 8):
    #             obj = { 'applicants': { 'resident': row[i+1], 'nonResident': row[i+2]}}
    #             finalDict[row[i]] = obj
    #             break
    # print('finalDict', finalDict)

# get tables with pre draw applicants
def checkIfNotRelevantData(dataRow):
    if 'Pre-Draw Applicants\nChoice' in dataRow or 'Adult' in dataRow or 'Preference Points' in dataRow:
        return False
    elif 'Total Choice 1' in dataRow or 'Total Choice 2' in dataRow or 'Total Choice 3' in dataRow or 'Total Choice 4' in dataRow or 'Grand Total' in dataRow:
        return False
    else:
        return True


for table in allTables:
    sameUnit = True
    # print(table.data)
    if 'Pre-Draw Applicants' in table.data[0][0]:
        #get data
        breakoutPreferencePointsObj(table.data)
        # for row in table.data:
        #     print(row)
        sameUnit = True
    elif 'Post-Draw Successful' in table.data[0][0]:
        # print(table.df)
        sameUnit = False
    else: 
        print('Not a relevant table')
        # drawTable = table
# get table with post draw applicants

#print(allTables[4].df)
# print(allTables[4].df)
# print(allTables[5].df)
# print(allTables[1].df)
# print(allTables[2].df)
