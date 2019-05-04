#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : second.py
# @Author  : jinjianfeng
# @Contact : 553041800@qq.com
# @Link    : https://github.com/jinjf553
# @software: PyCharm
# @Date    : 2019/5/4 18:42
# @Version : ??
import time
from pprint import pprint


def method1():
    print(b'foo bar')
    print(list(b'foo bar'))
    print(tuple(b'foo bar'))
    print(type('some string'))
    print(type(b'some bytes'))
    print('foo'.encode('utf-8', errors='ignore'))
    print(b'foo'.decode('utf-8', errors='ignore'))
    substrings = list('aljsfoa' * 5000000)
    s = ''
    print(time.time())
    for substring in substrings:
        s += substring
    print(time.time())
    a = ''.join(substrings)
    print(time.time())


def method2():
    print(time.time())
    evens = []
    for i in range(50):
        if i % 2 == 0:
            evens.append(i)
    print(time.time())
    evens = [i for i in range(50) if i % 2 == 0]
    print(time.time())

    with open('get.txt', 'a+') as f:
        f.write(str(time.time()) + '\n')
        i = 0
        for element in ['one', 'two', 'three'] * 500000:
            print(i, element)
            i += 1
        f.write(str(time.time()) + '\n')
        for i, element in enumerate(['one', 'two', 'three'] * 500000):
            print(i, element)
        f.write(str(time.time()) + '\n')


def method3():
    for item in zip([1, 2, 3], [4, 5, 6]):
        print(item)

    for item in zip(*zip([1, 2, 3], [4, 5, 6])):
        print(item)
    squares = {number: number ** 2 for number in range(100)}
    pprint(squares)

    a = {str(number): None for number in reversed(range(5))}.keys()
    print(a)
    b = {1, 2, 3, 4, 5}
    print(b)


if __name__ == '__main__':
    method3()
