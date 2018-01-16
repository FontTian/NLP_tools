# - * - coding: utf - 8 -*-
# 作者：田丰(FontTian)
# 创建时间:'2017/8/15'
import nltk
import jieba
from ftools import cnlp
from os import path

d = path.dirname(__file__)

from nltk.stem import PorterStemmer  # import Porter stemmer

# 词干提取
from nltk.stem.lancaster import LancasterStemmer

pst = PorterStemmer()  # create obj of the PorterStemmer
lst = LancasterStemmer()  # create obj of LancasterStemmer
print(lst.stem("eating"))
print(pst.stem("shopping"))
'''
eat
shop
'''

# 词形还原(归并器)
from nltk.stem import WordNetLemmatizer

wlem = WordNetLemmatizer()
str = wlem.lemmatize("ate")
print(str)

# 停用词移除
# 英文版
from nltk.corpus import stopwords

stoplist = stopwords.words('english')  # 配置语言
en_text = 'This is just a words to test NLTK'
cleaner = [word for word in en_text.split() if word not in stoplist]

print(cleaner)

# 中文版本
stopwords_path = d + '/stopwords/CNENstopwords.txt'  # 停用词词表
text_path = d + '/txt/simple_test.txt'  # 设置要分析的文本路径
cnlp_basis = cnlp.basis(textPath=text_path, stopwordsPath=stopwords_path, ReadText=True)
cuter = cnlp_basis.jiebaCutText()
print(cuter)
cleaner1 = cnlp_basis.getText().split()

print(cleaner1)

# 拼写检查
from nltk.metrics import edit_distance
str1 = edit_distance("rain",'shine')
print(str1)
