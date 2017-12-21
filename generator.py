def odd():
    print('step1')
    yield 1
    print('step2')
    yield (3)
    print('step3')
    yield (5)

o = odd()

for x in o:
    print(x)