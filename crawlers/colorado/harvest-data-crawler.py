import json
from crawlerMap import colorado
from pypdf import PdfReader

def main():
    index = 0
    reader = PdfReader(colorado['elk']['harvestStatsInput'])
    page = reader.pages
    # pageText = page.extract_text()
    # pageLines = pageText.splitlines()
    finalDataObj = {}

    for page in reader:
        print(page)

    # with open(colorado['elk']['populationStatsOutput'], "w") as outfile:
    #     json.dump(finalDataObj, outfile)

main()