# - * - coding: utf - 8 -*-
#
# 作者：田丰(FontTian)
# 创建时间:'2017/7/3'
# 邮箱：fonttian@Gmaill.com
# CSDN：http://blog.csdn.net/fontthrone
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append("../")

import nltk
import FontCN_NLPtools as fts
# 解决乱码问题
import matplotlib as mpl

mpl.rcParams[u'font.sans-serif'] = [u'KaiTi']
mpl.rcParams[u'font.serif'] = [u'KaiTi']

# mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题,或者转换负号为字符串

text_path = 'txt/lztest.txt'  # 设置要分析的文本路径
stopwords_path = 'stopwords\CNENstopwords.txt'  # 停用词词表

fontsTools = fts.FontCN_NLPtools(textPath=text_path, stopwordsPath=stopwords_path)
fontsTools.addUserWords([u'路明非'])

tokenstr = nltk.word_tokenize(fontsTools.getText(isAddWord=True))
# 全文总词数

print u"词汇表 :",
for item in tokenstr:
    print item,

print

print u"词总数 :",
print len(tokenstr)
# 共出现多少词
print u"共出现词数 :",
print len(set(tokenstr))
# 词汇条目排序表
print u"词汇条目排序表 :"
for word in sorted(set(tokenstr)):
    print word,
print

# 每个词平均使用次数
print u"每个词平均使用次数:",
print float(len(tokenstr)) / float(len(set(tokenstr)))
# 统计词频
fdist1 = nltk.FreqDist(tokenstr)
for key, val in sorted(fdist1.iteritems()):
    print key, val,
print
print u".........路明非出现次数..............."
print fdist1[u'路明非']

print
print u".........李嘉图出现次数..............."
print fdist1[u'李嘉图']

# 统计出现最多的前5个词
print
print u".........统计出现最多的前10个词..............."
fdist1 = nltk.FreqDist(tokenstr)
for key, val in sorted(fdist1.iteritems(), key=lambda x: (x[1], x[0]), reverse=True)[:10]:
    print key, val

# 前10个高频词的累积频率分布图
print u'...............前10个高频词的累积频率分布图...............'
fdist1.plot(10, cumulative=True)
