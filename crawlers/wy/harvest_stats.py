from pypdf import PdfReader


def getHarvestStats(input, startIndex, endIndex):
    print(input, startIndex, endIndex)

    reader = PdfReader(input)
    for i in range(startIndex, endIndex):
        page = reader.pages[i]
        pageText = page.extract_text()
        pageLines = pageText.splitlines()
        for j in range(len(pageLines)):
            if j > 4:
                splitLine = pageLines[j].strip().split(' ')
                # print(splitLine)
                if isHerdRow(splitLine):
                    beginDataCollection = True
                    dataCounter = 1
                    (unit, herd) = getHerdRow(splitLine)
                    print(unit, herd)
                    # startDataCollection()
                    while beginDataCollection:
                        currentIndex = j + dataCounter
                        if (currentIndex < len(pageLines)):
                            collectArr = pageLines[currentIndex].strip().split(
                                ' ')
                            if isHerdRow(collectArr):
                                beginDataCollection = False
                            elif 'General' in collectArr or 'Pooled' in collectArr or 'Limited' in collectArr:
                                breakdownHarvestData(collectArr)
                        else:
                            beginDataCollection = False

                        dataCounter += 1
                # iterate through line
        print('========================')


def breakdownHarvestData(statArr):
    # clean up arr
    # remove anything before Limited/General/Pooled
    # type (limited, general and pooled aka total)
    # hunters bull spike cow calf total success days/harvest hunter days issued licenses
    cleanedUpArr = []
    drawType = ''
    statType = ''
    activeHunters = 0
    bull = 0
    spike = 0
    cow = 0
    calf = 0
    total = 0
    hunterSuccess = 0
    daysHarvest = 0
    hunterDays = 0
    licensesSold = 0

    [general]: {}
    limited: {[limitedType]: {}}
    pooled: {}
    for i in range(len(statArr)):
        item = statArr[i]
        # get index and set cleanup arr to it
        if item == 'Limited' or item == 'General' or item == 'Pooled':
            cleanedUpArr = statArr[i:]

    if cleanedUpArr[0] == 'Limited':
        drawType = cleanedUpArr[0]
        statType = cleanedUpArr[1]
        activeHunters = cleanedUpArr[2]
        bull = cleanedUpArr[3]
        spike = cleanedUpArr[4]
        cow = cleanedUpArr[5]
        calf = cleanedUpArr[6]
        total = cleanedUpArr[7]
        hunterSuccess = cleanedUpArr[8]
        daysHarvest = cleanedUpArr[9]
        hunterDays = cleanedUpArr[10]
        licensesSold = cleanedUpArr[11]
    elif cleanedUpArr[0] == 'General':
        drawType = cleanedUpArr[0]
        activeHunters = cleanedUpArr[1]
        bull = cleanedUpArr[2]
        spike = cleanedUpArr[3]
        cow = cleanedUpArr[4]
        calf = cleanedUpArr[5]
        total = cleanedUpArr[6]
        hunterSuccess = cleanedUpArr[7]
        daysHarvest = cleanedUpArr[8]
        hunterDays = cleanedUpArr[9]
        licensesSold = cleanedUpArr[10]
    elif cleanedUpArr[0] == 'Pooled':
        drawType = cleanedUpArr[0]
        statType = cleanedUpArr[1]
        activeHunters = cleanedUpArr[2]
        bull = cleanedUpArr[3]
        spike = cleanedUpArr[4]
        cow = cleanedUpArr[5]
        calf = cleanedUpArr[6]
        total = cleanedUpArr[7]
        hunterSuccess = cleanedUpArr[8]
        daysHarvest = cleanedUpArr[9]
        hunterDays = cleanedUpArr[10]


def isHerdRow(splitLine):
    if 2 <= len(splitLine) <= 5 and '(cross' not in splitLine and 'BY' not in splitLine and 'HUNTING' not in splitLine and 'I-A' not in splitLine:
        return True
    return False


def getHerdRow(splitLine):
    unit = splitLine[0]
    herd = " ".join(splitLine[1:])

    return (unit, herd)


def processLine(line):
    print(line)
    # check length of line, if 2-3
    # and doesn't have incl'
    # then it is the
