from this import d
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

mecab=Mecab()

Dataset = df(columns=[ "Host Institution", "Country/City","Period",'1', "2", "3", "4", "5", "6", "7", "8", "9"])

data = pd.read_excel("/Users/codok/Desktop/data /rawdata.xlsx", engine="openpyxl")


doc1=[]
doc2=[]
doc3=[]
doc4=[]
doc5=[]
doc6=[]
doc7=[]
doc8=[]
doc9=[]

datanum=1200 #data 총개수(행의개수)
for j in Dataset.columns:
    if j=='1':
        for i in range(datanum):
            doc1.append(data[int(j)][i])
       
    if j=='2':
        for i in range(datanum):
            doc2.append(data[int(j)][i])
        
    if j=='3':
        for i in range(datanum):
            doc3.append(data[int(j)][i])
      
    if j=='4':
        for i in range(datanum):
            doc4.append(data[int(j)][i])
      
    if j=='5':
        for i in range(datanum):
            doc5.append(data[int(j)][i])
     
    if j=='6':
        for i in range(datanum):
            doc6.append(data[int(j)][i])
      
    if j=='7':
        for i in range(datanum):
            doc7.append(data[int(j)][i])
     
    if j=='8':
        for i in range(datanum):
            doc8.append(data[int(j)][i])
  
    if j=='9':
        for i in range(datanum):
            doc9.append(data[int(j)][i])
 

resultdoc1=[]
resultdoc2=[]
resultdoc3=[]
resultdoc4=[]
resultdoc5=[]
resultdoc6=[]
resultdoc7=[]
resultdoc8=[]
resultdoc9=[]




##for line in tqdm(lines): 
##    if line:
##       result1.append(mecab.morphs(line))
## 형태소 분석용.

def tokenize(a:list,b:list):
    for line in tqdm(a):
        if line:
            b.append(mecab.nouns(line))

tokenize(doc1,resultdoc1)
tokenize(doc2,resultdoc2)
tokenize(doc3,resultdoc3)
tokenize(doc4,resultdoc4)
tokenize(doc5,resultdoc5)
tokenize(doc6,resultdoc6)
tokenize(doc7,resultdoc7)
tokenize(doc8,resultdoc8)
tokenize(doc9,resultdoc9)
       
        
def remove2word(a:list,b:int) :
    for i in range(b):
        for j in a[i]:
            if len(j)<2:
                a[i].remove(j)

remove2word(resultdoc1,datanum)
remove2word(resultdoc2,datanum)
remove2word(resultdoc3,datanum)
remove2word(resultdoc4,datanum)
remove2word(resultdoc5,datanum)
remove2word(resultdoc6,datanum)
remove2word(resultdoc7,datanum)
remove2word(resultdoc8,datanum)
remove2word(resultdoc9,datanum)


def lda_sketch(a:list,b:int):
    dictionary=corpora.Dictionary(a)
    corpus = [dictionary.doc2bow(text) for text in a]
    NUM_TOPICS = 7 # 20개의 토픽, k=20
    ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics = NUM_TOPICS, id2word=dictionary, passes=15)
    topics = ldamodel.print_topics(num_words=4)
    lda_visualization = gensimvis.prepare(ldamodel, corpus, dictionary, sort_topics=False)
    pyLDAvis.save_html(lda_visualization, str(b)+'.html')

lda_sketch(resultdoc1,1)
lda_sketch(resultdoc2,2)
lda_sketch(resultdoc3,3)
lda_sketch(resultdoc4,4)
lda_sketch(resultdoc5,5)
lda_sketch(resultdoc6,6)
lda_sketch(resultdoc7,7)
lda_sketch(resultdoc8,8)
lda_sketch(resultdoc9,9)
