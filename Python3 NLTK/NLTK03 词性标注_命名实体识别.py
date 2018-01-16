# - * - coding: utf - 8 -*-
# 作者：田丰(FontTian)
# 创建时间:'2017/8/15'

import nltk
from ftools import cnlp
from os import path

d = path.dirname(__file__)

# 词性标注
from nltk import word_tokenize



stopwords_path = d + '/stopwords/CNENstopwords.txt'  # 停用词词表
text_path = d + '/txt/simple_test.txt'  # 设置要分析的文本路径
cnlp_basis = cnlp.basis(textPath=text_path, stopwordsPath=stopwords_path, ReadText=True)
cleaner1 = cnlp_basis.getText().split()

# 词性标注 英文
en_text = 'This is just a words to test NLTK'
print(nltk.pos_tag(word_tokenize(en_text)))

# 词性标注 中文
list_pos = cnlp_basis.jiebaCutWithPos()
print(list_pos)

# 根据词性过滤
tagged = nltk.pos_tag(word_tokenize(en_text))
allnoun = [word for word, pos in tagged if pos in ['NN', 'NNP']]
print(allnoun)

# 根据词性过滤 中文
allnoun_cn = [word for word, pos in list_pos if pos in ['n', 'v']]
print(allnoun_cn)

# POS tags freq distribtuion
from nltk.corpus import brown
import nltk

tags = [tag for (word, tag) in brown.tagged_words(categories='news')]
print(nltk.FreqDist(tags))

# default tagger
brown_tagged_sents = brown.tagged_sents(categories='news')
default_tagger = nltk.DefaultTagger('NN')
print(default_tagger.evaluate(brown_tagged_sents))
# 0.13089484257215028

# N-gram 标注器

from nltk.tag import UnigramTagger
from nltk.tag import TrigramTagger
from nltk.tag import BigramTagger
from nltk.tag import DefaultTagger

# we are dividing the data into a test and train to evaluate our taggers.
train_data = brown_tagged_sents[:int(len(brown_tagged_sents) * 0.9)]
test_data = brown_tagged_sents[int(len(brown_tagged_sents) * 0.9):]

unigram_tagger = UnigramTagger(train_data, backoff=default_tagger)
# unigram_tagger = UnigramTagger(train_data, backoff=regexp_tagger)
print(unigram_tagger.evaluate(test_data))
# 0.8361407355726104

bigram_tagger = BigramTagger(train_data, backoff=unigram_tagger)
print(bigram_tagger.evaluate(test_data))
# 0.8452108043456593

trigram_tagger = TrigramTagger(train_data, backoff=bigram_tagger)
print(trigram_tagger.evaluate(test_data))
# 0.843317053722715

# 命名实体识别
# NER tagger
from nltk import ne_chunk
from nltk import word_tokenize
sent = "Mark is studying at Stanford University in California"
print(ne_chunk(nltk.pos_tag(word_tokenize(sent)), binary=False))
print(ne_chunk(nltk.pos_tag(word_tokenize(sent)), binary=True))
