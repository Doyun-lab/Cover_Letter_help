import numpy as np
import pandas as pd

data = pd.read_csv("C:/Users/user/Desktop/2020_text_mining/jobkorea_data.csv")

from konlpy.tag import Komoran
komoran=Komoran()

x_list = data['답변']
x_list

data_word=[]
for i in range(len(x_list)):
    try:
        data_word.append(komoran.nouns(x_list[i]))
    except Exception as e:


        continue

Data_list=x_list.values.tolist()


from gensim import corpora, models
from gensim.models.wrappers import LdaMallet

id2word=corpora.Dictionary(data_word)
id2word.filter_extremes(no_below = 0) #20회 이하로 등장한 단어는 삭제
