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