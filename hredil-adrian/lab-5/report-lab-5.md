## МІНІСТЕРСТВО ОСВІТИ ТА НАУКИ

## Львівський національний університет ветеринарії і біотехнологій імені С.З.Ґжицького

# Звіт

**про виконання лаборатоної роботи №3**

**з дисципліни "Об'єктно-орієнтоване програмування"**

**на тему** 

**Створення та використання класів.**

Виконав: студент групи КН-21 Греділь Адріан

Перевірив: доц. А.Татомир

##### Львів 2025

*Мета роботи – ознайомитися з поняттями класів та об’єктів та закріпити на практиці методи їх створення та використання.*

## Хід роботи


1. Навчитися оголошувати класи в Python 3.

2. Навчитися створювати об’єкти (“class instances”).

```py
class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def info(self):
        return f"{self.brand} — {self.year}"

my_car = Car("Toyota", 2020)
print(my_car.info())  

```




3. Ознайомитися з поняттям змінної (властивості) обʼєкту. Навчитися їх задавати та отримувати їхні значення.

```py

class Car:
    def __init__(self, brand, year):
        self.brand = brand     
        self.year = year       


my_car = Car("Audi", 2021)


print(my_car.brand)  
print(my_car.year)   


my_car.year = 2025
print(my_car.year)   
```
4. Ознайомитися з поняттям функцій об’єкту. Навчитися їх оголошувати та викликати.

```py
class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def update_year(self, new_year):
        self.year = new_year


my_car = Car("Honda", 2015)
my_car.update_year(2023)
print(my_car.year)  
```

5. Розв’язати приклад згідно виданого завдання.

```py
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str


car1 = Vehicle()
car1.name = "Fer"
car1.color = "red"
car1.kind = "convertible"
car1.value = 60000.00

car2 = Vehicle()
car2.name = "Jump"
car2.color = "blue"
car2.kind = "van"
car2.value = 10000.00


print(car1.description())
print(car2.description())
```

## Висновок:

У ході роботи №5 я навчився оголошувати класи в пайтоні, створювати об'єкти (екземпляри класів), працювати з їхніми властивостями та методами. Закріпив знання на прикладі класу Vehicle, де створив кілька об'єктів і вивів їх опис за допомогою методу.
