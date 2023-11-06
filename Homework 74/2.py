class Channel:
    def __init__(self, name):
        self.name = name
        self.subscribers = []

    def add_subscriber(self, subscriber):
        self.subscribers.append(subscriber)

    def remove_subscriber(self, subscriber):
        self.subscribers.remove(subscriber)

    def publish_video(self, video):
        for subscriber in self.subscribers:
            subscriber.notify_new_video(video)

class Subscriber:
    def __init__(self, name):
        self.name = name

    def notify_new_video(self, video):
        print(f"{self.name} отримав сповіщення про нове відео на каналі: {video.channel_name}")


class Video:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.channel_name = "Мій канал"

    def __str__(self):
        return f"Назва: {self.title}\nОпис: {self.description}\nКанал: {self.channel_name}"

video = Video("Новий відеоурок", "HTML та CSS")

print(video)


channel = Channel("Мій канал")
subscriber = Subscriber("Олексій")
channel.add_subscriber(subscriber)
video = Video("Новий відеоурок", "HTML та CSS")
channel.publish_video(video)

# Перевірка, що підписник отримав сповіщення
print(subscriber.name)
