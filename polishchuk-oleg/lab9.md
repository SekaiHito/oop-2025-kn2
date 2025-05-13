## Міністерство освіти і науки України

## Львівський національний університет ветеринарії і біотехнологій імені С.З.Ґжицького

# Звіт

про виконання лаборатоної роботи №9 з дисципліни ***Об'єктно-орієнтоване програмування*** на тему **Поліморфізм в Python 3**

Виконала: студент групи КН-21 **Поліщук Олег**

Прийняв: доц. А.Татомир

## Львів 2025

Мета: засвоїти застосування принципу поліморфізму в
об’єктно-орієнтованому програмуванні.

## Хід роботи

1. Ознайомилися з поняттям поліморфізму в ООП. Навчилися перевизначати поведінку методів.

2. Реалізували декілька “магічних методів”: **__repr__**, **__str__**, **__add__**, **__len__** для роботи з визначеними раніше класами.

```py

class Entity:
    growth_factor = 100

    def __init__(self, first_name, last_name, value):
        self.first_name = first_name
        self.last_name = last_name
        self.email = f"{first_name}.{last_name}@entity.com"
        self.value = value

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def apply_growth(self):
        self.value = round(self.value * self.growth_factor, 2)

    def __repr__(self):
        return f"Entity('{self.first_name}', '{self.last_name}', {self.value})"

    def __str__(self):
        return f"{self.full_name()} - {self.email}"

    def __add__(self, other):
        return self.value + other.value

    def __len__(self):
        return len(self.full_name())

ent_1 = Entity('Alpha', 'Beta', 5000)
ent_2 = Entity('Gamma', 'Delta', 6000)

print(ent_1 + ent_2)  # 11000
print(len(ent_1))  # 10
```
## Висновки
дізнався що таке поліморфізм і попрактикувався кодити 
