def findMinAndMax(L):
    if(len(L) == 0):
        max = min= None
    else:
        max = min= L[0]
    for n in L:
        if(n > max):
            max = n
        if(n < min):
            min = n
    return (min, max)

print(findMinAndMax([1, 3, 4, 5, 6, 6, 6, 9]))

if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')