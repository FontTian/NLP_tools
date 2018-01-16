# - * - coding: utf - 8 -*-
# 作者：田丰(FontTian)
# 创建时间:'2017/8/16'

import nltk
import jieba
from ftools import cnlp
from os import path

d = path.dirname(__file__)

import re
from nltk.corpus import words

# 输入法联想提示（9宫格输入法）
# 查找类似于hole和golf序列（4653）的单词。
wordlist = [w for w in words.words('en-basic') if w.islower()]
same = [w for w in wordlist if re.search(r'^[ghi][mno][jlk][def]$',w)]
print(same)

# 手指绕口令 ^[ghijklmno]+$ ?
# [^aeiouAEIOU]就是匹配除元音外的所有字母。

# 寻找字符块
# 查找两个或两个以上的元音序列，并且确定相对频率。
wsj = sorted(set(nltk.corpus.treebank.words()))
fd = nltk.FreqDist(vs for word in wsj for vs in re.findall(r'[aeiou]{2,}',word))
print(fd.items())

# 查找词干
# apples和apple对比中，apple就是词干。写一个简单脚本来查询词干。

def stem(word):
    for suffix in ['ing','ly','ed','ious','ies','ive','es','s','ment']:
        if word.endswith(suffix):
            return word[:-len(suffix)]
    return None

# 而使用正则表达式，只需要一行：
word_str = ' '.join(wordlist)
stem = stem(word_str)
stem_re = re.findall(r'^(.*?)(ing|ly|ed|ious|ies|ive|es|s|ment)$',word_str)

print(stem)
print(stem_re)