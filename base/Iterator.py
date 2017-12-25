# 迭代器
# 可以直接作用于for循环的数据类型有以下几种：

# 一类是集合数据类型，如list、tuple、dict、set、str等；

# 一类是generator，包括生成器和带yield的generator function。

from collections import Iterable  # 可以for循环

print(isinstance([], Iterable))

print(isinstance({}, Iterable))

print(isinstance('bac', Iterable))

print(isinstance((x for x in range(10)), Iterable))

print(isinstance(100, Iterable))

# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。
print("\n")
from collections import Iterator  # 不仅可以for循环，也可以next()

print(isinstance([], Iterator))

print(isinstance({}, Iterator))

print(isinstance((x for x in range(10)), Iterator))

for x in [1, 2, 3, 4]:
    pass

it = iter([1, 2, 3, 4])
while True:
    try:
        x = next(it)
    except StopIteration:
        break
