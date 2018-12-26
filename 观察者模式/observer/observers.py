from abc import ABCMeta, abstractmethod


class Subscriber(metaclass=ABCMeta):   # 订户抽象基类
    @abstractmethod
    def update(self):
        pass

