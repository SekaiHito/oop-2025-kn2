class Animal:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value:
            self._name = value
        else:
            raise ValueError("Name cannot be empty")

    def speak(self):
        return f"{self.name} makes a generic sound"

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

    def __str__(self):
        return f"Dog: {self.name}"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

    def __str__(self):
        return f"Cat: {self.name}"

def main():
    dog = Dog("Rex")
    cat = Cat("Misty")

    print(dog.speak()) 
    dog.name = "Buddy" 
    print(dog.speak()) 
    
    try:
        dog.name = ""  
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()