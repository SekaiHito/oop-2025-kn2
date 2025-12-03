class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

# Використання
a = Singleton()
b = Singleton()
print(a is b)  # True, один екземпляр
