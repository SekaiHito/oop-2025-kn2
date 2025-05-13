# Батьківський клас
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

# Дочірній клас Dog
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Використання super()
        self.breed = breed

    def speak(self):
        return f"{self.name} barks."

# Дочірній клас Cat з використанням Dog
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def speak(self):
        return f"{self.name} meows."

    def interact_with_dog(self, dog: Dog):
        return f"{self.name} the cat meets {dog.name} the dog: {dog.speak()}"

# Демонстрація роботи
def main():
    dog = Dog("Rex", "Shepherd")
    cat = Cat("Misty", "gray")

    print(dog.speak())                 # Rex barks.
    print(cat.speak())                 # Misty meows.
    print(cat.interact_with_dog(dog))  # Виклик методу іншого об'єкта

    # isinstance
    print("\nПеревірки isinstance:")
    print(isinstance(dog, Animal))    # True
    print(isinstance(cat, Dog))       # False

    # issubclass
    print("\nПеревірки issubclass:")
    print(issubclass(Dog, Animal))    # True
    print(issubclass(Cat, Animal))    # True
    print(issubclass(Cat, Dog))       # False


if __name__ == "__main__":
    main()