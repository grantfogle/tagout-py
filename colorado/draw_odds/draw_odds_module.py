from PyPDF2 import PdfReader

input = '../../data/colorado/draw_reports/2023ElkDrawnOut.pdf'
output = '../../data/colorado/draw_reports/outputs/2023_elk_draw_stats.json'

def get_draw_odds(pdf_file):
    # read the pdf
    reader = PdfReader(pdf_file)

    for i in range(0, 1):
        page = reader.pages[i]
        pageText = page.extract_text()
        pageLines = pageText.splitlines()
        for line in pageLines:
            print(line)
        

    print('get_draw_odds')



get_draw_odds(input)