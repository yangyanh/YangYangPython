#__author__:Administrator
#__date__:2019/11/16

# 不可变数据类型:数字,字符串,元组         可变类型:列表,字典

l=[2,2,3]
print(id(l))
l[0]=5
print(id(l))   # 当你对可变类型进行修改时,比如这个列表对象l,它的内存地址不会变化,注意是这个列表对象l,不是它里面的元素
#                # this is the most important
#
s='alex'
print(id(s))   #像字符串,列表,数字这些不可变数据类型,,是不能修改的,比如我想要一个'Alex'的字符串,只能重新创建一个'Alex'的对象,然后让指针只想这个新对象
#
# s[0]='e'       #报错
# print(id(s))

# 重点:浅拷贝
a = [[1, 2], 3, 4]
# b = a[:]
b=a.copy()
print(a, b)
print(id(a), id(b))
print('*************')
print('a[0]:', id(a[0]), 'b[0]:', id(b[0]))
print('a[0][0]:', id(a[0][0]), 'b[0][0]:', id(b[0][0]))
print('a[0][1]:', id(a[0][1]), 'b[0][1]:', id(b[0][1]))
print('a[1]:', id(a[1]), 'b[1]:', id(b[1]))
print('a[2]:', id(a[2]), 'b[2]:', id(b[2]))
#
# print('___________________________________________')
b[0][0] = 8
b[1] = 5

print(a, b)
print(id(a), id(b))
print('*************')
print('a[0]:', id(a[0]), 'b[0]:', id(b[0]))
print('a[0][0]:', id(a[0][0]), 'b[0][0]:', id(b[0][0]))
print('a[0][1]:', id(a[0][1]), 'b[0][1]:', id(b[0][1]))
print('a[1]:', id(a[1]), 'b[1]:', id(b[1]))
print('a[2]:', id(a[2]), 'b[2]:', id(b[2]))   # outcome