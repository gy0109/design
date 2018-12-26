
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
