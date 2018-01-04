#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" a test module """

__author__ = 'YF'

from wsgiref.simple_server import make_server
from hello_interface import interface_hello

httpd = make_server('', 8000, interface_hello)
print('Serving HTTP on port 8000...')
httpd.serve_forever()
