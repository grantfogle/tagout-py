import json
from pypdf import PdfReader

drawStatsObj = {}

# read the pdf
# get data
# save it into a global obj
# return that object
# repeat
textArr = []


# get draw type

def extractDrawStats():
    reader = PdfReader(
        '/Users/grantfogle/Desktop/workspace/startups/tagout/tagout-py/inputs/wyoming/elk/draw_stats/random/2022-NR-Elk-Random-Draw-Report.pdf')
    print(reader)

    for i in range(0, 1):
        page = reader.pages[i]
        pageText = page.extract_text()
        pageLines = pageText.splitlines()
        for line in pageLines:
            formattedLine = line.split('  ')
            for char in formattedLine:

                if char != '':
                    textArr.append(char)

    # for
    print(textArr)
    # look for description
    # look for
    # if line:
    #     print(line)
    # else:
    #     print('empty cell')
    # for line in pageLines:
    #     print()


def getWyomingDrawStats(resInput, nonResInput):
    return drawStatsObj


extractDrawStats()
