# - * - coding: utf - 8 -*-
# 作者：田丰(FontTian)
# 创建时间:'2017/8/17'
import nltk
from ftools import cnlp

import matplotlib as mpl

mpl.rcParams[u'font.sans-serif'] = [u'KaiTi']
mpl.rcParams[u'font.serif'] = [u'KaiTi']
# mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题,或者转换负号为字符串

stopwords_path = u'/home/fonttian/Data/NLP/stopwords/CNENstopwords.txt'  # 停用词词表
text_path = u'/home/fonttian/Data/NLP/txt/lz.txt'  # 设置要分析的文本路径

fontsTools = cnlp.basis(textPath=text_path, stopwordsPath=stopwords_path, ReadText=True)
fontsTools.addUserWords([u'路明非'])

cutAndclearStr = fontsTools.getText()

print(u'nltk 文本分析基本操作')

print(u'nltk.word_tokenize(cutAndclearStr')
print(u'nltk.FreqDist(tokenstr)')

tokenstr = nltk.word_tokenize(cutAndclearStr)

print(u'====== 其他基本指标并绘图 ======')

print(u'下面是nltk的其他类 ')
print(u'nltk.collocations.BigramCollocationFinder')
print(u'nltk.collocations.BigramCollocationFinder')

bigramcolloc = nltk.collocations.BigramCollocationFinder.from_words(tokenstr)
print(u"----出现最频繁的前10个词-----")
fdist1 = bigramcolloc.word_fd
for key, val in sorted(fdist1.items(), key=lambda x: (x[1], x[0]), reverse=True)[:10]:
    print(key, u":", val, u"||", end=' ')
print()

print(u"----只出现1次的低频词-----")
fdist1 = bigramcolloc.word_fd
for w in fdist1.hapaxes():
    print(w, u"||", end=' ')
print()

# 找出文本中的搭配词
print(u'找出文本中的搭配词')
print(u'nltk.bigrams(tokenstr)')
print(u'nltk.collocations.TrigramCollocationFinder')

bigramwords = nltk.bigrams(tokenstr)

print(u'====== 双连搭配词 ======')
for fw, sw in set(bigramwords):
    print(fw, u' ', sw, u"||", end=' ')
print()

trigramcolloc = nltk.collocations.TrigramCollocationFinder.from_words(tokenstr)
print(u"----三连搭配词-----")
for fw, sw, tw in trigramcolloc.ngram_fd:
    print(fw, u" ", sw, u" ", tw, u"|", end=' ')
print()


# strs1 = getNewWordsByNLPIR(filestr, 50)
# ShowByItem(strs1)
