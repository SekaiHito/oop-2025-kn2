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