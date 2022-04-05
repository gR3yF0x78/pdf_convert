'''
PDF to PNG - SP - 03/04/2022
User selects PDF file to convert
User selects output folder
'''

import fitz # For PDF to PNG conversion
from PyPDF2 import PdfFileReader # To count number of pages
from tkinter.filedialog import askopenfilename # Simple user file selector
from tkinter.filedialog import askdirectory # Simple user directory selector

filename = askopenfilename()
pdf = PdfFileReader(open(filename,'rb'))
number_of_pages = pdf.getNumPages()
pdffile = filename
doc = fitz.open(pdffile)
output_location = askdirectory()
count = 0

while count <= number_of_pages:   
    page = doc.loadPage(count)  # number of page
    pix = page.get_pixmap()
    output = f"{output_location}/_page_{count}.png"
    pix.save(output)
    count += 1