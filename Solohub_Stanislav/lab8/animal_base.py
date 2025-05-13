class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name) 
        self.breed = breed

    def speak(self):
        return f"{self.name} barks."

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def speak(self):
        return f"{self.name} meows."

    def interact_with_dog(self, dog: Dog):
        return f"{self.name} the cat meets {dog.name} the dog: {dog.speak()}"

def main():
    dog = Dog("Rex", "Shepherd")
    cat = Cat("Misty", "gray")

    print(dog.speak())             
    print(cat.speak())                 
    print(cat.interact_with_dog(dog))  

    print("\nПеревірки isinstance:")
    print(isinstance(dog, Animal))    
    print(isinstance(cat, Dog))      

    print("\nПеревірки issubclass:")
    print(issubclass(Dog, Animal))    
    print(issubclass(Cat, Animal))   
    print(issubclass(Cat, Dog))     


if __name__ == "__main__":
    main()