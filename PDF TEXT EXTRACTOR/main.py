import PyPDF2
a=PyPDF2.PdfFileReader('The_Intelligent_Investor.pdf')
print(a.getDocumentInfo())
# print(a.getNumPages()) #Number of pages in a book
# print(a.getPage(22).extractText()) #Text content of a page
str=""
for i in range(22,35):
    str+=a.getPage(i).extractText()

with open("text.txt","w") as f:
    f.write(str)