# - * - coding: utf - 8 -*-
# 作者：田丰(FontTian)
# 创建时间:'2017/8/17'

import nltk
import jieba
from ftools import cnlp
from os import path

d = path.dirname(__file__)

from nltk.corpus import names
import random

labeled_names = ([(name, 'male') for name in names.words('male.txt')] +
                 [(name, 'female') for name in names.words('female.txt')])


# 获取单词特征 last_letter
def gender_features(word):
    return {'last_letter': word[-1]}


# 打乱数据集
random.shuffle(labeled_names)

# train test
featuresets = [(gender_features(n), gender) for (n, gender) in labeled_names]
train_set, test_set = featuresets[500:], featuresets[:500]

# train start
classifier = nltk.NaiveBayesClassifier.train(train_set)


class Classifier():
    def __init__(self):
        pass

    def get_Result(self, name, classsify_name=None):
        if classsify_name:
            result = classsify_name.classify(gender_features(name))
        else:
            result = classifier.classify(gender_features(name))
        print(result)
        return result


class1 = Classifier()
class1.get_Result(name='Neo')
class1.get_Result(name='Trinity')

# accuracy and Most Informative Features
print("\n accuracy and Most Informative Features :")
print(nltk.classify.accuracy(classifier, test_set))
classifier.show_most_informative_features(5)

'''
在处理大型语料库时，构建一个包含每一个实例的特征的单独的列表会使用大量的内存。在这些情况下，使用函数nltk.classify.apply_features，返回一个行为像一个列表而不会在内存存储所有特征集的对象：

from nltk.classify import apply_features
train_set = apply_features(gender_features, labeled_names[500:])
test_set = apply_features(gender_features, labeled_names[:500])
'''


def gender_features1(name):
    features = {}
    features["first_letter"] = name[0].lower()
    features["last_letter"] = name[-1].lower()
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        features["count({})".format(letter)] = name.lower().count(letter)
        features["has({})".format(letter)] = (letter in name.lower())
    return features


print("\n利用第二个特征构建器,获取John和FontThrone的特征 :")
print(gender_features1('John'))
print(gender_features1('FontThrone'))

featuresets1 = [(gender_features1(n), gender) for (n, gender) in labeled_names]
train_set1, test_set1 = featuresets1[500:], featuresets1[:500]
classifier = nltk.NaiveBayesClassifier.train(train_set1)

print("accuracy:", nltk.classify.accuracy(classifier, test_set1))

# 特征的选取
print("特征的选取")

# 一旦初始特征集被选定，完善特征集的一个非常有成效的方法是错误分析。首先，我们选择一个开发集，包含用于创建模型的语料数据。然后将这种开发集分为训练集和开发测试集。
train_names2 = labeled_names[1500:]
devtest_names2 = labeled_names[500:1500]
test_names2 = labeled_names[:500]

# 已经将语料分为适当的数据集，我们使用训练集训练一个模型，然后在开发测试集上运行.
train_set2 = [(gender_features(n), gender) for (n, gender) in train_names2]
devtest_set2 = [(gender_features(n), gender) for (n, gender) in devtest_names2]
test_set2 = [(gender_features(n), gender) for (n, gender) in test_names2]
classifier2 = nltk.NaiveBayesClassifier.train(train_set2)

print("accuracy 特征工程 :", nltk.classify.accuracy(classifier2, devtest_set2))

# 使用开发测试集，我们可以生成一个分类器预测名字性别时的错误列表：
errors = []
for (name, tag) in devtest_names2:
    guess = classifier.classify(gender_features(name))
    if guess != tag:
        errors.append((tag, guess, name))


# 然后，可以检查个别错误案例，在那里该模型预测了错误的标签，尝试确定什么额外信息将使其能够作出正确的决定（或者现有的哪部分信息导致其做出错误的决定）。
# 然后可以相应的调整特征集。
# 我们已经建立的名字分类器在开发测试语料上产生约100个错误：

# for (tag, guess, name) in sorted(errors):
#     print('correct={:<8} guess={:<8s} name={:<30}'.format(tag, guess, name))
# 然后我们就可以通过观察分类错误的数据的特点来调整我们的特征构造器

def gender_features2(word):
    return {'suffix1': word[-1:],
            'suffix2': word[-2:]}


train_set3 = [(gender_features2(n), gender) for (n, gender) in train_names2]
devtest_set3 = [(gender_features2(n), gender) for (n, gender) in devtest_names2]
classifier3 = nltk.NaiveBayesClassifier.train(train_set3)
print("accuracy 三号特征构建器 :",nltk.classify.accuracy(classifier3, devtest_set3))
print("在同样的数据集的情况下,三号特征构建器的accuracy普遍高于二号构建器")