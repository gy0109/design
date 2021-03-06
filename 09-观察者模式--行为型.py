"""
行为型模式:
关注对象的责任,用来处理对象之间的交互,从而实现更强大的功能,    对象之间要能够交互,并且松散耦合
"""
from abc import ABCMeta, abstractmethod


class Subject(object):
    def __init__(self):
        self.__observers = []

    def register(self, observer):
        self.__observers.append(observer)

    def notify_all(self, *args, **kwargs):
        for observer in self.__observers:
            observer.notify(self, *args, **kwargs)


class Observer1:
    def __init__(self, subject):
        subject.register(self)

    def notify(self, subject, *args):
        print(type(self).__name__, args, subject, 'observer1')


class Observer2:
    def __init__(self, subject):
        subject.register(self)

    def notify(self, subject, *args):
        print(type(self).__name__, args, subject, 'observer2')


class NewsPublisher:      # 给订户的接口  实例化为一个对象
    def __init__(self):
        self.__subscribers = []    # 所有订户的列表
        self.__latest_news = None

    def attach(self, subscriber):   # 注册订户-- 添加到订户表
        self.__subscribers.append(subscriber)

    def detach(self):
        return self.__subscribers.pop()   # 注销订户 -- 删除订户表

    def subscribers(self):   # 获取订户表
        return [type(x).__name__ for x in self.__subscribers]

    def notify_subscribers(self):   # 遍历订户表  调用订户的方法
        for sub in self.__subscribers:
            sub.update()

    def add_new(self, news):   # 添加新消息
        # self.__subscribers.append(news)
        self.__latest_news = news

    def get_news(self):   # 获取消息
        return self.__latest_news


class Subscriber(metaclass=ABCMeta):   # 订户抽象基类
    @abstractmethod
    def update(self):
        pass


class EmailSubscriber(Subscriber):     # email订户  具体观察者
    def __init__(self, publisher):
        self.publisher = publisher     # 新闻发布者
        self.publisher.attach(self)

    def update(self):                  # 通知添加新的新闻
        print(type(self).__name__, self.publisher.get_news())


class SMSSubscriber(Subscriber):
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        print(type(self).__name__, self.publisher.get_news())


class AnyOtherSubscriber(Subscriber):
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        print(type(self).__name__, self.publisher.get_news())


if __name__ == '__main__':
    # subject = Subject()
    # Observer1(subject)
    # Observer2(subject)
    # subject.notify_all('not!!!')
    # print(type(subject).__name__, subject, 'Subject')

    news_publisher = NewsPublisher()
    for Subscribers in [SMSSubscriber, EmailSubscriber, AnyOtherSubscriber]:
        Subscribers(news_publisher)
    print('Subscribers:', news_publisher.subscribers())

    news_publisher.add_new('hello world')
    news_publisher.notify_subscribers()

    print('Detached: ', type(news_publisher.detach()).__name__)
    print('Subscribers: ', news_publisher.subscribers())

    news_publisher.add_new('second world')
    news_publisher.notify_subscribers()


"""
观察者模式的通知方式: 
1,拉模型:
2,推模型:
"""
