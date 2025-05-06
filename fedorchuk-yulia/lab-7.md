## Міністерство освіти і науки України

## Львівський національний університет ветеринарії і біотехнологій імені С.З.Ґжицького

# Звіт

про виконання лаборатоної роботи №7 з дисципліни ***Об'єктно-орієнтоване програмування*** на тему **classmethods and staticmethods**

Виконала: студентка групи КН-21 **Федорчук Юлія**

Прийняв: доц. А.Татомир

## Львів 2025

Мета: Ознайомлення з методами класу classmethod і статичними методами staticmethod у Python, їхніми особливостями, відмінностями та практичним застосуванням у програмуванні.

## Хід роботи

1.  Засвоїли різницю між звичайними методами "(self)", методами класу "(@classmethod і cls)" та
статичними методами "(@staticmethod)".

2. Навчилися створювати альтернативні конструктори. Для створеного у попередній роботі класу реалізували метод класу "def set_raise_amt", 
"def from_string", який повинен працювати зі змінними класу. 

3. Створили статичний метод "def is_workday" і перевірили його роботу.

```py


class Employee:

    num_of_emps = 0
    raise_amt = 2.03

    def __init__(self, first, last, pay, nature):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay
        self.nature = nature

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    def what_person(self):
        return '{} {} {}'.format(self.first, self.last, self.nature)
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


emp_1 = Employee('Yulia', 'Fedorchuk', 800, "kind")
emp_2 = Employee('Lia', 'Mia', 9000, "good person")

Employee.set_raise_amt(1.05)

print(Employee.raise_amt) #1.05
print(emp_1.raise_amt) #1.05
print(emp_2.raise_amt) #1.05

emp_str_1 = 'Johans-Do-4000'
emp_str_2 = 'Hero-Smith-3000'
emp_str_3 = 'January-Boo-1000'

first, last, pay = emp_str_1.split('-')

#new_emp_1 = Employee(first, last, pay)
new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email) #Johans.Do@email.com
print(new_emp_1.pay)#4000

import datetime
my_date = datetime.date(2016, 7, 11)

print(Employee.is_workday(my_date)) #True

```

## Висновки

Покращила розуміння відміностей і випадків використання classmethod і staticmethod. Дізналася як переглядати атрибути об'єкта динамічно. Також вдосконалила англіську на слух.