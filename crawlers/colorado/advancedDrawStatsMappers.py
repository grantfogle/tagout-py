
# statsObj is the currentCodeMap

def assignPreDrawStats(huntCode, preferencePoint, data):
    cleanStatsObj = {}

    


    return cleanStatsObj
    # check if first choice or total choice

# statsObj is the currentCodeMap[huntCode]
def assignPostDrawStats(statsObj, dataArr):
    dataArrLen = len(dataArr) - 1
    counter = 0
    while counter < dataArrLen:
        prefPt = dataArr[counter]
        print(prefPt)
        resSuccess = dataArr[counter + 1]
        nonResSuccess = dataArr[counter + 2]
        counter += 7
        statsObj[prefPt]['res']['success'] = 0 if resSuccess == '-' else int(resSuccess)
        statsObj[prefPt]['nonRes']['success'] = 0 if nonResSuccess == '-' else int(nonResSuccess)

    print(statsObj)
    return statsObj
