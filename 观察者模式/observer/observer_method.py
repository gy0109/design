from .observers import Subscriber


class EmailSubscriber(Subscriber):     # email订户  具体观察者
    def __init__(self, publisher):
        self.publisher = publisher     # 观察者
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

