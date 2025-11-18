from datetime import date
from typing import ClassVar, List, Optional

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
            print('-->', member.get_fullname())


eng_1 = Engineer('Olga', 'Kovalenko', 70000, 'Python')
eng_2 = Engineer('Maksym', 'Bondar', 80000, 'Java')

sup_1 = Supervisor('Natalia', 'Shevchenko', 100000, [eng_1])

print(sup_1.email)

sup_1.add_worker(eng_2)
sup_1.remove_worker(eng_2)

sup_1.show_team()

some_date = date(2023, 3, 15)
print(Worker.check_workday(some_date))
