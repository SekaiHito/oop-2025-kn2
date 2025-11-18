class Vehicle:
    def __init__(self, name, kind="car", color="unknown", value=100.00):
        self.name = name
        self.kind = kind
        self.color = color
        self.value = value

    def description(self):
        return f"{self.name} is a {self.color} {self.kind} worth ${self.value:.2f}."

    def change_color(self, new_color):
        self.color = new_color

    def update_value(self, new_value):
        self.value = new_value

    def compare_price(self, other_vehicle):
        if self.value > other_vehicle.value:
            return f"{self.name} is more expensive than {other_vehicle.name}."
        elif self.value < other_vehicle.value:
            return f"{self.name} is cheaper than {other_vehicle.name}."
        else:
            return f"{self.name} and {other_vehicle.name} have the same price."

# Клас-нащадок для автомобілів
class Car(Vehicle):
    def __init__(self, name, color, value, doors=4):
        super().__init__(name, "car", color, value)
        self.doors = doors

    def car_info(self):
        return f"{self.description()} It has {self.doors} doors."

# Створення об'єктів
car1 = Car("Fer", "red", 60000.00, 2)
car2 = Vehicle("Jump", "van", "red", 10000.00)

# Вивід опису
print(car1.car_info())
print(car2.description())

# Зміна параметрів
car2.change_color("blue")
print(car2.description())

# Порівняння вартості
print(car1.compare_price(car2))

