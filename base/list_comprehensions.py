# 列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。

print(list(range(1, 11)))

L = []
for x in range(1, 11):
    L.append(x*x)
print(L)

print([x * x for x in range(1, 11)])

print([x * x for x in range(1, 11) if x % 2 == 1])

print([x * x for x in range(1, 11) if x == 2])

print([x * y for x in range(1, 11) for y in range(11, 20)])

print([x * y for x in "ABC" for y in range(11, 20)])

import os
print([d for d in os.listdir('.')])

d = {'x':'A', 'y':'B', 'z':'C'}
for x, y in d.items():
    print(x,y)

print([k+'='+v for k, v in d.items()])

L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])

L = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L if isinstance(s, str) is True]
print()