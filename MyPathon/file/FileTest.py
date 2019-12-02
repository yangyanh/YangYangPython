# encoding:utf-8
#__author__:Administrator
#__date__:2019/11/23
f = open('小重山','a',encoding='utf8')
print(f.fileno())
f.write("\n123")
f.close()