# coding: utf-8

# 函数可变参数，*args
def add(*args):  # 这里的星号表示可变参数
    print(type(args))  # <type 'tuple'>
    print(u"args length: ", len(args))
    s = 0
    for i in args:
        s += i
    print(s)
    print(u"========================================")
    
    
    
add(1, 2, 3)

t = (4, 5, 6)
l = [9, 9]
add(*t)  # 这里的星号*表示把tuple或者list转成可变参数 => add(4, 5, 6)
add(*l)



# 关键字参数，**kw

def person(**kw):
    print(kw)
    print(u"========================================")
    
person()
person(name=u"leo", age=26)

m = {"name":u"tom", "age":26}
person(**m)  # 这里的双星号**表示dict转成关键字参数  => person(name=u"tom", age=26)


def func(*args, **kw):
    print(args)
    print(kw)
    print(u"========================================")
    
func(1, 2, name=u"leo")    


#=================================















