'''
PDF to PNG - SP - 03/04/2022
User system dependincies must be installed
User selects PDF file to convert
User selects output folder
'''

import fitz # For PDF to PNG conversion
from PyPDF2 import PdfFileReader # To count number of pages
from PyPDF2 import PdfFileMerger
import tkinter as tk # Recommended prescriptive naming convention
from tkinter.filedialog import askopenfilename # Simple user file selector
from tkinter.filedialog import askopenfilenames # Multiple file selector
from tkinter.filedialog import askdirectory # Simple user directory selector

filename = ""
file_tuple = ()
output_location = ""

def get_file_name():
    global filename
    filename = askopenfilename()

def get_combine_pdf_names():
    global file_tuple
    file_tuple = askopenfilenames()
    print(file_tuple)

def combine_pdf():
    merger = PdfFileMerger()
    for pdf in file_tuple:
        merger.append(pdf)
    combined_output_location = f"{output_location}/combined.pdf"
    merger.write(combined_output_location)
    merger.close()

def get_output_directory():
    global output_location
    output_location = askdirectory()

def convert_pdf():
    pdf = PdfFileReader(open(filename,'rb'))
    number_of_pages = pdf.getNumPages()
    pdffile = filename
    doc = fitz.open(pdffile)
    count = 0

    while count < number_of_pages:   
        page = doc.load_page(count)  # number of page
        pix = page.get_pixmap()
        output = f"{output_location}/_page_{count}.png"
        pix.save(output)
        count += 1

'''
GUI toolkit Python interface to Tcl/Tk
'''
r = tk.Tk()
r.title("PDF to PNG Convertor by Simon Parker")
r.geometry("400x425+10+10")
r['background']='#666666'
button1 = tk.Button(r, text='Select Output Folder', width=25, pady= 10, padx= 10, command=get_output_directory)
button2 = tk.Button(r, text='Select PDF to Combine', width=25, pady= 10, padx= 10, command=get_combine_pdf_names)
button3 = tk.Button(r, text='Add PDF', width=25, pady= 10, padx= 10, command=get_file_name)
button4 = tk.Button(r, text='Combine!', width=25, pady= 10, padx= 10, command=combine_pdf)
button5 = tk.Button(r, text='Convert!', width=25, pady= 10, padx= 10, command=convert_pdf)
button1.place(x=100, y=50)
button2.place(x=100, y=120)
button3.place(x=100, y=190)
button4.place(x=100, y=260)
button5.place(x=100, y=330)
print(file_tuple)
r.mainloop()