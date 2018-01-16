# - * - coding: utf - 8 -*-
#
# 作者：田丰(FontTian)
# 创建时间:'2017/7/3'
# 邮箱：fonttian@Gmaill.com
# CSDN：http://blog.csdn.net/fontthrone
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

# 获取停用词的Set
def GetSetOfStopWords(filepath):
    f_stop = open(filepath)
    try:
        f_stop_text = f_stop.read()
        f_stop_text = unicode(f_stop_text, 'utf-8')
    finally:
        f_stop.close()
    f_stop_seg_list = f_stop_text.split('\n')

    return set(f_stop_seg_list)

# 保存Set
def SaveSet(set, filename):
    f_stop = open(filename, 'w')
    set = list(set)
    for item in range(len(set)):
        if item != len(set):
            f_stop.writelines((set[item].encode('utf-8')) + '\n')
        else:
            f_stop.writelines(set[item].encode('utf-8'))
    f_stop.close()


# 求Set并集
def GetSetUnion(list):
    listOfSet = []
    for item in list:
        print item
        listOfSet.append(GetSetOfStopWords(item))
    SetUnion = set('!')
    for item in listOfSet:
        SetUnion = SetUnion | item

    return SetUnion


def GetStopWords(listOfFileName, UnionTxT='CNstopwords.txt', FileName='CNstopwords.txt'):
    if UnionTxT.lower() == 'en':
        stopwords_path0 = 'ENstopwords.txt'
        listOfFileName.append(stopwords_path0)
        FileName = 'CNstopwords.txt'
    elif UnionTxT.lower() == 'none':
        stopwords_path0 = 'ENstopwords.txt'
        listOfFileName.append(stopwords_path0)
        FileName = 'CNstopwords.txt'
    else:
        stopwords_path0 = 'CNstopwords.txt'
        listOfFileName.append(stopwords_path0)

    SetUnion = GetSetUnion(listOfFileName)
    # ShowSet(SetUnion)

    SaveSet(SetUnion, FileName)


stopwords_path1 = 'stopwords1893.txt'  # 需要添加的停用词词表
stopwords_path2 = 'stopwords1229.txt'  # 需要添加的停用词词表
stopwords_path3 = 'stopwordshagongdakuozhan.txt'  # 需要添加的停用词词表

listOfFileName = []
listOfFileName.append(stopwords_path1)
listOfFileName.append(stopwords_path2)
listOfFileName.append(stopwords_path3)

GetStopWords(listOfFileName)