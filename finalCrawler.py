import camelot
import json
from elkCodes import elkCodes

allTables = camelot.read_pdf("../../../../2021ElkDrawRecap-1.pdf", pages="all")

allElkData = []
currentHuntIndex = 0

pattern = 'E[A-Z]\d\d\d[A-Z]\d[A-Z]'


def getUnitStats():
    print('asdf')
# for i in range(len(elkCodes)):
# for i in range(10):
def extractDataFromTables():
    for table in allTables:
        currentCode = elkCodes[currentHuntIndex]
        print(currentCode)

        # get applicant data
        # get success data
        # pass them to the above 
        #if tableIncludes
        finalHuntObj = {
            [currentCode]: getUnitStats(applicantData, successData)
        }
        allElkData.append(finalHuntObj)
# design for resuability for different species

# go through each page
# look for elk code
# if there is an elk code
# go through the steps of recording the data from the page
# if there is no elk code
# go on
extractDataFromTables()