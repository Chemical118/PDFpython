import pikepdf
import os

path = "pass/"
file_list = os.listdir(path)
for i in file_list:
    print(i)
    input_pdf = pikepdf.Pdf.open(path + i)
    pdf = pikepdf.Pdf.new()
    for n, page in enumerate(input_pdf.pages):
        pdf.pages.append(page)
    pdf.save("word/" + i)
