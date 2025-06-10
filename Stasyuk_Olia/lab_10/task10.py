class Person:
    def __init__(self,name:str = "stranger", age:float = 0):
        self.name = name
        self.age = age

    @property
    def isChild(self) -> bool:
        return True if self.age < 18 else False

    @isChild.setter
    def isChild(self, value: bool):
        if value:
            self.age = 10
        else:
            self.age = 20

    @isChild.deleter
    def isChild(self):
        self.name = ""
        self.age = None

if __name__ == "__main__":
    p = Person("Alice", 25)
    print(f"Name: {p.name}, Age: {p.age}, Is child: {p.isChild}")  

    p.isChild = True
    print(f"Name: {p.name}, Age: {p.age}, Is child: {p.isChild}")  

    p.isChild = False
    print(f"Name: {p.name}, Age: {p.age}, Is child: {p.isChild}")
    
    del p.isChild
    print(f"Name: {p.name}, Age: {p.age}")
