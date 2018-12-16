"""单例模式简介"""

"""
使用意图:
确保类有且只有一个对象被创建
提供一个访问点是程序可以全局访问该对象
控制共享资源的并行访问

应用实例: 数据库  日志 单一实例的程序

实现方法: 将构造函数私有化,并创建一个函数来完成对象的私有化
"""


class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


# print(Singleton())      # 两次的内存空间是一样的
# print(Singleton())      # 创建之前会检查对象是否存在, 如果已经存在便给你返回之前存在的   __new__


# 单例中的懒汉式实例化
class Singleton1(object):
    __instance = None

    def __init__(self):
        if not self.__instance:
            print('__init__ method')
        else:
            print('singleton :', self.get_instance())

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = Singleton1()
        return cls.__instance


# s = Singleton1()   # 只调用了初始化方法 而没有创建实例

# 调用初始化方法  instance被修改了  此时实例的内存空间给instance属性了
# print(s.get_instance(), '懒汉式单例模式的实现方式')

# s1 = Singleton1()
# print(s1, '===========第二次调用')       # cls.instance属性的内存和s 的一样    再次调用get_instance内存不会再被修改
# print(Singleton1(), '===========第三次调用')



