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
            collect_stats_count = 2

            if isHuntCode(currentLine):
                huntCode = currentLine
                listType = pageLines[index + 1]
                collectDrawStats = True
                unitData = {
                    'state': 'CO',
                    'species': huntCode[0],
                    'gender': huntCode[1],
                    'unit': huntCode[2:5],
                    'season': huntCode[5:7],
                    'method': huntCode[7],
                    'list_type': listType,
                    'resident_status': 'resident',
                    'draw_odds': {
                        'resident': {
                            'first_choice': [],
                            'second_choice': [],
                            'third_choice': [],
                        },
                        'non_resident': {
                            'first_choice': [],
                            'second_choice': [],
                            'third_choice': [],
                        }
                    }
                }

                while collectDrawStats:
                    # keeps track of current index in selected hunt code
                    tableData = pageLines[index + collect_stats_count]
                    # determine if 
                    # if pref 
                    # if Choice 2
                    if 


                    if isHuntCode(tableData) or isEndOfPage(tableData):
                        collectDrawStats = False
                        index += collect_stats_count
                        # count = 2
                        found = True
                        break
                    
                    print(tableData)

                    collect_stats_count += 1
                print("======================")
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