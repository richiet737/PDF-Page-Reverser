#!/Library/Frameworks/Python.framework/Versions/3.12/bin/python3
# coding: utf-8

# importing PyPDF2 library
# get_doc_info.py
from PyPDF2 import PdfReader, PdfWriter
import os
import sys


def get_input():
    if len(sys.argv) < 2:
        print("./pdfReverse.py <fileName.pdf>")
        sys.exit(1)
    
    for apdf in sys.argv[1:]:
        pdf_file = os.path.expanduser(apdf)
        if not pdf_file.endswith('.pdf'):
            print("PDF file type required")
            sys.exit(1)
        
        global path
        path = os.path.expanduser(apdf)

def get_info(path):
    with open(path, 'rb') as f:
        pdf = PdfReader(f)
        #info = pdf.getDocumentInfo()
        number_of_pages = len(pdf.pages)
        print("processing", path, number_of_pages, "pages")
        
        #print(info)
        #author = info.author
        #creator = info.creator
        #producer = info.producer
        #subject = info.subject
        #title = info.title
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
