from io import StringIO
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
import re

### 

def read_pdf_PDFMINER(pdf_file_path):
    """
    read_pdf to string and preprocessing [공백, x0c, - num -]

    doc : https://pdfminersix.readthedocs.io/en/latest/tutorials/composable.html
    """
    output_string = StringIO()
    with open(pdf_file_path, 'rb') as f:
        parser = PDFParser(f)
        doc = PDFDocument(parser)
        rsrcmgr = PDFResourceManager()
        device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.create_pages(doc):
            interpreter.process_page(page)
    string_data = output_string.getvalue()

    replaced_string = string_data.replace('\n',' ').replace('  ',' ').replace('국제처 국제교류팀','').strip()
    re_string = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\xff]', '', replaced_string)

    # Delete page number
    for i in range(1,30):
        re_string = re_string.replace('- '+ str(i) + ' -','')
    
    return str(re_string)

print(read_pdf_PDFMINER('docu1.pdf'))