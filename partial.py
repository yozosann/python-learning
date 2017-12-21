import functools

int2 = functools.partial(int, base=2)

print(int2('10'))

max2 = functools.partial(max, 10)
print(max2(1, 3, 4))