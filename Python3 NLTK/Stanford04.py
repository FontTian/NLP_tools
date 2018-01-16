#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:fonttian
@file: Stanford04.py
@time: 2017/09/26
"""

from nltk.tag.stanford import StanfordPOSTagger
st = StanfordPOSTagger('/home/fonttian/NLP/stanford-postagger-full-2015-12-09/models/chinese-distsim.tagger',"/home/fonttian/NLP/stanford-postagger-full-2015-12-09/stanford-postagger-3.6.0.jar")

print(st)