"""
类和对象是面向对象的实体,结构型设计模式是类和对象之间的交互
类模式: 通过继承描述抽象,从而提供更有用的程序接口

门面模式: 定义一个高级接口将子系统进行组合实现更简单的使用子系统 -- 并不是封装子系统  而是将底层子系统进行组合  促进了与子系统的解耦
"""

# UML类图
# 1,门面: 将一组子系统进行组合成一个高级的接口方便给客户端使用 -- 将客户端的请求委派给相应的子系统对象
# 2,系统: 一组混乱的子系统, 系统是一个类  是一组不同人物类型的类组合, 处理门面分配的工作  并不引用门面
# 3,客户端:与子系统记性通信并完成工作,不用担心复杂性    实例化门面的类 像门面提出请求

# 门面模式: 


class EventManager(object):
    def __init__(self):
        print('Event Manager: Let me talk to the folks !\n')

    def arrange(self):
        self.hotelier = Hotelier()
        self.hotelier.book_hotel()
        self.florist = Florist()
        self.florist.set_flower_requirements()
        self.caterer = Caterer()
        self.caterer.ser_cuisione()
        self.musician = Musician()
        self.musician.set_music_type()


class Hotelier(object):
    def __init__(self):
        print('Hotelier')

    def __is_available(self):
        return True

    def book_hotel(self):
        if self.__is_available():
            print('requirements the booking\n\n')


class Florist(object):
    def __init__(self):
        print('Florist')

    def set_flower_requirements(self):
        print('set_flower_requirements')


class Caterer(object):
    def __init__(self):
        print('Caterer')

    def ser_cuisione(self):
        print('ser_cuisione')


class Musician(object):
    def __init__(self):
        print('Musician')

    def set_music_type(self):
        print('set_music_type')


class You(object):
    def __init__(self):
        print('you')

    def ask_event_manager(self):
        print('you to event_manager')
        EventManager().arrange()

    def __del__(self):
        print('干完活  撤销团队')


if __name__ == '__main__':
    You().ask_event_manager()
