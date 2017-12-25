# 在Python中，这种一边循环一边计算的机制，称为生成器：generator
# 列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，从而节省大量的空间

# 第一种方法，列表生成式的[]改为()
L = [x * x for x in range(10)]
print(L)
g = (x * x for x in range(10))
print(g)
# 通过next()函数获得下一个返回值，也可以直接循环,创建了一个generator后，基本上永远不会调用next()，而是通过for循环来迭代它
for n in g:
    print(n)


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'


# fib(6)
# 定义generator的另一种方法。如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
def fib1(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


print(fib1(3))
for n in fib1(6):
    print(n)

print('\nTest')


def triangles():
    L = [1]
    while True:
        yield L
        L = [L[i] + L[i + 1] for i in range(len(L) - 1)]
        L.insert(0, 1)
        L.append(1)


n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break



