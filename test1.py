# 正则表达式

import re

pattern = 'something'
string = 'something123'
prog = re.compile(pattern)
result = prog.match(string)
print(result)


# 常用元字符
# . :除了换行符（\n)以外单个字符
# ^:字符串的开头
# $：字符串的结尾
# *:*前面多个重复字符，包含0个
# +:+前面多个重复字符，不包含0个
# ?:?前面字符出现0或1次
# (n):前面字符出现n次，{m,n}表示出现m到n次
# \:转义字符

pattern = 's.*g'
string = 'something123'
string2 = 'sshuihbxfffgg'
prog = re.compile(pattern)
result = prog.match(string)
print(result)

# re.match(pattern,string)

#分组
re.match('(.*)@(.*\.com)','xyz@baidu.com').group(1)
