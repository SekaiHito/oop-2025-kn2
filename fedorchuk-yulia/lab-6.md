## Міністерство освіти і науки України

## Львівський національний університет ветеринарії і біотехнологій імені С.З.Ґжицького

# Звіт

про виконання лаборатоної роботи №6 з дисципліни ***Об'єктно-орієнтоване програмування*** на тему **Class Variables and Instances**

Виконала: студентка групи КН-21 **Федорчук Юлія**

Прийняв: доц. А.Татомир

## Львів 2025

Мета: поглибити знання про класи та дізнатися про екземпряри і варіації класів.

## Хід роботи

1. Розглянули екземпряри і варіації класів.

```py

class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

print(emp_1.email) #Corey.Schafer@email.com
print(emp_2.pay) #60000

```

## Висновки

Я зрозуміла як працювати з класами, для чого використовують self і вдосконалила англіську мову на слух.
