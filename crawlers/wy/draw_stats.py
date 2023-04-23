import json
from pypdf import PdfReader

# testPdfFile = '/Users/grantfogle/Desktop/workspace/startups/tagout/tagout-py/inputs/wyoming/elk/draw_stats/random/2022-NR-Elk-Random-Draw-Report.pdf'
# read the pdf
# get data
# save it into a global obj
# return that object
# repeat
# PATTERNS TO KEEP AN EYE ON

# if there is a prolonged --------


# for new page, look for
# unit, hunt type, description, quota, first choice, second choice, third choice
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------

# get draw type

# STEP ONE, get the primary code that will be used to call data
def getRandomDrawStats(input):
    # drawStatsObj = {}
    # print()
    # huntCode =
    returnObj = {}
    returnObj = extractDrawStats(input)
    print('RETURN OBJ:', returnObj)
    return returnObj


# we are going to begin the extraction of species data by parsing the PDF,
# def extractDrawStats(huntCode, pdfFile) we will use an input passed to get the data
def extractDrawStats(pdfFile):
    reader = PdfReader(pdfFile)
    drawStatsObj = {}
    # remove any unwanted characters
    textArr = []
    # get number of pages
    print(len(reader.pages))
    for i in range(0, len(reader.pages)):
        page = reader.pages[i]
        pageText = page.extract_text()
        pageLines = pageText.splitlines()
        for line in pageLines:
            formattedLine = line.split('  ')
            for char in formattedLine:

                if char != '':
                    textArr.append(char)

    # extract text from formatted array
    counter = 0
    textArrLen = len(textArr)
    while counter < textArrLen:
        if '----------------------------------' in textArr[counter]:
            # begin text extraction
            extractText = True
            textCounter = 0

            while extractText:
                totalCount = textCounter + counter
                area = ''
                type = ''
                statsObj = {
                    'description': '',
                    'quota': '',
                    'firstChoice': '',
                    'secondChoice': '',
                    'thirdChoice': ''
                }

                if textCounter == 0:
                    # extract data from the first area
                    # then increment counter
                    area = textArr[totalCount][-3:]
                    type = textArr[totalCount+1]
                    # firstAreaKey = area + '_' + type
                    firstAreaKey = area
                    statsObj['description'] = getDescription(
                        textArr[totalCount+2])
                    statsObj['quota'] = textArr[totalCount+3]
                    statsObj['firstChoice'] = textArr[totalCount+4]
                    statsObj['secondChoice'] = textArr[totalCount+5]
                    statsObj['thirdChoice'] = textArr[totalCount+6]
                    if firstAreaKey in drawStatsObj:
                        drawStatsObj[firstAreaKey][type] = statsObj
                    else:
                        drawStatsObj[firstAreaKey] = {}
                        drawStatsObj[firstAreaKey][type] = statsObj
                    textCounter += 7
                elif textArrLen <= totalCount or 'Demand Report' in textArr[counter+textCounter]:
                    counter += textCounter
                    extractText = False
                elif 'GEN' in textArr[totalCount]:
                    areaKey = 'GENERAL'
                    statsObj['description'] = 'GENERAL'
                    statsObj['quota'] = textArr[totalCount+2]
                    statsObj['firstChoice'] = textArr[totalCount+3]
                    statsObj['secondChoice'] = textArr[totalCount+4]
                    statsObj['thirdChoice'] = textArr[totalCount+5]
                    drawStatsObj[areaKey] = statsObj
                    print(textArr[totalCount])
                    textCounter += 6
                else:
                    area = textArr[totalCount]
                    type = textArr[totalCount+1]
                    areaKey = area
                    statsObj['description'] = getDescription(
                        textArr[totalCount+2])
                    statsObj['quota'] = textArr[totalCount+3]
                    statsObj['firstChoice'] = textArr[totalCount+4]
                    statsObj['secondChoice'] = textArr[totalCount+5]
                    print(area, type, statsObj)
                    statsObj['thirdChoice'] = textArr[totalCount+6]

                    if areaKey in drawStatsObj:
                        drawStatsObj[areaKey][type] = statsObj
                    else:
                        drawStatsObj[areaKey] = {}
                        drawStatsObj[areaKey][type] = statsObj
                    drawStatsObj[areaKey][type] = statsObj
                    textCounter += 7

        counter += 1

    return drawStatsObj


def getDescription(desc):
    if 'ARCHERY' in desc:
        return 'ARCHERY'
    return desc.replace(" ", "_")


def getDrawStats(input, species, residency, drawType):
    if drawType == 'random':
        print(input, species, residency, drawType)
        return getRandomDrawStats(input)
    # return drawStatsObj


# getRandomDrawStats('E', 'NR', 'Random')
# extract preference draw stats
# extract other draw stats
