class Animal:
    def __init__(self,breed:str = "deafult") -> None:
        self.breed = breed

class Dog(Animal):
    def __init__(self,breed: str = "dog breed") -> None:
        super().__init__(breed)

    def voice(self) -> None:
        print("bark")

    def react(self,animal) -> None:
        
        if isinstance(animal,Cat):
            print("bark aggressive")
        else:
            print("bark friendly")

class Cat(Animal):
    def __init__(self,breed: str = "cat breed") -> None:
        super().__init__(breed)
    
    def voice(self) -> None:
        print("meow")

class Horse(Animal):
    def __init__(self,breed: str = "horse breed") -> None:
        super().__init__(breed)

    def voice(self) -> None:
        print("neigh")

if __name__ == "__main__":
    d = Dog("mops")
    c = Cat("ginger one")
    h = Horse("arabian")

    d2 = Dog("chay")

    d.react(c)
    d.react(d2)
