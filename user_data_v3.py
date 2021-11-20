#程序设计目的，用户输入姓名、性别、出生年月日后，计算用户的年龄、生肖、星座、运势信息，并且把信息存储到txt、Excel文件中

#问题1：解决存入Excel文件内的内容会被覆盖掉
#问题2：每次程序的执行结果都会覆盖上次的执行结果，下个版本解决，user_data_v2.py

import os    #os即operating system（操作系统），Python 的 os 模块封装了常见的文件和目录操作
import datetime,time
import xlrd     #读取 Excel 文件
import xlwt     #写入 Excel 文件
from xlutils.copy import copy  #操作 Excel 文件的实用工具，如复制、分割、筛选等
import json


#定义变量十二生肖、星座，日期，赋值序列（字符串、元组、列表），= 把右边的值赋给左边
ChineseZodiac = "猴鸡狗猪鼠牛虎兔龙蛇马羊"    #字符串
TwelveConstellations = (u"摩羯座", u"水瓶座", u"双鱼座", u"白羊座", u"金牛座", u"双子座", u"巨蟹座", u"狮子座",
                        u"处女座", u"天秤座", u"天蝎座", u"射手座")  #列表，内容不可变更，适合存储一些不改变的值
Time = ((1, 20), (2, 19), (3, 21), (4, 20), (5, 21), (6, 22), (7, 23), (8, 23), (9, 23), (10, 24), (11, 24), (12, 22))


#定义答应和写入文本函数
def P_W_function(content):    #缩进4个空格、一个语句块
    print(content)
    with open('user_data.txt','a',encoding='utf-8') as f:
        f.write(content +'\n')

# 定义一个字典，用于统计使用该工具用户的生肖和星座分布情况,映射的类型：字典{哈希值：'对象'}
dict_Zodiac = {}
for i in ChineseZodiac:
    dict_Zodiac[i] = 0  #切片操作符   [:]

dict_Constellations = {}
for i in TwelveConstellations:
    dict_Constellations[i] = 0

#把数据写入Excel里面
def write_excel_xls(path, sheet_name, value):
    index = len(value)  # 获取需要写入数据的行数
    workbook = xlwt.Workbook()  # 新建一个工作簿
    sheet = workbook.add_sheet(sheet_name)  # 在工作簿中新建一个表格
    for i in range(0, index):
        for j in range(0, len(value[i])):
            sheet.write(i, j, value[i][j])  # 像表格中写入数据（对应的行和列）
    workbook.save(path)  # 保存工作簿
    print("xls格式表格写入数据成功！")

def write_excel_xls_append(path, value):
    index = len(value)  # 获取需要写入数据的行数
    workbook = xlrd.open_workbook(path,formatting_info=True)  # 打开工作簿，formatting_info=True写入excel数据而不改变excel原有样式
    sheets = workbook.sheet_names()  # 获取工作簿中的所有表格
    worksheet = workbook.sheet_by_name(sheets[0])  # 获取工作簿中所有表格中的的第一个表格
    rows_old = worksheet.nrows  # 获取表格中已存在的数据的行数
    new_workbook = copy(workbook)  # 将xlrd对象拷贝转化为xlwt对象
    new_worksheet = new_workbook.get_sheet(0)  # 获取转化后工作簿中的第一个表格
    for i in range(0, index):
        for j in range(0, len(value[i])):
            new_worksheet.write(i + rows_old, j, value[i][j])  # 追加写入数据，注意是从i+rows_old行开始写入
    new_workbook.save(path)  # 保存工作簿
    print("xls格式表格【追加】写入数据成功！")


def read_excel_xls(path):
    workbook = xlrd.open_workbook(path)  # 打开工作簿
    sheets = workbook.sheet_names()  # 获取工作簿中的所有表格
    worksheet = workbook.sheet_by_name(sheets[0])  # 获取工作簿中所有表格中的的第一个表格
    for i in range(0, worksheet.nrows):
        for j in range(0, worksheet.ncols):
            print(worksheet.cell_value(i, j), "\t", end="")  # 逐行逐列读取数据
        print()

#获取系统时间
currenttime = datetime.datetime.now()
P_W_function('系统当前时间：%s' % currenttime)
#获取当前年份
year = currenttime.year
# print(year)

