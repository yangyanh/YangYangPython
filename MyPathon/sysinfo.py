import sys
import time
def printTime():
    time_format= '%Y-%m-%d %X'
    time_content = time.strftime(time_format)
    print(time_content)
    time_result =time.strptime(time_content,time_format)
    print(time_result)

import math
def printsysParam():
    print(sys.version_info)
def testinputandoutput():
    # 输入
    name = input("Enter your Name:")
    # 输出
    print("Your name is", name)
printsysParam()

def my_abs(x):
    if not isinstance(x, (int, float)):#检查类型
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
#返回多个值
#比如在游戏中经常需要从一个点移动到另一个点，给出坐标、位移和角度，就可以计算出新的坐标：
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
def quadratic(a, b, c):
    x1=(b*(-1)+math.sqrt(b*b-4*a*c))/(2*a)
    x2=(b*(-1)-math.sqrt(b*b-4*a*c))/(2*a)
    return x1,x2
print("quadratic",quadratic(2,3,1))
#可变参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print(calc(1,2,3))
nums = [1, 2, 3]
print("len",len(nums))
print(calc(*nums))
def person(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)
person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)
#在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

# print(move(1,2,3,math.pi/2))#
# print(abs(-100))#取绝对值
# print(max(2,3,4,2,1))#计算最大值
# print(int('123'),int(12.67))#其他类型转换成int
# print(str(123),str(12.67))#其他类型转换成String
# print(bool(123),bool('a'),bool(0),bool('0'),bool(''))#其他类型转换成boolean
# #          True   True    False   True       False
# print(hex(10))#十进制转换成十六进制
#
# #函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”：
a = abs # 变量a指向abs函数
print(a(-1)) # 所以也可以通过a调用abs函数
print(type(a))
a=person
print(type(a))
def fact(n):
    return fact_iter(n, 1)


def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
print(fact(100))

printsysParam()
printTime()

