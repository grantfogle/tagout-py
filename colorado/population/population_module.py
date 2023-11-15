from pdf2image import convert_from_path
import pytesseract

def extract_text_from_pdf(pdf_path):
    # Convert PDF to images
    pages = convert_from_path(pdf_path)

    # Process each page
    text = ""
    for page in pages:
        text += pytesseract.image_to_string(page) + "\n"

    return text


pdf_path = '../../data/colorado/population_estimates/2022ElkPopulationEstimates.pdf'
extracted_text = extract_text_from_pdf(pdf_path)
# print(extracted_text)

extractedTextArr =  extracted_text.split('\n')
for i in range(6, len(extractedTextArr) - 10):
    splitTextArr = extractedTextArr[i].split(' ')
    print(splitTextArr)
    dau = splitTextArr[0]
    populationEstimate = splitTextArr[-2]
    maleFemaleRatio = splitTextArr[-1]
    print(dau, populationEstimate, maleFemaleRatio)
    # print(extractedTextArr[i].split(' '))
    # index zero is the DAU
    # index 2 -> 3/4 is the herd name
    # other units are the GMU's
    # index second to last is the post hunt estimate
    # index last is bull cow ratio
# print(extractedTextArr)