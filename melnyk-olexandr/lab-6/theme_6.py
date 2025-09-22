class Balls:
    count = 0

    def __init__(self,color:str = "red") -> None:
        self.color = color
        self.price = 10 if self.color == "red" else 20
        Balls.count += 1

    def printInfo(self) -> None:
        print(f"Color of that ball is {self.color}, it`s number is {Balls.count} and it price is {self.price}$")

if __name__ == "__main__":    
    b1 = Balls()
    b1.printInfo()
    b2 = Balls("blue")
    b2.printInfo()
    b3 = Balls()
    b3.printInfo()
    b4 = Balls("green")
    b4.printInfo()
