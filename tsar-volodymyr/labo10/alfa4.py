
class Worker:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def email(self):
        return f"{self.first_name}.{self.last_name}@company.com"

    @property
    def fullname(self):
        return f"{self.first_name} {self.last_name}"
    
    @fullname.setter
    def fullname(self, name):
        first_name, last_name = name.split(' ')
        self.first_name = first_name
        self.last_name = last_name
    
    @fullname.deleter
    def fullname(self):
        print("Ім'я видалено!")
        self.first_name = None
        self.last_name = None


emp_1 = Worker("Alex", "Johnson")  # Змінені імена
emp_1.fullname = "Jamie Taylor"  # Змінене нове ім'я

print(emp_1.first_name)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname
