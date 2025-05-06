class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Привіт, мене звати {self.name}!")

person1 = Person("Оля")
person1.greet()
