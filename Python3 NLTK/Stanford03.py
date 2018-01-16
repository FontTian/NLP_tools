#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:fonttian
@file: Stanford03.py
@time: 2017/09/25
"""

from nltk.parse.stanford import *
import os
os.environ['CLASSPATH'] = "/home/fonttian/NLP/stanford-2015/*"

dep_parser=StanfordDependencyParser('/home/fonttian/NLP/stanford-2015/models/chinese-distsim.tagger',"/home/fonttian/NLP/stanford-2015/stanford-parser.jar")
dep_parser.raw_parse("自然语言处理的测试句子")

# dep_parser=StanfordDependencyParser('/home/fonttian/NLP/stanford/stanford-chinese-corenlp-2017-06-09-models/edu/stanford/nlp/models/lexparser/chinesePCFG.ser.gz',"/home/fonttian/NLP/stanford/stanford-chinese-corenlp-2017-06-09-models.jar")

# CoreNLPServer = CoreNLPServer(path_to_jar="/home/fonttian/NLP/stanford/")

# dep_parser=StanfordDependencyParser(model_path="/home/fonttian/NLP/stanford/stanford-chinese-corenlp-2017-06-09-models/edu/stanford/nlp/models/lexparser/chinesePCFG.ser.gz")
# GenericStanfordParser._MAIN_CLASS ="/home/fonttian/NLP/stanford-2015/stanford-parser-full/stanford-parser/edu/stanford/nlp/parser/lexparser/LexicalizedParser"

