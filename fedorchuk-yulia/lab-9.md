## Міністерство освіти і науки України

## Львівський національний університет ветеринарії і біотехнологій імені С.З.Ґжицького

# Звіт

про виконання лаборатоної роботи №9 з дисципліни ***Об'єктно-орієнтоване програмування*** на тему **Поліморфізм в Python 3**

Виконала: студентка групи КН-21 **Федорчук Юлія**

Прийняв: доц. А.Татомир

## Львів 2025

Мета: засвоїти застосування принципу поліморфізму в
об’єктно-орієнтованому програмуванні.

## Хід роботи

1. Ознайомилися з поняттям поліморфізму в ООП. Навчилися перевизначати поведінку методів.

2. Реалізували декілька “магічних методів”: **__repr__**, **__str__**, **__add__**, **__len__** для роботи з визначеними раніше класами.

```py

class Love:

    raise_of_love = 100

    def __init__(self, first_love, last_love, email_of_love, pay_of_love):
        self.first_love = first_love 
        self.last_love= last_love
        self.email_of_love = first_love + '.' + last_love+ '@it.is.love'
        self.pay_of_love = pay_of_love

    def fulllove(self):
        return '{} {}'.format(self.first_love, self.last_love)

    def apply_raise_of_love(self):
        self.pay_of_love = int(self.pay_of_love * self.raise_of_love)

    def __repr__(self):
        return "Love('{}', '{}', {})".format(self.first_love, self.last_love self.pay_of_love)

    def __str__(self):
        return '{} - {}'.format(self.fulllove(), self.email_of_love)

    def __add__(self, other):
        return self.pay_of_love + other.pay_of_love

    def __len__(self):
        return len(self.fulllove())


lov_1 = Love('Fairy', 'Fly', 5000)
lov_2 = Love('Mermeid', 'Water', 6000)

print(lov_1 + lov_2)

print(len(lov_1))

```
## Висновки

Любов не завадить і для коду бо любов це гарно, а нам потрібен гарний код. Виконуючи лабораторну №9, я вдосконалила англіську на слух, що безперечно допоможе мені на іспиті. Дізналася, що за "print(1+2)" стоїть "print(__add__(1, 2))" і що так з багатьма іншими операторами. 