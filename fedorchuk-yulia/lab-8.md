## Міністерство освіти і науки України

## Львівський національний університет ветеринарії і біотехнологій імені С.З.Ґжицького

# Звіт

про виконання лаборатоної роботи №8 з дисципліни ***Об'єктно-орієнтоване програмування*** на тему **Inheritance - Creating Subclasses**

Виконала: студентка групи КН-21 **Федорчук Юлія**

Прийняв: доц. А.Татомир

## Львів 2025

Мета: навчитися створювати підкласи, які успадковують властивості та методи від батьківських класів.

## Хід роботи

1. Навчилися повторно використовувати існуючий код завдяки
наслідуванню.

2. Створили один батьківський клас і декілька дочірніх. Наслідували частину
властивостей та функціоналу від батьківського класу в дочірніх класах.
Освоїли використання методу super.

3. У одному з дочірніх класів організували використання методів
об’єктів-представників іншого дочірнього класу.

4. Ознайомилися з методами instanceof, issubclassof.

```py

class Employee:
    raise_amt = 2.03

    def __init__(self, first, last, pay, nature):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay
        self.nature = nature

    def fullname(self):
        return f'{self.first} {self.last}'

    def what_person(self):
        return f'{self.first} {self.last} {self.nature}'

    def apply_raise(self):
        self.pay = round(self.pay * self.raise_amt, 2)


class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, nature, prog_lang):
        super().__init__(first, last, pay, nature)
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self, first, last, pay, nature, employees=None):
        super().__init__(first, last, pay, nature)
        self.employees = employees if employees is not None else []

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())


dev_1 = Developer('Yulia', 'Fedorchuk', 800, "kind", "Python")
dev_2 = Developer('Lia', 'Mia', 9000, "good person", "JavaScript")

mgr_1 = Manager('Susan', 'Smurf', 90000, "organized", [dev_1])

print(mgr_1.email)  # Susan.Smurf@email.com

mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_2)

mgr_1.print_emps() #--> Yulia Fedorchuk
```

## Висновки

Дізналася виконуючи лабораторну №8, як класи можуть успадковувати вміст інших класів, дізналася як це перевірити і як це працює. Удосконалила англіську на слух.
