# - * - coding: utf - 8 -*-
#
# 作者：田丰(FontTian)
# 创建时间:'2017/5/23'
# 邮箱：fonttian@163.com
# CSDN：http://blog.csdn.net/fontthrone

from os import path
from nlpir import *
from scipy.misc import imread
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
from ctypes import *
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

d = path.dirname(__file__)
# 添加用户自定义词语
AddUserWord('龙族')
AddUserWord('路明非')
AddUserWord('大和炮')
AddUserWord('竞技类')
DelUsrWord('竞技类')

# Init()
# SaveTheUsrDic('路明非')

text_path = 'txt/lztest.txt'  # 设置要分析的文本路径
stopwords_path = 'stopwords\stopwords1893.txt'  # 停用词词表
text = open(path.join(d, text_path)).read()
txt = seg(text)
kw_list = []
seg_list = []


# 获得新词,第二个参数控制新词的个数,排名按照TF-IDF（term frequency–inverse document frequency排序
# 该功能可以和AddUserWord()方法配合使用,以更好地获取分词效果

# print strs1
# print type(strs1)
# 富山雅史/n_new/28.45#白王血裔/n_new/19.83#秘仪咒文/n_new/19.19#风纪委员会主席/n_new/15.30#龙族/n_new/14.48#龙类/n_new/13.79#龙族血裔/n_new/13.78#龙族血统/n_new/13.19#执行部/n_new/12.74#白王/n_new/12.68#炼金/n_new/11.75#
# <type 'str'>

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


strs1 = getNewWordsByNLPIR(text, 10)
for i in strs1:
    print i

# 获得新词,第二个参数控制新词的个数,排名按照TF-IDF（term frequency–inverse document frequency)排序
# 该功能可以和AddUserWord()方法配合使用,以更好地获取分词效果
# strs1 = GetNewWords(text,c_int(10),[c_char_p, c_int, c_bool])
# print strs1
# 获得新词(从txt文件中),第二个参数控制新词的个数,排名按照TF-IDF（term frequency–inverse document frequency)排序
# strs10 = GetFileNewWords(text,c_int(10),[c_char_p, c_int, c_bool])
# print strs10
# WindowsError: exception: access violation reading 0x0000000000000000
# 获得关键词,第二个参数控制新词的个数,排名按照TF-IDF（term frequency–inverse document frequency)排序
# strs2= GetKeyWords(text,c_int(10),[c_char_p, c_int, c_bool])
# print strs2

for t in txt:
    seg_list.append(t[0].encode('utf-8'))
    # seg_list += ' '


# 使用NLPIR进行中文分词
# print seg_list
# for j in seg_list:
#     print j

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


# 去除完停用词的文本
strs = NLPIRclearText(seg_list)
# print s

# s = '''文案 文案
# The  抱抱 Zen of LOVE 抱抱 Python, 快乐 by Tim Peters
# 公众号 公众号 Python 最好的 语言 语言
# 一辈子 is better LOVE than 一辈子.
# 喵小姐 is 爱你 than  implicit.爱你 喵小姐
# 蟹先生 is 爱你 than complex.
# 一辈子 is 蟹先生  than complicated.
# 二中 is 喵小姐 我想你了 than nested. 二中 蟹先生
# 清湖 is 胜于 than 清湖.
# 思旺 counts. 想你
# Special 喵小姐 我想你了 aren't special enough 思旺 break 思旺 rules.
# 别生气 practicality beats 厨艺好.
# Errors should 我想你了 never pass 小龙虾 silently. 运营
# 别生气 explicitly 好不好. LOVE
# In the face of ambiguity, 程序员 the 厨艺好 to guess.龙华 龙华
# There 快乐 should be one-- 我想你了 and preferably 红烧肉 only one 小龙虾--obvious way to do it.运营
# Although 共享单车 way may not 我想你了 be obvious at first unless you're Dutch. 新媒体 地铁
# Now is better 红烧肉 than never.
# 程序员 Although 共享单车 is often 高铁 than 东莞 now. 高铁 地铁
# If the implementation 想你 is hard to explain, it's a bad idea. 想你了
# If 成都 implementation is 想你 easy to explain, it may be a good idea.
# Namespaces are 端午one 端午 honking great idea -- 成都 do more of those! 想你了
# 深圳 晚安 深圳 新媒体
# '''
font_path = r'C:\Windows\Fonts\simfang.ttf'  # 为worldcloud设置中文字体路径没

# 设置词云属性
wc = WordCloud(font_path=font_path,  # 设置字体
               background_color="white",  # 背景颜色
               max_words=200,  # 词云显示的最大词数
               max_font_size=100,  # 字体最大值
               random_state=42,
               width=1000, height=860, margin=2,  # 设置图片默认的大小,但是如果使用背景图片的话,那么保存的图片大小将会
               )

# 因为NLPIR在处理中文时,会自动修改文本编码,所以在使用worldcloud时需要修改文本编码
# 否则会造成:无法在wordcloud中显示NLPIR分词后的汉语词语,而只能显示其中的英文


wc.generate(unicode(strs, encoding='utf8'))

plt.imshow(wc)
plt.axis("off")
plt.show()

wc.to_file('test001.png')
