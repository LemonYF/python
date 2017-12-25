#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" a test module """

__author__ = 'YF'

def fileread():

    try:
        f = open('/path/to/file', 'r')
        print(f.read())
    finally:
        if f:
            f.close()

def fileread1():
    with open('/path/to/file', 'r') as f:
        print(f.read())