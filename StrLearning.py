#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Learning for type str build-in method
"""


class StrLearning(object):
	field_str = "For Test"

	def __init__(self):
		self.test_str = "Hello World"

	def count_str(self, sub_str):
		"""str.count(string, beg=0, end=len(str)) 统计str中,beg-end 范围内出现string的次数"""
		return self.test_str.count(sub_str)

	def ends_with(self, sub_str, beg=0):
		"""
		str.endswith(string, beg=0, end=len(str)), str.startswith(string, beg=0, end=len(str)) str在范围内是否以string结尾或开头
		:param sub_str:
		:param beg:
		:return:
		"""
		return self.test_str.endswith(sub_str, start=beg, end=len(sub_str))

	def find_str(self, target_str):
		"""
		str.find(string, beg=0, end=len(str)) 如果str的范围存在string则返回第一个匹配的索引值, 不存在返回-1, rfind()从右开始查找
		:param target_str: str to find
		:return: first index of target str
		"""
		return self.test_str.find(target_str)

	def index(self, target_str):
		"""
		str.index(string, beg=0, end=len(str)) 与find类似, 不过不存在则抛出ValueError的异常, rindex()
		:param target_str:
		:return:
		"""
		return self.test_str.index(target_str)

	@staticmethod
	def join_by(splice, *str_args):
		"""str.join(iterble_sequence) 将可迭代序列以str拼接起来, 且该序列元素类型相同, 否在抛出TypeError异常"""
		return splice.join(str_args)

	@staticmethod
	def to_lower(string):
		"""
		str.lower() 将str字符串中的大写转为小写字符,其他不变,  str.upper()
		swapcase() 将字符串中大写转换为小写，小写转换为大写
		"""
		return string.lower()

	@staticmethod
	def aligned(a_string, width, method='center', fill_char=' '):
		"""
		str.center(width, fillchar), str.rjust(width, fillchar), str.ljust(width, fillchar)
		返回以指定宽度width的以str居中,左对齐,右对齐的, 如果原字符串不够width,则以fillchar补充,
		如果超出指定width则原样返回(不做切片处理)  str.zfill(width) = str.rjust(width,fillchar='0')
		:param a_string:
		:param method:
		:param width:
		:param fill_char:
		:return:
		"""
		if method == "center":
			return a_string.center(width, fill_char)
		elif method == "right":
			return a_string.ljust(width, fill_char)
		elif method == "left":
			return a_string.right(width, fill_char)
		else:
			print("un-support method")

	@staticmethod
	def replace(origin_string, old_string, new_string):
		"""str.replace(old_str, new_str, [max_times])将str中的old_str替换成new_str,
		且最多不超过max_times次, 默认值为 -1, 替换所有"""
		return origin_string.replace(old_string, new_string)

	@staticmethod
	def split_by(splice, a_string):
		"""
		str.split(chars='',maxsplit=str.count(chars)) 通过指定字符(默认为所有空字符空格, 换行,制表符号\t)为分隔符,
		返回分隔后的字符串列表, 分隔次数maxsplit(默认为-1, 即分隔所有)
		:param splice:
		:param a_string:
		:return:
		"""
		return a_string.split(splice)

	@staticmethod
	def strip(string_to_strip, chars=' '):
		"""
		str.strip(chars=' ') 截掉str头尾的指定字符chars, rstrip(), lstrip()
		:param string_to_strip:
		:param chars:
		:return:
		"""
		return string_to_strip.strip(chars)


if __name__ == "__main__":
	str_learning = StrLearning()
	print(str_learning.field_str)
	sub_str_numb = str_learning.count_str(sub_str="o")
	print(sub_str_numb)
	print(StrLearning.join_by('/', 'a', 'b', 'c'))
	print(StrLearning.to_lower("AbcD"))
	print(StrLearning.strip(" Hello!"))
	print(StrLearning.aligned("abc", width=5))
	print(" Hello".strip())
