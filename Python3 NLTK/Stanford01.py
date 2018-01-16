# - * - coding: utf - 8 -*-
# 作者：田丰(FontTian)
# 创建时间:'2017/8/16'

import nltk
import jieba
from ftools import cnlp

# from nltk.tokenize.stanford_segmenter import StanfordSegmenter

# 3.2.4版本无法使用standford的2015版本,3.2.1可以
# from nltk.tokenize import StanfordTokenizer
# tokenizer = StanfordTokenizer(path_to_jar=r"E://StanfordNLTK/stanford-parser.jar")
# sent = "我爱我的祖国，我也愿为全人类的幸福而奋斗终生。无论什么时刻，我都是人类的伙伴。"
# print(tokenizer.tokenize(sent))

from nltk.tokenize.stanford_segmenter import StanfordSegmenter
# from nltk.parse.corenlp import *

# 3.2.4版本无法使用standford的2015版本,3.2.1可以

# CoreNLPServer(path_to_jar="/home/fonttian/NLP/stanford/")




# seg = StanfordSegmenter(path_to_slf4j='/home/fonttian/NLP/stanford-corenlp/slf4j-api.jar')
seg = StanfordSegmenter()
seg.default_config('zh')
sent = u'这是斯坦福中文分词器测试'
sent2 = u'我爱我的祖国,我也愿为全人类的幸福而奋斗终生 。'
print(seg.segment(sent))

# segmenter = StanfordSegmenter(
#     path_to_jar="D:/Anaconda3/envs/MLEnv/StanfordNLTK/stanford-segmenter.jar",
#     path_to_slf4j="D:/Anaconda3/envs/MLEnv/StanfordNLTK/slf4j-api.jar",
#     path_to_sihan_corpora_dict="D:/Anaconda3/envs/MLEnv/StanfordNLTK/data",
#     path_to_model="D:/Anaconda3/envs/MLEnv/StanfordNLTK/data/pku.gz",
#     path_to_dict="D:/Anaconda3/envs/MLEnv/StanfordNLTK/data/dict-chris6.ser.gz"
# )
# str = "我在博客园开了一个博客，我的博客名叫伏草惟存，写了一些自然语言处理的文章。"
# result = segmenter.segment(str)
# print(type(result))
# print(result)
