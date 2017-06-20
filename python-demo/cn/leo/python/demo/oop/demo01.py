# coding: utf-8

class Person(object):  # 括号中表示该类的父类，如果没有自定义父类，一般用object
    
    # 和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，并且，调用时，不用传递该参数。
    def __init__(self, name, sex="man"):
        self.name = name
        self.__sex = sex
     
    # 方法就是与实例绑定的函数，和普通函数不同，方法可以直接访问实例的数据；   
    def getName(self):
        return self.name
    
    def getSex(self):
        return self.__sex
    

p = Person(u"leo")
print p
print p.name
print p.getName()

p.age = 15
print p.age

# print p.__sex    __开头的对象属性不能直接访问, 会报错.
print p.getSex()
print dir(p)
