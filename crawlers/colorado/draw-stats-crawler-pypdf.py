import json
from crawlerMap import colorado
from pypdf import PdfReader
from advancedDrawStatsMappers import assignPostDrawStats, assignPreDrawStats

reader = PdfReader(colorado['elk']['drawStatsInput'])  
finalObj = {}
pageIndex = 0
prefPointIndex = 0
# currentPreferencePoint = 0
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

    for i in range(2, 4, 1):
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

        if unitExceededOnePage:
            beginStatCollection = True
            beginSecondPagePostDrawStatsFlow = False
            beginCounter = True
            statCounter = 0
            postDrawCounter = 0
            postDrawCounter = 0
            preDrawData = []
            postDrawData = []

            ## while -> instead of for loop
            if pageLines[0] == '1':
                statCounter+=1
                while statCounter < len(pageLines):
                    # identify what part of the collection we are in
                    # continue 1st draw choice or
                    # total choice
                    # tbh might be in the first line of text....
                    # will always be pre draw data first
                    # count how much data i need to collect
                    while beginCounter:
                        enterPreDrawFlow = False
                        currentText = pageLines[textIndex + statCounter]
                        if currentText == 'Landowner Leftover Choice 3':
                            beginCounter = False
                            beginSecondPagePostDrawStatsFlow = True
                            statCounter += 4
                            textIndex = statCounter + textIndex

                        preDrawData.append(currentText)
                        statCounter+=1
                
                    while beginSecondPagePostDrawStatsFlow and postDrawCounter < statCounter:
                        currentText = pageLines[textIndex + postDrawCounter]
                        if  'Colorado Parks and Wildlife' in currentText:
                            beginSecondPagePostDrawStatsFlow = False
                            currentCodeMap[huntCode] = assignPreDrawStats(currentCodeMap[huntCode], preDrawData)
                            currentCodeMap[huntCode] = assignPostDrawStats(currentCodeMap[huntCode], postDrawData)
                            print(currentCodeMap)
                        
                        postDrawCounter += 1
                        postDrawData.append(currentText)
                        statCounter += 1
                    
                    statCounter+=1
            statCounter+=1
                # while enterPreDrawFlow:
                #     secondPageIndex = 0

                # if 'Grand Total' in text:
                #     beginStatCollection = False
                #     enterPreDrawFlow = False
                # continue adding stats to previous unit

                # pre draw stats
                # post draw stats
                # total choice pre draw stats
                # total choice post draw stats
            
        else:
            for text in pageLines:
                if 'Hunt Code' in text:
                    huntCode = pageLines[textIndex + 3]
                    currentCodeMap[huntCode] = {}
                
                if 'Pre-Draw Applicants' in text:
                    enterPreDrawFlow = True
                    preDrawIndex = 0
                    drawStatsArr = []

                    while enterPreDrawFlow:
                        currentText = pageLines[textIndex + preDrawIndex]
                        
                        if beginStatCollection:
                            if 'Post-Draw' in currentText or 'Total Choice' in currentText:
                                currentCodeMap[huntCode] = assignPreDrawStats(currentCodeMap[huntCode], drawStatsArr)
                                enterPreDrawFlow = False
                                beginStatCollection = False
                            else:
                                drawStatsArr.append(currentText)
                        
                        if '1' in currentText and not beginStatCollection:
                            beginStatCollection = True
        
                        preDrawIndex+=1
                
                if 'Post-Draw Successful' in text:
                    enterPostDrawFlow = True
                    postDrawIndex = 0
                    drawStatsArr = []

                    while enterPostDrawFlow:
                        currentText = pageLines[textIndex + postDrawIndex]
                        if beginStatCollection:
                            if 'Colorado Parks' in currentText or 'Post-Draw' in currentText:
                                currentCodeMap[huntCode] = assignPostDrawStats(currentCodeMap[huntCode], drawStatsArr)
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

# count the amount of data i need to collect
# then get that for the second data

