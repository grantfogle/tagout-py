from PyPDF2 import PdfReader

def getPopulationData(source):
    reader = PdfReader(source)
    text = ""
    for page in reader.pages:
        # text += page.extract_text() + "\n"  # Concatenates text from each page
    # print(text)

getPopulationData('../../data/colorado/population_estimates/2022ElkPopulationEstimates.pdf')