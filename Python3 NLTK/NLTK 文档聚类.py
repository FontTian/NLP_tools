# - * - coding: utf - 8 -*-
# 作者：田丰(FontTian)
# 创建时间:'2017/8/17'

import nltk
import jieba
from ftools import cnlp
import numpy  as np
import time

datas = [np.array(v) for v in [(1,0),(0,1),(1,1),(5,5),(5,4),(4,5)]]


print('被分类的数据 :',datas)
print()

print("-------------混合高斯聚类--------------")

emc = nltk.cluster.em.EMClusterer(initial_means=[[4,2],[4,2.01]])
emc.cluster(vectors=datas)

time.sleep(3)
for data in datas:
    print(str(data),' : ',emc.classify(data))

#GAAC聚类
print("----------------GAAC聚类------------")
txtclassfier=nltk.cluster.gaac.GAAClusterer(num_clusters=5,normalise=True)
# GAAC的距离使用的是点积的结果，并不是余弦相似度，如果normalise设置为True，将相似度进行归一化，此时的距离为余弦相似度

txtclassfier.cluster(vectors=datas)

for data in datas:
    print(str(data),' : ',txtclassfier.classify(data))
print()
txtclassfier.dendrogram().show()
#kmeans聚类
print("-------------kmeans聚类--------------")
txtclassfier=nltk.cluster.kmeans.KMeansClusterer(num_means=5,distance=nltk.cluster.util.euclidean_distance)

txtclassfier.cluster(datas)

for data in datas:
    print(str(data),' : ',txtclassfier.classify(data))



