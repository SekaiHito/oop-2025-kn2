class MyClass:
    def __init__(self, value):
        self.value = value

    @classmethod
    def from_string(cls, text):
        """Створює екземпляр з рядка, наприклад, з числа в тексті"""
        number = int(text)
        return cls(number)

obj = MyClass.from_string("42")