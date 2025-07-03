from datetime import date
from typing import ClassVar

class Worker:
    total_workers: ClassVar[int] = 0
    default_raise: ClassVar[float] = 1.04

    def __init__(self, name: str, surname: str, salary: int) -> None:
        self.name = name
        self.surname = surname
        self.email = f"{name.lower()}.{surname.lower()}@company.com"
        self.salary = salary

        Worker.total_workers += 1

    def get_fullname(self) -> str:
        return f"{self.name} {self.surname}"

    def increase_salary(self) -> None:
        self.salary = int(self.salary * self.default_raise)

    @classmethod
    def update_raise_amount(cls, new_amount: float) -> None:
        cls.default_raise = new_amount

    @classmethod
    def create_from_string(cls, worker_str: str) -> 'Worker':
        try:
            name, surname, salary = worker_str.split('-')
            return cls(name, surname, int(salary))
        except ValueError:
            raise ValueError("Worker string must be in 'Name-Surname-Salary' format")

    @staticmethod
    def check_workday(day: date) -> bool:
        return day.weekday() < 5


worker_1 = Worker('Ivan', 'Petrov', 50000)
worker_2 = Worker('Oleg', 'Ivanov', 60000)

Worker.update_raise_amount(1.05)
print(Worker.default_raise)
print(worker_1.default_raise)
print(worker_2.default_raise)

worker_str = 'Anna-Sidorova-70000'
new_worker = Worker.create_from_string(worker_str)
print(new_worker.email)
print(new_worker.salary)

some_date = date(2023, 3, 15)
print(Worker.check_workday(some_date))
