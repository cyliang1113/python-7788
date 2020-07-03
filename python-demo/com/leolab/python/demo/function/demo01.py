# coding: utf-8

def myAbs(x):
    if x >= 0:
        return x
    else:
        return -x
    
    
# print myAbs(-5)
# print myAbs("-qq")


def swith(x, y):
    return y, x;


# print swith(1, 2)
t = (1, 2)
swith(*t)  # 相当于switch(1, 2)



# 函数有默认参数
def power(x, n=2):
    s = 1
    while n:
        n = n - 1
        s = s * x
    return s

# print power(3, 3)
# print power(3)

# 函数默认参数，在函数定义时就确定的，每次调用函数默认参数都是最初的那个值
# 要注意基本类型和对象类型
def a(x, n=[], m=1):
    n.append(1)
    m = m + 1
    print(len(n))
    print(u"m=", m)

a(100)
a(100)
a(100)

def get_stu(name, age = 20):
    age = age + 1
    print(age)
    return (name, age)
print(get_stu('leo'))
print(get_stu('leon'))

def aa(name, clazz = []):
    clazz.append('a')
    print(clazz)
    return (name, clazz)
print(aa('leo'))
print(aa('leon'))

def aaa(*arg):
    print(type(arg))
    print(arg)

aaa(11, 'leo')
ij = int(1)
def bb(name, **arg):
    print(name)
    print(arg)

bb('leo', sex = 'male')
bb('leo', sex = 'female')

print(type(1))
print(type(int(1)))

def ccc(num):
    num.append('11');
    return num
xx = ['00']
print(xx)
print(ccc(xx))
print(xx)

def ddd(name, age):
    print('name:' + name)
    print('age:' + str(age))

xxx = {'name': 'Tom', 'age': 25}
ddd(name='Jack', age=26)
ddd(**xxx)  # **xxx等效于name='Jack', age=26



