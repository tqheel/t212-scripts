import os
from pathlib import Path
from os import listdir
from os.path import isfile, join

import PyPDF2

merger = PyPDF2.PdfMerger()

#get PDFs files and path
path = Path('data/2023-lumiaria-final-sales-maps-scans/')
pdfs = [f for f in listdir(path) if isfile(join(path, f))]

os.chdir(path)


#iterate among the documents
for pdf in pdfs:
    try:
        #if doc exist then merge
        if os.path.exists(pdf):
            input = PyPDF2.PdfReader(open(pdf,'rb'))
            merger.append((input))
        else:
            print(f"problem with file {pdf}")
    
    except Exception as e:
        print(f"Can't merge {pdf}. Error: {str(e)}")
    else:
        print(f" {pdf} Merged !!! ")

os.chdir('..')
merger.write("2023-final-merged.pdf")