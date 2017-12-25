#   teration.py
#   python中迭代就是遍历
from collections import Iterable

d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

for x in d:
    print(x)
print("\n")

for x in d.values():
    print(x)
print("\n")

for x, y in d.items():
    print(x, y)
print("\n")

for x in "aefwefwefwef":
    print(x)
print("\n")

if isinstance("abc", Iterable):
    print(True)
print("\n")

# list c下标循环，使用enumerate函数
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)
print("\n")

for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)
print("\nTest")


def findMinAndMax(L):

    if len(L) == 0:
        return None, None
    max = L[0]
    min = L[0]
    for x in L:
        if x >= max:
            max = x
        if x < min:
            min = x
    return min, max


print(findMinAndMax([1, 2, 3, 4, 5, 6, 7, 8]))
print(findMinAndMax([]))
print(findMinAndMax([7]))
print(findMinAndMax([7, 1, 3, 9, 5]))

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


