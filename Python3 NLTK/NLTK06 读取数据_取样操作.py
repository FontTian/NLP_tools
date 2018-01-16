#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:fonttian
@file: NLTK06 读取数据_取样操作.py
@time: 2017/09/26
"""
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import csv
def preprocessing(text):
    text = text
    # tokenize into words
    tokens = [word for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]

    # remove stopwords
    stop = stopwords.words('english')
    tokens = [token for token in tokens if token not in stop]

    # remove words less than three letters
    tokens = [word for word in tokens if len(word) >= 3]

    # lower capitalization
    tokens = [word.lower() for word in tokens]

    # lemmatize
    lmtzr = WordNetLemmatizer()
    tokens = [lmtzr.lemmatize(word) for word in tokens]
    preprocessed_text= ' '.join(tokens)

    return preprocessed_text
sms = open('/home/fonttian/Data/NLP/NLTK_book/SMSSpamCollection',encoding='utf8') # check the structure of this file!
sms_data = []
sms_labels = []
csv_reader = csv.reader(sms,delimiter='\t')
for line in csv_reader:
     # adding the sms_id
    sms_labels.append( line[0])
    # adding the cleaned text We are calling preprocessing method
    sms_data.append(preprocessing(line[1]))

sms.close()
