import PyPDF2
import pandas as pd

month = '07/'

pdfFileObj = open('August 03_21.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pdfReader.decrypt('')
for page in range(0, pdfReader.numPages):
    pageObj = pdfReader.getPage(page).extractText()
    pageObj = pageObj.split(month)
    df = pd.DataFrame((sub.split(month) for sub in pageObj))
    (rows, column) = df.shape
    item_list = df.values[3:50].tolist()
    if item_list:
        item_list1 = []
        for item in zip(*item_list):
            item_list1.append(item)
        item_list2 = []
        for item in item_list1[0]:
            if item[2:41] not in item_list2:
                item_list2.append(item[2:41])
        print(item_list2)
