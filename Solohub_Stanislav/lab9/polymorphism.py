# Базовий клас
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a generic sound"

# Клас Dog з перевизначенням speak() і магічними методами
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

    def __str__(self):
        return f"Dog: {self.name}"

    def __add__(self, other):
        if isinstance(other, Dog):
            return f"{self.name} and {other.name} became friends!"
        return NotImplemented

# Клас Cat з перевизначенням speak() і магічними методами
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

    def __str__(self):
        return f"Cat: {self.name}"

    def __eq__(self, other):
        if isinstance(other, Cat):
            return self.name == other.name
        return False

# Функція, яка демонструє поліморфізм
def animal_says(animal: Animal):
    print(animal.speak())

# Основна частина програми
def main():
    dog1 = Dog("Rex")
    dog2 = Dog("Max")
    cat1 = Cat("Misty")
    cat2 = Cat("Misty")

    # Поліморфізм
    print("Поліморфізм:")
    animal_says(dog1)  # Rex says Woof!
    animal_says(cat1)  # Misty says Meow!

    # Магічні методи
    print("\nМагічні методи:")
    print(str(dog1))           # Dog: Rex
    print(str(cat1))           # Cat: Misty
    print(dog1 + dog2)         # Rex and Max became friends!
    print(cat1 == cat2)        # True
    print(cat1 == dog1)        # False (різні типи)


if __name__ == "__main__":
    main()