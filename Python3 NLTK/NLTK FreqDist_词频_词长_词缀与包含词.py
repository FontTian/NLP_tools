# - * - coding: utf - 8 -*-
# 作者：田丰(FontTian)
# 创建时间:'2017/8/17'

from ftools import cnlp
import nltk
from os import path

import matplotlib as mpl

mpl.rcParams['font.sans-serif'] = ['Yahei Mono']
mpl.rcParams['font.serif'] = ['Yahei Mono']
# mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题,或者转换负号为字符串

d = path.dirname(__file__)

stopwords_path = u'/home/fonttian/Data/NLP/stopwords/CNENstopwords.txt'  # 停用词词表
text_path = u'/home/fonttian/Data/NLP/txt/lz.txt'  # 设置要分析的文本路径

fontsTools = cnlp.basis(textPath=text_path, stopwordsPath=stopwords_path, ReadText=True)
fontsTools.addUserWords([u'路明非'])

cutAndclearStr = fontsTools.getText()

print(u'nltk web本分析基本操作')

print(u'nltk.word_tokenize(cutAndclearStr')
print(u'nltk.FreqDist(tokenstr)')

tokenstr = nltk.word_tokenize(cutAndclearStr)

print(u'词总数', len(tokenstr))
print(u'词语出现个数', len(set(tokenstr)))
print(u'词语平均使用个数(浮点数)', float(len(tokenstr)) / float(len(set(tokenstr))))
fdist1 = nltk.FreqDist(tokenstr)
print("统计李嘉图出现的次数",fdist1[u'李嘉图'])
print(u'样本总数', fdist1.N())
print(u'样本最大值', fdist1.max())
print(u'FreqDist.B 词语出现个数', fdist1.B())
print(u'FreqDist.freq 样本频率', fdist1.freq(u'路明非'))
print(u'FreqDist.Nr 依次返回词频出现次数', fdist1.r_Nr())
print(u'FreqDist.pprint(: print(a string representation of this FreqDist to "stream"', fdist1.pprint())
print(u'FreqDist.pformat Return a string representation of this FreqDist.', fdist1.pformat())

print(u'FreqDist.pformat(maxlen=10) maxlen : 返回的字符串中的单词数量,默认为10', fdist1.pprint(maxlen=10))

print(u'')

# for item in list(fdist1.r_Nr()):
#     print(item
print(len(list(fdist1.r_Nr())))
print(u'所有单词出现的次数 fdist1.values()', fdist1.values())

print()
print(u"词汇条目排序表")
for word in sorted(set(tokenstr)):
    print(word, end=' ')
print()

print(u'====== 绘图与制表 ======')
# os.system('pause')
# 绘图
# 前10个高频词的累积频率分布图
print(u'前10个高频词的累积频率分布图')
fdist1.plot(10, cumulative=True)
# print('降序词频曲线图'
# fdist1.plot()
print(u'降序词频表')
fdist1.tabulate()

# os.system(u'pause')

print(u'=============== 词频统计 并 排序 ===============')
for key, val in sorted(fdist1.items()):
    print(key, val, u"||", end=' ')
print()
# print(type(fdist1)
# <class 'nltk.probability.FreqDist'>

print(u'=============== 出现了三次及以上次数的词语,并排序 ===============')
# for key,val in sorted(fdist1.items(),key = lambda  x:(x[1],x[0]),reverse=True)[:7]:
#     print(key,val
for key, val in sorted(fdist1.items(), key=lambda x: (x[1], x[0]), reverse=True):
    if val >= 3:
        print(key, val, u"||", end=' ')
print()

print(u'查询路明非出现的次数', fdist1[u'路明非'])
# print(cutAndclearStr

print(u'====== 出现了一次的低频词= =====')
for word in fdist1.hapaxes():
    print(word, u"||", end=' ')
print()

print(u'====== 长度大于三的长词 ======')
for word in [w for w in set(tokenstr) if len(w) > 5]:
    print(word, fdist1[word], u"||", end=' ')
print()

print(u'====== 长度大于三 且出现次数大于2 的长词 ======')
for word in [w for w in set(tokenstr) if len(w) > 3 and fdist1[w] > 2]:
    print(word, fdist1[word], u"||", end=' ')
print()

print(u'====== 词缀包含词分析 ======')

# 以词频递减顺序访问所有以“神”开头的词
print(u"以词频递减顺序访问所有以“神”开头的词")
mywords = [w for w in fdist1.keys() if w.startswith(u"神")]
for word in mywords:
    print(word, u"||", end=' ')

# 以词频递减顺序访问所有以“学”结尾的词
print()
print(u"以词频递减顺序访问所有以“学”结尾的词")
mywords = [w for w in fdist1.keys() if w.endswith(u"学")]
for word in mywords:
    print(word, u"||", end=' ')

# 以词频递减顺序访问所有包含“美国”的搭配词
print()
print(u"以词频递减顺序访问所有包含“美国”的搭配词 use nltk.bigrams(tokenstr)")