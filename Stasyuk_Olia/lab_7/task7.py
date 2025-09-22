class Person:
    personId = 0  # змінна класу — лічильник людей

    def __init__(self, name: str = "stranger", age: int = 0) -> None:
        self.name = name
        self.age = age
        Person.personId += 1
        self.id = Person.personId
        self.isChild = self.age < 18

    def getPersonInfo(self) -> None:
        print(f"Name: {self.name}, Age: {self.age}, Is child: {self.isChild}, ID: {self.id}")

    @classmethod
    def getTotalPersons(cls) -> int:
        """Метод класу для отримання кількості створених об'єктів."""
        return cls.personId

    @classmethod
    def fromName(cls, name: str):
        """Альтернативний конструктор: створює людину тільки з ім’ям (вік 0 за замовчуванням)."""
        return cls(name=name, age=0)

    @classmethod
    def fromIsChild(cls, name: str, is_child: bool):
        """Альтернативний конструктор: створює людину на основі статусу дитини."""
        age = 10 if is_child else 25  # умовні значення віку
        return cls(name=name, age=age)

    @staticmethod
    def isValidAge(age: int) -> bool:
        """Статичний метод: перевіряє, чи вік допустимий."""
        return age >= 0


if __name__ == "__main__":
    p1 = Person()
    p1.getPersonInfo()

    p2 = Person("Petro", 71)
    p2.getPersonInfo()

    p3 = Person("Alex", 19)
    p3.getPersonInfo()

    p4 = Person("Janeth", 15)
    p4.getPersonInfo()

    print(f"\nTotal persons created: {Person.getTotalPersons()}")

    # Використання альтернативного конструктора
    p5 = Person.fromName("OnlyName")
    p5.getPersonInfo()

    p6 = Person.fromIsChild("ChildExample", True)
    p6.getPersonInfo()

    p7 = Person.fromIsChild("AdultExample", False)
    p7.getPersonInfo()

    # Перевірка статичного методу
    print("Is -5 a valid age?", Person.isValidAge(-5))
    print("Is 22 a valid age?", Person.isValidAge(22))