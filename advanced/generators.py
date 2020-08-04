r"""
迭代: 从一个可迭代对象中取出元素的过程
可迭代对象就是能提供迭代器的任意对象(可支持遍历定义__iter__, 下标索引遍历__getitem__)
迭代器: 定义了 next(python2) 或 __next__方法
生成器: 也是一种迭代器, 但是只能迭代一次(只能不断next), 使用yied生出值,
(csv reader 就是一个迭代器, 只能next往下遍历, 但这从文件阅读器来讲, 是文件加载到内存后一行行的读的)
使用生成器的最佳引用的场景是: 不想同一时间见所有计算出来的大量结果分配到内存中去
"""


def fibon(n):
    """该函数没有return, 但是因为yield 会将每次yield的a 组装成一个可迭代对象
    这里可以简单想象成一个返回list类型的方法 [a1, a2, ..., an]"""
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b


def test(n):
    return [j for j in range(n)]


if __name__ == "__main__":
    gen = fibon(3)
    print(gen)  # <generator object> 使用了yield 的方法会返回生成器对象
    print(test(3))  # [0, 1, 2] 对比来说如果n 很大, 那么这里list占用内存就会很大
    next(gen)  # 可用next 遍历生成器
    test_string = "Hello, world"
    # for i in test_string:  # string 可遍历, 但是不可next, 因为它不是生成器, 迭代器
    #     print(i)
    # print(next(test_string))  # 'str' object is not an iterator
    string_inter = iter(test_string)
    print(next(string_inter))
