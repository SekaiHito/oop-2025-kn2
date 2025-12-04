class Pizza:
    def price(self):
        return 100

class Cheese:
    def __init__(self, item):
        self.item = item

    def price(self):
        return self.item.price() + 20

class Salami:
    def __init__(self, item):
        self.item = item

    def price(self):
        return self.item.price() + 30

base = Pizza()
print(base.price())

with_cheese = Cheese(base)
print(with_cheese.price())

mega_pizza = Salami(with_cheese)
print(mega_pizza.price())