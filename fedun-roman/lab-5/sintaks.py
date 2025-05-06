class Cat:
    def __init__(self, name):
        self.name = name

    def meow(self):
        print(f"{self.name} каже: Мяу!")

    def eat(self, food):
        print(f"{self.name} їсть {food}")

cat1 = Cat("Персик")

cat1.meow()
cat1.eat("рибу")