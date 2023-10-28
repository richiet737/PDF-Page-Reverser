#!/Library/Frameworks/Python.framework/Versions/3.12/bin/python3
# coding: utf-8
# Created by Richard Bradshaw 28 Oct 2023

# importing libraries
from PyPDF2 import PdfReader, PdfWriter
import os
import sys

#Check command line format
def get_input():
    if len(sys.argv) < 2:
        print("./pdfReverse.py <fileName.pdf>")
        sys.exit(1)
    
    for apdf in sys.argv[1:]:
        pdf_file = os.path.expanduser(apdf)
        if not pdf_file.endswith('.pdf'):
            print("PDF file type required. Did you forget the extension (.pdf)?")
            sys.exit(1)
        
        global path
        path = os.path.expanduser(apdf)

# main function
# open file to read
# reverse the page order
# write to file
def get_info(path):
    with open(path, 'rb') as f:
        pdf = PdfReader(f)
        number_of_pages = len(pdf.pages)
        print("processing", path, number_of_pages, "pages")
        
        if number_of_pages == 1:
            sys.exit('only one page found')
            
        # build output PDF filename
        writer = PdfWriter()
        bpath, ext = os.path.splitext(path)
        pdfrev = os.path.basename(bpath + '_reversed' + ext)
        #pdf_out = open(pdfrev, 'wb')
        
        # n is sequential page increase, r is the reversed page number
        for n in (reversed(range(0, number_of_pages))):
            writer.add_page(pdf.pages[n])
       
        pdf_out = open(pdfrev, 'wb')
        writer.write(pdf_out)
        pdf_out.close()

if __name__ == '__main__':
    get_input()
    get_info(path)
