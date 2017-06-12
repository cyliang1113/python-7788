# !/usr/bin/env python
# coding: utf-8

# print "hello world"


str1 = u"中国"
print str1
print len(str1)

str2 = "中国"
print str2
print len(str2)

str3 = "中国"
print str3.decode("utf-8")
print len(str3.decode("utf-8"))

str31 = str3.decode("utf-8")
print str31
print len(str31)


# str4 = raw_input()
# print str4
# print len(str4)
# 
# print str4.decode("utf-8")
# print len(str3.decode("utf-8"))
