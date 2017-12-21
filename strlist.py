import re

str1 = 'ABCD'
strlist = list(str1)

print(str1[1:3])
print(strlist[1:3])

def trim(s):
    if type(s)==str:
        while  s[:1]==' ':
                s=s[1:]
        while s[-1:]==' ':
            s=s[:-1]
    return s

if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')

