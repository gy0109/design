from .observer import NewsPublisher

if __name__ == '__main__':
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
