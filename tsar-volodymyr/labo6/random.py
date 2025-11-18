class Worker:
    total_employees = 0
    salary_increase = 1.06  # Змінене значення підвищення зарплати

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.email = f"{first_name}.{last_name}@company.com"
        self.salary = salary

        Worker.total_employees += 1

    def get_fullname(self):
        return f"{self.first_name} {self.last_name}"
    
    def apply_salary_increase(self):
        self.salary = int(self.salary * self.salary_increase)

employee_1 = Worker('Alex', 'Johnson', 58000)  # Змінена зарплата
employee_2 = Worker('Sam', 'Taylor', 63000)  # Змінена зарплата

print(employee_1.__dict__)
print(employee_1.email)
print(employee_2.email)
print(employee_1.get_fullname())
print(employee_2.get_fullname)

employee_1.salary_increase = 1.09  # Змінене значення для конкретного працівника

print(employee_1.salary)
print(employee_2.salary)

employee_1.apply_salary_increase()
employee_2.apply_salary_increase()

print(employee_1.salary)
print(employee_2.salary)

print(Worker.total_employees)
print(employee_1.salary_increase)
print(employee_2.salary_increase)
