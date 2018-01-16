# - * - coding: utf - 8 -*-
# 作者：田丰(FontTian)
# 创建时间:'2017/8/16'

import nltk
import jieba
from ftools import cnlp

# NP chunking (NER)
print('\n命名实体识别')
f=open("/home/fonttian/PycharmProjects/ML/Python3 NLTK/txt/simple_test_en.txt",encoding='utf8')
text=f.read()
sentences = nltk.sent_tokenize(text) # 句子标识化
tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences] # cut word
tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences] # POS

for sent in tagged_sentences:# NER
    print(nltk.ne_chunk(sent))


# 关系提取
print('\n关系提取')
import re
IN = re.compile(r'.*\bin\b(?!\b.+ing)')
for doc in nltk.corpus.ieer.parsed_docs('NYT_19980315'): # 使用了ieer的内置语料库
    for rel in nltk.sem.extract_rels('ORG', 'LOC', doc, corpus='ieer', pattern = IN):
        print(nltk.sem.rtuple(rel))


# 显示解析树

from nltk.corpus import treebank
t = treebank.parsed_sents('wsj_0001.mrg')[0]
t.draw()