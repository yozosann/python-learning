from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2float(s):
    def char2num(s):
        if(s in DIGITS):
            return DIGITS[s]
        else:
            return s
    
    def mul(x, y, L = [1, 0.1]):
        if((not y == '.') and L[0] == 1):
            return x*10 + y
        elif L[0] == 0:
            result = x + L[1]*y
            L[1] = L[1] * 0.1
            return result
        else:
            L[0] = 0
            return x
    return reduce(mul, map(char2num,s))

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')

