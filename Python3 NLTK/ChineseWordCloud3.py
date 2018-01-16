# - * - coding: utf - 8 -*-
# 作者：田丰(FontTian)
# 创建时间:'2017/8/12'

from os import path
from scipy.misc import imread

from ftools import cnlp

d = path.dirname(__file__)

text_path = d + '/txt/lztest.txt'  # 设置要分析的文本路径
stopwords_path = d + '/stopwords/CNENstopwords.txt'  # 停用词词表

fontsTools = cnlp.basis(textPath=text_path, stopwordsPath=stopwords_path)
fontsTools.addUserWords([u'路明非'])

font_path = d + '/Fonts/simkai.ttf'  # 为worldcloud设置中文字体路径没
back_coloring_path = d + '/img/lz1.jpg'  # 设置背景图片路径

imgname1 = d +'/WordCloudDefautColors.png'  # 保存的图片名字1(只按照背景图片形状)
imgname2 = d + '/WordCloudColorsByImg.png'  # 保存的图片名字2(颜色按照背景图片颜色布局生成)
back_coloring = imread(path.join(d, back_coloring_path))  # 设置词云的形状

# 设置词云属性
wc = fontsTools.wordcloud(text=None, image_path=back_coloring_path, to_file_path=imgname2, show=True,
                          font_path=font_path,  # 设置字体
                          background_color='white',  # 背景颜色
                          max_words=2000,  # 词云显示的最大词数
                          mask=back_coloring,  # 设置词云形状
                          max_font_size=100,  # 字体最大值
                          random_state=42,
                          width=1000, height=860, margin=2,  # 设置图片默认的大小,但是如果使用背景图片的话,那么保存的图片大小将会
                          )
