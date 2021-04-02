import pikepdf
import os

a,b = map(int,input().split())
if a > b:
    error
path = "pass/"
file_list = os.listdir(path)
for i in file_list:
    print(i)
    input_pdf = pikepdf.Pdf.open(path + i)
    pdf = pikepdf.Pdf.new()
    for n, page in enumerate(input_pdf.pages):
        if a <= n+1 and n+1 <= b:
            pdf.pages.append(page)
    pdf.save("word/" + i.split('.')[0] + '_slic' + "_%d_%d" %(a,b) + ".pdf")
