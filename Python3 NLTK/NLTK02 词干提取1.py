# - * - coding: utf - 8 -*-
# 作者：田丰(FontTian)
# 创建时间:'2017/8/16'

import nltk
import jieba
from ftools import cnlp

# nltk提供了PorterStemmer 和 LancasterStemmer两个词干提取器，Porter比较好，可以处理lying这样的单词。

porter = nltk.PorterStemmer()
print(porter.stem('lying'))
# lie

Lanc = nltk.LancasterStemmer()
print(Lanc.stem('lying'))
# lying

# 如果需要处理women这样的词，需要词性归并器：WordNetLemmatizer
wnl = nltk.WordNetLemmatizer()
print(wnl.lemmatize("women"))
# woman

# 利用词干提取器实现索引文本(concordance)
# 利用到nltk.Index这个函数，nltk.Index((word , i) for (i,word) in enumerate(['a','b','a']))

class IndexText:
    def __init__(self,stemmer,text):
        self._text = text
        self._stemmer = stemmer
        self._index = nltk.Index((self._stem(word),i) for (i,word) in enumerate(text))
    def _stem(self,word):
        return self._stemmer.stem(word).lower()
    def concordance(self,word,width =40):
        key = self._stem(word)
        wc = width/4 #words of context
        for i in self._index[key]:
            lcontext = ' '.join(self._text[int(i-wc):int(i)])
            rcontext = ' '.join(self._text[int(i):int(i+wc)])
            ldisplay = '%*s' % (width,lcontext[-width:])
            rdisplay = '%-*s' % (width,rcontext[:width])
            print(ldisplay,rdisplay)
porter = nltk.PorterStemmer()
grail = nltk.corpus.webtext.words('/home/fonttian/PycharmProjects/ML/Python3 NLTK/txt/AliceEN.txt')
text = IndexText(porter,grail)
text.concordance('lie')
'''
 eye fell on a little glass box that was lying under the table : she opened it , 
      ! It was as much as she could do , lying down on one side , to look through
ut again , and the little golden key was lying on the glass table as before , ` a
m for this , and she tried the effect of lying down with one elbow against the do
rather doubtful whether she ought not to lie down on her face like the three gard
 ,' thought she , ` if people had all to lie down upon their faces , so that they
pointing to the three gardeners who were lying round the rosetree ; for , you see
 rosetree ; for , you see , as they were lying on their faces , and the pattern o
d . They very soon came upon a Gryphon , lying fast asleep in the sun . ( IF you 
ied to beat them off , and found herself lying on the bank , with her head in the
'''