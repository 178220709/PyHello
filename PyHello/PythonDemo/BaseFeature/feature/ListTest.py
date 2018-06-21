# -*- coding: utf-8 -*-
array = [1, 2, 3]
print(array[0])
# 输出 1
array[0] = 'a'
print(array)
# 输出 ['a', 2, 3]


test = [0]  # 列表可以这样定义
print(type(test))  # 输出<type 'list'>
test = [0, ]  # 也可以这样定义
print(type(test))  # 输出<type 'list'>
test = (0,)  # 元组可以这样定义
print(type(test))  # 输出<type 'tuple'>
test = (0)  # 但不能这样定义，Python会认为它是一个括号表达式
print(type(test))  # 输出<type 'int'>
test = 0,  # 也可以省略括号，但要注意与C的逗号表达式不同
print(type(test))  # 输出<type 'tuple'>

a = 1
b = 2
a, b = b, a

a = [11, 22, 33, 44, 11, 22, 11, 11, 22, 22, 33, 33, 33]
b = sorted(set(a))
print(b)
# 输出 set([33, 11, 44, 22])

a = ["11", "22", "33"]
b = ["11", "33"]
c = set(a) & set(b)
print(c)
# 输出 set(['11', '33'])
