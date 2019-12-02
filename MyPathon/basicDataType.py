#__author__:Administrator
#__date__:2019/11/16
#列表，元组

def testlist():
    a = ["a","b","f","a"]
    print(a)
    print(len(a),a[0],a[1],a.index("f"))# 索引(下标) ，都是从0开始 4 a
    print(a[1:3])#切片 ['b', 1]
    # print(a.count("a")) #查某个元素的出现次数 2
    # print(a.index("a")) # 根据内容找其对应的位置 0
    print("hai" in a)#判断某个元素是否在列表 False
    #增加
    a.append("s")#追加
    print(a)
    a.insert(2, "内容")#在指定位置插入元素
    print(a)
    b =["w","e","s","a"]
    print(a+b)
    print(a)
    a.extend(b)#扩展
    print(a)
    #修改
    a[3] = "新的值"
    print(a)
    a[1:3] = ['c','r']
    print(a)
    # #删除
    a.remove("新的值")
    print(a)
    a.pop()
    print(a)
    a.pop(3)
    print(a)
    # del a
    # del a[3]
    # a.clear()#清空
    a.sort(reverse=True)
    print(a)
    a.reverse()
    print(a)
    print(type(a) is list)

def copytest():
    names_class1 = ['张三', '李四', '王五', '赵六', [1, 2, 3]]
    names_class1_copy = names_class1.copy()
    names_class1[0] = 'zhangsan'
    names_class1[4][0] = 4

    print(names_class1)
    print(names_class1_copy)
    print(id(names_class1),id(names_class1_copy))

# testlist()
# copytest()
def testtuple():
    a=(1,2,5,4)
    print(a)
    print(type(a) is tuple)
    print(a[1],a[1:3])
# testtuple()

def testdict():
    a={"name":"yyh","hobby":{"sport":"climbing","reading":"tec"},"sex":"boy"}
    print(a["hobby"])

    # a["age"]=18
    # print(a)
    d=a.setdefault("age",20)#有值直接返回，无值则设置一个默认值，并返回默认值
    print(d)
    print(a)
    # c=(("name","hello"),)
    # print(c,type(c))
    # print(c[0],type(c[0]))
    # b=dict((("name","hello"),))
    # print(b,type(b))
    # a = '{"id":"e325dc8f59320bb85c6d0324da56565e","url_token":"bu-xiang-lian-ai-49","name":"不想恋爱"}'
    # d = eval(a)#将字符串转化为字典形式
    # print(d)
    # print(d['id'])
    keys = a.keys()
    print(type(keys),keys)
    # for i in keys:
    #     print(i)
    k = list(keys)
    print(type(k),k)
    values =a.values()
    print(type(values),values)
    items = a.items()
    print(type(items), items)
    print(a)
    b={"name":"huazai","color":"red"}
    a.update(b)
    print(a)
    del a["color"]
    print(a)
    print(a.pop("age"))#返回被删除键值对的值
    print(a)
    # print(a.popitem())#返回被删除键值对
    # print(a)
    b = dict.fromkeys(["host1","host2","host3"],["test1","test2"])
    print(b)
    b['host2']='abc'
    print(b)
    print(sorted(a))
    print(sorted(a.keys()))
    # print(sorted(a.values()))
    print(sorted(a.items()))
    for i in a:#效率高
        print(i,a[i])
    for i,v in a.items():#很耗时
        print(i,v)
# testdict()
def testStr():
    a="hello world 123"
    # print(a*2)#重复打印
    # print(a[2:])#切片
    # print('or' in a,'ort' in a)#关键字in
    # print('%s is a good teacher'% 'alex')
    #字符串拼接
    a='123'
    b='abc'
    print(a+b)
    print(a.join(b))
    print('***'.join([a,b]))
    str ="hello kTTTy"
    print(str.count('kitty'))#统计字符个数
    print(str.capitalize())#首字母大写
    print(str.ljust(50,'-'))#靠左
    print(str.rjust(50,'-'))#靠右
    print(str.center(50,'-'))#居中
    print(str.casefold())#无大小写版本
    print(str.endswith('ty'))#以什么结尾
    print(str.startswith('He'))#以什么开头
    print(str.expandtabs(tabsize=10))#tab设置空格个数
    print(str.find('t'))#返回字符第一个索引位置，找不到返回-1
    #格式化输出
    a = "Hello {name} is {age}"
    print(a.format(name='alex',age =18))
    print(a.format_map({'name':'alex','age':18}))
    # print(str.index('t6'))#找不到会报错
    print('汉子'.isalnum())#是否是字母或数字
    print('98.89'.isdecimal())
    print('98'.isdigit())#不是整型
    print('sa'.isidentifier())#判断是否是标示符
    print('My Title'.istitle())
    print('My Title'.swapcase())#大小写反转
    print(' My \nTitle\n'.strip())#去掉空格和换行符
    print('My title title'.replace('title','session',1))
    print('Mt title'.find('t'))
    print('Mt title'.rfind('t'))
    print('My title test'.split(' '))
    print('My title test'.rsplit(' ',1))
    print(' '.join(['My', 'title', 'test']))
    print('My titTe test'.title())
# testStr()

def testSet():
    a = set([("a","b"),"c"])
    print(type(a),a)
    li = [("1",'2'),"d","c"]
    s=set(li)
    print(type(s),s)
    print(("1",'2') in s)
    s.add('u')
    print(s)
    s.add('c')
    print(s)
    s.remove('c')
    print(s)
    s.pop()
    print(s)
    s.pop()
    print(len(s),s)
    s.clear()
    print(s)
    s={('a', 'b'), 'c', 'c'}
    print(type(s), s)
    a = set('abcd')
    b = set('cdfe')
    print(a.intersection(b))#交集
    print(a.union(b))#并集
    print(a.difference(b))#差集 in a not in b
    print(b.difference(a))#差集 in b not in a
    print(a.symmetric_difference(b))#对称差集
    print(a.symmetric_difference_update(b))#对称差集
    print(a and b)#都取
    print(a or b)

testSet()