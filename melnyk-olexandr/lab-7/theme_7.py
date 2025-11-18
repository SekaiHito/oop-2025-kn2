class Balls:
    count = 0  # змінна класу

    def __init__(self, color: str = "red") -> None:
        self.color = color
        self.price = 10 if self.color == "red" else 20
        Balls.count += 1

    def printInfo(self) -> None:
        print(f"Color of that ball is {self.color}, its number is {Balls.count} and its price is {self.price}$")

    @classmethod
    def getCount(cls) -> int:
        # Метод класу для повернення кількості створених об'єктів.
        return cls.count

    @classmethod
    def fromPrice(cls, price: int):
        # Альтернативний конструктор: створює об'єкт на основі ціни.
        if price == 10:
            return cls("red")
        else:
            return cls("blue")

    @staticmethod
    def isValidColor(color: str) -> bool:
        # Статичний метод: перевіряє, чи колір допустимий.
        valid_colors = {"red", "blue", "green"}
        return color.lower() in valid_colors


if __name__ == "__main__":
    b1 = Balls()
    b1.printInfo()

    b2 = Balls("blue")
    b2.printInfo()

    b3 = Balls()
    b3.printInfo()

    b4 = Balls("green")
    b4.printInfo()

    print(f"\nTotal number of Balls created: {Balls.getCount()}")

    b5 = Balls.fromPrice(10)
    b5.printInfo()

    print("Is 'yellow' a valid color?", Balls.isValidColor("yellow"))
    print("Is 'green' a valid color?", Balls.isValidColor("green"))
