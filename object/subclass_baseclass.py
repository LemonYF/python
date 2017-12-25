#  父类和基类

class Animal(object):
    def run(self):
        print('Animal is running...')


class Dog(Animal):

    def run(self):
        print('Dog is running')

    def eat(self):
        print('Dog is eating')

    pass


class Cat(Animal):
    pass


dog1 = Dog()
dog1.eat()
dog1.run()


def run_twice(animal):
    animal.run()
    animal.run()


run_twice(Dog())
run_twice(Cat())


class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')


run_twice(Tortoise())

#  python开闭原则  对扩展开放：允许新增Animal子类；对修改封闭：不需要修改依赖Animal类型的run_twice()等函数。

"""
                      ┌───────────────┐
                      │    object     │
                      └───────────────┘
                             │
                ┌────────────┴────────────┐
                │                         │
                ▼                         ▼
          ┌─────────────┐           ┌─────────────┐
          │   Animal    │           │    Plant    │
          └─────────────┘           └─────────────┘
                │                         │
          ┌─────┴──────┐            ┌─────┴──────┐
          │            │            │            │
          ▼            ▼            ▼            ▼
     ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐
     │   Dog   │  │   Cat   │  │  Tree   │  │ Flower  │
     └─────────┘  └─────────┘  └─────────┘  └─────────┘
"""


class Timer(object):
    def run(self):
        print('Start...')


run_twice(Timer())

print(type(123))
print(type(dog1))

import types  # 判断是否为函数的拓展库


def fn():
    pass


print(type(fn))


class Husky(Dog):

    def __init__(self, name, sex):  # self参数表示实例本身
        self.name = name
        self.sex = sex


a = Animal()
d = Dog()
h = Husky("you", 'female')

print(isinstance(h, Husky))
print(isinstance(h, Dog))
print(isinstance(d, Husky))

print(dir(dog1))
print(dog1.__hash__())


def sum(L):
    sum = 0
    for x in L:
        sum = sum + x
    return sum


print(isinstance(sum, types.FunctionType))

print(hasattr(h, 'ni'))
setattr(h, 'y', 19)  # 设置一个属性'y'
print(hasattr(h, 'run'))

print(h.name + h.sex)


class Student(object):

    def __init__(self, name1):
        self.name = name1


s = Student(None)
s1 = Student('yefan1')
print(s.name)
print(s1.name)
