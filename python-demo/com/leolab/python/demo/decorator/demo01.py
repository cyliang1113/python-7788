# coding: utf-8


# decorator就是一个返回函数的高阶函数
# fn是被装饰的函数
def logDecorator(fn):
    a = 0
    def newFn(*args, **kw):
        print(u"打印日志...", a)
        rn = fn(*args, **kw)
        return rn
    return newFn


@logDecorator
def printName(fname, lname):
    print(fname, lname)

# 相当于先调用logDecorator(printName), 然后把printName指向返回的结果
    
    
print(printName.__name__)  # newFn     在函数上加上@log后, 函数名printName指向了newFn
print(printName)  # <function newFn at 0x0000000002763048> 在函数上加上@log后, 函数名printName



printName(u"yoyou", u"kk")
    

