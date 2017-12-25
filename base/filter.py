# filter()函数用于过滤序列

def is_odd(n):
    return n % 2 == 1


print(list(filter(is_odd, [2, 3, 4, 5, 6])))


def notempty(s):
    return s and s.strip()


print(list(filter(notempty, ['2', '', 'A', 'B', '2', None])))


def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter()  # 初始序列
    while True:
        n = next(it)  # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it)  # 构造新序列