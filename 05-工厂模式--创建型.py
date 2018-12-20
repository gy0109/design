"""
工厂函数的优点:
1, 松耦合,对象的创建不依赖与类的
2, 客户端无需知道对象创建的过程,只需知道需要传递的接口,方法和参数---简化了客户端的实现
3, 可轻松的添加其他类来创建其他类型的对象,最简单的情况下只需要传进一个参数便可以更换一种类型的对象
4, 可以实现重用对象
"""
from abc import ABCMeta, abstractmethod


# 1,简单工厂模式: 创建对象  不让用户知道创建的逻辑过程
class Animal(metaclass=ABCMeta):    # 声明元类
    @abstractmethod
    def do_say(self):
        pass


class Cat(Animal):
    def do_say(self):
        print('miaomiao')


class Dog(Animal):
    def do_say(self):
        print('wangwang')


class ForestFactory(object):
    def make_sound(self, object_anm):
        return eval(object_anm)().do_say()


# 2,工厂方法模式: 创建对象  让子类指定谁创建
class Section(metaclass=ABCMeta):
    @abstractmethod
    def describe(self):
        pass


class PersonalSection(Section):
    def describe(self):
        print('PersonalSection')


class AlbumSection(Section):
    def describe(self):
        print('AlbumSection')


class PatentSection(Section):
    def describe(self):
        print('PatentSection')


class PublicationSection(Section):
    def describe(self):
        print('PublicationSection')


class Profile(metaclass=ABCMeta):
    def __init__(self):
        self.sections = []
        self.createprofile()

    @abstractmethod
    def createprofile(self):
        pass

    def get_sections(self):
        return self.sections

    def add_sections(self, section):
        return self.sections.append(section)


class Linkedin(Profile):
    def createprofile(self):
        self.add_sections(PersonalSection())
        self.add_sections(PatentSection())
        self.add_sections(PublicationSection())


class Facebook(Profile):
    def createprofile(self):
        self.add_sections(PersonalSection())
        self.add_sections(AlbumSection())


"""
工厂模式的优点:
1, 具有更大的灵活性,通用性更强 向客户端开放了一个创建对象的方法
2, 松耦合  使用继承和子类来决定要创建哪个对象
3, 用于创建一个产品
"""


# 3,抽象工厂模式: 创建一系列相关对象而无需指定或公开其具体类的接口----课提供其他工厂的对象,在器内部进行创建对象
"""
抽象工厂包含一个或多个工厂方法来创建一系列相关的对象 -- 用于创建一系列相关产品  
使用组合将创建委托给其他类
"""


class PizzaFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_vegpizza(self):
        pass

    @abstractmethod
    def create_non_vegpizza(self):
        pass


class IndianPizzaFactory(PizzaFactory):
    def create_vegpizza(self):
        return DeluxVegpizza()

    def create_non_vegpizza(self):
        return ChickenPizza()


class USPizzaFactory(PizzaFactory):
    def create_vegpizza(self):
        return MexicanVegPizza()

    def create_non_vegpizza(self):
        return HamPizza()


class VegPizza(metaclass=ABCMeta):
    @abstractmethod
    def prepare(self):
        pass


class NonVegPizza(metaclass=ABCMeta):
    @abstractmethod
    def serve(self, VegPizza):
        pass


class DeluxVegpizza(VegPizza):
    def prepare(self):
        print(type(self).__name__, 'deluxvegpizza')


class ChickenPizza(NonVegPizza):
    def serve(self, vegpizza):
        print(type(self).__name__, type(vegpizza).__name__, 'Chickenpizza')


class MexicanVegPizza(VegPizza):
    def prepare(self):
        print(type(self).__name__, 'MexicanVegPizza')


class HamPizza(NonVegPizza):
    def serve(self, vegpizza):
        print(type(self).__name__, type(vegpizza).__name__, 'HamPizza')


# 用户制作pizza的工厂
class PizzaFactory(object):
    def __init__(self):
        # self.factory = None
        # self.NonVegPizza = None
        # self.VegPizza = None
        pass

    def make_pizza(self):
        for fac in [IndianPizzaFactory, USPizzaFactory]:
            factory = fac()
            NonVegPizza = factory.create_non_vegpizza()
            VegPizza = factory.create_vegpizza()
            VegPizza.prepare()
            NonVegPizza.serve(VegPizza)


if __name__ == '__main__':
    # ForestFactory().make_sound(input('请输入要听的动物种类:'))    # 简单工厂函数
    # profile = eval(input('请输入要写的文档类型:').capitalize())()
    # print('要写的类型是:', type(profile).__name__, '他的属性有:', profile.get_sections())

    PizzaFactory().make_pizza()
