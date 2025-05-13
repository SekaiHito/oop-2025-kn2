## Міністерство освіти і науки України

## Львівський національний університет ветеринарії і біотехнологій імені С.З.Ґжицького

# Звіт

про виконання лаборатоної роботи №8 з дисципліни ***Об'єктно-орієнтоване програмування*** на тему **Inheritance - Creating Subclasses**

Виконав студент групи КН-21 **Поліщук Олега**

Прийняв: доц. А.Татомир

## Львів 2025

Мета: навчитися створювати підкласи, які успадковують властивості та методи від батьківських класів.

## Хід роботи

1. 

```py

class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())


dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Developer('Test', 'Employee', 60000, 'Java')

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

print(mgr_1.email) #Sue.Smith@email.com

mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_2)

mgr_1.print_emps()
```

## Висновки

дізнався що класи можуть успадковувати інформацію зінших класів і як це взагалі працює 
