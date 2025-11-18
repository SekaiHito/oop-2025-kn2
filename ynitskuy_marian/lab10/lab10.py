from datetime import date
from typing import ClassVar, List, Optional

class Worker:
    total_workers: ClassVar[int] = 0
    default_raise: ClassVar[float] = 1.04

    def __init__(self, name: str, surname: str, salary: int) -> None:
        self.name = name
        self.surname = surname
        self.salary = salary

        Worker.total_workers += 1

    @property
    def email(self) -> str:
        return f"{self.name.lower()}.{self.surname.lower()}@company.com"

    @property
    def fullname(self) -> str:
        return f"{self.name} {self.surname}"

    @fullname.setter
    def fullname(self, full_name: str) -> None:
        self.name, self.surname = full_name.split(' ')

    @fullname.deleter
    def fullname(self) -> None:
        print("Delete Name!")
        self.name = None
        self.surname = None

    def increase_salary(self) -> None:
        self.salary = int(self.salary * self.default_raise)

    def __repr__(self) -> str:
        return f"Worker('{self.name}', '{self.surname}', {self.salary})"

    def __str__(self) -> str:
        return f"{self.fullname} - {self.email}"

    def __add__(self, other: 'Worker') -> int:
        return self.salary + other.salary

    def __len__(self) -> int:
        return len(self.fullname)

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


class Engineer(Worker):
    default_raise: ClassVar[float] = 1.10

    def __init__(self, name: str, surname: str, salary: int, language: str) -> None:
        super().__init__(name, surname, salary)
        self.language = language


class Supervisor(Worker):
    def __init__(self, name: str, surname: str, salary: int, team: Optional[List[Worker]] = None) -> None:
        super().__init__(name, surname, salary)
        self.team = team if team is not None else []

    def add_worker(self, worker: Worker) -> None:
        if worker not in self.team:
            self.team.append(worker)

    def remove_worker(self, worker: Worker) -> None:
        if worker in self.team:
            self.team.remove(worker)

    def show_team(self) -> None:
        for member in self.team:
            print('-->', member.fullname)


# Приклад використання:
eng_1 = Engineer('Olga', 'Kovalenko', 70000, 'Python')
eng_2 = Engineer('Maksym', 'Bondar', 80000, 'Java')

sup_1 = Supervisor('Natalia', 'Shevchenko', 100000, [eng_1])

print(sup_1.email)

sup_1.add_worker(eng_2)
sup_1.remove_worker(eng_2)

sup_1.show_team()

some_date = date(2023, 3, 15)
print(Worker.check_workday(some_date))

# Додаткове використання спеціальних методів:
print(repr(eng_1))
print(str(eng_1))
print(eng_1 + eng_2)
print(len(eng_1))

# Перевірка властивостей:
worker_demo = Worker('Ivan', 'Pavlenko', 65000)
worker_demo.fullname = "Andrii Hnatiuk"
print(worker_demo.name)
print(worker_demo.email)
print(worker_demo.fullname)

del worker_demo.fullname
