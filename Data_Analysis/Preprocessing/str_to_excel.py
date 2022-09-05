from pdf_regex import preprocessing
import os
import openpyxl
import time

BASE_DIR = "/Users/onmywave/Desktop/download"
os.chdir(BASE_DIR)


if __name__ == "__main__":

    pdf_list = []

    for f_name in os.listdir():
        if f_name.endswith('.pdf'):
            pdf_list.append(f_name)

    print(len(pdf_list))

    wb = openpyxl.Workbook()
    ws = wb.active
    for i in range(len(pdf_list)):
        data_list = preprocessing(pdf_list[i])
        for j in range(12):
            ws[chr(65+j)+str(i+2)] = data_list[j]
    wb.save(filename = 'data.xlsx')
    wb.close()

        
    