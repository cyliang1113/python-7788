# coding: utf-8


class Person(object):
    def __init__(self, name):
        self.__name = name
        
    @property
    def name(self):
        return self.__name
    
    def __enter__(self):
        print "__enter__()..."
        return self
        
    def __exit__(self, e_t, e_v, t_b):
        print e_t
        print e_v
        print t_b
        print "__exit__()..."
        
with Person("xixi") as p:
    print p.name
    1/0
