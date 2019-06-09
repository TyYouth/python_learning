"""
内容参考:github@jackfrued/Python-100-Days/Day08&09
面向对象编程
"""
# from abc import ABCMeta, abstractclassmethod
# class person(object, metaclass=ABCMeta):
# 使用 ABCMeta元类 和 abstractclassmethod包装器 可将类抽象化


class person(object):

    # __slots__ 限定自定义类型对象只能某些属性, 只对当前类对象生效, 对子类不起作用
    __slots__ = ('name', '_age', '_gender')

    # __init__:用于创建对象时进行初始化操作的特殊方法
    # 属性前缀 _ 来声明属性受保护, 不建议直接访问
    # 类的方法第一个参数为 self, 表示当前对象实例(地址)
    def __init__(self, name, age):
        self.name = name
        self._age = age

    # 静态方法: 可在对象未创建前使用的方法
    @staticmethod
    def is_person(age):
        is_person = True
        if age > 150:
            is_person = False
        return is_person

    # # 动态类方法
    # @classmethod
    # 类方法的第一个参数 cls 表示该类自身
    # def person_info(cls):
    #     student = person('xiaoming', age)
    #     return cls(student)

    # 访问器 - getttr方法
    @property
    def age_get(self):
        return self._age

    # 修改器, getter_name.setter 格式, 需对应
    @age_get.setter
    def age_set(self, age):
        self._age = age

    @property
    def gender(self):
        return self._gender

    def study(self, course_name):
        print("%s is studying %s" % (self.name, course_name))

    def watch_movie(self):
        if self._age < 18:
            print("%s is %d years old and can watch cartoon only" %
                  (self.name, self._age))
        else:
            print("%s is %d years old and is watching adult video" %
                  (self.name, self._age))

    # __ 前缀表示私有化方法
    def __fighting(self):
        print("%s is fighting with other" % (self.name))

    # 内部应用私有化方法
    # @abstractclassmethod
    # 如果不注释@abstractclassmethod 则person1 会创建对象失败
    # 是因为如果将person 进行抽象化, 使其他类可以继承它
    def fighting(self):
        self.__fighting()


# 继承与父类方法的重写
# 继承对象 person
class teacher(person):
    def __init__(self, name, age, title):
        # 使用 super()方法继承父辈属性
        super().__init__(name, age)
        self._title = title

    def teach(self, course_name):
        print("%s %s is teaching %s" % (self._title, self.name, course_name))

    # 父类方法重写?
    def fighting(self):
        print('a teacher should not fight with anybody')


def main():
    age1 = int(input("请输入人物年龄:"))
    if person.is_person(age1):
        student1 = person('xiaoming', age1)
        student1.watch_movie()
        student1.study("math")
        # 'person' object has no attribute '__fighting'
        # student1.__fighting()
        # 使用 _object__private 来引用私有化方法
        student1._person__fighting()
        student1.fighting()
        # age_set 使用修改器修改属性
        student1.age_set = 17
        student1.watch_movie()
        # __slots__ 绑定的属性
        student1._gender = 'man'
        print(student1._gender)
        # student1.person_info()
    else:
        print("are you sure???")

    age2 = int(input("请输入人物年龄:"))
    if person.is_person(age2):
        teacher1 = teacher('laowang', age2, 'professor')
        teacher1.teach('Chinese')
        teacher1.watch_movie()
        teacher1.fighting()
    else:
        print("are you sure???")


if __name__ == '__main__':
    main()

