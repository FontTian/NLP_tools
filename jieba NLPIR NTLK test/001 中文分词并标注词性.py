# - * - coding: utf - 8 -*-
#
# 作者：田丰(FontTian)
# 创建时间:'2017/7/3'
# 邮箱：fonttian@Gmaill.com
# CSDN：http://blog.csdn.net/fontthrone

import nltk
import sys
import nlpir

sys.path.append("../")

reload(sys)
sys.setdefaultencoding('utf-8')

import jieba
from jieba import posseg


def cutstrpos(txt):
    # 分词+词性
    cutstr = posseg.cut(txt)
    result = ""
    for word, flag in cutstr:
        result += word + "/" + flag + ' '
    print type(cutstr)
    return result


def cutstring(txt):
    # 分词
    cutstr = jieba.cut(txt)
    result = " ".join(cutstr)
    return result


# 读取文件
txtfileobject = open('txt/nltest1.txt')
textstr = ""
try:
    filestr = txtfileobject.read()
finally:
    txtfileobject.close()


# 使用NLPIR2016 进行分词
def ChineseWordsSegmentationByNLPIR2016(text):
    txt = nlpir.seg(text)
    seg_list = []

    for t in txt:
        seg_list.append(t[0].encode('utf-8'))

    return seg_list


stopwords_path = 'stopwords\stopwords1893.txt'  # 停用词词表


# 去除停用词
def ClearStopWordsWithListByNLPIR2016(seg_list):
    mywordlist = []
    liststr = "/ ".join(seg_list)
    f_stop = open(stopwords_path)
    try:
        f_stop_text = f_stop.read()
        f_stop_text = unicode(f_stop_text, 'utf-8')
    finally:
        f_stop.close()
    f_stop_seg_list = f_stop_text.split('\n')
    for myword in liststr.split('/'):
        if not (myword.strip() in f_stop_seg_list) and len(myword.strip()) > 1:
            mywordlist.append(myword)
    return ''.join(mywordlist)


# print filestr
filestr2 = ClearStopWordsWithListByNLPIR2016(ChineseWordsSegmentationByNLPIR2016(filestr)).replace(' ', '')

# 中文分词并标注词性
posstr = cutstrpos(filestr2)

print type(posstr)

# print filestr

print '**** show is end ****'

print ' '
print 'This is posster'
print posstr

strtag = [nltk.tag.str2tuple(word) for word in posstr.split()]
# for item in strtag:
#     print item
strsBySeg = nlpir.seg(filestr)
strsBySeg2 = nlpir.seg(filestr2)
strsByParagraphProcess = nlpir.ParagraphProcess(filestr, 1)
strsByParagraphProcessA = nlpir.ParagraphProcessA(filestr, ChineseWordsSegmentationByNLPIR2016(filestr)[0], 1)

print ' '
print ' '
print '**** strtag ****'

for word, tag in strtag:
    print word, "/", tag, "|",

print ' '
print ' '
print '**** strsBySeg ****'
for word, tag in strsBySeg:
    print word, "/", tag, "|",

print ' '
print ' '
print '**** strsBySeg2 ****'
for word, tag in strsBySeg2:
    print word, "/", tag, "|",

print ' '
print ' '
print '**** strsByParagraphProcess ****'
print strsByParagraphProcess

print type(strsByParagraphProcess)
print type(strsBySeg2)

# print ' '
# print ' '
# print '**** strsByParagraphProcessA ****'
#
# for item in strsByParagraphProcessA:
#     print item,

print ' '
print ' '
print '**** show is end ****'


