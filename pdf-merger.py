from PyPDF2 import PdfFileMerger
from sys import argv
from datetime import datetime

pdf1 = argv[1]
pdf2 = argv[2]
now = datetime.now()
now = now.strftime("%Y%d%m-%H%M%S")
outputFile = "merge_result" + now + ".pdf"

merger = PdfFileMerger()
merger.append(pdf1)
merger.append(pdf2)
merger.write(outputFile)
merger.close()

print('Merged pdfs "' + pdf1 + '"' + ' and ' + '"' + pdf2 + '"' + ' successfully into a file:\n\n"' + outputFile + '"\n')