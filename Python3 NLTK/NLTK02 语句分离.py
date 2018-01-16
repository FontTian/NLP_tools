#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:fonttian
@file: NLTK02 语句分离.py
@time: 2017/09/26
"""

inputstring = ' This is an example sent. The sentence splitter will split on sent markers. Ohh really !!'
from nltk.tokenize import sent_tokenize
all_sent=sent_tokenize(inputstring)
print(all_sent)
inputstring2 = ' 我爱我的祖国,我也愿为全人类的幸福而奋斗终生 。 我爱我的祖国,我也愿为全人类的幸福而奋斗终生 。'
inputstring3 = ' 我爱我的祖国,我也愿为全人类的幸福而奋斗终生 . 我爱我的祖国,我也愿为全人类的幸福而奋斗终生 。'

all_sent=sent_tokenize(inputstring2)
print(all_sent)
all_sent=sent_tokenize(inputstring3)
print(all_sent)
# [' This is an example sent', 'The sentence splitter will split on markers.','Ohh really !!']