print("hello world".title())
print("--")
name = "tom"
print(name.title())
print(name.upper())
print(name.lower())

first_name = "curry"
last_name = "tom"
print(first_name.title() + " " + last_name.title())

abc = ['a', 'b', 'c', 'd', 'e']
print(abc)
print(abc[2])
print(abc[-1])  # -1表示最后一个

abc.append('d')  # 末尾追加一个元素
print(abc)

abc.insert(1, 'aa')  # 指定位置插入元素
print(abc)

end = abc.pop()  # 弹出末尾元素
print(abc)
print(end)

print(len(abc))  # 计算列表长度

for x in abc:  # 遍历列表
    print(x)

num = list(range(1, 11))
print(num[0:-1])

t = (100, 200)  # 元组元素不能修改
print(t)

tt = 'abc'
tu = (tt, '123')
print(tu)
tt = 'cba'
print(tu)

for x in num:
    if x % 2 == 0:
        print(x)

if True == True:
    print(True)

for x in num:
    if x % 2 == 1:
        print('111')
    elif x % 2 == 0:
        print('222')

if 11 in num:
    print('in')
else:
    print('not in')


dic = {'tom' : 25, 'lili' : 26}
print(dic)
print(dic['lili'])
dic['David'] = 35
print(dic)
del dic['tom']
print(dic)
for k, v in dic.items():
    print(k + " : " + str(v))

for k in dic.keys():
    print(k)

stu = {'name' : 'Tom', 'class' : ['cn', 'eg', 'math']}
for k, v in stu.items():
    print(v)


print(4 // 3)  # 整除

