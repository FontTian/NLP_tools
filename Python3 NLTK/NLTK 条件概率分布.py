# - * - coding: utf - 8 -*-
# 作者：田丰(FontTian)
# 创建时间:'2017/8/16'

import nltk
import matplotlib.pylab as plot

# 函数接收list类型的参数后，会自动创建字典，生成对应的值为键值，而value就是元素的次数
tem = ['hello','world','hello','dear']
Fre = nltk.FreqDist(tem)
print(Fre.items())
Fre.tabulate()
Fre.plot(cumulative=True) # 累积频率
Fre.plot() # 数量


from nltk.corpus import brown
# 以一个配对链表作为输入，需要给分配的每个事件关联一个条件，输入时类似于 (条件,事件) 的元组。之后的工作交给nltk就可以了，更多的精力可以用来关注上层逻辑。
cfd = nltk.ConditionalFreqDist((genre,word) for genre in brown.categories() for word in brown.words(categories=genre))
print("conditions are:",cfd.conditions()) #查看conditions
print(cfd['news'])
print(cfd['news']['could'])#类似字典查询

'''
尤其对于plot() 和 tabulate() 有了更多参数选择： 
- conditions：指定条件 
- samples：迭代器类型，指定取值范围 
- cumulative：设置为True可以查看累积值
'''

cfd.tabulate(conditions=['news','romance'],samples=['could','can']) # 累积频率图
cfd.tabulate(conditions=['news','romance'],samples=['could','can'],cumulative=True) # # 频率图

