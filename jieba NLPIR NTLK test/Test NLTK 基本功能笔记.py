# - * - coding: utf - 8 -*-
#
# 作者：田丰(FontTian)
# 创建时间:'2017/7/3'
# 邮箱：fonttian@Gmaill.com
# CSDN：http://blog.csdn.net/fontthrone
import jieba
jieba.add_word(u'路明非')
import nltk
from os import path
import os
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


import matplotlib as mpl


d = path.dirname(__file__)

stopwords_path = u'stopwords/CNENstopwords.txt'  # 停用词词表

numNewWords = 50

text_path = u'txt/lz.txt'  # 设置要分析的文本路径
font_path = u'D:/Fonts/simkai.ttf'  # 中文字体路径没
txtfileobject = open(text_path, 'r')

try:
    filestr = txtfileobject.read()
finally:
    txtfileobject.close()


def ShowByItem(List):
    print u'********* show ', str(List), u' end *********'
    for item in List:
        print item.encode(u'utf-8'),
    print
    print u'********* show ', str(List), u' end *********'


def jiebaclearText(text):
    mywordlist = []
    seg_list = jieba.cut(text, cut_all=False)
    liststr = u"/ ".join(seg_list)
    f_stop = open(stopwords_path)
    try:
        f_stop_text = f_stop.read()
        f_stop_text = unicode(f_stop_text, u'utf-8')
    finally:
        f_stop.close()
    f_stop_seg_list = f_stop_text.split(u'/n')
    for myword in liststr.split(u'/'):
        if not (myword.strip() in f_stop_seg_list) and len(myword.strip()) > 1:
            mywordlist.append(myword)
    return u''.join(mywordlist)


def cutstring(txt):
    # 分词
    cutstr = jieba.cut(txt)
    result = u" ".join(cutstr)
    return result


cutAndclearStr = jiebaclearText(filestr)

os.system(u'nltk web本分析基本操作')
print u'nltk.word_tokenize(cutAndclearStr'
print u'nltk.FreqDist(tokenstr)'

tokenstr = nltk.word_tokenize(cutAndclearStr)

print u'词总数', len(tokenstr)
print u'词语出现个数', len(set(tokenstr))
print u'词语平均使用个数(浮点数)', float(len(tokenstr)) / float(len(set(tokenstr)))
fdist1 = nltk.FreqDist(tokenstr)
print u'样本总数', fdist1.N()
print u'样本最大值', fdist1.max()
print u'FreqDist.B 词语出现个数', fdist1.B()
print u'FreqDist.freq 样本频率', fdist1.freq(u'路明非')
print u'FreqDist.Nr 依次返回词频出现次数', fdist1.r_Nr()
print u'FreqDist.pprint : Print a string representation of this FreqDist to "stream"', fdist1.pprint()
print u'FreqDist.pformat Return a string representation of this FreqDist.', fdist1.pformat()

print u'FreqDist.pformat(maxlen=10) maxlen : 返回的字符串中的单词数量,默认为10', fdist1.pprint(maxlen=10)
# FreqDist.pprint : Print a string representation of this FreqDist to "stream"FreqDist({u'/u8def/u660e/u975e': 700, u'/u6559/u6388': 270, u'/u82ac/u683c/u5c14': 156, u'/u53e4/u5fb7/u91cc/u5b89': 153, u'/u8bfa/u8bfa': 144, u'/u5b66/u751f': 126, u'/u5b66/u9662': 117, u'/u53f6/u80dc': 114, u'/u50cf/u662f': 106, u'/u58f0/u97f3': 97, ...})
#  None
# FreqDist.pformat Return a string representation of this FreqDist. FreqDist({u'/u8def/u660e/u975e': 700, u'/u6559/u6388': 270, u'/u82ac/u683c/u5c14': 156, u'/u53e4/u5fb7/u91cc/u5b89': 153, u'/u8bfa/u8bfa': 144, u'/u5b66/u751f': 126, u'/u5b66/u9662': 117, u'/u53f6/u80dc': 114, u'/u50cf/u662f': 106, u'/u58f0/u97f3': 97, ...})
# FreqDist.pformat(maxlen=10) FreqDist({u'/u8def/u660e/u975e': 700, ...})
#  None

