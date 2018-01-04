#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" a test module """

__author__ = 'YF'

#def application(environ, start_response):
#    start_response('200 OK', [('Content-Type', 'text/html')])
#   return [b'<h1>Hello, web!</h1>']

def interface_hello(environ,start_response):  # environ包含所有http请求的dict对象,start_response 发送http响应的函数
    print(start_response('200 OK',[('Content_Type', 'text/html')]))
    body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'Interface')
    return [body.encode('utf-8')]
