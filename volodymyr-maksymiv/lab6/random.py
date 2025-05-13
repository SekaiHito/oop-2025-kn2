class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

        Employee.num_of_emps +=1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def aply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)
print(emp_1.__dict__)
print(emp_1.email)
print(emp_2.email)
print(emp_1.fullname())
print(emp_2.fullname)
emp_1.raise_amount = 1.07
print(emp_1.pay)
print(emp_2.pay)
emp_1.aply_raise()
emp_2.aply_raise()
print(emp_1.pay)
print(emp_2.pay)
print(Employee.num_of_emps)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
        