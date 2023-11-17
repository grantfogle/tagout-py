from PyPDF2 import PdfReader
import re

input = '../../data/colorado/draw_reports/2023ElkDrawnOut.pdf'
output = '../../data/colorado/draw_reports/outputs/2023_elk_draw_stats.json'
pattern = r'E[EFM]\d{3}[A-Z]\d[A-Z]'

def isHuntCode(line):
    # regex match
    print(line)

def get_draw_odds(pdf_file):
    # read the pdf
    reader = PdfReader(pdf_file)
    endPageText = 'Hunts shaded gray'

    for i in range(0, 1):
        page = reader.pages[i]
        pageText = page.extract_text()
        pageLines = pageText.splitlines()
        index = 0
        found = False
        beginDataCollection = False

        while index < len(pageLines):
            if re.match(pattern, pageLines[index]):
                print('match', pageLines[index])
                beginDataCollection = True

                while beginDataCollection:
                    # iterate through the next x amount of lines
                    ## look for keywords, whether a unit is a preference unit or choice 2/3 or if it made it
                    ## to leftover draw
                    ## if it made it to preference point draw only, then everything else is 0% draw odds
                    ## if it made it to choice 2 then pref points is 100%
                    ## if it made it to choice 3 then pref points is 100% and choice 2 is 100%
                    ## if it made it to leftover draw, then all previous choices have 100% draw odds

                    ## we will return objects in the following data format
                    # { state: , unit: , season: , huntCode: , prefPoints: , choice2: , choice3: , leftover: }
                    beginDataCollection = False
            else:
                index += 1
            if endPageText in pageLines[index]:
                print('found')
                found = True
                break
            # print(pageLines[index])



get_draw_odds(input)