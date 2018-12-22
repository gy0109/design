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


class NewsPublisher:
    def __init__(self):
        self.__subscribers = []
        self.__latest_news = None

    def attach(self, subscriber):
        self.__subscribers.append(subscriber)

    def detach(self):
        return self.__subscribers.pop()

    def subscribers(self):
        return [type(x).__name__ for x in self.__subscribers]

    def notify_subscribers(self):
        for sub in self.__subscribers:
            sub.update()

    def add_new(self, news):
        self.__subscribers.append(news)

    def get_news(self):
        return self.__latest_news


class Subscriber(metaclass=ABCMeta):
    @abstractmethod
    def update(self):
        pass


class EmailSubscriber(Subscriber):
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
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

    news
