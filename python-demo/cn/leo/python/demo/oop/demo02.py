# coding: utf-8
# from cn.leo.python.demo.oop.demo01 import Person as Persn
import cn.leo.python.demo.oop.demo01 as demo01
class Person(object):  # 括号中表示该类的父类，如果没有自定义父类，一般用object
    
    def __init__(self, name, sex="man"):
        self.name = name
        self.__sex = sex
     
    def get_name(self):
        return self.name
    
    def get_sex(self):
        return self.__sex
    
    def __str__(self):
        return u"Person[name=\"%s\", sex=\"%s\"]" % (self.name, self.__sex)
    
    
p = Person("tom")
print(str(p))

pp = demo01.Person("Lily")
print(pp.get_name())

