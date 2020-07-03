# coding: utf-8


# decorator就是一个返回函数的高阶函数
def log(fn):
    def newFn(*args, **kw):
        print("打印日志...")
        rn = fn(*args, **kw)
        return rn
    return newFn


@log
def printName(fname, lname):
    print(fname,lname)
    
    
print(printName.__name__) # newFn     在函数上加上@log后, 函数名printName指向了newFn
print(printName) # <function newFn at 0x0000000002763048> 在函数上加上@log后, 函数名printName



printName("yoyou", "kk")
    

