class MyClass:
    count = 0

    def __init__(self, value):
        self.value = value
        MyClass.count += 1

    @classmethod
    def get_count(cls):
        return cls.count

    def show(self):
        print(f"Значення об'єкта: {self.value}")

a = MyClass(100)
b = MyClass(200)
c = MyClass(300)

a.show()
b.show()
c.show()

print(f"Кількість створених об'єктів: {MyClass.get_count()}")