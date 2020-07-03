# coding: utf-8


class Person(object):  # 括号中表示该类的父类，如果没有自定义父类，一般用object

    def __init__(self, name, sex="man"):
        self.name = name
        self.__sex = sex

    def getName(self):
        return self.name

    def getSex(self):
        return self.__sex

    def __str__(self):
        return u"Person[name=\"%s\", sex=\"%s\"]" % (self.name, self.__sex)


p = Person("tom")
print(p)
print(Person.getName())
