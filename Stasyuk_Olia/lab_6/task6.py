class Person:

    personId = 0

    def __init__(self,name:str = "stranger",age:int = 0) -> None:
        self.name = name
        self.age = age
        Person.personId += 1
        self.isChild = True if self.age < 18 else False

    def getPersonInfo(self) -> None:
        print(f"Name of the person is {self.name} with age {self.age}. Is child: {self.isChild}. ID: {Person.personId}")



if __name__ == "__main__":
    p1 = Person()
    p1.getPersonInfo()

    p2 = Person("Petro",71)
    p2.getPersonInfo()

    p3 = Person("Alex",19)
    p3.getPersonInfo()

    p4 = Person("Janeth", 15)
    p4.getPersonInfo()
    