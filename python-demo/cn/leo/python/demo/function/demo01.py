# coding: utf-8

def myAbs(x):
    if x >= 0:
        return x
    else:
        return -x
    
    
print myAbs(-5)
print myAbs("-qq")


def swith(x, y):
    return y, x;


print swith(1, 2)

def power(x, n=2):
    s = 1
    while n:
        n = n - 1
        s = s * x
    return s

print power(3, 3)
print power(3)
