# - * - coding: utf - 8 -*-
# 作者：田丰(FontTian)
# 创建时间:'2017/8/16'

from ftools import cnlp
import sys
import matplotlib.pyplot as plt
import nltk
import pandas as pd

import matplotlib as mpl

mpl.rcParams['font.sans-serif'] = ['Yahei Mono']
mpl.rcParams['font.serif'] = ['Yahei Mono']
# mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题,或者转换负号为字符串
# import seaborn as sns
#
# sns.set_style("darkgrid", {"font.sans-serif": ['KaiTi', 'Arial']})

sys.path.append("../")

text_path = u'txt/lztest.txt'  # 设置要分析的文本路径
stopwords_path = u'stopwords/CNENstopwords.txt'  # 停用词词表

fontsTools = cnlp.basis(textPath=text_path, stopwordsPath=stopwords_path, ReadText=True)

print()
fontsTools.addUserWords([u'路明非'])
lztext = fontsTools.getText()

tokenstr = nltk.word_tokenize(lztext)
fdist1 = nltk.FreqDist(tokenstr)

listkey = []
listval = []

print(u".........统计出现最多的前30个词...............")
for key, val in sorted(fdist1.items(), key=lambda x: (x[1], x[0]), reverse=True)[:30]:
    listkey.append(key)
    listval.append(val)
    print(key, val, u' ',end=' ')

df = pd.DataFrame(listval, columns=[u'次数'])
df.index = listkey
df.plot(kind='bar')
plt.title(u'关于龙族一的词频统计')

plt.show()

posstr = fontsTools.jiebaCutWithPos()

cutTextList = []
for word, tag in posstr:
    # 获取动词
    if tag[0] == "v":
        cutTextList.append(word)

tokenstr = nltk.word_tokenize(" ".join(cutTextList))

fdist1 = nltk.FreqDist(tokenstr)

listkey = []
listval = []

print()
print(u".........统计出现最多的前30个动词...............")
for key, val in sorted(fdist1.items(), key=lambda x: (x[1], x[0]), reverse=True)[:30]:
    listkey.append(key)
    listval.append(val)
    print(key, val, u' ',end=' ')

df = pd.DataFrame(listval, columns=[u'次数'])
df.index = listkey
df.plot(kind='bar')
plt.title(u'关于龙族一中动词的词频统计')
plt.show()
