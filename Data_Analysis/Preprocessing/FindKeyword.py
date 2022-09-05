import pandas as pd
from pandas import DataFrame as df

data = pd.read_excel("/Users/codok/Desktop/datathon python/rawdataset/Dataset.xlsx", engine="openpyxl")
Dataset=df(data)



datanum=768
univnum=111
Refined_Data=[]
Key=[]


def Document(a:int):
    text1=""
    text2=""
    text3=""
    text4=""
    text5=""
    text6=""
    text7=""
    text8=""
    text9=""
    li=[]
    for i in range(datanum):
        if Dataset["univnum"][i]==a:
            text1+=Dataset["col1"][i].strip()
            text2+=Dataset["col2"][i].strip()
            text3+=Dataset["col3"][i].strip()
            text4+=Dataset["col4"][i].strip()
            text5+=Dataset["col5"][i].strip()
            text6+=Dataset["col6"][i].strip()
            text7+=Dataset["col7"][i].strip()
            text8+=Dataset["col8"][i].strip()
            text9+=Dataset["col9"][i].strip()
        if Dataset["univnum"][i]==a+1:
            break
    li.append(text1)
    li.append(text2)
    li.append(text3)
    li.append(text4)
    li.append(text5)
    li.append(text6)
    li.append(text7)
    li.append(text8)
    li.append(text9)
    return(li)

def RefineDocument():
    for i in range(univnum):
        Refined_Data.append(Document(i+1))
        
        


def FindKeyword(a:str,b:int,c:int):
    RefineDocument()
    KK=[]
    ll=([x for x in Refined_Data[b-1][c-1].split('.') if x])
    for k in range(len(ll)):
        if a in ll[k]:
            KK.append(ll[k])
    return(KK)

print(FindKeyword("인실",15,5))  # FindKeyword("키워드(형태소 아니여도 됨)","univnum","col num")
