import re

with open('./game_short.txt', 'r') as f:
    comment = f.readline()
print(comment)

# 尝试将一行替换成多行
temp_comment = re.sub('==', '\n', comment)
print(temp_comment)

print(type(temp_comment))

print(re.split('==',comment)[0])

print(re.split('==',comment)[0].split("::"))


temp = re.split('==', comment)[0]
print(temp)
print(re.sub('\[\'allstar([0-9]{1,2})\'\]', r'*** \1 ***', comment))


# 分数
star = re.sub('\[\'.*?allstar([0-9]{1,2})\'\].*?==', r'\1,', comment)
print(star)
star_list = re.split(',', star)
star_list.pop()
print(star_list)

#评论
comment_list = []
comment_line = re.split(r'::', comment)
for line in comment_line:
    if (re.search('==', line)):
        comment_txt = re.split('==', line)[0]
        # 写入列表
        comment_list.append(re.sub('\[\'(.*)\'\]', r'\1', comment_txt))
print(comment_list)



#统计重复分值个数
from collections import Counter
result=Counter(star_list)
print(result)
result['50'] = 0

list=[]
for i in sorted(result):
    list.append(result[i])

print(list)

# 柱状图
from pyecharts.charts import Bar

from pyecharts.globals import CurrentConfig, NotebookType
CurrentConfig.NOTEBOOK_TYPE = NotebookType.JUPYTER_LAB
CurrentConfig.ONLINE_HOST

bar = Bar()
bar.add_xaxis(["0分", "10分", "20分", "30分", "40分", "50分"])
bar.add_yaxis("赛博朋克 2077", [result[i] for i in sorted(result)])
#bar.render("mycharts.html")
bar.load_javascript()
bar.render_notebook()

#饼图
from pyecharts.charts import Pie

attr = ["0分", "10分", "20分", "30分", "40分", "50分"]
values = [result[i] for i in sorted(result)]
pie = Pie()

pie.add("", [z for z in zip(attr, values)])
pie.render("mypie.html")

import jieba
my_comment='那个把绀碧大厦当成妓院的人，你玩过游戏吗？很可惜感觉不是我想要的赛博朋克'
#分词
seg_list=jieba.cut(my_comment)
print("/".join(seg_list))


#动态调整词典
jieba.add_word('赛博朋克')

seg_list=jieba.cut(my_comment)
print("//   ".join(seg_list))


import jieba.analyse

#增加停止词
jieba.analyse.set_stop_words('./stop_words.txt')
topK=10
result=','.join(comment_list)
tags=jieba.analyse.extract_tags(result,topK=topK,withWeight=True,allowPOS=('v','vn','n'))
#top10=",".join(tags)
print(tags)

from pyecharts import options as opts
from pyecharts.charts import WordCloud
from pyecharts.globals import  SymbolType


wordcloud=WordCloud()
wordcloud.add("",tags,word_size_range=[20,100],shape=SymbolType.DIAMOND)
wordcloud.render("myWordCoud.html")


