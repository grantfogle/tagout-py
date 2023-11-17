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
                    # iterate through
                    beginDataCollection = False
            else:
                index += 1
            if endPageText in pageLines[index]:
                print('found')
                found = True
                break
            # print(pageLines[index])



get_draw_odds(input)