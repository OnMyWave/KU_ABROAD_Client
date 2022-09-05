import pandas as pd
from pandas import DataFrame as df

from gensim import corpora
from gensim import models

from konlpy.tag import Mecab
from tqdm import tqdm

from gensim.models.ldamodel import LdaModel
from gensim import corpora
import gensim
import pickle
import pyLDAvis.gensim_models as gensimvis
import pyLDAvis
from gensim.models.coherencemodel import CoherenceModel
import matplotlib.pyplot as plt
import math

mecab=Mecab()


data = pd.read_excel("/Users/codok/Desktop/datathon python/rawdataset/Dataset.xlsx", engine="openpyxl")
Dataset=df(data)

datanum=768
univnum=111
Refined_Data=[]

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

def TF(a:str,b:int,c:int):
    t=Refined_Data[c-1][b-1]
    l=mecab.morphs(t)
    for line in tqdm(l):
        tf=l.count(a)
    return(tf)


def IDF(a:str):
    Totalnum=0
    DF=0
    for i in range(univnum):
        for j in range(9):
            li=([x for x in Refined_Data[i][j].split('.') if x])
            Totalnum+=len(li)
            for k in range(len(li)):
                if a in li[k]:
                    DF+=1
    return(math.log(Totalnum/1+DF))

def Score(a:str,b:int,c:int):
    RefineDocument()
    tf=TF(a,b,c)
    idf=IDF(a)
    return(tf*idf)


print(Score("덥",3,49)) ## Score("키워드(형태소)", "몇번 col", "univ num")
