L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [ n.lower() for n in L1 if isinstance(n, str)]

if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')