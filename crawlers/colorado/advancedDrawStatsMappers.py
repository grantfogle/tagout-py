
def assignPreDrawStats(statsObj, dataArr):
    dataArrLen = len(dataArr) - 1
    counter = 0
    while counter < dataArrLen:
        prefPt = dataArr[counter]
        resApps = 0 if dataArr[counter + 1] == '-' else int(dataArr[counter + 1])
        nonResApps = 0 if dataArr[counter + 2] == '-' else int(dataArr[counter + 2])
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
        statsObj[prefPt] = newObj
        counter+=7

    return statsObj

def assignPostDrawStats(statsObj, dataArr):
    dataArrLen = len(dataArr) - 1
    counter = 0
    while counter < dataArrLen:
        prefPt = dataArr[counter]
        resSuccess = dataArr[counter + 1]
        nonResSuccess = dataArr[counter + 2]
        statsObj[prefPt]['res']['success'] = 0 if resSuccess == '-' else int(resSuccess)
        statsObj[prefPt]['nonRes']['success'] = 0 if nonResSuccess == '-' else int(nonResSuccess)
        counter += 7

    return statsObj

# def assignTotalChoicePreDrawStats(statsObj, dataArr):
# def assignTotalChoicePostDrawStats(statsObj, dataArr):