print u''
# FreqDist.Nr  defaultdict(<type 'int'>, {0: 0, 1: 5214, 2: 1334, 3: 645, 4: 357, 5: 239, 6: 145, 7: 105, 8: 68, 9: 60, 10: 50, 11: 39, 12: 28, 13: 24, 270: 1, 15: 21, 16: 14, 17: 16, 18: 10, 19: 8, 20: 13, 21: 10, 22: 7, 153: 1, 24: 5, 25: 5, 26: 4, 27: 6, 28: 4, 29: 3, 30: 2, 31: 5, 32: 2, 33: 1, 35: 1, 36: 1, 37: 1, 38: 1, 39: 1, 40: 1, 156: 1, 42: 1, 43: 3, 44: 2, 46: 1, 48: 1, 50: 1, 51: 1, 52: 1, 53: 1, 54: 1, 55: 1, 23: 9, 57: 1, 58: 1, 60: 1, 62: 2, 75: 2, 84: 1, 14: 22, 144: 1, 97: 1, 700: 1, 106: 1, 114: 1, 117: 1, 41: 1, 126: 1, 85: 1})

# Create a copy of this frequency distribution.
# fdist1.copy()


# for item in list(fdist1.r_Nr()):
#     print item
print len(list(fdist1.r_Nr()))
print u'所有单词出现的次数 fdist1.values()', fdist1.values()

print
print u"词汇条目排序表"
for word in sorted(set(tokenstr)):
    print word,
print

'''
 # 默认的集合操作
 # Mathematical operatiors

    def __add__(self, other):
        """
        Add counts from two counters.

        >>> FreqDist('abbb') + FreqDist('bcc')
        FreqDist({'b': 4, 'c': 2, 'a': 1})

        """
        return self.__class__(super(FreqDist, self).__add__(other))

    def __sub__(self, other):
        """
        Subtract count, but keep only results with positive counts.

        >>> FreqDist('abbbc') - FreqDist('bccd')
        FreqDist({'b': 2, 'a': 1})

        """
        return self.__class__(super(FreqDist, self).__sub__(other))

    def __or__(self, other):
        """
        Union is the maximum of value in either of the input counters.

        >>> FreqDist('abbb') | FreqDist('bcc')
        FreqDist({'b': 3, 'c': 2, 'a': 1})

        """
        return self.__class__(super(FreqDist, self).__or__(other))

    def __and__(self, other):
        """
        Intersection is the minimum of corresponding counts.

        >>> FreqDist('abbb') & FreqDist('bcc')
        FreqDist({'b': 1})

        """
        return self.__class__(super(FreqDist, self).__and__(other))

    def __le__(self, other):
        if not isinstance(other, FreqDist):
            raise_unorderable_types("<=", self, other)
        return set(self).issubset(other) and all(self[key] <= other[key] for key in self)

    # @total_ordering doesn't work here, since the class inherits from a builtin class
    __ge__ = lambda self, other: not self <= other or self == other
    __lt__ = lambda self, other: self <= other and not self == other
    __gt__ = lambda self, other: not self <= other
'''

print u'====== 绘图与制表 ======'
os.system('pause')
# 绘图
# 前10个高频词的累积频率分布图
print u'前10个高频词的累积频率分布图'
fdist1.plot(10, cumulative=True)
# print '降序词频曲线图'
# fdist1.plot()
print u'降序词频表'
fdist1.tabulate()

os.system(u'pause')

print u'=============== 词频统计 并 排序 ==============='
for key, val in sorted(fdist1.iteritems()):
    print key, val, u"||",
print
# print type(fdist1)
# <class 'nltk.probability.FreqDist'>

print u'=============== 出现了三次及以上次数的词语,并排序 ==============='
# for key,val in sorted(fdist1.iteritems(),key = lambda  x:(x[1],x[0]),reverse=True)[:7]:
#     print key,val
for key, val in sorted(fdist1.iteritems(), key=lambda x: (x[1], x[0]), reverse=True):
    if val >= 3:
        print key, val, u"||",
