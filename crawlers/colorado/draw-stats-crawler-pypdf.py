import json
from crawlerMap import colorado
from pypdf import PdfReader
from advancedDrawStatsMappers import assignPostDrawStats

reader = PdfReader(colorado['elk']['drawStatsInput'])  
finalObj = {}
pageIndex = 0
prefPointIndex = 0
# currentPreferencePoint = 0

def main():
    for i in range(2, 15, 1):
        allDrawDataOnOnePage = False

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

            #     textIndex = textIndex + preDrawCounter
            # if 'Post-Draw' in text:
            #     beginPostDrawStats = True
            # if checkForExtraDrawStats:
                

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

def mainTryTwo():
    huntCode = ''
    currentCodeMap = {}
    unitExceededOnePage = False

    for i in range(2, 10, 1):
        page = reader.pages[i]
        pageText = page.extract_text()
        pageLines = pageText.splitlines()
        # print('NEW PAGE', i, pageLines[0])
        # find out what type of page it is, either continue with logic
        # or create new unit
        pageType = ['new unit', 'continue unit']
        currentPageType = pageLines[0]
        textIndex = 0
        if pageLines[0] == '# Drawn':
            unitExceededOnePage = False
        else:
            unitExceededOnePage = True

        # reset collection flows when we get to a new page
        enterPreDrawFlow = False
        enterPostDrawFlow = False
        enterTotalChoicePreFlow = False
        enterTotalChoicePostFlow = False
        beginStatCollection = False
        # print(pageLines)
        if unitExceededOnePage:
            # identify what part of the collection we are in
            # continue 1st draw choice or
            # total choice
            # tbh might be in the first line of text....
            beginStatCollection = True
            # will always be pre draw data first
            while beginStatCollection:
                enterPreDrawFlow = True

                while enterPreDrawFlow:
                    secondPageIndex = 0

                if 'Grand Total' in text:
                    beginStatCollection = False
                    enterPreDrawFlow = False
                print(text)
                # continue adding stats to previous unit
            
        else:
            for text in pageLines:
                if 'Hunt Code' in text:
                    huntCode = pageLines[textIndex + 3]
                    currentCodeMap[huntCode] = {}
                
                if 'Pre-Draw Applicants' in text:
                    preDrawIndex = 0
                    enterPreDrawFlow = True
                    while enterPreDrawFlow:
                        currentText = pageLines[textIndex + preDrawIndex]
                        
                        if beginStatCollection:
                            # break out of pre draw flow
                            if 'Post-Draw' in currentText or 'Total Choice' in currentText:
                                enterPreDrawFlow = False
                                beginStatCollection = False
                            else:
                                prefPt = currentText
                                resApps = 0 if pageLines[textIndex + preDrawIndex + 1] == '-' else int(pageLines[textIndex + preDrawIndex + 1])
                                nonResApps = 0 if pageLines[textIndex + preDrawIndex + 2] == '-' else int(pageLines[textIndex + preDrawIndex + 2])
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
                                currentCodeMap[huntCode][prefPt] = newObj
                                preDrawIndex+=6
                        
                        if '1' in currentText and not beginStatCollection:
                            beginStatCollection = True
        
                        preDrawIndex+=1
                    
                    # textIndex += preDrawIndex
                
                if 'Post-Draw Successful' in text:
                    enterPostDrawFlow = True
                    postDrawIndex = 0
                    drawStatsArr = []

                    while enterPostDrawFlow:
                        currentText = pageLines[textIndex + postDrawIndex]
                        if beginStatCollection:
                            if 'Colorado Parks' in currentText or 'Post-Draw' in currentText:
                                currentCodeMap[huntCode] = assignPostDrawStats(currentCodeMap[huntCode], drawStatsArr)
                                print('IT FINISHED')
                                enterPostDrawFlow = False
                                beginStatCollection = False
                            else:
                                drawStatsArr.append(currentText)
                            
                        if '1' in currentText and not beginStatCollection:
                            beginStatCollection = True
                        
                        postDrawIndex+=1

                textIndex +=1

            # print(text)
                
                # while enterPostDrawFlow:
                #     return
                #     if text == '1' and not beginStatCollection:
                #         beginStatCollection = True
                #     # elif 'Pre-Draw' in text:
                #     elif 'Total Choice' in text:
                #         enterTotalChoicePostFlow = True
                #         enterPostDrawFlow = False
                #         beginStatCollection = False
                #     else:
                #         # assing draw stats to parent obj
                #         print(text)
                #         currentPreDrawIndex+=6

                #     currentPreDrawIndex+=1

                # while enterTotalChoicePreFlow:
                    # return
                    # if 'Total Choice' in text and not beginStatCollection:
                    #     beginStatCollection = True
                    # what would cause this shit to break?
                    # else:
                    #     print(text)
                    #     currentPreDrawIndex+=6

                # while enterTotalChoicePostFlow:
                #     return
                #     if 'Total Choice' in text and not beginStatCollection:
                #         beginStatCollection = True
                    # what would cause this shit to break?
                    # else:
                    #     print(text)
                    #     currentPreDrawIndex+=6

            
            
        # reset flags

mainTryTwo()