"""
内容参考: github@jackfrued/Python-100-Days/Day12
          blog@deerchao/正则表达式30分钟入门教程
          菜鸟教程网/python3/正则表达式
"""
import re
# 正则表达式语法
# 正则表达式表示一串特殊的字符串序列, 用于检查对象是否与某种模式匹配
"""
. 匹配换行符以外任意字符 \w 匹配字母,数字,下划线或汉字
\s 匹配任意空白符 \d 数字 
^ 字符串的开始 $ 结束 这两个都匹配一个位置
反义: \W 匹配不是\w的字符 \S \D 
      \B 不是单词开头或结束的位置
      [^x] 匹配除了x以外的任意字符 [^aeiou] 除了aeiou这个元音之外的任意字符 
转义: \\->\, \* ->*
重复: * 重复零次或更多次, + 一次或更多次, ? 零次或一次
      {n} 重复n次, {n,} n次或更多次 {n,m} n到m次
字符范围: [0-9a-zA-Z] 等同于\w
分枝规则: 指有几种规则, 满足其中任意一种则为匹配, | 分隔不同规则, 注意规则顺序
如 0\d{2}-\d{8}|0\d{3}-\d{7} 匹配 012-12345678 或 0123-1234567
分组: 重复多个字符的方法, 用(子表达式) 如 (\d{1,3}) 
组号组名: 每个分组会自动拥有一个组号用于重复引用, 规则: 从左到右,以分组左括号为标志
      (exp) 匹配exp表达式, 并自动分配组名
      (?<name>exp) 或 (?'name'exp) 匹配,并命名组名为name
      (?:exp) 匹配, 但是不捕获, 不分配组号
零宽断言: 查找某些内容是否满足一定条件
      (?=exp) 匹配exp前面的位置, (?>=exp) 后面
      (?!exp) 后面跟的不是exp的位置 (?<!exp)前面不是
注释: (?#comment)
"""

# python3 中re 模块对正则表达式
"""
groups(): 返回包含所有小组字符串的元组
sub(pattern, repl, string, count=0, flags=0): 检索与替换, repl 要替换成的字符串,可为函数
findall(string[, pos[, endpos]]): 匹配所有子串
finditer():与findall类似, 匹配所有子串, 并将它们作为迭代器返回
split():
purge(): 清除隐性编译的正则表达式的缓存
"""
# python3 正则表达式修饰符
"""
re.l 对大小写不敏感, L 做本地识别匹配
M 多行匹配, 影响^ 和 $, 
S 使.匹配包括换行在内的所有字符
"""


def qq_number_verify():
    is_over = False
    verify_again = True
    while verify_again:
        while not is_over:
            username = input("请输入用户名:")
            qq_number = input("请输入qq账号:")
            m1 = re.match(r'^[0-9a-zA-Z_]{6,20}$', username)
            if not m1:
                print("该用户名无效")
            m2 = re.match(r'^[1-9]\d{4,11}$', qq_number)
            if not m2:
                print("该qq号无效")
            if m1 and m2:
                is_over = True
                verify_again = False
                print("验证通过")
            else:
                is_over = False
                verify_again = input("再次验证?(yes|no)") == 'yes'


# match(pattern, string, flags): 只匹配字符串的开始
# search(pattern, string, flags): 扫描整个字符串并返回第一个成功的匹配
# group(num=0):
def match_search():
    line = "Cats are smarter than dogs"
    match_object = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)
    if match_object:
        print("matchobject.group():", match_object.group())
        print("matchobject.group(1)(组1则(.*)):", match_object.group(1))
        print("matchobject.group(2)(组2则(.*?)):", match_object.group(2))
    else:
        print('no string to match')
    # match 与 search 的差异
    match_object2 = re.match(r'dogs', line, re.M | re.I)
    if match_object2:
        print("matchobject.group():", match_object.group())
    else:
        print('no string to match')
    search_object = re.search(r'dogs', line, re.M | re.I)
    if search_object:
        print("search_object.group():", search_object.group())
    else:
        print('no string to match')


# compile(pattern[,flags]): 用于编译正则表达式, 供match() 和search()使用
def compile_function():
    pattern_string = re.compile(r'\d+')
    m = pattern_string.match('string123')
    print(m)
    mpos = pattern_string.match('string123', 6, 8)
    print(mpos)
    print('mpos.group():', mpos.group())
    print('mpos.start():', mpos.start())
    print("mpos.end():", mpos.end())
    print('mpos.span():', mpos.span())
    s = pattern_string.search('string123')
    print("pattern_string.search():", s)
    print('s.group():', s.group())
    print('s.start():', s.start())
    print("s.end():", s.end())
    print('s.span():', s.span())
# 复杂的正则表达式练习


def main():
    # qq_number_verify()
    match_search()
    compile_function()
    phone = "2004-959-559 #号码"
    # 匹配字符串中的非数字字符串, 并将其去掉
    print(re.sub(r'\D', "", phone))


if __name__ == '__main__':
    main()
