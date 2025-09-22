class Car:
    count = 0  

    def __init__(self, brand, model, year):
        self.brand = brand             
        self.model = model
        self.year = year
        self.full_name = f"{brand} {model} ({year})"  
        Car.count += 1 
            def describe(self):
        return f"Автомобіль: {self.full_name}"
        car1 = Car("Toyota", "Camry", 2020)
car2 = Car("BMW", "X5", 2022)

print(car1.describe())
print(car2.describe())

print(f"Загальна кількість машин: {Car.count}")
    @classmethod
    def get_total(cls):
        return f"Створено обʼєктів Car: {cls.count}"
        print(Car.get_total())