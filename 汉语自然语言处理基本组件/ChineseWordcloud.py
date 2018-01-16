# - * - coding: utf - 8 -*-
#
# 作者：田丰(FontTian)
# 创建时间:'2017/5/23'
# 邮箱：fonttian@163.com
# CSDN：http://blog.csdn.net/fontthrone
from os import path
from scipy.misc import imread
import matplotlib.pyplot as plt
import jieba
from nlpir import *
from ctypes import *
# jieba.load_userdict("txt\userdict.txt")
# 添加用户词库为主词典,原词典变为非主词典
# ImportUserDict('userdic.txt')
# 为NLPIR2016 添加用户词典
from wordcloud import WordCloud, ImageColorGenerator
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

# 获取当前文件路径
# __file__ 为当前文件, 在ide中运行此行会报错,可改为
# d = path.dirname('.')
d = path.dirname(__file__)

stopwords = {}
isCN = 1  # 默认启用中文分词
isJieba = 1  # 默认使用NLPIR2016进行分词 = 0
isGetNewWords = 1  # 默认使用NLPIR获取新词
number = 20  # 在使用NLPIR 时候默认自动获取的新词
back_coloring_path = "img/lz1.jpg"  # 设置背景图片路径
text_path = 'txt/lztest.txt'  # 设置要分析的文本路径
font_path = 'D:\Fonts\simkai.ttf'  # 为worldcloud设置中文字体路径没
stopwords_path = 'stopwords\stopwords1893.txt'  # 停用词词表
imgname1 = "WordCloudDefautColors.png"  # 保存的图片名字1(只按照背景图片形状)
imgname2 = "WordCloudColorsByImg.png"  # 保存的图片名字2(颜色按照背景图片颜色布局生成)

my_words_list = [u'路明非']  # 在结巴的词库中添加新词

back_coloring = imread(path.join(d, back_coloring_path))  # 设置背景图片

# 设置词云属性
wc = WordCloud(font_path=font_path,  # 设置字体
               background_color="white",  # 背景颜色
               max_words=2000,  # 词云显示的最大词数
               mask=back_coloring,  # 设置背景图片
               max_font_size=100,  # 字体最大值
               random_state=42,
               width=1000, height=860, margin=2,  # 设置图片默认的大小,但是如果使用背景图片的话,那么保存的图片大小将会
               )


# 使用NLPIR 自动发现新词
def add_word(text, number):
    strs1 = getNewWordsByNLPIR(text, number)
    if isJieba == 0:
        if isGetNewWords == 1:
            for i in strs1:
                AddUserWord(i)
        for i in my_words_list:
            AddUserWord(i)
    else:
        if isGetNewWords == 1:
            for i in strs1:
                jieba.add_word(i)
        for i in my_words_list:
            jieba.add_word(i)


text = open(path.join(d, text_path)).read()


# 使用 jieba 清理停用词
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


#  使用NLPIR2016 进行分词
def useNLPIR2016(text):
    txt = seg(text)
    seg_list = []

    for t in txt:
        seg_list.append(t[0].encode('utf-8'))

    return seg_list


# 去除停用词
def NLPIRclearText(seg_list):
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


# 如果使用中文分词的话
if isCN == 1:
    add_word(text, number)
    if isJieba == 0:
        seg_list = useNLPIR2016(text)
        text = NLPIRclearText(seg_list)
        text = unicode(text, encoding='utf8')
    else:
        text = jiebaclearText(text)

# 生成词云, 可以用generate输入全部文本(wordcloud对中文分词支持不好,建议启用中文分词),也可以我们计算好词频后使用generate_from_frequencies函数
wc.generate(text)
print text
# wc.generate_from_frequencies(txt_freq)
# txt_freq例子为[('词a', 100),('词b', 90),('词c', 80)]
# 从背景图片生成颜色值
image_colors = ImageColorGenerator(back_coloring)

plt.figure()
# 以下代码显示图片
plt.imshow(wc)
plt.axis("off")
plt.show()
# 绘制词云

# 保存图片
wc.to_file(path.join(d, imgname1))

image_colors = ImageColorGenerator(back_coloring)

plt.imshow(wc.recolor(color_func=image_colors))
plt.axis("off")
# 绘制背景图片为颜色的图片
plt.figure()
plt.imshow(back_coloring, cmap=plt.cm.gray)
plt.axis("off")
plt.show()
# 保存图片
wc.to_file(path.join(d, imgname2))
