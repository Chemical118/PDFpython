from pdfminer.layout import LAParams, LTTextBox
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
import pyperclip as cp
import os
path = "open/"
file_list = os.listdir(path)
for i in file_list:
    fp = open(path + i, 'rb')
    rsrcmgr = PDFResourceManager()
    laparams = LAParams()
    device = PDFPageAggregator(rsrcmgr, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    pages = PDFPage.get_pages(fp)
    fp.close()
    st = []
    nd = []

    for ind, page in enumerate(pages):
        interpreter.process_page(page)
        layout = device.get_result()
        for num, lobj in enumerate(layout):
            if isinstance(lobj, LTTextBox):
                t = lobj.get_text().replace(" ", "")
                if "일반정보" in t:
                    st.append(ind + 1)
                    # print("st")
                if "출제의도" in t:
                    nd.append(ind + bool(num))
                    # print("nd")
    ans = ""
    if len(st) == len(nd):
        for i in range(len(st)):
            if st[i] == nd[i]:
                print(nd[i], end="")
                ans += str(nd[i])
            else:
                print("%d-%d" % (st[i], nd[i]), end="")
                ans += "%d-%d" % (st[i], nd[i])
            print((len(st) != i + 1) * "," + " ", end="")
            ans += ((len(st) != i + 1) * ", ")
        cp.copy(ans)
        print("\nclipboard complete!")
    else:
        print("Error")
