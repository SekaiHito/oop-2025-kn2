class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a generic sound"

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

    def __str__(self):
        return f"Dog: {self.name}"

    def __add__(self, other):
        if isinstance(other, Dog):
            return f"{self.name} and {other.name} became friends!"
        return NotImplemented

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

    def __str__(self):
        return f"Cat: {self.name}"

    def __eq__(self, other):
        if isinstance(other, Cat):
            return self.name == other.name
        return False

def animal_says(animal: Animal):
    print(animal.speak())

def main():
    dog1 = Dog("Rex")
    dog2 = Dog("Max")
    cat1 = Cat("Misty")
    cat2 = Cat("Misty")

    print("Поліморфізм:")
    animal_says(dog1)
    animal_says(cat1)

    print("\nМагічні методи:")
    print(str(dog1))          
    print(str(cat1))           
    print(dog1 + dog2)         
    print(cat1 == cat2)      
    print(cat1 == dog1)      


if __name__ == "__main__":
    main()