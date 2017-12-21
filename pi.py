import itertools

def pi(N):
    number = 0
    sum = 0
    minus = -1

    for n in itertools.count(1):
        if n % 2 != 1:
            continue
        if number >= N:
            break

        number += 1
        minus *= -1
        # print(n,minus)
        sum += (4/n) * minus

    return sum

print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')