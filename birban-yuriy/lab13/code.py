class NewsPublisher:
    def __init__(self):
        self.subscribers = []
        self.news = None

    def attach(self, subscriber):
        self.subscribers.append(subscriber)

    def detach(self, subscriber):
        self.subscribers.remove(subscriber)

    def notify(self):
        for sub in self.subscribers:
            sub.update(self.news)

    def add_news(self, news):
        self.news = news
        self.notify()

class Subscriber:
    def __init__(self, name):
        self.name = name

    def update(self, news):
        print(f"{self.name} отримав новину: {news}")

news_publisher = NewsPublisher()

alice = Subscriber("Аліса")
bob = Subscriber("Боб")

news_publisher.attach(alice)
news_publisher.attach(bob)

news_publisher.add_news("Новий випуск журналу доступний!")