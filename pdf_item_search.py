import PyPDF2
import re
import pandas as pd

month = '07/'
item = 'MART'


def rFind(gotcha):
    rlist = []
    for r in range(0, rows):
        if isinstance(df.values[r, 0], str):
            ds = df.values[r, 0]
            m1 = re.search(gotcha, ds)
            if m1:
                found = m1.group(0)
                rlist.append(r)
    return rlist


pdfFileObj = open('August 03_21.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pdfReader.decrypt('')
for page in range(0, pdfReader.numPages):
    pageObj = pdfReader.getPage(page).extractText()
    pageObj = pageObj.split(month)
    df = pd.DataFrame((sub.split(month) for sub in pageObj))
    (rows, column) = df.shape

    ds1 = rFind(item)
    for i in ds1:
        if item in str(df.values[i])[1:50]:
            print(str(df.values[i])[1:4] + ' ' + str(df.values[i])[4:43] + ' ' + str(df.values[i])[43:50])
