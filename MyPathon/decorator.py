#__author__:Administrator
#__date__:2019/12/1
import time
def logger(flag=""):
    def  show_time(func):
        def inner(*args):
            print("flag:"+flag)
            a = time.time()
            func(*args)
            b = time.time()
            print("spend %s " %(b-a))
        return inner
    return show_time

@logger(flag="true")
def add(a,b):
    print(a+b)
    time.sleep(1)

@logger()
def minus(a,b):
    print(a-b)
    time.sleep(1.5)

minus(3,1)
add(1,2)




