# - * - coding: utf - 8 -*-
#
# 作者：田丰(FontTian)
# 创建时间:'2017/7/28'
# 邮箱：fonttian@Gmaill.com
# CSDN：http://blog.csdn.net/fontthrone
from os import path
from scipy.misc import imread
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import sys

import time

time1 = time.clock()
reload(sys)
sys.setdefaultencoding('utf-8')

import FontCN_NLPtools as fts

d = path.dirname(__file__)

text_path = 'txt/lztest.txt'  # 设置要分析的文本路径
stopwords_path = 'stopwords\CNENstopwords.txt'  # 停用词词表

fontsTools = fts.FontCN_NLPtools(textPath=text_path, stopwordsPath=stopwords_path)

fontsTools.addUserWords([u'路明非'])

text = fontsTools.getText(isAddWord=True)

list1 = fontsTools.jiebaCutWithPos()
list2 = fontsTools.NLPIRCutWithPos()
result=""
for word, flag in list1:
    result+=word+"/"+flag+' '
print result
print 'end'
result=""
for word, flag in list2:
    result+=word+"/"+flag+' '
print result
print 'end'

time2 = time.clock()
print time2-time1
x = input(u'按任意键以继续')
# 69.4755886028
# 71.0062005684
font_path = 'D:\Fonts\simkai.ttf'  # 为worldcloud设置中文字体路径没
back_coloring_path = "img/lz1.jpg"  # 设置背景图片路径

imgname1 = "WordCloudDefautColors.png"  # 保存的图片名字1(只按照背景图片形状)
imgname2 = "WordCloudColorsByImg.png"  # 保存的图片名字2(颜色按照背景图片颜色布局生成)
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

# 生成词云, 可以用generate输入全部文本(wordcloud对中文分词支持不好,建议启用中文分词),也可以我们计算好词频后使用generate_from_frequencies函数
wc.generate(text)
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
