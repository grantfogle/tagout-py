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
print(extracted_text)