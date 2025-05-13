## Міністерство освіти і науки України

## Північний кампус Львівського національного університету ветеринарної медицини та біотехнологій імені С.З. Ґжицького.

# Звіт
Про виконання лаборотарної роботи №10 з дисципліни **"Об'єктно орієнтоване програмування"** на тему: **"Використання декораторів методів"**

Виконав: студент групи КН-21 Скальський Володимир

Прийняв: доц. А.Татомир
## Львів 2025

Мета: освоїти роботу з декораторами в Python 3.

## Хід роботи
Створив [програму](property_decorator.py) для демострації використання декораторів @property, getter'ів, setter'ів та deleter'ів

```
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
```

## Висновки
1. Опанував використання декоратора @property для створення властивостей класу
2. Навчився використовувати getter'и, setter'и та deleter'и для контролю доступу до атрибутів класу 