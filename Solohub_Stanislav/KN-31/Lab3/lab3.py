class YouTubeChannel:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, user):
        self.subscribers.append(user)

    def upload_video(self, video_name):
        print(f"🎬 КАНАЛ: Завантажено відео '{video_name}'")
        for user in self.subscribers:
            user.notify(video_name)

class Subscriber:
    def __init__(self, name):
        self.name = name

    def notify(self, video_name):
        print(f"   🔔 {self.name} отримав сповіщення: Дивись нове відео '{video_name}'!")

channel = YouTubeChannel()

user1 = Subscriber("Олег")
user2 = Subscriber("Марія")

channel.subscribe(user1)
channel.subscribe(user2)

channel.upload_video("Python за 5 хвилин")