#--coding:utf-8--
#code by myhaspl 
#NLTK05 识别名词短语及语法树分析.py
from __future__ import unicode_literals
from __future__ import division
import nltk


import sys
sys.path.append("../")
import matplotlib as mpl

mpl.rcParams['font.sans-serif'] = ['Yahei Mono']
mpl.rcParams['font.serif'] = ['Yahei Mono']

from jieba import posseg


def cutstrpos(txt):
    #分词+词性
    cutstr = posseg.cut(txt)
    result=""
    for word, flag in cutstr:
        result+=word+"/"+flag+' '
    return result
    
sentencestr=[]
txtstr="""
据美国华盛顿自由灯塔网站2月17日报道，政府问责局16日发布的这份报告称，美国导弹防御局继续将大笔资金用于未被证明能够应对来自伊朗或朝鲜的弹道导弹袭击的技术。
根据这份报告，虽然美军领导人称当前的这个系统很可能能够抵御“来自于朝鲜和伊朗的小数量简单弹道导弹威胁”，但对该系统的实际测试并不支持这一说法。
在美国导弹防御局努力研发一个能发挥作用的导弹防御系统之际，伊朗和朝鲜正继续研发先进的弹道导弹技术，而国际社会对此并没有作出多大反应。
美国需要重新设计并重新测试其陆基中段防御系统的关键组成部分，以完成总统所提出的该防御系统到2017年底部署44枚拦截器的要求。负责监督的官员们称，这一目标不太可能实现。
这份报告称：“导弹防御局尚未通过飞行测试证明它能保护美国本土不受当前的导弹防御威胁。”报告还称，该局“尚未证明”陆基中段防御系统“能够保卫本土”，并且该局“可能在改进该系统方面面临挑战”。
根据这份报告，目前不可能对该系统的有效性作出全面评估。
报道称，虽然美国国防部按照要求定期提供有关该导弹系统进展的最新情况，但它未能解释该系统未来将如何得到改进。此外，导弹防御局未能证明该防御系统在拦截弹道导弹袭击方面能够完成它最为关键的任务。
根据报告中透露的数字，“数百亿美元”已经用于陆基中段防御系统，修复现有的缺陷还将需要再投入巨额资金。该系统目前的设计将必须得到彻底修改，以改进其功能。
另据俄罗斯《观点报》网站2月18日报道，美国国会下属的政府问责局日前在一份15页的报告中指出，美国反导系统无力保护本土免遭朝鲜或伊朗弹道导弹的打击。
塔斯社援引报告的内容称：“五角大楼经常介绍美国国防部导弹防御局在提高国家反导防御水平方面取得的成效。我们发现，该局遇到了一些风险和问题。国防部宣称，美国目前能够防御来自朝鲜和伊朗弹道导弹的有限打击。导弹防御局展现出了部分能力，但还有几个不可或缺的关键证据并没有提交。”
报告指出，导弹防御局耗费巨资研发反导系统，包括不断改进系统和“进行了8次拦截试验，其中4次是成功的”。但其他反导装备的测试结果无法证实美国能彻底防御弹道导弹的袭击。
报告称，导弹防御局在测试中无法证明它能保护美国躲避现有威胁。
报告起草者提醒说，运用尚未通过全部测试的反导系统增加了美国军人面临的风险，迫使他们不得不操作一个能力和缺陷都暂时无法彻底明确的系统。反导系统的最终建成还需要耗费数十亿美元，因为还需要进行大规模的更新。
"""

#生成nltk格式的词性单词集
posstr=cutstrpos(txtstr)
strtag=[nltk.tag.str2tuple(word) for word in posstr.split()]

#句子分割
sentstr=[]
for wtag in strtag:    
    if wtag[0].strip() in ["，","。","！","？","："]:
        sentencestr.append(sentstr)
        sentstr=[]
    else :
        if wtag[1]!="X":
           sentstr.append((wtag[0].strip(),wtag[1]))

#输出分割后的句子
for wordstr in sentencestr:
    print(' ')
    for word in wordstr:
        print(word[0],"/",word[1],end=' ')

#名词短语识别
grammar=r"""
NP:{(<A>|<R>|<MQ>)*<N>+<K>*}
NP:{(<A>|<R>|<MQ>)*<NS>+<K>*}
NP:{<M>+}
"""
cp=nltk.RegexpParser(grammar)
result1=cp.parse(sentencestr[0])
result1.draw()

result2=cp.parse(sentencestr[1])
result2.draw()


    







