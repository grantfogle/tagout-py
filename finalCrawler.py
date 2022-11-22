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
    # print(finalStatsObj)
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
                if row[i] and row[i].isnumeric() and int(row[i]) != 1:
                    obj = {
                        'resident': {
                            'applicants': row[i+1],
                            'success': 0
                        },
                        'nonResident': {
                            'applicants': row[i+2],
                            'success': 0
                        }
                    }
                    combinedData[row[i]] = obj
                    applicantIndex +=1 
                    break
            elif applicantIndex == (len(applicantData)-1):
                if row[i] and row[i].isnumeric():
                    rowInt = int(row[i])
                    print('=====================', rowInt)
                    if rowInt < 10:
                        obj = {
                            'resident': {
                                'applicants': row[i+1],
                                'success': 0
                            },
                            'nonResident': {
                                'applicants': row[i+2],
                                'success': 0
                            }
                        }
                        combinedData[row[i]] = obj
                        applicantIndex +=1
                        break
            else:
                if row[i] and row[i].isnumeric():
                    obj = {
                        'resident': {
                            'applicants': row[i+1],
                            'success': 0
                        },
                        'nonResident': {
                            'applicants': row[i+2],
                            'success': 0
                        }
                    }
                    combinedData[row[i]] = obj
                    applicantIndex +=1
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
        applicantData = tableData

        elkDataObj = getUnitStats(applicantData, successData)
        allElkData[currentCode] = elkDataObj
        currentHuntIndex += 1
        applicantData = ''
        successData = ''

    elif 'Post-Draw Successful' in tableHeader:
        successData = tableData


with open("elk-final-stats.json", "w") as outfile:
    json.dump(allElkData, outfile)