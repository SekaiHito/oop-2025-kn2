
## Міністерство освіти і науки України

## Львівський національний університет ветеринарії і біотехнологій імені С.З.Ґжицького

# Звіт

про виконання лаборатоної роботи №7 з дисципліни ***Об'єктно-орієнтоване програмування*** на тему **classmethods and staticmethods**

Виконав : студент групи КН-21 **Поліщук Олег **

Прийняв: доц. А.Татомир

## Львів 2025

Мета: Ознайомлення з методами класу classmethod і статичними методами staticmethod у Python, їхніми особливостями, відмінностями та практичним застосуванням у програмуванні.

## Хід роботи

1. Розглянули різницю між методами класу і статистичними методами.

```py


class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

Employee.set_raise_amt(1.05)

print(Employee.raise_amt) #1.05
print(emp_1.raise_amt) #1.05
print(emp_2.raise_amt) #1.05

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

first, last, pay = emp_str_1.split('-')

#new_emp_1 = Employee(first, last, pay)
new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email) #John.Doe@email.com
print(new_emp_1.pay)#70000

import datetime
my_date = datetime.date(2016, 7, 11)

print(Employee.is_workday(my_date)) #True

```

## Висновки

попрацював з такими поняттями як classmethod і staticmethod.дізнався  як переглядати атрибути об'єкта динамічно
