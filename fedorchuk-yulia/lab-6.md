## Міністерство освіти і науки України

## Львівський національний університет ветеринарії і біотехнологій імені С.З.Ґжицького

# Звіт

про виконання лаборатоної роботи №6 з дисципліни ***Об'єктно-орієнтоване програмування*** на тему **Class Variables and Instances**

Виконала: студентка групи КН-21 **Федорчук Юлія**

Прийняв: доц. А.Татомир

## Львів 2025

Мета: ознайомитися з різними типами змінних в
об’єктно-орієнтованому програмуванні.

## Хід роботи

1. Створили клас **"class Employee"**, який приймає декілька аргументів **"(self, first, last, pay, nature)"** . На їх основі у конструкторі класу створили набір атрибутів об’єкта (класу), один з яких створюється на основі інших.

2. Реалізували метод **"def what_person(self)"**, який генерує опис об’єкта на основі його
властивостей. Навчитилися створювати об’єкти **"emp_1"**. Створили декілька об’єктів на основі
класу. Викликали реалізований метод, використовуючи об’єкт і клас.

3. Познайомилися з поняттям змінної класу **"raise_amount = 2.03"**. Реалізували змінну класу і
метод **"def aplly_raise(self)"**, що її використовує.

4. Реалізували лічильник створених за допомогою класу об’єктів.

```py

class Employee:
    num_of_emp = 0
    raise_amount = 2.03
    def __init__(self, first, last, pay, nature):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay
        self.nature = nature

    Employee.num_of_emp += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    def what_person(self):
        return '{} {} {}'.format(self.first, self.last, self.nature)
    def aplly_raise(self):
        self.pay = int(self.pay * self.raise_amount)

emp_1 = Employee('Yulia', 'Fedorchuk', 800, "kind")
emp_2 = Employee('Lia', 'Mia', 9000, "good person")

print(emp_1.email) #Yulia.Fedorchuk@email.com
print(emp_2.pay) #9000
print(emp_1.what_person()) #Yulia Fedorchuk is kind
print(Employee.num_of_emp) #2

```

## Висновки

Я зрозуміла як працювати з класами, для чого використовують self і вдосконалила англіську мову на слух.