print

print u'查询路明非出现的次数', fdist1[u'路明非']
# print cutAndclearStr

print u'====== 出现了一次的低频词= ====='
for word in fdist1.hapaxes():
    print word, u"||",
print

print u'====== 长度大于三的长词 ======'
for word in [w for w in set(tokenstr) if len(w) > 5]:
    print word, fdist1[word], u"||",
print

print u'====== 长度大于三 且出现次数大于2 的长词 ======'
for word in [w for w in set(tokenstr) if len(w) > 3 and fdist1[w] > 2]:
    print word, fdist1[word], u"||",
print

print u'====== 词缀包含词分析 ======'
os.system(u'pause')

# 以词频递减顺序访问所有以“神”开头的词
print u"以词频递减顺序访问所有以“神”开头的词"
mywords = [w for w in fdist1.keys() if w.startswith(u"神")]
for word in mywords:
    print word, u"||",

# 以词频递减顺序访问所有以“学”结尾的词
print
print u"以词频递减顺序访问所有以“学”结尾的词"
mywords = [w for w in fdist1.keys() if w.endswith(u"学")]
for word in mywords:
    print word, u"||",

# 以词频递减顺序访问所有包含“美国”的搭配词
print
print u"以词频递减顺序访问所有包含“美国”的搭配词 use nltk.bigrams(tokenstr)"
bigramwords = nltk.bigrams(tokenstr)
mywords = [w for w in set(bigramwords) if u"美国" in w]
for fw, sw in mywords:
    print fw, u" ", sw, u"|",
print

os.system(u'pause')
print u'====== 其他基本指标并绘图 ======'

print u'下面是nltk的其他类 '
print u'nltk.collocations.BigramCollocationFinder.from_words(tokenstr)'
print u'nltk.collocations.BigramCollocationFinder.from_words(tokenstr).word_fd'
os.system(u'pause')

bigramcolloc = nltk.collocations.BigramCollocationFinder.from_words(tokenstr)
print u"----出现最频繁的前10个词-----"
fdist1 = bigramcolloc.word_fd
for key, val in sorted(fdist1.iteritems(), key=lambda x: (x[1], x[0]), reverse=True)[:10]:
    print key, u":", val, u"||",
print

print u"----只出现1次的低频词-----"
fdist1 = bigramcolloc.word_fd
for w in fdist1.hapaxes():
    print w.encode(u"utf-8"), u"||",
print

# 找出文本中的搭配词
print u'找出文本中的搭配词'
print u'nltk.bigrams(tokenstr)'
print u'nltk.collocations.TrigramCollocationFinder.from_words(tokenstr)'
os.system(u'pause')
bigramwords = nltk.bigrams(tokenstr)

print u'====== 双连搭配词 ======'
for fw, sw in set(bigramwords):
    print fw, u' ', sw, u"||",
print

print u'====== 双连搭配词 及 词频 ======'
for w, c in sorted(bigramcolloc.ngram_fd.iteritems(), key=lambda x: (x[1], x[0]), reverse=True)[:100]:
    fw, sw = w
    print fw, u' ', sw, u'=>', c, u"||",
print
print u"----双连搭配词以及词频-----"
for w, c in sorted(bigramcolloc.ngram_fd.iteritems(), key=lambda x: (x[1], x[0]), reverse=True)[:100]:
    fw, sw = w
    print fw, u" ", sw, u"=>", c, u"||",
print

trigramcolloc = nltk.collocations.TrigramCollocationFinder.from_words(tokenstr)
print u"----三连搭配词-----"
for fw, sw, tw in trigramcolloc.ngram_fd:
    print fw.encode(u"utf-8"), u" ", sw.encode(u"utf-8"), u" ", tw.encode(u"utf-8"), u"|",
print

# strs1 = getNewWordsByNLPIR(filestr, 50)
# ShowByItem(strs1)
