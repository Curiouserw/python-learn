
from PyPDF2 import PdfFileWriter, PdfFileReader


readFile = 'material-pdf/test.pdf'
outFile = 'material-pdf/test-add-blanlpage.pdf'
pdfFileWriter = PdfFileWriter()
    
pdfFileReader = PdfFileReader(readFile)
numPages = pdfFileReader.getNumPages()

for index in range(0, numPages):
    pageObj = pdfFileReader.getPage(index)
    pdfFileWriter.addPage(pageObj)
    pdfFileWriter.write(open(outFile, 'wb'))

pdfFileWriter.addBlankPage() 
pdfFileWriter.write(open(outFile,'wb'))
