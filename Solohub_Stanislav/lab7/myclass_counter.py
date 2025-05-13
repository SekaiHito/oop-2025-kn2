class MyClass:
    count = 0

    def __init__(self, value):
        self.value = value
        MyClass.count += 1

    @classmethod
    def get_count(cls):
        """Повертає кількість створених екземплярів"""
        return cls.count