#!/usr/bin/env python
# coding=utf-8

"""
dict 是一种可变容器(collections)模型, 且可以通过键值对的形式存储任意类型的对象
键值对以 : 分隔, dict_type = {key1: "str", key2: int, key3: bool}
键名应该唯一且不可变, 否则会被最后一个键值对覆盖, 可为字符串,数字, 元组, 但不能用列表
"""

dict_type = {'name': "test",
             'is_alive': 'True',
             'age': '21',
             1: '2',
             "empty": None
             }

print(len(dict_type))
print(dict_type.keys())  # keys获取所有键名
print(dict_type.values())
print(dict_type.items())  # items获取所有键值对(元组) (key, value)
for key, value in dict_type.items():
    # TypeError: can only concatenate str (not "bool") to str
    # TypeError: unsupported operand type(s) for +: 'int' and 'str'
    print(str(key) + " : " + str(value))

print(dict_type['name'])
# print(dict_type['Age'])  # 访问不存在的键名会有KeyError
print(dict_type.get("nonexist", None))  # dict.get(key, default=None) 不存在对应key时返回默认值

dict_type['name'] = "update"  # 修改值
dict_type['demo'] = "new"  # 添加新键值对
print(dict_type)

# update(**dict1, **dict2)
dict_type.update({'name': 'update'})


# 使用fromkeys(seq[, values]) 使用 key seq(iterable),默认值 对应的键值创建新dict,
new_dict = dict.fromkeys(['a', 'c', 'b'], 'Na')
print(new_dict)

# del 根据键名删除对应键值(不指定时删除整个dict), clear()清空
del new_dict['a']
print(new_dict)

print(new_dict.pop('b'), new_dict)  # pop 弹出该键值对

other_dict = new_dict.copy()
print(other_dict)
