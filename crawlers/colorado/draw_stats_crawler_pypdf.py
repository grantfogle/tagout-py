import json
from crawler_map import colorado
from pypdf import PdfReader
from pre_post_draw_stats_breakdown import assignPostDrawStats, assignPreDrawStats

def main(input, startIndex, endIndex):
    huntCode = ''
    currentCodeMap = {}
    unitExceededOnePage = False
    # finalObj = {}
    # pageIndex = 0
    # prefPointIndex = 0
    reader = PdfReader(input) 


    for i in range(startIndex, endIndex, 1):
        print(huntCode)
        page = reader.pages[i]
        pageText = page.extract_text()
        pageLines = pageText.splitlines()
        pageType = ['new unit', 'continue unit']
        currentPageType = pageLines[0]
        textIndex = 0
        
        if pageLines[0] == '# Drawn':
            unitExceededOnePage = False
        else:
            unitExceededOnePage = True

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
            
            if 'Total Choice' in pageLines[0]:
                while statCounter < len(pageLines):
                    while beginCounter:
                        enterPreDrawFlow = False
                        currentText = pageLines[textIndex + statCounter]
                        if currentText == 'Landowner Leftover Choice 3':
                            beginCounter = False
                            beginSecondPagePostDrawStatsFlow = True
                            statCounter += 3
                            textIndex = statCounter + textIndex

                        preDrawData.append(currentText)
                        statCounter+=1
                
                    while beginSecondPagePostDrawStatsFlow and postDrawCounter < statCounter:
                        currentText = pageLines[textIndex + postDrawCounter]
                        if  'Colorado Parks and Wildlife' in currentText:
                            beginSecondPagePostDrawStatsFlow = False
                            currentCodeMap[huntCode] = assignPreDrawStats(currentCodeMap[huntCode], preDrawData)
                            currentCodeMap[huntCode] = assignPostDrawStats(currentCodeMap[huntCode], postDrawData)
                            statCounter = len(pageLines)
                        
                        postDrawCounter += 1
                        postDrawData.append(currentText)
                        statCounter += 1
                    
                    statCounter+=1


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
                            statCounter = len(pageLines)
                        
                        postDrawCounter += 1
                        postDrawData.append(currentText)
                        statCounter += 1
                    
                    statCounter+=1
            statCounter+=1

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
                            if 'Post-Draw' in currentText:
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
    
    return currentCodeMap


def getDrawStats(input, startIndex, endIndex):
    return main(input, startIndex, endIndex)


