import numpy as np
import pandas as pd

data = pd.read_csv("jobkorea_data.csv")

data.shape
data.columns.tolist()

from konlpy.tag import Hannanum  
hannanum=Hannanum()

x_list = data['답변']
x_list

data_word=[]
for i in range(len(x_list)):
    try:
        data_word.append(hannanum.nouns(x_list[i]))
    except Exception as e:
        continue

Data_list=x_list.values.tolist()

from gensim import corpora, models
from gensim.models.wrappers import LdaMallet

id2word=corpora.Dictionary(data_word)
id2word.filter_extremes(no_below = 0) #20회 이하로 등장한 단어는 삭제