from abc import ABC, abstractmethod

class Message(ABC):
    @abstractmethod
    def send(self):
        pass

class EmailMessage(Message):
    def send(self):
        print("📧 Відправлено Email: 'Вітаємо! Ваш акаунт активовано.'")

class SMSMessage(Message):
    def send(self):
        print("📩 Відправлено SMS: 'Ваш код підтвердження: 9452'")

class PushMessage(Message):
    def send(self):
        print("🔔 Відправлено Push: 'У вас нове повідомлення в додатку!'")

class MessageFactory:
    @staticmethod
    def create_message(msg_type: str) -> Message:
        if msg_type == "email":
            return EmailMessage()
        elif msg_type == "sms":
            return SMSMessage()
        elif msg_type == "push":
            return PushMessage()
        else:
            raise ValueError("Невідомий тип повідомлення!")

message1 = MessageFactory.create_message("email")
message1.send()

message2 = MessageFactory.create_message("sms")
message2.send()

message3 = MessageFactory.create_message("push")
message3.send()
