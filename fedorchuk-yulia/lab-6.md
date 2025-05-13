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

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

# добавив метод класу 
Employee.set_raise_amount(2.5)

emp_1 = Employee('Yulia', 'Fedorchuk', 800, "kind")
emp_2 = Employee('Lia', 'Mia', 9000, "good person")

print(Employee.raise_amount)  # 2.5
print(emp_1.raise_amount)  # 2.5
print(emp_2.raise_amount)  # 2.5
