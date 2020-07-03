# coding: utf-8


# 匿名函数
def add(f, *a):
    for i in a:
        print(f(i))

    
add(lambda x: x + x, 1, 2, 3)
