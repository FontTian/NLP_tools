# - * - coding: utf - 8 -*-
#
# 作者：田丰(FontTian)
# 创建时间:'2017/7/4'
# 邮箱：fonttian@Gmaill.com
# CSDN：http://blog.csdn.net/fontthrone
import sys
import jieba
from nlpir import *
import nltk

reload(sys)
sys.setdefaultencoding('utf-8')

AddUserWord('创新')


def ShowList(List):
    print '********* show ', str(List), ' end *********'
    for item in List:
        print item.encode('utf-8')
    print '********* show ', str(List), ' end *********'


def cutstring(txt):
    # 分词
    cutstr = jieba.cut(txt)
    result = " ".join(cutstr)
    return result


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


txtfileobject = open('txt/lz.txt', 'r')

try:
    filestr = txtfileobject.read()
finally:
    txtfileobject.close()


# 使用NLPIR2016 进行分词
def ChineseWordsSegmentationByNLPIR2016(text):
    txt = seg(text)
    seg_list = []

    for t in txt:
        seg_list.append(t[0].encode('utf-8'))
        # print t[0]
    return seg_list


stopwords_path = 'stopwords/CNENstopwords.txt'  # 停用词词表


# 去除停用词
def ClearStopWordsWithListByNLPIR2016(seg_list):
    mywordlist = []
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


# print filestr
# cutstr = seg(filestr2)

# cutstr=cutstring(filestr.replace(' ',''))
cutAndclearStr = jiebaclearText(filestr)

# 使用NLPIR进行分词,但是会有很多编码问题
# filestr2 = ClearStopWordsWithListByNLPIR2016(ChineseWordsSegmentationByNLPIR2016(filestr)).encode('utf-8')
# tokenstr = nltk.word_tokenize(filestr2)
tokenstr = nltk.word_tokenize(cutAndclearStr)

# ShowList(tokenstr)

# ShowList(filestr2)
# print filestr2
# print cutstr
