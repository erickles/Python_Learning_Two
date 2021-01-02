# Install this dependency before
# pip install PyPDF2

import PyPDF2

f = open('Working_business_Proposal.pdf','rb')

pdf_reader = PyPDF2.PdfFileReader(f)

print(pdf_reader.numPages)

page_one = pdf_reader.getPage(0)

print(page_one)

page_one_text = page_one.extractText()

print(page_one_text)

pdf_writer = PyPDF2.PdfFileWriter()

pdf_writer.addPage(page_one)

pdf_output = open('Some_Brand_New_Doc.pdf','wb')

pdf_writer.write(pdf_output)

pdf_text = []

pdf_reader = PyPDF2.PdfFileReader(f)

for num in range(pdf_reader.numPages):

    page = pdf_reader.getPage(num)

    pdf_text.append(page.extractText())

print(pdf_text)

f.close()

pdf_output.close()

