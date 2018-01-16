# - * - coding: utf - 8 -*-
#
# 作者：田丰(FontTian)
# 创建时间:'2017/7/28'
# 邮箱：fonttian@Gmaill.com
# CSDN：http://blog.csdn.net/fontthrone
from os import path
import jieba
import nlpir
from ctypes import *
# jieba.load_userdict("txt\userdict.txt")
# 添加用户词库为主词典,原词典变为非主词典
# ImportUserDict('userdic.txt')
# 为NLPIR2016 添加用户词典
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


class FontCN_NLPtools():
    def __init__(self, textPath, stopwordsPath):
        self.__TextPath = textPath
        self.d = path.dirname(__file__)
        self.__stopwordsPath = stopwordsPath
        self.__newWords = []
        self.__userWords = []

    def ReadText(self, NewTextPath=False):
        if NewTextPath == False:
            self.__text = open(path.join(self.d, self.__TextPath)).read().replace('\n','').replace(' ','')
        else:
            self.__text = open(path.join(self.d, NewTextPath)).read().replace('\n','').replace(' ','')

    def getNewWords(self, GetNewWordsNumber=20):
        txt1 = nlpir.GetNewWords(self.__text, c_int(GetNewWordsNumber), [c_char_p, c_int, c_bool])
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

        for i in txt5:
            self.__newWords.append(i)

        return self.__newWords

    def addUserWords(self, NewWordsList):
        for i in NewWordsList:
            self.__userWords.append(i)

    def jiebaCutText(self, isAddWord=False):

        if isAddWord == True:
            for i in self.__newWords:
                jieba.add_word(i)

        for i in self.__userWords:
            jieba.add_word(i)

        seg_list = list(jieba.cut(self.__text, cut_all=False))

        self.__seg_list = []
        for i in seg_list:
            if i.isspace() == False:
                self.__seg_list.append(i)

        return ' '.join(self.__seg_list)

    def clearText(self, NewStopWordsPath='no'):

        if NewStopWordsPath != 'no':
            self.__stopwordsPath = NewStopWordsPath

        mywordlist = []
        f_stop = open(self.__stopwordsPath)

        try:
            f_stop_text = f_stop.read()
            f_stop_text = unicode(f_stop_text, 'utf-8')
        finally:
            f_stop.close()
        f_stop_seg_list = f_stop_text.split('\n')

        for myword in self.__seg_list:
            if not (myword.strip() in f_stop_seg_list) and len(myword.strip()) > 1:
                mywordlist.append(myword)

        return ' '.join(mywordlist)

    def NLPIRCutText(self, isAddWord=False):

        if isAddWord == True:
            for i in self.__newWords:
                nlpir.AddUserWord(i)

        for i in self.__userWords:
            nlpir.AddUserWord(i)

        txt = nlpir.seg(self.__text)
        self.__seg_list = []

        for t in txt:
            self.__seg_list.append(t[0].encode('utf-8'))

        return ' '.join(self.__seg_list)

    def getText(self, isJieba=True, isAddWord=False, GetNewWordsNumber=20):

        self.ReadText()
        if isAddWord == True:
            self.getNewWords(GetNewWordsNumber)
        if isJieba == True:
            self.jiebaCutText(isAddWord=isAddWord)
        else:
            self.NLPIRCutText(isAddWord=isAddWord)

        clearText = self.clearText()
        return clearText

    def jiebaCutWithPos(self,isClearText = False):

        from jieba import posseg
        if isClearText == False:
            self.__strWithPos = list(posseg.cut(self.__text))
        else:
            self.__strWithPos = list(posseg.cut(self.clearText()))

        return self.__strWithPos

    def NLPIRCutWithPos(self,isClearText = False):

        if isClearText == False:
            self.__strWithPos = list(nlpir.seg(self.__text))
        else:
            self.__strWithPos = list(nlpir.seg(self.clearText()))

        return self.__strWithPos
