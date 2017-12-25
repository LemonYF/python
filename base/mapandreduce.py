# map()函数

def f(x):
    return x * x


r = map(f, [1, 2, 3, 4, 5, 6, 7])
print(list(r))

str = map(str, [1, 3, 4, 6])
print(list(str))

# reduce函数,reduce把结果继续和序列的下一个元素做累积计算
from functools import reduce


def fn(x, y):
    return 10 * x + y


print(reduce(fn, [1, 2, 3, 4, 5]))

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def strtoint(s):
    def fn(x, y):
        return x * 10 + y

    def chartonum(s):
        return DIGITS[s]

    return reduce(fn, map(chartonum, s))


