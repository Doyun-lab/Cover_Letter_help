from konlpy.tag import Kkma
from konlpy.tag import Komoran
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import normalize
from preprocess_all import preprocess_answer
import numpy as np
import pandas as pd

data = pd.read_csv("C:/Users/user/Desktop/2020_text_mining/jobkorea_data.csv")


data = preprocess_answer(data)

# 문장 토큰화
class SentenceTokenizer(object):
    def __init__(self):
        self.kkma = Kkma()
        self.komoran = Komoran()
    
    # 텍스트를 입력으로 받아서 문장단위로 나누어 줌
    def text_sentences(self, text):
        sentences = self.kkma.sentences(text)
        for idx in range(0, len(sentences)):
            if len(sentences[idx]) <= 10:
                sentences[idx-1] += (' ' + sentences[idx])
                sentences[idx] = ''
        return sentences
