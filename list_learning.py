#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
list 列表, 循环
内容参考: 菜鸟python3教程 list https://www.runoob.com/python3/python3-list.html
列表 list = [v0, v1, v2, v3]  可进行操作: 索引, 切片, 加, 更新, 乘,删, 检查成员
"""

list_type = [1, 3, 4, 5]
# 更新: 直接替换 list[1]=v3 即可, 拼接组合 list1 + list2
list_type[1] = 2
print(list_type)
# 从指定位置开始打印
# 索引,切片: [1] 第2个元素 [1:]从第二个元素开始,[::2] 遍历, 间隔为2: [v1,v3], [-1]倒数第一个元素, [::-1] 遍历, 间隔为-1
print(list_type[1:])
print(list_type[::2])
print(list_type[::-1])
"""
python的list内置方法大多无返回值, 直接更新list
"""
# list.append(v) 列表末尾添加新元素, list.count (obj) 统计列表中obj
list_type.append(3)
# list.sort(key=none, reverser=Flase) 将列表元素排序, 默认reverse=Flase 升序, key为排序依据, 某元素或子元素; 内置函数 sorted()
list_type.sort(reverse=True)
print(list_type)
# list.reverse() 将列表反向
list_type.reverse()
print(list_type)
# list.pop(index=-1)移除一个元素(默认最后一个index=-1的元素),
list_type.pop()
print(list_type)
# list.remove(obj)移除第一个匹配的obj, 如果obj不在,则ValueError
# list_type.remove(6)
# list.index(obj,strat=0, end=len(list)) 返回list中第一个obj 的索引index
list_type.append(2)
print(list_type.index(2))

# for/else 循环:
for n in range(2, 10):
	for x in range(2, n):
		if n % x == 0:
			print(n, 'equals', x, '*', n / x)
			break
	# 其实应该是相当于n 还属于第一个for的方法域内, 将不满足第二个for的n打印出
	else:
		# loop fell through without finding a factor
		print(n, 'is a prime number')
