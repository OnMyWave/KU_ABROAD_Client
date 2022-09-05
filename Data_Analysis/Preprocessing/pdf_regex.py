import re
import openpyxl
from read_pdf import read_pdf_PDFMINER

# Env Setting



def preprocessing(f_path):
    personal_info = [
                '(Host Institution) ',
                ' 파견 국가/도시',
                '(Country/City) ',
                ' 파견기간',
                '(Period) ',
                '※ 작성하신 후'
                ]

    reg_list = [
                '1. 해외교 지원절차 (서류 준비 및 제출 등)',
                '2. 비자 준비과정',
                '3. 학교 크기, 지리적 위치, 주변 환경, 현지 날씨 등',
                '4. 수업 (수강신청, 수업 진행 방법 등)',
                '5. 숙소 (기숙사 신청, 기숙사 시설, 외부 숙소 정보 등) 및 식사',
                '6. 학교 관련 기타 정보 (부대시설, 동아리, 교환학생을 위한 프로그램 등)',
                '7. 해외교 International Office (위치, 담당자, 받은 도움 등)',
                '8. 기타 (현지에서의 생활, culture shock 등)',
                '9. 교환학생 프로그램 관련 전반적인 의견'
                ]


    data = read_pdf_PDFMINER(f_path)
    string_index = [data.find(reg_list[i]) for i in range(len(reg_list))]
    string_index.append(len(data)-1)
    string_list = [data[string_index[i]+len(reg_list[i]):string_index[i+1]] for i in range(len(reg_list))]
    string_index2 = [data.find(personal_info[i]) for i in range(len(personal_info))]
    string_list2 = [data[string_index2[i]+len(personal_info[i]):string_index2[i+1]] for i in [0,2,4]]
    data_list = string_list2 + string_list
    
    return data_list

    # return [학교, 도시, 파견기간, column 1 ~ 9]