'''
国外 / S | 媒体报道 / N | 美国 / NS | 科学家 / N | 近日 / T | 2800 / M | 万美元 / M | 约合 / VN | 1.84 / M | 亿 / M | 人民币 / N | 研究 / VN | 经费 / VN | 用于 / V | 设计 / VN | 款 / M | 人类 / N | 识别 / V | 图形 / N | 速度 / N | 相媲美 / Z | 计算机系统 / N | 情报机构 / N | 数据 / N | 越来越 / D | 数据分析 / L | 人类 / N | 难 / A | 工作 / VN | 速度 / N | 计算机 / N | 学习 / V | 能力 / N | 有限 / A | 哈佛大学 / NT | 研究 / VN | 团队 / N | 正 / D | 着手 / V | 解决 / V | 希望 / V | 弄清 / V | 大脑 / N | 活动 / VN | 过程 / N | 赋予 / V | 人类 / N | 识别 / V | 图形 / N | 出色 / V | 能力 / N | 终极目标 / N | 研发 / J | 仿生 / V | 计算机系统 / N | 制造 / V | 聪明 / A | 人工智能 / N | 系统 / N | 人类 / N | 天生 / N | 擅长 / V | 识别 / V | 图案 / N | 东西 / NS | 次 / Q | 见到 / V | 认出 / V | 计算机 / N | 训练 / VN | 上 / F | 千次 / M | 难 / A | 培养能力 / N | 受 / V | 人类 / N | 大脑 / N | 启发 / V | 研发 / J | 出 / V | 智能 / N | 计算机 / N | 察觉 / V | 网络 / N | 入侵 / V | 读取 / V | 核磁共振 / L | 图像 / N | 驾驶 / V | 汽车 / N | 哈佛大学 / NT | 工程 / N | 应用科学 / L | 学院 / N | SEAS / ENG | 称 / V | 弄清 / V | 人类 / N | 哺乳动物 / N | 一点 / M | 研究 / VN | 人员 / N | 记录 / N | 大脑 / N | 视觉 / N | 皮层 / N | 活动 / VN | 情况 / N | 创新 / V | 技术 / N | 之间 / F | 绘制 / N | 接 / V | 逆向 / N | 工程 / N | 数据 / N | 高智能 / NR | 计算机 / N | 算法 / N | 研发 / J | 中高级 / B | 情报研究 / N | 计划署 / N | IARPA / ENG | 资金 / N | 拨给 / V | 哈佛大学 / NT | 工程 / N | 应用科学 / L | 学院 / N | SEAS / ENG | 脑科学 / N | 中心 / N | CBS / ENG | 分子 / N | 细胞 / N | 生物学系 / N | 挑战 / VN | 规模 / N | 类似 / V | 人类 / N | 基因组 / N | 计划 / N | 项目 / N | 领导 / N | 分子 / N | 细胞 / N | 生物学系 / N | 计算机科学 / N | 系 / V | 助理 / VN | 教授 / N | 戴维 / NR | · / X | 考克斯 / NRT | DavidCox / ENG | 说道 / V | 记录 / N | 神经元 / NZ | 活动 / VN | 绘制 / N | 之间 / F | 项 / N | 工作 / VN | 科学 / N | 价值 / N | 项目 / N | 头 / N | 一半 / M | 弄清 / V | 大脑 / N | 学习 / V | 方法 / N | 准则 / N | 设计 / VN | 款 / M | 媲美 / V | 超越 / V | 人类 / N | 计算机系统 / N |  
据 / p | 国外 / s | 媒体 / n | 报道 / v | ， / wd | 美国 / nsf | 科学家 / n | 近日 / t | 获得 / v | 了 / ule | 2800万 / m | 美元 / q | （ / wkz | 约合 / nrf | 1.84亿 / m | 人民币 / n | ） / wky | 的 / ude1 | 研究 / vn | 经费 / n | ， / wd | 用于 / v | 设计 / v | 一 / m | 款 / q | 能 / v | 与 / p | 人类 / n | 识别 / vn | 图形 / n | 速度 / n | 相 / d | 媲美 / vi | 的 / ude1 | 计算机 / n | 系统 / n | 情报 / n | 机构 / n | 要 / v | 处理 / v | 的 / ude1 | 数据 / n | 越来越 / d | 多 / a | ， / wd | 这些 / rz | 数据 / n | 都 / d | 必须 / d | 进行 / vx | 迅速 / a | 分析 / vn | ， / wd | 但 / c | 问题 / n | 是 / vshi | ， / wd | 人类 / n | 很 / d | 难 / ad | 保持 / v | 这样 / rzv | 的 / ude1 | 工作 / vn | 速度 / n | ， / wd | 计算机 / n | 的 / ude1 | 学习 / vn | 能力 / n | 又 / d | 很 / d | 有限 / a | 。 / wj | 哈佛 / ns | 大学 / n | 的 / ude1 | 研究 / vn | 团队 / n | 如今 / t | 正 / d | 着手 / v | 解决 / v | 这 / rzv | 一 / m | 问题 / n | 。 / wj | 他们 / rr | 希望 / v | 能 / v | 弄清 / v | ， / wd | 是 / vshi | 怎样 / ryv | 的 / ude1 | 大脑 / n | 活动 / vn | 过程 / n | 赋予 / v | 了 / ule | 人类 / n | 识别 / vn | 图形 / n | 的 / ude1 | 出色 / a | 能力 / n | 。 / wj | 他们 / rr | 的 / ude1 | 终极 / n | 目标 / n | 是 / vshi | ， / wd | 研发 / v | 出 / vf | 仿生 / b | 计算机 / n | 系统 / n | ， / wd | 从而 / c | 制造 / v | 出 / vf | 更加 / d | 聪明 / a | 的 / ude1 | 人工智能 / n | 系统 / n | 。 / wj | 人类 / n | 天生 / d | 就 / d | 擅长 / v | 识别 / vn | 图案 / n | ， / wd | 一个 / mq | 东西 / n | 只 / d | 需要 / v | 看 / v | 几 / m | 次 / qv | ， / wd | 再次 / d | 见到 / v | 的 / ude1 | 时候 / n | 就 / d | 能 / v | 认出 / v | 来 / vf | 了 / y | 。 / wj | 计算机 / n | 则 / c | 不然 / c | ， / wd | 就算 / d | 训练 / v | 上千 / m | 次 / qv | ， / wd | 也 / d | 很 / d | 难 / ad | 培养 / v | 出 / vf | 这样 / rzv | 的 / ude1 | 能力 / n | 。 / wj | 受 / v | 人类 / n | 大脑 / n | 启发 / vn | 而 / cc | 研 / v | 发出 / v | 的 / ude1 | 智能 / n | 计算机 / n | 可以 / v | 用来 / v | 察觉 / v | 网络 / n | 入侵 / v | 、 / wn | 读取 / vn | 核磁共振 / n | 图像 / n | 、 / wn | 甚至 / d | 能 / v | 驾驶 / v | 汽车 / n | 。 / wj | 据 / p | 哈佛 / ns | 大学 / n | 工程 / n | 与 / cc | 应用科学 / nl | 学院 / n | （ / wkz | SEAS / x | ） / wky | 称 / v | ， / wd | 为了 / p | 弄清 / v | 为何 / ryv | 人类 / n | 和 / cc | 其它 / rz | 哺乳动物 / nl | 能够 / v | 做到 / v | 这 / rzv | 一点 / mq | ， / wd | 研究 / v | 人员 / n | 记录 / v | 了 / ule | 大脑 / n | 视觉 / n | 皮层 / n | 的 / ude1 | 活动 / vn | 情况 / n | ， / wd | 并 / cc | 使用 / v | 创 / vg | 新 / a | 技术 / n | 将 / p | 它们 / rr | 之间 / f | 的 / ude1 | 联系 / vn | 绘制 / v | 出 / vf | 来 / vf | 。 / wj | 接 / v | 下来 / vf | ， / wd | 他们 / rr | 再 / d | 使用 / v | 逆向 / b | 工程 / n | 处理 / v | 这些 / rz | 数据 / n | ， / wd | 并 / cc | 将 / p | 其 / rz | 运用 / v | 到 / v | 高 / a | 智能 / n | 计算机 / n | 算法 / n | 的 / ude1 | 研发 / v | 中 / f | 去 / vf | 。 / wj | 高级 / a | 情报 / n | 研究 / vn | 计划署 / n | （ / wkz | IARPA / x | ） / wky | 将 / p | 资金 / n | 拨给 / v | 了 / ule | 哈佛 / ns | 大学 / n | 工程 / n | 与 / cc | 应用科学 / nl | 学院 / n | （ / wkz | SEAS / x | ） / wky | 、 / wn | 脑 / n | 科学 / a | 中心 / n | （ / wkz | CBS / x | ） / wky | 、 / wn | 以及 / cc | 分子 / n | 与 / cc | 细胞 / n | 生物学 / n | 系 / v | 。 / wj | 这 / rzv | 是 / vshi | 一个 / mq | 巨大 / a | 的 / ude1 | 挑战 / vn | ， / wd | 它 / rr | 的 / ude1 | 规模 / n | 类似 / v | 于 / p | 人类 / n | 基因组 / n | 计划 / n | 。 / wj | 该 / rz | 项目 / n | 的 / ude1 | 领导 / n | 、 / wn | 分子 / n | 与 / cc | 细胞 / n | 生物学 / n | 系 / v | 和 / cc | 计算机 / n | 科学 / ad | 系 / v | 的 / ude1 | 助理 / n | 教授 / n | 戴维·考克斯 / nrf | （ / wkz | David / x | Cox / x | ） / wky | 说道 / v | ， / wd | 要 / v | 记录 / v | 这么 / rz | 多 / a | 神经元 / n | 的 / ude1 | 活动 / vn | 、 / wn | 并 / d | 绘制 / v | 出 / vf | 它们 / rr | 之间 / f | 的 / ude1 | 联系 / vn | ， / wd | 单 / d | 是 / vshi | 这 / rzv | 一 / m | 项 / q | 工作 / vn | 就 / d | 具有 / v | 巨大 / a | 的 / ude1 | 科学 / n | 价值 / n | ， / wd | 但 / c | 这 / rzv | 只 / d | 是 / vshi | 我们 / rr | 项目 / n | 的 / ude1 | 头 / n | 一半 / m | 而已 / y | 。 / wj | 等 / v | 我们 / rr | 弄清 / v | 了 / ule | 大脑 / n | 学习 / v | 方法 / n | 的 / ude1 | 基本 / a | 准则 / n | 之后 / f | ， / wd | 我们 / rr | 迟早 / d | 会 / v | 设计 / v | 出 / vf | 一 / m | 款 / q | 能够 / v | 媲美 / vi | 、 / wn | 甚至 / d | 超越 / v | 人类 / n | 的 / ude1 | 计算机 / n | 系统 / n | 。 / wj |  
国外 / s | 媒体 / n | 报道 / v | 美国 / nsf | 科学家 / n | 近日 / t | 2800万 / m | 美元 / q | 约 / d | 合 / v | 1.84亿 / m | 人民币 / n | 研究 / vn | 经费 / n | 用于 / v | 设计 / vn | 款 / n | 人类 / n | 识别 / vn | 图形 / n | 速度 / n | 相 / d | 媲美 / vi | 计算机 / n | 系统 / n | 情报 / n | 机构 / n | 数据 / n | 越来越 / d | 数据 / n | 分析 / vn | 人类 / n | 难 / a | 工作 / vn | 速度 / n | 计算机 / n | 学习 / v | 能力 / n | 有限 / a | 哈佛 / ns | 大学 / n | 研究 / vn | 团队 / n | 正 / d | 着手 / v | 解决 / v | 希望 / v | 弄清 / v | 大脑 / n | 活动 / vn | 过程 / n | 赋予 / v | 人类 / n | 识别 / vn | 图形 / n | 出色 / a | 能力 / n | 终极 / n | 目标 / n | 研发 / v | 仿生 / b | 计算机 / n | 系统 / ad | 制造 / v | 聪明 / a | 人工智能 / n | 系统 / n | 人类 / n | 天生 / d | 擅长 / v | 识别 / vn | 图案 / n | 东西 / n | 次 / qv | 见到 / v | 认出 / v | 计算机 / n | 训练 / v | 上千 / m | 次 / qv | 难 / ad | 培养 / v | 能力 / n | 受 / v | 人类 / n | 大脑 / n | 启发 / v | 研发 / v | 出 / vf | 智能 / n | 计算机 / n | 察觉 / v | 网络 / n | 入侵 / v | 读取 / v | 核磁共振 / n | 图像 / n | 驾驶 / vn | 汽车 / n | 哈佛 / ns | 大学 / n | 工程 / n | 应用科学 / nl | 学院 / n | SEAS / x | 称 / v | 弄清 / v | 人类 / n | 哺乳动物 / nl | 一点 / mq | 研究 / vn | 人员 / n | 记录 / v | 大脑 / n | 视觉 / n | 皮层 / n | 活动 / vn | 情况 / n | 创 / vg | 新 / a | 技术 / n | 之间 / f | 绘制 / v | 接 / v | 逆向 / b | 工程 / n | 数据 / n | 高 / a | 智能 / n | 计算机 / n | 算法 / n | 研发 / v | 中高级 / b | 情报 / n | 研究 / vn | 计划署 / n | IARPA / x | 资金 / n | 拨给 / v | 哈佛 / ns | 大学 / n | 工程 / n | 应用科学 / nl | 学院 / n | SEAS / x | 脑 / n | 科学 / a | 中心 / n | CBS / x | 分子 / n | 细胞 / n | 生物学 / n | 系 / v | 挑战 / vn | 规模 / n | 类似 / a | 人类 / n | 基因组 / n | 计划 / n | 项目 / n | 领导 / vn | 分子 / n | 细胞 / n | 生物学 / n | 系 / v | 计算机 / n | 科学 / ad | 系 / v | 助理 / n | 教授 / n | 戴维·考克斯 / nrf | DavidCox / x | 说道 / v | 记录 / v | 神经元 / n | 活动 / vn | 绘制 / v | 之间 / f | 项 / q | 工作 / vn | 科学 / n | 价值 / n | 项目 / n | 头 / m | 一半 / m | 弄清 / v | 大脑 / n | 学习 / v | 方法 / n | 准则 / n | 设计 / vn | 款 / n | 媲美 / vi | 超越 / v | 人类 / n | 计算机 / n | 系统 / n | 
'''
# 进入语料库
# cutstr = cutstring(filestr)
# print ''
# # print cutstr
# # 注意在 cutsr 的存储格式,格式如结尾注释所示
# mytext = nltk.text.Text(cutstr)
# # 在该语料库中查找包括“人”的语句
# print 'strat the last part'
# print "在该语料库中查找包括“人”的语句"
# # print(mytext.concordance(u"人"))
# for i  in mytext.concordance(u"人"):
#     print i,'end'
'''
国外 媒体报道 美国 科学家 近日 2800 万美元 约合 1.84 亿 人民币 研究 经费 用于 设计 款 人类 识别 图形 速度 相媲美 计算机系统 情报机构 数据 越来越 数据分析 人类 难 工作 速度 计算机 学习 能力 有限 哈佛大学 研究 团队 正 着手 解决 希望 弄清 大脑 活动 过程 赋予 人类 识别 图形 出色 能力 终极目标 研发 仿生 计算机系统 制造 聪明 人工智能 系统 人类 天生 擅长 识别 图案 东西 次 见到 认出 计算机 训练 上 千次 难 培养能力 受 人类 大脑 启发 研发 出 智能 计算机 察觉 网络 入侵 读取 核磁共振 图像 驾驶 汽车 哈佛大学 工程 应用科学 学院 SEAS 称 弄清 人类 哺乳动物 一点 研究 人员 记录 大脑 视觉 皮层 活动 情况 创新 技术 之间 绘制 接 逆向 工程 数据 高智能 计算机 算法 研发 中高级 情报研究 计划署 IARPA 资金 拨给 哈佛大学 工程 应用科学 学院 SEAS 脑科学 中心 CBS 分子 细胞 生物学系 挑战 规模 类似 人类 基因组 计划 项目 领导 分子 细胞 生物学系 计算机科学 系 助理 教授 戴维 · 考克斯 DavidCox 说道 记录 神经元 活动 绘制 之间 项 工作 科学 价值 项目 头 一半 弄清 大脑 学习 方法 准则 设计 款 媲美 超越 人类 计算机系统
strat the last part
在该语料库中查找包括“人”的语句
Displaying 11 of 11 matches:
 2 8 0 0   万 美 元   约 合   1 . 8 4   亿   人 民 币   研 究   经 费   用 于   设 计   款   人
   人 民 币   研 究   经 费   用 于   设 计   款   人 类   识 别   图 形   速 度   相 媲 美   计 算 机
 统   情 报 机 构   数 据   越 来 越   数 据 分 析   人 类   难   工 作   速 度   计 算 机   学 习   能
   希 望   弄 清   大 脑   活 动   过 程   赋 予   人 类   识 别   图 形   出 色   能 力   终 极 目 标
   研 发   仿 生   计 算 机 系 统   制 造   聪 明   人 工 智 能   系 统   人 类   天 生   擅 长   识 别
 算 机 系 统   制 造   聪 明   人 工 智 能   系 统   人 类   天 生   擅 长   识 别   图 案   东 西   次
 机   训 练   上   千 次   难   培 养 能 力   受   人 类   大 脑   启 发   研 发   出   智 能   计 算
   应 用 科 学   学 院   S E A S   称   弄 清   人 类   哺 乳 动 物   一 点   研 究   人 员   记 录
 称   弄 清   人 类   哺 乳 动 物   一 点   研 究   人 员   记 录   大 脑   视 觉   皮 层   活 动   情
 子   细 胞   生 物 学 系   挑 战   规 模   类 似   人 类   基 因 组   计 划   项 目   领 导   分 子  
 习   方 法   准 则   设 计   款   媲 美   超 越   人 类   计 算 机 系 统
None
'''
