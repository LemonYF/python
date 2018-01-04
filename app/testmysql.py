#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" a test module """

__author__ = 'YF'

import mysql.connector

try:
    conn = mysql.connector.connect(user='root', password='', database='test')
except:
    print('error')

cursor = conn.cursor()
all_table = cursor.execute('show tables')
tb_list = []  #  存放数据表列表
for tb in cursor.fetchall():
    tb_list.append(tb[0])

if 'user' in tb_list:
    print('111')
    print("222")
    print(cursor.rowcount)
    cursor.execute('select * from user where id = %s', ('1',))
    values = cursor.fetchall()
    print(values)
else:
    try:
        cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
    except:
        print('table存在')
cursor.close()
conn.close()
print('连接关闭')