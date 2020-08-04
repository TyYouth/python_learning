"""
map 将一个函数映射到输入列表上的所有元素上面
用法 map(function_to_apply, function_input_values_list) (the list element can be function)
"""

"""
非map写法:
items = [1, 2, 3, 4, 5]
squared = []
for i in items:
    squared.append(i**2)
"""
items = [j for j in range(1, 5)]
print(list(map(lambda x: x ** 2, items)))  # list 是为了兼容python版本

funcs_list = [lambda x: x * x, lambda x: x + x]  # 函数对象列表
for i in range(3):
    print(list(map(lambda x: x(i), funcs_list)))

"""
filter 过滤列表中的元素, 并返回符合要求的元素列表
类似for, 但是速度更快
"""
less_than_zero_list = list(filter(lambda x: x > 0, [j for j in range(-100, 4)]))
print(less_than_zero_list)

"""
需要对一个列表进行计算并返回结果时, reduce
"""
from functools import reduce

result = reduce((lambda x, y: x * y), [j for j in range(1, 5)])
print(result)  # 24 = 1 * 2 * 3 * 4
