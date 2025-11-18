from abc import ABC, abstractmethod

# === 1. Adapter ===
class EuropeanSocket:
    def voltage(self): return 230
    def plug_type(self): return "Type C"

class AmericanSocket:
    def voltage(self): return 120
    def plug_type(self): return "Type A"

class Adapter:
    """Адаптер, який дозволяє підключити європейський пристрій до американської розетки"""
    def __init__(self, socket: EuropeanSocket):
        self.socket = socket

    def voltage(self):
        return 120  # знижує напругу для сумісності

    def plug_type(self):
        return "Type A"

# === 2. Decorator ===
class Notifier(ABC):
    @abstractmethod
    def send(self, message): pass

class EmailNotifier(Notifier):
    def send(self, message):
        print(f"Відправлено Email: {message}")

class SMSDecorator(Notifier):
    def __init__(self, notifier: Notifier):
        self.notifier = notifier
    def send(self, message):
        self.notifier.send(message)
        print(f"Відправлено SMS: {message}")

class SlackDecorator(Notifier):
    def __init__(self, notifier: Notifier):
        self.notifier = notifier
    def send(self, message):
        self.notifier.send(message)
        print(f"Відправлено Slack повідомлення: {message}")

# === 3. Facade ===
class CPU:
    def freeze(self): print("CPU заморожено")
    def execute(self): print("CPU виконує інструкції")

class Memory:
    def load(self): print("Пам’ять завантажує дані")

class HardDrive:
    def read(self): print("Диск читає дані")

class ComputerFacade:
    """Фасад для запуску комп’ютера"""
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.disk = HardDrive()

    def start(self):
        print("=== Запуск комп’ютера ===")
        self.disk.read()
        self.memory.load()
        self.cpu.freeze()
        self.cpu.execute()

# === 4. Proxy ===
class Image(ABC):
    @abstractmethod
    def display(self): pass

class RealImage(Image):
    def __init__(self, filename):
        self.filename = filename
        self.load_from_disk()

    def load_from_disk(self):
        print(f"Завантаження {self.filename} з диска...")

    def display(self):
        print(f"Відображення зображення {self.filename}")

class ProxyImage(Image):
    def __init__(self, filename):
        self.filename = filename
        self.real_image = None

    def display(self):
        if self.real_image is None:
            self.real_image = RealImage(self.filename)
        print("Проксі доступ до зображення:")
        self.real_image.display()


# === Використання ===
if __name__ == "__main__":
    # Adapter
    print("=== Adapter ===")
    eu_socket = EuropeanSocket()
    adapter = Adapter(eu_socket)
    print(f"Адаптована напруга: {adapter.voltage()}V, тип: {adapter.plug_type()}")

    # Decorator
    print("\n=== Decorator ===")
    notifier = SlackDecorator(SMSDecorator(EmailNotifier()))
    notifier.send("Патерни працюють!")

    # Facade
    print("\n=== Facade ===")
    pc = ComputerFacade()
    pc.start()

    # Proxy
    print("\n=== Proxy ===")
    img = ProxyImage("example.png")
    img.display()  # перше завантаження
    img.display()  # повторний доступ без завантаження
