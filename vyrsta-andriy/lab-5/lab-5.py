# Оголошення класу
class Car:
    def __init__(self, brand, model, year):
        # Властивості об'єкта
        self.brand = brand
        self.model = model
        self.year = year

    # Метод для отримання інформації про автомобіль
    def get_info(self):
        return f"{self.year} {self.brand} {self.model}"

    # Метод для зміни року випуску
    def update_year(self, new_year):
        self.year = new_year

# Створення об'єкта (екземпляра класу)
car1 = Car("Toyota", "Camry", 2020)

# Використання властивостей об'єкта
print(car1.get_info())  # Виведе: "2020 Toyota Camry"

# Зміна значення властивості
car1.update_year(2025)
print(car1.get_info())  # Виведе: "2025 Toyota Camry"