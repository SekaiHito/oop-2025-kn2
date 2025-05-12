## Міністерство освіти і науки України

## Львівський національний університет ветеринарії і біотехнологій імені С.З.Ґжицького

# Звіт

про виконання лаборатоної роботи №10 з дисципліни ***Об'єктно-орієнтоване програмування*** на тему **Використання декораторів методів**

Виконала: студентка групи КН-21 **Федорчук Юлія**

Прийняв: доц. А.Татомир

## Львів 2025

Мета: освоїти роботу з декораторами в Python 3.

## Хід роботи

1. Навчилися використовувати декоратор “@property”. Написали принаймні один метод з його використанням.

2. Ознайомилися з концепцією getter’ів, setter’ів і delete’рів. Реалізували хоча б один метод з їх використанням.

```py

class Love:

    def __init__(self, first_love, last_love):
        self.first_love = first_love
        self.last_love = last_love

    @property
    def email_of_love(self):
        return '{}.{}@it.is.love'.format(self.first_love, self.last_love)

    @property
    def fulllove(self):
        return '{} {}'.format(self.first_love, self.last_love)
    
    @fulllove.setter
    def fulllove(self, name):
        first_love, last_love = name.split(' ')
        self.first_love = first_love
        self.last_love = last_love
    
    @fulllove.deleter
    def fulllove(self):
        print('Delete Name_of_love!')
        self.first_love = None
        self.last_love = None


lov_1 = Love('John', 'Smith')
lov_1.fulllove = "Corey Schafer"

print(lov_1.first_love)
print(lov_1.email_of_love)
print(lov_1.fulllove)

del lov_1.fulllove
```
## Висновки

