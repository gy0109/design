"""单例模式简介"""

"""
使用意图:
确保类有且只有一个对象被创建
提供一个访问点是程序可以全局访问该对象
控制共享资源的并行访问

应用实例: 数据库  日志 单一实例的程序

实现方法: 将构造函数私有化,并创建一个函数来完成对象的私有化
"""


# 1, 单例的经典实现模式
class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


# print(Singleton())      # 两次的内存空间是一样的
# print(Singleton())      # 创建之前会检查对象是否存在, 如果已经存在便给你返回之前存在的   __new__


# 2,单例中的懒汉式实例化
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


# 3,模块导入式的实现方式
"""
当一个模块被导入的时候就会被实例化,但是再次被导入的时候就不会实例化了
如果没导入就导入并实例化   导入就但会模块的实例化对象
"""


# 4, Monostate单例模式: 所有对象共享资源
class Borg:
    __shared_state = {'1': '2'}

    def __init__(self):
        self.x = 1
        self.__dict__ = self.__shared_state

    # def __new__(cls, *args, **kwargs):
    #     obj = super(Borg, cls).__new__(cls)
    #     obj.__dict__ = cls.__shared_state
    #     return obj


# b = Borg()
# b1 = Borg()
# b.x = 4        # 修改了资源,
# print('b: ', b)
# print('b1: ', b1)
# print('b: ', b.__dict__)
# print('b1: ', b1.__dict__)


# 单例和元类的应用
class MyInt(type):
    def __call__(cls, *args, **kwargs):
        print(*args, **kwargs)
        return type.__call__(cls, *args, **kwargs)


class Int(metaclass=MyInt):
    def __init__(self, x, y):
        self.x = x
        self.y = y


i = Int(4, 5)     # 元类是类的类
print(i)


class MetaSingleton(type):
    __instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls.__instances[cls]


class Logger(metaclass=MetaSingleton):
    pass


logger1 = Logger()
logger2 = Logger()
print(logger1, logger2)     # 元类创建单例  元类对实例化对象的创建具有更好的控制权 为了控制类的创建和初始化 用元类将覆盖__new__和__init__


