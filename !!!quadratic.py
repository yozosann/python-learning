# -*- coding: utf-8 -*-

import math

def quadratic(a, b, c):
    for n in (a,b,c):# 遍历三个参数
        if not isinstance(n,(int,float)):#遍历判断参数是整型或浮点型
            raise TypeError('你输入的是什么玩意儿')#错误提示
    temp = b*b - 4*a*c
    if temp < 0:
        print('无解')
        return
    else:
        return (-b + math.sqrt(temp))/(2 * a), (-b - math.sqrt(temp))/(2 * a)


print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')