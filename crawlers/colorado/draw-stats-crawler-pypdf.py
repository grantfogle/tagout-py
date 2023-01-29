import json
from crawlerMap import colorado
from pypdf import PdfReader

reader = PdfReader(colorado['elk']['drawStatsInput'])  
finalObj = {}  

def main():
    for i in range(3, 5, 1):
        page = reader.pages[i]
        pageText = page.extract_text()
        print('new page =====================: ', pageText)
        # pageLines = pageText.splitlines()
        # for line in pageLines:
        #     print(line)

    # with open("../../outputs/colorado/co-elk-harvest-stats2.json", "w") as outfile:
    #     json.dump(finalObj, outfile)


main()