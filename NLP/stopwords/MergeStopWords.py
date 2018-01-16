# - * - coding: utf - 8 -*-
#
# 作者：田丰(FontTian)
# 创建时间:'2017/7/4'
# 邮箱：fonttian@Gmaill.com
# CSDN：http://blog.csdn.net/fontthrone
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


# 获取停用词的List
def GetListOfStopWords(filepath):
    f_stop = open(filepath)
    try:
        f_stop_text = f_stop.read()
        f_stop_text = unicode(f_stop_text, 'utf-8')
    finally:
        f_stop.close()
    f_stop_seg_list = f_stop_text.split('\n')

    return f_stop_seg_list


# 保存List
def SaveFile(list, filename):
    f_stop = open(filename, 'w')
    for item in range(len(list)):
        if item != len(list):
            f_stop.writelines((list[item].encode('utf-8')) + '\n')
        else:
            f_stop.writelines(list[item].encode('utf-8'))
    f_stop.close()


# 求List并集
def GetListUnion(listName):
    ListUnion = ['!']
    for item in listName:
        # print item
        ListUnion.extend(GetListOfStopWords(item))
    return list(set(ListUnion))


def GetStopWords(listOfFileName, FileName='CNstopwords.txt', keynumber=1):
    stopwords_pathCN = 'CNstopwords.txt'  # 默认中文总表 1
    stopwords_pathEN = 'ENstopwords.txt'  # 默认英文总表 2
    stopwords_pathCNEN = 'CNENstopwords.txt'  # 默认中英文混合总表 4
    if keynumber == 1:
        listOfFileName.append(stopwords_pathCN)
    elif keynumber == 2:
        listOfFileName.append(stopwords_pathEN)
    elif keynumber == 3:
        listOfFileName.append(stopwords_pathCN)
        listOfFileName.append(stopwords_pathEN)
    elif keynumber == 5:
        listOfFileName.append(stopwords_pathCN)
        listOfFileName.append(stopwords_pathCNEN)
    elif keynumber == 6:
        listOfFileName.append(stopwords_pathEN)
        listOfFileName.append(stopwords_pathCNEN)
    elif keynumber == 7:
        listOfFileName.append(stopwords_pathCN)
        listOfFileName.append(stopwords_pathEN)
        listOfFileName.append(stopwords_pathCNEN)
    else:
        listOfFileName.append(stopwords_pathCN)
        print 'The keynumber is wrong,chage keynumber to 1 '

        listOfFileName.append(stopwords_pathCNEN)
    ListUnion = GetListUnion(listOfFileName)
    SaveFile(ListUnion, FileName)


'''
stopwords_pathCN = 'CNstopwords.txt' # 默认中文总表 1
stopwords_pathEN = 'CNstopwords.txt' # 默认英文总表 2
stopwords_pathCNEN = 'CNstopwords.txt' # 默认中英文混合总表 4
'''

listOfFileName = []

# 需要添加的 中文 停用词词表
stopwords_path1 = 'stopwords1893.txt'
stopwords_path2 = 'stopwords1229.txt'
stopwords_path3 = 'stopwordshagongdakuozhan.txt'
stopwords_path4 = 'stop_words_zh.txt'

# 需要添加的 英文 停用词词表
stopwords_path5 = 'stop_words_eng.txt'
stopwords_path6 = 'ENstopwords891.txt'

# 需要添加的 中文 停用词词表路径
# listOfFileName.append(stopwords_path1)
# listOfFileName.append(stopwords_path2)
# listOfFileName.append(stopwords_path3)
# listOfFileName.append(stopwords_path4)

# 需要添加的 英文 停用词词表路径
listOfFileName.append(stopwords_path5)
listOfFileName.append(stopwords_path6)

GetStopWords(listOfFileName, FileName='ENstopwords.txt', keynumber=2)
