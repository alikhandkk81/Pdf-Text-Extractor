from asyncore import write
import PyPDF2

a = PyPDF2.PdfFileReader("C:\\Users\\jimmy khan\\Desktop\\python.pdf")
print(a.documentInfo)
print(a.getNumPages())
str = ""
for i in range(1,50):
   str += a.getPage(i).extractText()
print("Text Extracted Done")

with open("C:\\Users\\jimmy khan\\Desktop\\python.txt", "w", encoding='utf-8') as f:
    f.write(str)