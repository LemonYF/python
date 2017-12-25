import functools

int2 = functools.partial(int, base=2)

print(int2('1001'))

#  总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。

#  创建偏函数时，实际上可以接收函数对象、*args和**kw这3个参数

int2 = functools.partial(int, base=2)