#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" a test module """

__author__ = 'YF'

from collections import namedtuple

point = namedtuple('point', ['x', 'y'])
p = point(1, 2)

print(p.x)
print(p.y)