# 加入循环,并且限制循环次数
i = 1
while True:
    i += 1
    if i > 4:
        break

    #用户输入姓名、性别、出生日期（年、月、日），数据类型int整数、str字符串、bool布尔值（True，False）、float浮点数
    str_name = str(input('请输入姓名：'))
    while True:
        str_sex = input('请输入性别：')
        if str_sex == '男' or str_sex == '女':
            int_year = int(input('请输入出生年份：'))
            int_month = int(input('请输入出生月份：'))
            int_day = int(input('请输入出生日期：'))
            break
        elif str_sex != '男' or str_sex != '女':
            print('性别请输入：男\女')
            str_sex = input('请输入性别：')
            if str_sex == '男' or str_sex == '女':
                int_year = int(input('请输入出生年份：'))
                int_month = int(input('请输入出生月份：'))
                int_day = int(input('请输入出生日期：'))
                break
            elif str_sex != '男' or str_sex != '女':
                print('性别请输入：男\女')
                continue

    #计算用户年龄
    age = year - int_year    #运算符
    P_W_function('用户 %s 性别 %s 年龄 %s' % (str_name,str_sex,age))

    #计算用户生肖
    zodiac = ChineseZodiac[int_year%12]
    P_W_function('出生年份 %s 生肖 %s' % (int_year, zodiac))

    #计算用户星座，方法一
    constellations = TwelveConstellations[len(list(filter(lambda x:x <= (int_month,int_day),Time)))%12]
    #比较操作符   <	小于    <=	小于或等于   !=   不等于  检查某些东西是否为True，如果是，则执行此操作。如果它不是True（False），则不执行
    P_W_function('出生日期 %s 星座 %s'%((int_month,int_day),constellations))

    #计算用户星座，方法一
    n = 0
    while Time[n] < (int_month,int_day):
        if int_month == 12 and int_day > 23:
            #逻辑操作符	and	如果两个操作数均为True，则condition变为True.
            #           or 如果两个操作数中的任何一个为True，则condition变为True.
            #           not	用于反转逻辑（不是False变为True，而不是True变为False
            break
        n +=1
    # P_W_function('星座为：%s' % TwelveConstellations[n])

    # 计算用户星座，方法三
    for zd_num in range(len(Time)):
        if Time[zd_num] >= (int_month, int_day):
            # P_W_function('%s 的星座为：%s' % ((int_month, int_day), TwelveConstellations[zd_num]))
            break  # 输出了所有符合 if 条件的星座，即日期 >= 输入日期
        elif int_month == 12 and int_day > 23:
            # P_W_function('%s 的星座为：%s' % ((int_month, int_day), TwelveConstellations[0]))
            break

    # 字典进行数据统计
    dict_Zodiac[zodiac] +=1
    dict_Constellations[constellations] +=1


    P_W_function('用户生肖的解释：')

    # 对用户输入的生肖运势进行解释
    if constellations == '金牛座':   #if后面可以有任意数量的elif语句,elif语句语句允许您检查True的多个表达式，并在其中一个条件求值为True时立即执行代码块
        P_W_function('金牛座很保守，喜欢稳定，一旦有什么变动就会觉得心里不踏实，性格也比较慢热，但你是理财高手，'
                          '对于投资理财都有着独特的见解。金牛男的性格有点儿自我，而金牛女就喜欢投资自己，想要过得更好。')
    elif constellations == '狮子座':
        P_W_function('狮子座有着宏伟的理想，总想靠自己的努力成为人上人，你向往高高在上的优越感，也期待被仰慕被崇拜的感觉，'
                          '有点儿自信有点儿自大。狮子男的大男人气息很重，爱面子，狮子女热情阳光，对朋友讲义气。')
    elif constellations == '摩羯座':
        P_W_function('真心朋友很少，有的话，一定是真诚而持久的。土星是时间的象征，影响力是限制性的，此行星主要是关于所有感情的固定性，'
                     '它的力量在于稳定，坚忍，坚持和毅力。节俭和小心投资，能带来利益，个性坚定。双重性格很明显，需要一个支点，他们对事物的态度很乐观。')
    elif constellations == '白羊座':
        P_W_function('做事爱激动、好斗和有纪律观念。总喜欢把生活这弦绷得紧紧的。内心的激动常常表现在行动上，很少顾及到后果。'
                     '这是个不满足于平淡无味生活，渴望出人头地和奋发拼搏的人。休息会使你感到疲倦，而困难会给你增添力量。'
                     '你随时都准备重整旗鼓，继续前进，即使在遭到彻底失败的情况下，亦然如故。')
    elif constellations == '双子座':
        P_W_function('遇事总是优柔寡断、不知所措或进退维谷。从而使他不能把自己的力量集中在一个确定的目标上。'
                     '他有可能流于徒劳无益的夸夸其谈之中。一切都能使他兴趣盎然；一切对他也能变得淡漠厌倦。')
    else:      #仅当上面的所有“if”和“elif”语句都为False时才会执行
        P_W_function('系统维护中，请稍候再试')

    P_W_function('-'*80)

    #把数据存入元组
    user_data = []   #元组内容可变更
    user_data.append(str_name)
    user_data.append(str_sex)
    user_data.append(age)
    user_data.append(zodiac)
    user_data.append(constellations)
    print(user_data)


    #Excel文件写入
    book_name_xls = 'user_data.xls'

    sheet_name_xls = 'user'

    value_title = [["姓名", "性别", "年龄", "生肖", "星座"], ]

    value1 = [user_data]

    if (os.path.exists(book_name_xls)):  #os.path模块主要用于文件的属性获取,exists是“存在”的意思，
        # os.path.exists()就是判断括号里的文件是否存在的意思，括号内的可以是文件路径
        write_excel_xls_append(book_name_xls,value1)
    else:
        write_excel_xls(book_name_xls, sheet_name_xls, value_title)
        write_excel_xls_append(book_name_xls, value1)

read_excel_xls(book_name_xls)

# 将年龄列表写入到json文件中
filename = 'user_data.json'
with open(filename, 'a',encoding='utf-8') as file_obj:
    json.dump(user_data, file_obj)

# 输出字典的值
P_W_function('本轮使用工具用户的生肖分布情况：')
for each in dict_Zodiac.keys():  #获取字典里面所有的值
    P_W_function('生肖%s 有 %s 个' % (each, dict_Zodiac[each]))
    time.sleep(1)
P_W_function('本轮使用工具用户的星座分布情况：')
for each in dict_Constellations.keys():
    P_W_function('星座 %s 有 %s 个' % (each, dict_Constellations[each]))
    time.sleep(1)

P_W_function('*' * 80)    #重复操作符*
