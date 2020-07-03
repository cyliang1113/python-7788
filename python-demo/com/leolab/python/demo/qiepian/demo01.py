# coding: utf-8

# 切片

l = [1, 2, 3, 4]
print l[0:]  # [1, 2, 3, 4] 从下标0开始，取后面所有的
print l[1:2]  # [2] 从下标1开始，到下标2，但不包括下标2
print l[-1:]  # [4]
print l[-2:]  # [3, 4]

print l[0::2]  # [1, 3] 从下标0开始，每隔两个，取后面所有的

t = (5, 6, 7)
print t[1:]

s = u"我们abcde"
print s[0:3]

print range(3)  # 从0开始，到3，但不包括3
print range(2, 3)   # 从2开始，到3，但不包括3
