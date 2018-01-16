# - * - coding: utf - 8 -*-
#
# 作者：田丰(FontTian)
# 创建时间:'2017/7/28'
# 邮箱：fonttian@Gmaill.com
# CSDN：http://blog.csdn.net/fontthrone
# github: https://github.com/FontTian
import jieba
# jieba.load_userdict("txt\userdict.txt")
# 添加用户词库为主词典,原词典变为非主词典
from wordcloud import WordCloud, ImageColorGenerator
from scipy.misc import imread
import matplotlib.pyplot as plt


class basis():
    def __init__(self, textPath, stopwordsPath, load_userdict=False, ReadText=False):
        self.__TextPath = textPath
        self.__stopwordsPath = stopwordsPath
        self.__userWords = []
        if load_userdict != False:
            jieba.load_userdict(load_userdict)
        if ReadText != False:
            self.ReadText()

    def ReadText(self, NewTextPath=False):
        if NewTextPath == False:
            self.__text = open(self.__TextPath, encoding='utf8').read().replace('\n', '').replace(' ', '')
        else:
            self.__text = open(NewTextPath, encoding='utf8').read().replace('\n', '').replace(' ', '')

    def addUserWords(self, NewWordsList):
        for i in NewWordsList:
            self.__userWords.append(i)

    def jiebaCutText(self):

        for i in self.__userWords:
            jieba.add_word(i)

        seg_list = list(jieba.cut(self.__text, cut_all=False))

        self.__seg_list = []
        for i in seg_list:
            if i.isspace() == False:
                self.__seg_list.append(i)

        return ' '.join(self.__seg_list)

    def clearText(self, NewStopWordsPath=None):

        if NewStopWordsPath:
            self.__stopwordsPath = NewStopWordsPath

        mywordlist = []
        f_stop = open(self.__stopwordsPath, encoding='utf8')

        try:
            f_stop_text = f_stop.read()
        finally:
            f_stop.close()
        f_stop_seg_list = f_stop_text.split('\n')

        for myword in self.__seg_list:
            if not (myword.strip() in f_stop_seg_list) and len(myword.strip()) > 1:
                mywordlist.append(myword)

        return ' '.join(mywordlist)

    def getText(self):

        self.ReadText()
        self.jiebaCutText()
        clearText = self.clearText()

        return clearText

    def jiebaCutWithPos(self, isClearText=False):

        from jieba import posseg
        if isClearText == False:
            self.__strWithPos = list(posseg.cut(self.__text))
        else:
            self.__strWithPos = list(posseg.cut(self.clearText()))

        return self.__strWithPos

    def wordcloud(self,
                  text=None, image_path=None, to_file_path=None, show=None,
                  font_path=None, width=400, height=200, margin=2,
                  ranks_only=None, prefer_horizontal=.9, mask=None, scale=1,
                  color_func=None, max_words=200, min_font_size=4,
                  stopwords=None, random_state=None, background_color='black',
                  max_font_size=None, font_step=1, mode="RGB",
                  relative_scaling=.5, regexp=None, collocations=True,
                  colormap=None, normalize_plurals=True):
        if text:
            text = text
        else:
            text = self.getText()

        wc = WordCloud(font_path=font_path, width=width, height=height, margin=margin,
                       ranks_only=ranks_only, prefer_horizontal=prefer_horizontal, mask=mask, scale=scale,
                       color_func=color_func, max_words=max_words, min_font_size=min_font_size,
                       stopwords=stopwords, random_state=random_state, background_color=background_color,
                       max_font_size=max_font_size, font_step=font_step, mode=mode,
                       relative_scaling=relative_scaling, regexp=regexp, collocations=collocations,
                       colormap=colormap, normalize_plurals=normalize_plurals).generate(text)

        if show:
            if image_path:
                img_background_color = ImageColorGenerator(imread(image_path))
                plt.imshow(wc.recolor(color_func=img_background_color), interpolation="bilinear")
            else:
                plt.imshow(wc, interpolation="bilinear")

            plt.axis("off")
            plt.show()

        if to_file_path:
            wc.to_file(to_file_path)
