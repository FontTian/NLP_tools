#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:fonttian
@file: Stanford02.py
@time: 2017/09/25
"""

import sys
import os
from Stanford import StanfordPOSTagger


root = '/home/fonttian/NLP/stanford-corenlp/'
modelpath = root + "models/pos-tagger/chinese-distsim/chinese-distsim.tagger"
st = StanfordPOSTagger(root,modelpath)
seg_sent = '我 爱 我 的 祖国 ， 我 也 愿 为 全人类 的 幸福 而 奋斗终生 。 无论 什么 时刻 ， 我 都 是 人类 的 伙伴 。'
tag_list = st.tag(seg_sent)

print(tag_list)


