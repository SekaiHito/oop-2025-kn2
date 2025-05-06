# МІНІСТЕРСТВО ОСВІТИ ТА НАУКИ

## Львівський національний університет ветеринарії і біотехнологій імені С.З.Ґжицького

# Звіт

**про виконання лаборатоної роботи №6**

**з дисципліни "Об'єктно-орієнтоване програмування"**

**на тему** 

**Створення та використання класів.**

Виконав: студент групи КН-21 Греділь Адріан

Перевірив: доц. А.Татомир

### Львів 2025

Мета роботи – ознайомитися з різними типами змінних в об’єктно-орієнтованому програмуванні

## Хід роботи

Я набув навичок у створенні класів. Створив клас, який приймає кілька аргументів. На основі цих аргументів у конструкторі класу я створив набір атрибутів об'єкта, один з яких розраховується на основі інших.

```py
class Car:
    def __init__(self, brand, model, year, mileage):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage
        self.age = 2025 - self.year

    def display_info(self):
        print(f"Марка: {self.brand}")
        print(f"Модель: {self.model}")
        print(f"Рік випуску: {self.year}")
        print(f"Пробіг: {self.mileage} км")
        print(f"Вік: {self.age} років")

my_car = Car("Toyota", "Corolla", 2015, 150000)
my_car.display_info()

```
2. Я реалізував метод, який генерує опис об'єкта на основі його властивостей. Цей метод створює текст, що містить інформацію про об'єкт, використовуючи його атрибути.

```py
class Car:
    def __init__(self, brand, model, year, mileage):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage
        self.age = 2025 - self.year

    def generate_description(self):
        return f"Це {self.year} року {self.brand} {self.model}. Пробіг: {self.mileage} км. Вік: {self.age} років."

my_car = Car("Toyota", "Corolla", 2015, 150000)
description = my_car.generate_description()
print(description)

```
3. Я навчився створювати об'єкти на основі класу. Створив кілька об'єктів і викликав реалізований метод, використовуючи як об'єкти, так і сам клас. Це дозволило краще зрозуміти, як працювати з інстанціями класу та їх методами.

```py
class Car:
    def __init__(self, brand, model, year, mileage):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage
        self.age = 2025 - self.year

    def generate_description(self):
        return f"Це {self.year} року {self.brand} {self.model}. Пробіг: {self.mileage} км. Вік: {self.age} років."

car1 = Car("Toyota", "Corolla", 2015, 150000)
car2 = Car("Honda", "Civic", 2018, 120000)
car3 = Car("Ford", "Focus", 2020, 80000)

print(car1.generate_description())
print(car2.generate_description())
print(car3.generate_description())

print(Car.generate_description(car1))
print(Car.generate_description(car2))
print(Car.generate_description(car3))

```
4. Я познайомився з поняттям змінної класу. Реалізував змінну класу, яка зберігає спільне значення для всіх об'єктів класу, та метод, який використовує цю змінну для виконання певних операцій, наприклад, підрахунку кількості створених об'єктів.

```py
class Car:
    total_cars = 0

    def __init__(self, brand, model, year, mileage):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage
        self.age = 2025 - self.year
        Car.total_cars += 1

    def generate_description(self):
        return f"Це {self.year} року {self.brand} {self.model}. Пробіг: {self.mileage} км. Вік: {self.age} років."

    @classmethod
    def get_total_cars(cls):
        return f"Кількість створених автомобілів: {cls.total_cars}"

car1 = Car("Toyota", "Corolla", 2015, 150000)
car2 = Car("Honda", "Civic", 2018, 120000)

print(car1.generate_description())
print(car2.generate_description())

print(Car.get_total_cars())

```
5. Я реалізував лічильник створених об'єктів за допомогою класу. Для цього використав змінну класу, яка автоматично збільшується кожного разу, коли створюється новий об'єкт. Це дозволило відстежувати кількість об'єктів, створених на основі класу.

```py
class Car:
    counter = 0

    def __init__(self, brand, model, year, mileage):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage
        self.age = 2025 - self.year
        Car.counter += 1

    def generate_description(self):
        return f"Це {self.year} року {self.brand} {self.model}. Пробіг: {self.mileage} км. Вік: {self.age} років."

    @classmethod
    def get_object_count(cls):
        return f"Кількість створених автомобілів: {cls.counter}"

car1 = Car("Toyota", "Corolla", 2015, 150000)
car2 = Car("Honda", "Civic", 2018, 120000)
car3 = Car("Ford", "Focus", 2020, 80000)

print(car1.generate_description())
print(car2.generate_description())
print(car3.generate_description())

print(Car.get_object_count())

```
## Висновок:

Під час роботи я навчився ствроювати класи та об'єкти в Python, а також працювати з їхніми аттрибутами та методами. Створив методи для генерування опису об'єкта на основі його властивостей і використовував змінну класу для підрахунку кількості створених об'єктів. Це дозволило краще зрозуміти, як працюють класи та об'єкти, а також як управлляти спільними властивостями для всіх об'єктів класу. Зокрема, реалізація лічильника створених об'єктів допомогла освоїти принципи роботи з класами та їхніми методами.