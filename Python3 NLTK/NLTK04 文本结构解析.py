# - * - coding: utf - 8 -*-
# 作者：田丰(FontTian)
# 创建时间:'2017/8/16'

import nltk
from ftools import cnlp
from os import path

d = path.dirname(__file__)


# 1. 基于规则的文本解析器
print('\n****** 基于规则的解析器 ******')
# toy CFG

grammar = nltk.CFG.fromstring("""
  S -> NP VP
  VP -> V NP | V NP PP
  PP -> P NP
  V -> "saw" | "ate" | "walked"
  NP -> "John" | "Mary" | "Bob" | Det N | Det N PP
  Det -> "a" | "an" | "the" | "my"
  N -> "man" | "dog" | "cat" | "telescope" | "park"
  P -> "in" | "on" | "by" | "with"
  """)
sent = 'Mary saw Bob'.split()
rd_parser = nltk.RecursiveDescentParser(grammar)
print('\nCFG解析器:')
for i in rd_parser.parse(sent):
    print(i)

# Regex parser
# 正则表达式解析器

from nltk.chunk.regexp import *

chunk_rules = ChunkRule("<.*>+", "chunk everything")
reg_parser = RegexpParser('''
 		NP: {<DT>? <JJ>* <NN>*}
  		 P: {<IN>}
             V: {<V.*>}          
  	      PP: {<P> <NP>} 
   	      VP: {<V> <NP|PP>*}
  ''')

test_sent = "Mr. Obama played a big role in the Health insurance bill"
test_sent_pos = nltk.pos_tag(nltk.word_tokenize(test_sent))
paresed_out = reg_parser.parse(test_sent_pos)
print('\n正则表达式解析器:')
print(paresed_out)

# 语块分解
print('\n语块分解')
# Chunking 

from nltk.chunk.regexp import *
test_sent="I love my country, and I will strive for the happiness of all mankind.I am a human companion at all times."

test_sent_pos=nltk.pos_tag(nltk.word_tokenize(test_sent))
rule_vp = ChunkRule(r'(<VB.*>)?(<VB.*>)+(<PRP>)?', 'Chunk VPs')
parser_vp = RegexpChunkParser([rule_vp],chunk_label='VP')
print('\nparser_vp.parse(test_sent_pos) :')
print(parser_vp.parse(test_sent_pos))
rule_np = ChunkRule(r'(<DT>?<RB>?)?<JJ|CD>*(<JJ|CD><,>)*(<NN.*>)+', 'Chunk NPs')
parser_np = RegexpChunkParser([rule_np],chunk_label="NP")
print('\nparser_np.parse(test_sent_pos) :')
print(parser_np.parse(test_sent_pos))

test_sent1='我 爱 我 的 祖国 , 我 也 愿 为 全人类 的 幸福 而 奋斗终生 。' # 上面的方法无法对中文使用
'''
parser_vp.parse(test_sent_pos) :
(S
  我/JJ
  爱/NNP
  我/NNP
  的/NNP
  祖国/NNP
  ,/,
  我/NNP
  也/NNP
  愿/NNP
  为/NNP
  全人类/NNP
  的/NNP
  幸福/NNP
  而/NNP
  奋斗终生/NNP
  。/NN)

parser_np.parse(test_sent_pos) :
(S
  (NP 我/JJ 爱/NNP 我/NNP 的/NNP 祖国/NNP)
  ,/,
  (NP
    我/NNP
    也/NNP
    愿/NNP
    为/NNP
    全人类/NNP
    的/NNP
    幸福/NNP
    而/NNP
    奋斗终生/NNP
    。/NN))

'''