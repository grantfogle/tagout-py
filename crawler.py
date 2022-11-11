import camelot
import tkinter
print('cats')
allTables = camelot.read_pdf("../../../../2021ElkDrawRecap-1.pdf", pages="all")

def breakoutApplicantData(tableData):
    totalCountArr = list()
    index = 0
    lastPreferencePoint = 0
    finalDict = {}
    for row in tableData:
        if checkIfNotRelevantData(row):
            totalCountArr.append(row)

    for row in totalCountArr:
        # integer that gets preference point
        preferencePoint = len(tableData)
        # we are going to get the first
        # print(totalCountArr)
        print(index)
        for i in range(len(row)):
            if index == 0:
                # check if last number is greater than last index
                if row[i] and row[i].isnumeric():
                    obj = { 'applicants': { 'resident': row[i+2], 'nonResident': row[i+3]}}
                    finalDict[row[i+1]] = obj    
                    break
            # if preferencePoint > 5 and row[i] == 1 and row[i+1] :
                # we will assume that if the first integer is == 1
                # then it is most likely ahead of another type of int
            if row[i] and row[i].isnumeric():
                if i == 0:
                    obj = { 'applicants': { 'resident': row[i+2], 'nonResident': row[i+3]}}
                    finalDict[row[i+1]] = obj
                    # previousNumber = row[i+1]
                    break
                else:
                    # if previousNumber > row[i]:
                    #     break
                        obj = { 'applicants': { 'resident': row[i+1], 'nonResident': row[i+2]}}
                        finalDict[row[i]] = obj
                        # previousNumber = row[i]
                        break
        index += 1

    print('finalDict', finalDict)

def breakoutSuccessData():
    print('breakout success data')
    totalCountArr = list()
    index = 0
    lastPreferencePoint = 0
    finalDict = {}
    for row in tableData:
        if checkIfNotRelevantData(row):
            totalCountArr.append(row)

    for row in totalCountArr:
        # integer that gets preference point
        preferencePoint = len(tableData)
        # we are going to get the first
        # print(totalCountArr)
        print(index)
        for i in range(len(row)):
            if index == 0:
                # check if last number is greater than last index
                if row[i] and row[i].isnumeric():
                    obj = { 'success': { 'resident': row[i+2], 'nonResident': row[i+3]}}
                    finalDict[row[i+1]] = obj    
                    break
            # if preferencePoint > 5 and row[i] == 1 and row[i+1] :
                # we will assume that if the first integer is == 1
                # then it is most likely ahead of another type of int
            if row[i] and row[i].isnumeric():
                if i == 0:
                    obj = { 'applicants': { 'resident': row[i+2], 'nonResident': row[i+3]}}
                    finalDict[row[i+1]] = obj
                    # previousNumber = row[i+1]
                    break
                else:
                    # if previousNumber > row[i]:
                    #     break
                        obj = { 'applicants': { 'resident': row[i+1], 'nonResident': row[i+2]}}
                        finalDict[row[i]] = obj
                        # previousNumber = row[i]
                        break
        index += 1

    print('finalDict', finalDict)


# get tables with pre draw applicants
def checkIfNotRelevantData(dataRow):
    if 'Pre-Draw Applicants\nChoice' in dataRow or 'Adult' in dataRow or 'Preference Points' in dataRow:
        return False
    elif 'Total Choice 1' in dataRow or 'Total Choice 2' in dataRow or 'Total Choice 3' in dataRow or 'Total Choice 4' in dataRow or 'Grand Total' in dataRow:
        return False
    elif 'Pre-Draw Applicants\nChoice\nPreference Points\n1' in dataRow or 'Res \n-' in dataRow:
        return False
    else:
        return True


for table in allTables:
    sameUnit = True
    # print(table.data)
    if 'Pre-Draw Applicants' in table.data[0][0]:
        #get data
        breakoutApplicantData(table.data)
        # for row in table.data:
        #     print(row)
        sameUnit = True
    elif 'Post-Draw Successful' in table.data[0][0]:
        # print(table.df)
        breakoutSuccessData(table.data)
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
