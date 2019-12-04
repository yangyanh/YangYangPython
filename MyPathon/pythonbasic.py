#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；
# 第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。
# from sysinfo import printsysParam
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

def format():
    print('Hi, %s, you have $%d.' % ('小王', 1000000))
    print('%2d-%02d' % (3, 1))
    print('%.2f' % 3.1415926)
    print('growth rate: %d %%' % 7)#字符串里面的%是一个普通字符怎么办？这个时候就需要转义，用%%来表示一个%
    print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))

#Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素。
#1、查找和插入的时间随着元素的增加而增加；
#2、占用空间小，浪费内存很少。
def listtest():
    classmates = ['Michael', 'Bob', 'Tracy']
    print(len(classmates),classmates)
    classmates.append('Adam')#追加元素
    print(len(classmates), classmates)
    classmates.insert(1, 'Jack')# 把元素插入到指定的位置
    print(classmates.pop())#删除末尾的元素,并返回被删除的元素
    print(classmates.pop(2))#删除指定位置的元素，用pop(i)方法，其中i是索引位置，并返回被删除的元素
    classmates[1] = 'Sarah'# 要把某个元素替换成别的元素，可以直接赋值给对应的索引位置
    print(len(classmates), classmates)
    print(classmates[-1],classmates[-2])#-1表示最后一个，-2表示倒数第二个
    L = ['Apple', 123, True,['Michael', 'Bob', 'Tracy']]#list中可以有不同类型，也可以包含list
    print(L[3])

#另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改
#因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple
def tupletest():
    classmates = ('Michael', 'Bob', 'Tracy')
    a=(1)#没有逗号就当元素了
    b =(1,)#只有1个元素的tuple定义时必须加一个逗号
    print(a,b)

#dict的key必须是不可变对象
#dict有以下几个特点：
    # 查找和插入的速度极快，不会随着key的增加而变慢；
    # 需要占用大量的内存，内存浪费多。
def dicttest():
    d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
    d['Adam'] = 67
    print(d['Michael'],d['Adam'])
    if 'Thomas' in d:
        print(d['Thomas'])  # 不存在的key会报错
    for key in d:
        print(key+":",d[key])
    #通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value
    print(d.get("Adam"))
    print(d.get("Thomas"))
    print(d.get("Thomas","-1"))
    print(d.pop('Bob'))#要删除一个key，用pop(key)方法，对应的value也会从dict中删除
    print(d)


#set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key
def settest():
    s = set([1, 2, 3])#要创建一个set，需要提供一个list作为输入集合
    print(s)
    s = set([1, 1, 2, 2, 3, 3])#重复元素在set中自动被过滤
    print(s)
    s.add(4)#通过add(key)方法可以添加元素到set中
    print(s)
    s.add(4)#可以重复添加，但不会有效果
    print(s)
    s.remove(4)#通过remove(key)方法可以删除元素
    print(s)
    #set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作
    s1 = set([1, 2, 3])
    s2 = set([2, 3, 4])
    print("交集",s1 & s2)
    print("并集",s1 | s2)


def testinput():
    while True:
        num = input("Please put number:")
        if not num.isdigit():
            if num=='q':
                break
            print(num,"is not number")
            continue
        num = int(num)
        if num>10:
            print(num," is bigger than 10")
        elif num>=5:
            print(num," is not smaller than 5")
        else:
            print(num,"is too small")
# testStr();
# numric()
# encoding()
# format()
# listtest()
# tupletest()
# dicttest()
# settest()
# testinput()
