from read_pdf import read_pdf_PDFMINER
import re
import os

BASE_DIR = "/Users/onmywave/Desktop/download"
os.chdir(BASE_DIR)

if __name__ == "__main__":

    pdf_list = []

    for f_name in os.listdir():
        if f_name.endswith('.pdf'):
            pdf_list.append(f_name)

    print(len(pdf_list))

    disabled_info = [] 

    for pdf in pdf_list:
        data = read_pdf_PDFMINER(pdf)
        print(pdf)
        if re.match('장애', data):
            disabled_info.append(pdf)
    
    print(disabled_info)        

        
    