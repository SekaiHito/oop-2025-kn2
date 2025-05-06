class Vehicle:
    def __init__(self, brand="", model=""):
        self._brand = brand
        self._model = model

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        self._brand = value

    @brand.deleter
    def brand(self):
        del self._brand

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        self._model = value

    @model.deleter
    def model(self):
        del self._model

# Створюємо автомобіль
car = Vehicle("Toyota", "Camry")
print(f"Марка: {car.brand}")
print(f"Модель: {car.model}")

# Змінюємо значення
car.brand = "Honda"
car.model = "Accord"
print(f"\nНова марка: {car.brand}")
print(f"Нова модель: {car.model}")

# Видаляємо атрибути
del car.brand
del car.model 