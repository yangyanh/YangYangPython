# encoding:utf-8
#__author__:Administrator
#__date__:2019/11/17
import sys
print("hello:"+sys.getdefaultencoding())
s = "特斯拉"
print(type(s),s)
s_to_unicode = s.encode('utf-8')
print(type(s_to_unicode),s_to_unicode)
print(s_to_unicode.decode('utf-8'))
# unicode_to_utf8= s_to_unicode.encode("utf-8")
# print(unicode_to_utf8)
# unicode_to_utf8 = unicode_to_utf8.decode("utf-8")
#print(unicode_to_utf8)