# - * - coding: utf - 8 -*-
#
# 作者：田丰(FontTian)
# 创建时间:'2017/7/5'
# 邮箱：fonttian@Gmaill.com
# CSDN：http://blog.csdn.net/fontthrone
from __future__ import unicode_literals
from __future__ import division
import pylab
import sys
import jieba
from nlpir import *
import nltk
from os import path
import os

reload(sys)
sys.setdefaultencoding('utf-8')

pylab.mpl.rcParams['font.sans-serif'] = ['SimHei']

d = path.dirname(__file__)

stopwords_path = 'stopwords\CNENstopwords.txt'  # 停用词词表

my_words_list = ['路明非']  # 在结巴的词库中添加新词
numNewWords = 50

text_path = 'txt/lz.txt'  # 设置要分析的文本路径
font_path = 'D:\Fonts\simkai.ttf'  # 中文字体路径没
txtfileobject001 = open(text_path,'r')

try:
    filestr = txtfileobject001.read()
finally:
    txtfileobject001.close()


# 使用NLPIR 获取新词
def getNewWordsByNLPIR(text, number):
    txt1 = GetNewWords(text, c_int(number), [c_char_p, c_int, c_bool])
    txt2 = txt1.split('#')
    txt3 = []
    txt4 = []
    txt5 = []

    for item2 in txt2:
        txt3.append(item2.encode('utf-8').split('/'))
        if txt3 != []:
            txt4.append(txt3)
        txt3 = []
    for i in txt4:
        for j in i:
            if j[0] != [] and j[0] != '':
                txt5.append(j[0])

    return txt5


# 向jieba中添加新词
def add_word(text, number):
    strs1 = getNewWordsByNLPIR(text, number)
    for i in strs1:
        jieba.add_word(i)
    for i in my_words_list:
        jieba.add_word(i)

def ShowByItem(List):
    print '********* show ', str(List), ' end *********'
    for item in List:
        print item.encode('utf-8'),
    print
    print '********* show ', str(List), ' end *********'


def jiebaclearText(text):
    mywordlist = []
    seg_list = jieba.cut(text, cut_all=False)
    liststr = "/ ".join(seg_list)
    f_stop = open(stopwords_path)
    try:
        f_stop_text = f_stop.read()
        f_stop_text = unicode(f_stop_text, 'utf-8')
    finally:
        f_stop.close()
    f_stop_seg_list = f_stop_text.split('\n')
    for myword in liststr.split('/'):
        if not (myword.strip() in f_stop_seg_list) and len(myword.strip()) > 1:
            mywordlist.append(myword)
    return ''.join(mywordlist)

cutAndclearStr = jiebaclearText(filestr)

def cutstring(txt):
    # 分词
    cutstr = jieba.cut(txt)
    result = " ".join(cutstr)
    return result

samples = [('txt/nltest1.txt', u'科技'), ('txt/nltest2.txt', u'科技'), ('txt/nltest3.txt', u'财经'), ('txt/nltest4.txt', u'财经')]
samplewords = []
for (filename, categories) in samples:
    # 读取文件
    txtfileobject = open(filename, 'r')
    try:
        filestr = txtfileobject.read()
        add_word(filestr, 5)
    finally:
        txtfileobject.close()

    cutstr = jiebaclearText(filestr)
    tokenstr = nltk.word_tokenize(cutstr)

    mywords = [w for w in tokenstr]
    for word in mywords:
        samplewords.append((categories, word))
# 条件频率，每个词条在不同分类中出现的频率
print "------------------"
cfd = nltk.ConditionalFreqDist(samplewords)
fdist = cfd[u'财经']
for word in fdist:
    print word
print "---------流动性出现次数-----------"
print cfd[u'财经'][u'流动性']
print "----------条件:分类----------"
for cnd in cfd.conditions():
    print cnd
print "---------------------------"
# 频数最大的样本
print cfd[u'财经'].max()
print cfd[u'科技'].max()
# 条件频率分布
print "----------条件频率分布表----------"
cfd.tabulate(title=u'条件频率分布表', conditions=[u'科技', u'财经'])
cfd.plot(title=u'条件频率分布图', conditions=[u'科技', u'财经'])
