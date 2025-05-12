class Car:
    total_cars = 0
    engine_type = "Petrol"

    def __init__(self, brand, year, price):
        self.brand = brand
        self.year = year
        self.price = price * (1 - (2025 - year) * 0.05)
        Car.total_cars += 1

    def describe(self):
        return f"{self.brand} ({self.year}): ${self.price:.2f}, Engine: {self.engine_type}"

    @classmethod
    def engine_info(cls):
        return f"Engine: {cls.engine_type}"

    @classmethod
    def count_cars(cls):
        return f"Total cars: {cls.total_cars}"

car1 = Car("Toyota", 2020, 20000)
car2 = Car("BMW", 2022, 50000)

print(car1.describe())
print(car2.describe())
print(Car.engine_info())
print(Car.count_cars())

class Item:
    total_items = 0
    item_type = "Block"

    def __init__(self, name, rarity, base_value):
        self.name = name
        self.rarity = rarity
        self.value = base_value * (1 + rarity * 0.1)
        Item.total_items += 1

    def describe(self):
        return f"{self.name} [Rarity: {self.rarity}]: {self.value:.2f} coins, Type: {self.item_type}"

    @classmethod
    def type_info(cls):
        return f"Item Type: {cls.item_type}"

    @classmethod
    def count_items(cls):
        return f"Total items: {cls.total_items}"

diamond = Item("Diamond", 5, 100)
iron_ingot = Item("Iron Ingot", 2, 20)

print(diamond.describe())
print(iron_ingot.describe())
print(Item.type_info())
print(Item.count_items())