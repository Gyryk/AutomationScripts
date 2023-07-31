import PyPDF2
import sys
import os

# Merge all PDFs in same dir
merger = PyPDF2.PdfFileMerger()
for file in os.listdir(os.getcwd()):
	if file.endswith('pdf'):
		merger.append(file)
	merger.write("combinedDoc.pdf")
	