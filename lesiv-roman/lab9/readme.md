## Міністерство освіти і науки України

## Північний кампус Львівського національного університету ветеринарної медицини та біотехнологій імені С.З. Ґжицького.

# Звіт
Про виконання лаборотарної роботи №8 з дисциплини **"Об'єктно орієнтоване програмування"** на тему: **"Поліморфізм в Python 3"**
"**

Виконав: студент групи КН-22СП Лесів Роман

Прийняв: доц. А.Татомир
## Львів 2025

Мета: засвоїти застосування принципу поліморфізму в
об’єктно-орієнтованому програмуванні.

## Хід роботи

1. Ознайомився з поняттям поліморфізму в ООП
```python
# 1. Поліморфізм — це можливість використовувати один і той самий інтерфейс
# для різних типів об'єктів. У прикладі метод info() викликається однаково для різних класів.

class Dota2Items:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

    def info(self):
        # Базова реалізація методу info()
        print(f"Предмет: {self.name}, Вартість: {self.cost}")

class CarryItem(Dota2Items):
    def info(self):
        # Перевизначена реалізація методу info()
        print(f"[Carry] {self.name} коштує {self.cost} золота")

class SupportItem(Dota2Items):
    def info(self):
        # Ще одне перевизначення info()
        print(f"[Support] {self.name} з ціною {self.cost} підтримує команду")

# Демонстрація поліморфізму
items = [CarryItem("Butterfly", 4975), SupportItem("Glimmer Cape", 1950)]
for item in items:
    item.info()
```

2.  Навчився перевизначати поведінку методів

```python
# 2. Перевизначення методів — це заміна базової реалізації методу у дочірньому класі.
# У прикладі метод calculate_value() перевизначено у класі CarryItem.

class Dota2Items:
    def calculate_value(self):
        # Базовий підрахунок
        return 1

class CarryItem(Dota2Items):
    def calculate_value(self):
        # Перевизначено: додаємо бонус для carry-предметів
        return super().calculate_value() + 0.5
```
3. Реалізував декілька “магічних методів” для роботи з визначеними раніше
класами
```python
# 3. Магічні методи — це спеціальні методи Python, що починаються і закінчуються подвійним підкресленням.
# Наприклад, __str__, __repr__, __eq__, __lt__ тощо.

class Dota2Items:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

    def __str__(self):
        # Повертає зрозумілий рядок для користувача
        return f"{self.name} – {self.cost} золота"

    def __repr__(self):
        # Повертає офіційне представлення об'єкта
        return f"Dota2Items('{self.name}', {self.cost})"

    def __eq__(self, other):
        # Порівняння предметів за ціною
        return isinstance(other, Dota2Items) and self.cost == other.cost

    def __lt__(self, other):
        # Порівняння "менше" для сортування
        return isinstance(other, Dota2Items) and self.cost < other.cost

# Демонстрація
item1 = Dota2Items("Manta Style", 4600)
item2 = Dota2Items("Sange", 2050)
print(item1)           # Викликає __str__
print(repr(item2))     # Викликає __repr__
print(item1 == item2)  # Викликає __eq__
print(item1 < item2)   # Викликає __lt__
```
[Нажміть, щоб перейти до .py файла](dota2items.py)

## Висновки  
На цій практичні роботі я вивчив що таке поліморфізм в ООП, навчився перевизначати поведінку методів, реалізував декілька "магічних" методів для роботи з класом Dota2Items.