# encoding:utf-8
#__author__:Administrator
#__date__:2019/11/23
import time
fileName = 'smallmountant'

def readFile():
    f = open(fileName,'r',encoding='utf8')
    print(f.fileno())
    # print(f.read())
    # print(f.readline())
    # print(f.readlines())
    for i in f.readlines():
        print(i.strip())

def apendFile():
    f = open(fileName,'a',encoding='utf8')
    print(f.fileno())
    f.write("\n456")
    time.sleep(10)
    f.close()

def testPrint():
    for i in range(30):
        print("*",end='',flush=True)
        time.sleep(0.1)

testPrint()