from PyPDF2 import PdfReader
import re

reader = PdfReader("../../../../2021ElkDrawRecap.pdf")

page = reader.pages[0]
finalCodes = []

pattern = 'E[A-Z]\d\d\d[A-Z]\d[A-Z]'
# elkRegex = re.compile('E[A-Z]\d\d\d[A-Z]\d[A-Z]')
# print(re.search(pattern, page.extract_text()))
# m = elkRegex.match(page.extract_text())
# elkCodes = re.findall(pattern, page.extract_text())

# print(elkCodes)

for i in range(963):
    readPage = reader.pages[i]
    elkCodes = re.findall(pattern, readPage.extract_text())
    if (elkCodes):
        finalCodes.append(elkCodes[0])
    i+=1

print(finalCodes)
# print(m)
# if m:
#     print(m)

# print(page.extract_text())