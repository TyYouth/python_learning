#!/usr/bin/env python
# -*- coding: utf-8 -*-
import collections

"""
https://docs.python.org/3/library/collections.html#
class collections.defaultdict([default_factory[, ...]])
Returns a new dictionary-like object. defaultdict is a subclass of the built-in dict class. 
It overrides one method and adds one writable instance variable. 
The remaining functionality is the same as for the dict class and is not documented here.

The first argument provides the initial value for the default_factory attribute; `it defaults to None.` 
All remaining arguments are treated the same as if they were passed to the dict constructor, including keyword arguments.
"""
# 下面这样访问, 仍然会存在KeyError
# If the default_factory attribute is None, this raises a KeyError exception with the key as argument.
# dict_type = collections.defaultdict()
# print(dict_type["hello"])  # KeyError: 'hello'

# If default_factory is not None, it is called without arguments to provide a default value for the given key,
# this value is inserted in the dictionary for the key, and returned.
# 从下面输出可以看出, defaultdict 根据default_factory的类型来构建具有默认值Key的对应类型来避免KeyError
dict_type = collections.defaultdict(dict)
print(dict_type["hello"])  # {}
dict_type = collections.defaultdict(list)
print(dict_type["hello"])  # []

colours = (
    ('Yasoob', 'Yellow'),
    ('Ali', 'Blue'),
    ('Arham', 'Green'),
    ('Ali', 'Black'),
    ('Yasoob', 'Red'),
    ('Ahmed', 'Silver'),
)

favourite_colours = collections.defaultdict(list)

for name, colour in colours:
    favourite_colours[name].append(colour)

# 第一次输入时会, 自动添加键值对,
# defaultdict(<class 'list'>, {'Yasoob': ['Yellow', 'Red'], 'Ali': ['Blue', 'Black'], 'Arham': ['Green'], 'Ahmed': ['Silver']})
print(favourite_colours)
