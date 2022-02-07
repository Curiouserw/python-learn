from PyPDF2 import PdfFileWriter, PdfFileReader

pages_to_delete = [0, 2] # 想要删除的页码，页码从0开始
infile = PdfFileReader('material-pdf/test-add-blanlpage.pdf', 'rb')
output = PdfFileWriter()

for i in range(infile.getNumPages()):
    if i not in pages_to_delete:
        p = infile.getPage(i)
        output.addPage(p)

with open('material-pdf/test-add-blanlpage+del-some-page.pdf', 'wb') as f:
    output.write(f)