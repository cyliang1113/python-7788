# coding: utf-8


# 迭代

l = [1, 2, 3, 4]
for i in l:
    print i
    
m = {u"a":1, u"b":2, u"c":3}
for k in m:
    print k, u":", m.get(k)
    
    
for k, v in m.iteritems():
    print k, u":", v
