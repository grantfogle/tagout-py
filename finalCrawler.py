import camelot
import json
from elkCodes import elkCodes

allTables = camelot.read_pdf("../../../../2021ElkDrawRecap-1.pdf", pages="all")

allElkData = {}
currentHuntIndex = 0
applicantData = ''
successData = ''

pattern = 'E[A-Z]\d\d\d[A-Z]\d[A-Z]'

def getUnitStats(applicantTable, successTable):
    cleanApplicantTable = cleanTable(applicantTable)
    cleanSuccessTable = cleanTable(successTable)

    finalStatsObj = combineUnitStats(cleanApplicantTable, cleanSuccessTable)
    print(finalStatsObj)
    return finalStatsObj

def cleanTable(dirtyTable):
    cleanTableArr = list()

    for dataRow in dirtyTable:
        if checkDataRelevant(dataRow):
            cleanTableArr.append(dataRow)
    return cleanTableArr

def checkDataRelevant(dataRow):
    emptyRow = ['', '', '', '', '', '', '', '']
    if 'Pre-Draw Applicants\nChoice' in dataRow or 'Adult' in dataRow or 'Preference Points' in dataRow:
        return False
    elif 'Total Choice 1' in dataRow or 'Total Choice 2' in dataRow or 'Total Choice 3' in dataRow or 'Total Choice 4' in dataRow or 'Grand Total' in dataRow:
        return False
    elif 'Pre-Draw Applicants\nChoice\nPreference Points\n1' in dataRow or 'Res \n-' in dataRow:
        return False
    elif 'Post-Draw Successful' in dataRow  or dataRow == emptyRow or 'Post-Draw Successful\nChoice\nPreference Points\n1' in dataRow:
        return False
    else:
        return True

def combineUnitStats(applicantData, successData):
    combinedData = {}
    lastApplicantPrefPoint = 0
    applicantIndex = 0
    lastSuccessPrefPoint = 0
    successIndex = 0
    # iterate through list of applicant datas
    for row in applicantData:
        for i in range(len(row)):
            if applicantIndex == 0:
                if row[i] and row[i].isnumeric():
                    obj = {
                        'resident': {
                            'applicants': row[i+2],
                            'success': 0
                        },
                        'nonResident': {
                            'applicants': row[i+3],
                            'success': 0
                        }
                    }
                    combinedData[row[i+1]] = obj    
                    break
        
            if row[i] and row[i].isnumeric():
                obj = obj = {
                    'resident': {
                        'applicants': row[i+1],
                        'success': 0
                    },
                    'nonResident': {
                        'applicants': row[i+2],
                        'success': 0
                    }
                }
                combinedData[row[i+1]] = obj
                break
        #if 0 index, check if there is a one
        # if last index, check if it is a total row
        # ie get last value and if it's greater then omit data
        # assign applicant and success data, default to 0 success data
    # for row in successData:
        # first index check if one
        # check last index
        # print(row)
    # then go through successData
    return combinedData


for table in allTables:
    currentCode = elkCodes[currentHuntIndex]
    tableHeader = table.data[0][0]
    tableData = table.data

    if 'Pre-Draw Applicants' in tableHeader:
        # print('Pre Draw Table', tableData)
        applicantData = tableData

        # logic for setting data
        
        print(currentCode)
        elkDataObj = getUnitStats(applicantData, successData)
        allElkData[currentCode] = elkDataObj
        currentHuntIndex += 1
        applicantData = ''
        successData = ''

        # print(tableData)
    elif 'Post-Draw Successful' in tableHeader:
        # print(tableData)
        # print('Post Draw Table', tableData)
        # print(currentCode)
        successData = tableData
        # get applicant data
        # get success data
        # pass them to the above 
        #if tableInclude
# design for resuability for different species

# go through each page
# look for elk code
# if there is an elk code
# go through the steps of recording the data from the page
# if there is no elk code
# go on
# extractDataFromTables()
print('ALL ELK DATA: ', allElkData)
with open("elk-final-stats.json", "w") as outfile:
    json.dump(allElkData, outfile)