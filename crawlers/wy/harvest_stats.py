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
                # print('j: ', j, splitLine)

                if isHerdRow(splitLine):
                    (unit, herd) = getHerdRow(splitLine)
                    print(unit, herd)
                    startDataCollection()
                # iterate through line
        print('========================')


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
