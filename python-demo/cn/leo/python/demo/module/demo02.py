# coding: utf-8


# 模块
# 安装第三方模块一般使用pip命令
# https://pypi.python.org/pypi
import add

from add import add2

add
print(add)
print(add.add(1, 2))
print(add.sum)
print(add2(2, 2))

print(add.__name__)
print(__name__)

