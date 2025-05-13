## Міністерство освіти і науки України

## Північний кампус Львівського національного університету ветеринарної медицини та біотехнологій імені С.З. Ґжицького.

# Звіт
Про виконання лаборотарної роботи №8 з дисциплини **"Об'єктно орієнтоване програмування"** на тему: **"Наслідування в об’єктно-орієнтованому програмуванні"**
"**

Виконав: студент групи КН-22СП Лесів Роман

Прийняв: доц. А.Татомир
## Львів 2025

Мета: оволодіти концепцією наслідування класів


## Хід роботи

1. Навчився повторно використовувати існуючий код завдяки наслідуванню.
```python
# 1. Наслідування дозволяє повторно використовувати код.
# Ми створили базовий клас Dota2Items і використовуємо його функціональність у дочірніх класах.

class Dota2Items:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

    def info(self):
        print(f"Предмет: {self.name}, Вартість: {self.cost}")
```

2. Створити один батьківський клас Dota2Items і декілька дочірніх (Carryitem, SupportItem, UtilityItem, TankItem). Наслідував частину властивостей та функціоналу від батьківського класу в дочірніх класах. Освоїв використання методу super.             
```python
# 2. Дочірні класи наслідують від Dota2Items.
# Ми використовуємо super() для ініціалізації базового класу.

class CarryItem(Dota2Items):
    def __init__(self, name, cost):
        super().__init__(name, cost)  # Викликаємо конструктор батьківського класу
        self.role = "Carry"

class SupportItem(Dota2Items):
    def __init__(self, name, cost):
        super().__init__(name, cost)
        self.role = "Support"

class UtilityItem(Dota2Items):
    def __init__(self, name, cost):
        super().__init__(name, cost)
        self.role = "Utility"

class TankItem(Dota2Items):
    def __init__(self, name, cost):
        super().__init__(name, cost)
        self.role = "Tank"
```

```python

3. У одному з дочірніх класів організував використання методів об’єктів-представників іншого дочірнього класу.
# 3. Один дочірній клас використовує метод іншого дочірнього класу (виклик методу info()).

class SupportItem(Dota2Items):
    def __init__(self, name, cost):
        super().__init__(name, cost)
        self.role = "Support"

    def boost_carry(self, carry_item):
        # Перевірка, що передано саме CarryItem
        if isinstance(carry_item, CarryItem):
            print(f"🛡 Support '{self.name}' підсилює Carry '{carry_item.name}':")
            carry_item.info()
        else:
            print("Це не CarryItem!")
```

```python

4. Ознайомився з методами instanceof, issubclassof
# 4. Використання isinstance() та issubclass() — перевірка типу об'єкта та класу.

item1 = CarryItem("Monkey King Bar", 4175)

# isinstance(obj, Class) перевіряє, чи є об'єкт екземпляром класу або його нащадком
print(isinstance(item1, Dota2Items))   # True
print(isinstance(item1, SupportItem))  # False

# issubclass(SubClass, BaseClass) перевіряє, чи є клас нащадком іншого класу
print(issubclass(CarryItem, Dota2Items))  # True
print(issubclass(UtilityItem, SupportItem))  # False
```
[Нажміть, щоб перейти до .py файла](dota2items.py)


## Висновки  
На цій практичні роботі я зрозумів що таке принцип наслідування, створив декілька дочірніх класів для класу Dota2Items, наслідував частину функціоналу батьківського класу в дочірніх класах, вивчив метод super та його використання, ознайомився з методами instanceof, issubclassof.