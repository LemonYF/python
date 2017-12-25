def power(x):
    return x * x


'''
位置参数
'''


def power1(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


'''
默认参数
'''
print('\n');


def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)


print("这里是enroll函数")
enroll("A", "A")

print('\n')
x = power(5)
print(x)
print('\n')

x = power1(5, 3)
print(x)
print('\n')


def add_end(L=[]):
    L.append('END')
    return L


L = add_end([1, 2, 3])
print("这是第1个append", L)

L3 = add_end(['x', "y", "z"])
print("连续调用第2次", L3)

L = add_end()
print("第3次调用", L)
L1 = add_end()
print("第4次调用", L1)
L2 = add_end()
print("第5次调用", L2)
'''
Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，
因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，
如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
定义默认参数要牢记一点：默认参数必须指向不变对象！
'''

print('\n')


def add_end1(L=None):
    if L is None:
        L = []
    L.append('end')
    return L


L = add_end1()
print("第1次调用", L)
L1 = add_end1()
print("第2次调用", L1)
L2 = add_end1()
print("第3次调用", L2)
print('\n')

print('\n"这里需要组装一个list或者tuple，默认参数写法"')


def calc(num):
    sum = 0
    for i in num:
        sum = sum + i * i
    return sum


s = calc([1, 2, 3])
x = [2, 2, 2]
print("default para", s)
print("default para", calc([1, 2]))
print("default para", calc([x[0], x[1], x[2]]))
print("default para", calc(x))
print('\n');

print('\n"这里为可变参数写法"');


def calc1(*num):
    sum = 0
    for i in num:
        sum = sum + i * i
    return sum


print("flexable para", calc1(1, 2, 3))
print("flexable para", calc1())

print('\n"keyword para,kw是关键字参数')


def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


person("yefan", 23)
person("yefan", 23, city="BJ")
person("yefan", 23, city="BJ", sex="male")

print('\n"关键字参数可以先组装一个dict，在当作参数传入,不会改变原有参数"')
extra = {'city': 'bj', 'sex': 'female'}
person("yefan", 23, city=extra['city'], sex=extra['sex'])
person("yefan", 23, **extra)

print('\n"命名关键字参数，命名关键字参数必须传入参数名,针对特定的参数"');


def person1(name, age, **kw):
    if 'city' in kw:
        pass
    if 'sex' in kw:
        pass
    print('name:', name, 'age:', age, 'other:', kw)


person1('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)

print('\n"限制关键字参数名字，参数定义的顺序必须是：必选参数、默认参数、可变参数/命名关键字参数和关键字参数。"');


def person2(name, age, *, city, job):
    print(name, age, city, job)


person2('Jack', 24, city='Beijing', job='Teacher')

print('\n参数组合"命名关键字可以具有默认值，简化调用"');


def person3(name, age, *, city='BJ', sex):
    print(name, age, city, sex)


person3('yefan', 23, sex='female')

print('\n参数组合,可变参数可看作为一个tuple，关键字参数可以看作一个dict,所以，对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。');


def fun1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


def fun2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


fun1(1, 2)
fun1(1, 2, 3, 3, 4, 4)
fun1(1, 2, 3, 3, 4, 4, city='BJ')
fun1(1, 2, 3, 2, 22, 2, 2, city="WH", age='18')
args = (1, 2, 3)
kw = {'sex': 'female', 'age': 18}
fun1(*args, **kw)

print('\ntest');


def product(*args):
    sum = 1
    for x in args:
        sum = sum * x
    return sum


print('product() =', product())
print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试成功!')
    except TypeError:
        print('测试失败!')
