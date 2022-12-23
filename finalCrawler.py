import camelot
import json
from elkCodes import elkCodes

allTables = camelot.read_pdf("../../../../2021ElkDrawRecap.pdf", pages='3-50')
# coElkDrawTablesPdf = camelot.read_pdf("../../../../2021ElkDrawRecap-1.pdf", pages="all")
species = ['elk', 'deer', 'bear', 'antelope', 'sheep', 'goat', 'moose']
states = ['co', 'ut', 'wy', 'id', 'nm', 'nv', 'mt']

allElkData = {}

pattern = 'E[A-Z]\d\d\d[A-Z]\d[A-Z]'

def fetchCoElkDrawStats(pdfTables):
    currentHuntIndex = 0
    applicantData = ''
    successData = ''

    for table in pdfTables:
        currentCode = elkCodes[currentHuntIndex]
        tableHeader = table.data[0][0]
        tableData = table.data

        if 'Pre-Draw Applicants' in tableHeader:
            print('APPLICANTS: ', currentCode)
            applicantData = tableData

            elkDataObj = getUnitStats(applicantData, successData)
            allElkData[currentCode] = elkDataObj
            currentHuntIndex += 1
            applicantData = ''
            successData = ''

        elif 'Post-Draw Successful' in tableHeader:
            print('SUCCESSES: ', currentCode)
            successData = tableData

    with open("./output/colorado/2021-co-elk-draw-stats.json", "w") as outfile:
        json.dump(allElkData, outfile)

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
    emptyRowSix = ['', '', '', '', '', '', '']
    if 'Pre-Draw Applicants\nChoice' in dataRow or 'Adult' in dataRow or 'Preference Points' in dataRow:
        return False
    elif 'Total Choice 1' in dataRow or 'Total Choice 2' in dataRow or 'Total Choice 3' in dataRow or 'Total Choice 4' in dataRow or 'Grand Total' in dataRow:
        return False
    elif 'Pre-Draw Applicants\nChoice\nPreference Points\n1' in dataRow or 'Res \n-' in dataRow:
        return False
    elif 'Post-Draw Successful' in dataRow  or dataRow == emptyRow or 'Post-Draw Successful\nChoice\nPreference Points\n1' in dataRow:
        return False
    elif 'Post-Draw Successful\nChoice\nPreference Points' in dataRow or 'Res' in dataRow or '-\n-\n-' in dataRow or dataRow == emptyRowSix:
        return False
    else:
        return True

def combineUnitStats(applicantData, successData):
    combinedData = {}
    lastApplicantPrefPoint = 0
    applicantIndex = 0
    lastSuccessPrefPoint = 0
    successIndex = 0

    for row in applicantData:
        for i in range(len(row)):
            if applicantIndex == 0:
                if row[i] and row[i].isnumeric() and int(row[i]) != 1 and row[i+1] and row[i+2]:
                    lastApplicantPrefPoint = int(row[i])
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
                if row[i] and row[i].isnumeric() and int(row[i]) < lastApplicantPrefPoint:
                    rowInt = int(row[i])
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
                if row[i] and row[i].isnumeric() and int(row[i]) < lastApplicantPrefPoint:
                    lastApplicantPrefPoint = int(row[i])
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
    
    for row in successData:
        for i in range(len(row)):
            # firstIndex
            if successIndex == 0:
                print(row)
                if row[i] and row[i].isnumeric() and row[i] in combinedData:
                    lastSuccessPrefPoint = int(row[i])
                    combinedData[row[i]]['resident']['success'] = row[i+1]
                    combinedData[row[i]]['nonResident']['success'] = row[i+2]
                    successIndex += 1
                    break
            # last index
            elif successIndex == (len(successData) - 1):
                if row[i] and row[i].isnumeric() and row[i] in combinedData and int(row[i]) < lastSuccessPrefPoint:
                    rowInt = int(row[i])
                    if rowInt < 10:
                        lastSuccessPrefPoint = int(row[i])
                        combinedData[row[i]]['resident']['success'] = row[i+1]
                        combinedData[row[i]]['nonResident']['success'] = row[i+2]
                        successIndex +=1 
                        break
            # other indexes
            else:
                if row[i] and row[i].isnumeric() and row[i] in combinedData and int(row[i]) < lastSuccessPrefPoint:
                    lastSuccessPrefPoint = int(row[i])
                    combinedData[row[i]]['resident']['success'] = row[i+1]
                    combinedData[row[i]]['nonResident']['success'] = row[i+2]
                    successIndex +=1 
                    break
    return combinedData

fetchCoElkDrawStats(allTables)