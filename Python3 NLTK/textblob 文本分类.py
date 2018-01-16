# - * - coding: utf - 8 -*-
# 作者：田丰(FontTian)
# 创建时间:'2017/8/17'

#pip install textblob #需要安装
#python -m textblob.download_corpora #需要安装

from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob
import pickle

#训练数据
train = [
    ('ACACIA 骑行 服 套装 男 抓绒 长袖 山  车 秋冬 自行车 服  装备 骑行 裤 长裤', '服装'),
    ('自行车 行车 货架 货架 单车 货架 自行 自行车 行车 装备', '自行车配件'),
    ('acacia  骑行 裤 长裤  夏季 骑行 服饰 透气 防晒 自行车 裤  春秋 防风 裤', '服装'),
    ('ACACIA 自行车  LED 尾灯 骑行 警示灯 鞍座 灯 坐垫 灯  山  车 配件  尾灯', '自行车配件'),
    ('秋冬 加厚 打底 底裤 黑色 弹力 紧身 女裤 铅笔 裤子', '服装'),
    ('自行车 把 套 副 把  人体工学 把 套  羊角 把 套 套装  骑行 装备 山  车 配件', '自行车配件'),
    ("ACACIA 自行车  LED 尾灯 山  车 警示灯 骑行 车尾灯 自行车 装备 配件", '自行车配件'),
    ('acacia 山  车 挡泥板 山  自行车 挡泥板 挡雨板 快 拆 加长 全包 挡泥 配件', '自行车配件'),
    ('彩宝莉  春秋季 睡衣 女 长袖 长裤 针织 棉 可爱 卡通 pink 家居服 套装', '服装'),
    ("男士 保暖 裤加绒 秋冬 棉裤 男 绒裤 加厚 男士 打 底裤 冬 紧身 秋裤 单件 毛裤", '服装'),
    ('可外 穿  夏季 情侣 睡衣 女  格子裙  纯棉 短袖 家居服 套装 男士 全棉 夏款', '服装'),
    ('自行车 码表 磁头  扁 辐条 圆 辐条 磁头  码表  山  车 测速器 磁铁 强力', '自行车配件')
]

#测试用例
test = [
    ('新款 纯棉 夏季 短袖 睡衣 蕾丝 可爱 爱家 家居 家居服 套装', '服装'),
    ('ACACIA 自行车 多功能 组合 工具 山  车 修车 工具 骑行 带 截连器 修车 套装', '自行车配件'),
    ("屏幕 自行车 码表 夜光 防水 温度 骑行 码表 有线  骑行 装备", '自行车配件'),
    ("秋冬 加厚 打底 底裤 黑色 弹力 紧身 女裤 铅笔 裤子", '服装'),
    ('秋季 新款 打底 底裤 蕾丝 仿皮 铅笔 长裤 裤子', '服装'),
    ("自行 自行车 行车 条形 彩色 支架 防盗 防盗锁 电动 电动车 动车 锁具 钢丝 骑行 行装 装备", '自行车配件')
]

#训练
cl = NaiveBayesClassifier(train)

# 文本分类
print('文本分类 :')
print(cl.classify("屏幕 自行车 码表 夜光 防水 温度 骑行 码表 有线  骑行 装备"))  # "自行车配件"
print(cl.classify("男士 保暖 裤加绒 秋冬 棉裤 男 绒裤 加厚 男士 打 底裤 冬 紧身 秋裤 单件 毛裤"))   # "服装"
print('\n')

# 段落分类
blob = TextBlob("奶奶的 一大早 我的 自行车 坐垫 破了. 赶紧 叫 小明 穿上 他的 新款 打底裤. "
                "小明 骑上 他的 自行车 帮我买 自行车 坐垫.", classifier=cl)

print('段落分类:',blob.classify(),'\n')

for sentence in blob.sentences:
    print("句子 :",sentence) #段落中的句子
    print("类别 :",sentence.classify()) #句子分类
    print()

# 测试用例的精度
print("Accuracy: {0}".format(cl.accuracy(test)))
#
# 显示10条对比信息
print('显示10条对比信息')
cl.show_informative_features(10)


print('model')
#模型保存
f = open('model/Text_Classification/test.pickle', 'wb')
pickle.dump(cl, f)
f.close()

#加载模型
f = open('model/Text_Classification/test.pickle', 'rb')
model = pickle.load(f)
f.close()

#用加载的模型测试用例数据
print('利用加载的模型进行测试 :')

print(model.classify("屏幕 自行车 码表 夜光 防水 温度 骑行 码表 有线  骑行 装备"))  # "自行车配件"
print(model.classify("男士 保暖 裤加绒 秋冬 棉裤 男 绒裤 加厚 男士 打 底裤 冬 紧身 秋裤 单件 毛裤"))   # "服装"

print("Accuracy: {0}".format(model.accuracy(test)))
