import PyPDF2

pdf_file = open(
    '/Users/grantfogle/Desktop/workspace/startups/tagout/tagout-py/inputs/wyoming/elk/draw_stats/random/2022-NR-Elk-Random-Draw-Report.pdf', 'rb')

pdf_reader = PyPDF2.PdfFileReader(pdf_file)

# Initialize an empty string to store the extracted text
text = ''

# Iterate over each page of the PDF
# for page_num in range(pdf_reader.numPages):
for page_num in range(pdf_reader.numPages):
    # Get the page object
    page = pdf_reader.getPage(page_num)
    # Extract the text from the page
    page_text = page.extractText()
    # Add the page text to the overall text
    text += page_text

# Close the PDF file
pdf_file.close()

# Print the extracted text
print(text)
# Note that the above code will extract the text from all pages of the PDF and store it in a single string variable named text. You can modify the code to suit your specific requirements.
