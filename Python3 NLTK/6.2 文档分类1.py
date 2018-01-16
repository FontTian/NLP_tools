# - * - coding: utf - 8 -*-
# 作者：田丰(FontTian)
# 创建时间:'2017/8/17'

import nltk
from ftools import cnlp
from os import path
import random
import jieba

d = path.dirname(__file__)

from nltk.corpus import movie_reviews

# 电影评论资料库
documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]
random.shuffle(documents)

stopwords_path = 'stopwords\ENstopwords.txt'  # 停用词词表
def jiebaclearText(text):
    mywordlist = []
    seg_list = jieba.cut(text, cut_all=False)
    liststr = "/ ".join(seg_list)
    f_stop = open(stopwords_path,encoding='utf8')
    try:
        f_stop_text = f_stop.read()
    finally:
        f_stop.close()
    f_stop_seg_list = f_stop_text.split('\n')
    for myword in liststr.split('/'):
        if not (myword.strip() in f_stop_seg_list) and len(myword.strip()) > 1:
            mywordlist.append(myword)
    return mywordlist

def jiebaclearList(txtList):
    mywordlist = []
    f_stop = open(stopwords_path,encoding='utf8')
    try:
        f_stop_text = f_stop.read()
    finally:
        f_stop.close()
    f_stop_seg_list = f_stop_text.split('\n')
    for myword in txtList:
        if not (myword.strip() in f_stop_seg_list) and len(myword.strip()) > 1:
            mywordlist.append(myword)
    return mywordlist

all_words = jiebaclearList(list(movie_reviews.words()))
print(len(all_words))
clean_words = nltk.FreqDist(w.lower() for w in all_words)
word_features = list(clean_words)[:500]


def document_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains({})'.format(word)] = (word in document_words)
    return features

print(document_features(jiebaclearList(list(movie_reviews.words('pos/cv957_8737.txt')))))
