#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；
# 第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。

#数据类型
#字符串
def testStr():
    # 字符串内部既包含'又包含"怎么办？可以用转义字符\来标识
    str = 'I\'m \"OK\"!';
    print(str)
    # 为了简化，Python还允许用r''表示''内部的字符串默认不转义
    str = r'I\'m \"OK\"!';
    print(str)
    #如果字符串内部有很多换行，为了简化，Python允许用'''...'''的格式表示多行内容
    print('''line1
    ... line2
    ... line3''')
    print('''hello,\n world''')
    print(len('abc中文'))#计算str包含多少个字符
    #计算字节数，1个中文字符经过UTF-8编码后通常会占用3个字节，而1个英文字符只占用1个字节
    print(len('abc'.encode('utf-8')))
    print(len('中文'.encode('utf-8')))

def numric():
    print(10/4) #/除法计算结果是浮点数，即使是两个整数恰好整除，结果也是浮点数
    print(10//4) # 还有一种除法是//，称为地板除，两个整数的除法仍然是整数
    print( 10 % 3) #所以Python还提供一个余数运算，可以得到两个整数相除的余数

def encoding():
    print('包含中文的str')
    print(ord('A'),ord('中'))#对于单个字符的编码，Python提供了ord()函数获取字符的整数表示
    print(chr(65),chr(20013))#对于单个字符的编码，Python提供了chr()函数把编码转换为对应的字符：
    print(chr(66),chr(25991))#对于单个字符的编码，Python提供了chr()函数把编码转换为对应的字符：
    print( '\u4e2d\u6587')#如果知道字符的整数编码，还可以用十六进制这么写str
    x = b'ABC'
    print(x,type(x))
    print('ABC'.encode('ascii'))
    print('中文'.encode('utf-8'))
    # print('中文'.encode('ascii'))
    print(b'ABC'.decode('ascii'))
    print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
    print( b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore'))#如果bytes中只有一小部分无效的字节，可以传入errors='ignore'忽略错误的字节
testStr();
# numric()
# encoding()