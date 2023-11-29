from PyPDF2 import PdfReader
import re

input = '../../data/colorado/draw_reports/2023ElkDrawnOut.pdf'
output = '../../data/colorado/draw_reports/outputs/2023_elk_draw_stats.json'
pattern = r'E[EFM]\d{3}[A-Z]\d[A-Z]'
endPageText = 'Hunts shaded gray'
firstPage = 0
lastPage = 1


def isHuntCode(line):
    # regex match
    return re.match(pattern, line)

def isEndOfPage(line):
    return re.match(endPageText, line)

def get_draw_odds(pdf_file):
    # read the pdf
    reader = PdfReader(pdf_file)

    for i in range(firstPage, lastPage):
        page = reader.pages[i]
        pageText = page.extract_text()
        pageLines = pageText.splitlines()
        index = 0
        endOfPage = False

        while index < len(pageLines) and endOfPage == False:
            currentLine = pageLines[index]
            collectDrawStats = False
            count = 2

            if isHuntCode(currentLine):
                huntCode = currentLine
                listType = pageLines[index + 1]
                collectDrawStats = True
                residentUnitData = {
                    'state': 'CO',
                    'species': huntCode[0],
                    'gender': huntCode[1],
                    'unit': huntCode[2:5],
                    'season': huntCode[5:7],
                    'method': huntCode[7],
                    'list_type': listType,
                    'resident_status': 'resident',
                    'draw_odds': {
                        'firstChoice': [],
                        'secondChoice': [],
                        'thirdChoice': [],
                    }
                }
                nonResidentUnitData = {
                    'state': 'CO',
                    'species': huntCode[0],
                    'gender': huntCode[1],
                    'unit': huntCode[2:5],
                    'season': huntCode[5:7],
                    'method': huntCode[7],
                    'list_type': listType,
                    'resident_status': 'non_resident',
                    'draw_odds': {
                        'firstChoice': [],
                        'secondChoice': [],
                        'thirdChoice': [],
                    }
                }
                while collectDrawStats:
                    print('count:', count)
                    # keeps track of current index in selected hunt code

                    tableData = pageLines[index + count]

                    if isHuntCode(tableData) or isEndOfPage(tableData):
                        collectDrawStats = False
                        index += count
                        count = 2
                        found = True
                    
                    print(tableData)

                    count += 1
                    ## if it made it to preference point draw only, then everything else is 0% draw odds
                    ## if it made it to choice 2 then pref points is 100%
                    ## if it made it to choice 3 then pref points is 100% and choice 2 is 100%
                    ## if it made it to leftover draw, then all previous choices have 100% draw odds

                    ## we will return objects in the following data format
                    # { state: , unit: , season: , huntCode: , prefPoints: , choice2: , choice3: , leftover: }
                    # if re.match(pattern, pageLines[index]):
                    #     beginDataCollection = False
                    #     index += count
                index += 1
            else:
                index += 1



get_draw_odds(input)