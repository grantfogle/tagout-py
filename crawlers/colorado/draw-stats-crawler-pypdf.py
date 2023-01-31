import json
from crawlerMap import colorado
from pypdf import PdfReader

reader = PdfReader(colorado['elk']['drawStatsInput'])  
finalObj = {}
pageIndex = 0
prefPointIndex = 0
# currentPreferencePoint = 0

def main():
    for i in range(2, 4, 1):
        textIndex = 0
        unitCode = ''
        currentCodeMap = {}
        checkForExtraDrawStats = False
        newPage = False
        currentPreferencePoint = 0
        currentObj = {
            'resident': {
                'apps': 0,
                'success': 0
            },
            'nonRes': {
                'apps': 0,
                'success': 0
            }
        }
        beginPreDrawStats = False
        beginPostDrawStats = False
        finishedDrawStatsPage = False
        totalPreDrawApplicantsHit = False
        totalPostDrawSuccess = False

        page = reader.pages[i]
        pageText = page.extract_text()
        pageLines = pageText.splitlines()
        print('PAGELINES ===== ', pageLines)
        # print (pageText)
        for text in pageLines:
            if 'Hunt Code' in text:
                unitCode = pageLines[textIndex+3]
                print(unitCode)

            if 'Pre-Draw Applicants' in text and not finishedDrawStatsPage:
                beginPreDrawStats = True
                beginStatCollection = False
                preDrawCounter = 0

                while beginPreDrawStats:
                    currentText = pageLines[textIndex + preDrawCounter]
                    preferencePoint = 0
                    
                    if beginStatCollection:
                        if 'Post-Draw' in currentText:
                            beginPreDrawStats = False
                            beginPostDrawStats = True
                            beginStatCollection = False
                            if int(preferencePoint) > 0:
                                checkForExtraDrawStats = True
                        else:
                            preferencePoint = currentText
                            resApps = 0 if pageLines[textIndex + preDrawCounter + 1] == '-' else int(pageLines[textIndex + preDrawCounter + 1])
                            nonResApps = 0 if pageLines[textIndex + preDrawCounter + 2] == '-' else int(pageLines[textIndex + preDrawCounter + 2])
                            newObj = {
                                'res': {
                                    'applicants': resApps,
                                    'success': 0
                                },
                                'nonRes': {
                                    'applicants': nonResApps,
                                    'success': 0
                                },
                            } 
                            currentCodeMap[preferencePoint] = newObj
                            preDrawCounter+=6

                    if '1' in currentText and not beginStatCollection:
                        print('begin Pre draw stat collection')
                        beginStatCollection = True

                    preDrawCounter += 1


                while beginPostDrawStats:
                    currentText = pageLines[textIndex + preDrawCounter]
                    if beginStatCollection:
                        if 'Colorado Parks and Wildlife' in currentText or 'Post-Draw' in currentText:
                            beginPostDrawStats = False
                            beginStatCollection = False
                        else:
                            preferencePoint = currentText
                            resApps = 0 if pageLines[textIndex + preDrawCounter + 1] == '-' else int(pageLines[textIndex + preDrawCounter + 1])
                            nonResApps = 0 if pageLines[textIndex + preDrawCounter + 2] == '-' else int(pageLines[textIndex + preDrawCounter + 2])
                            currentCodeMap[preferencePoint]['res']['success'] = resApps
                            currentCodeMap[preferencePoint]['nonRes']['success'] = nonResApps
                            preDrawCounter+=6
                        
                    if '1' in currentText and not beginStatCollection:
                        print('begin Pre draw stat collection')
                        beginStatCollection = True

                    preDrawCounter += 1

                textIndex = textIndex + preDrawCounter
            # if 'Post-Draw' in text:
            #     beginPostDrawStats = True
            if checkForExtraDrawStats:
                

            # textIndex += 1

        # for line in pageLines:
        #     print(line)

    # with open("../../outputs/colorado/co-elk-harvest-stats2.json", "w") as outfile:
    #     json.dump(finalObj, outfile)

# pre-draw applicants (first)

## average length of draw stats is 7
## first item is preference point
## will need a preference point counter


# post-draw successful (second)


# left over pre draw/post draw data - if data goes outside of page
# 2021 Primary ELK Post Draw Report 
# Landowner Leftover Choice 
## Always has just two results
# Total Choice 1
# if (text == 'Total Choice 1'):
#     beginTotalChoice
# Total Choice 2
# Total Choice 3
# Total Choice 4



main()