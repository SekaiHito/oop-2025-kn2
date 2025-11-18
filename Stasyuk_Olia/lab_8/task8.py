class Transport:
    def __init__(self,name:str = "transport") -> None:
        self.name = name

    def __str__(self) -> str:
        return self.name
    
    def __repr__(self) -> str:
        return self.name

class Car(Transport):
    def __init__(self,name:str = "car") -> None:
        super().__init__(name)

    def isCar(self,transport) -> None:
        if isinstance(transport,Car):
            print(f"{transport.__class__.__name__} is a car")
        else:
            print(f"{transport.__class__.__name__} is not a car")

class Plane(Transport):
    def __init__(self,name: str = "plane") -> None:
        super().__init__(name)


if __name__ == "__main__":
    t = Transport()
    c1 = Car()
    c2 = Car()
    p = Plane()

    c1.isCar(p)
    c2.isCar(c1)
