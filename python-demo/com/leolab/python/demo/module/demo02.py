# coding: utf-8


# 模块
# 安装第三方模块一般使用pip命令
# https://pypi.python.org/pypi
import com.leolib.python.demo.module.add_module as add_module

from com.leolib.python.demo.module.add_module import add2

print(add_module)
print(add_module.add(1, 2))
print(add_module.sum)
print(add2(2, 2))

print(add_module.__name__)
print(__name__)

