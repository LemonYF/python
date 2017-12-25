#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" a test module """

__author__ = 'YF'


class Student(object):
    pass


#  给实例绑定属性和方法
from types import MethodType

s = Student()
s.name = 'yefan'


def age(self, age):
    self.age = age


s.age = MethodType(age, s)
s.age(18)
print(s.age, s.name)


class Dog():
    __slots__ = ('name', 'age')


d = Dog()
d.name = 'you'
d.age = 2
