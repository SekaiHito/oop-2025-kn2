
class Worker:
    salary_boost = 1.05  # Змінений коефіцієнт підвищення зарплати

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.email = f"{first_name}.{last_name}@company.com"
        self.salary = salary

    def get_fullname(self):
        return f"{self.first_name} {self.last_name}"

    def apply_boost(self):
        self.salary = int(self.salary * self.salary_boost)

class Engineer(Worker):
    salary_boost = 1.12  # Змінений коефіцієнт для розробника

    def __init__(self, first_name, last_name, salary, programming_language):
        super().__init__(first_name, last_name, salary)
        self.programming_language = programming_language

class Supervisor(Worker):
    def __init__(self, first_name, last_name, salary, team=None):
        super().__init__(first_name, last_name, salary)
        self.team = [] if team is None else team

    def add_team_member(self, worker):
        if worker not in self.team:
            self.team.append(worker)

    def remove_team_member(self, worker):
        if worker in self.team:
            self.team.remove(worker)

    def display_team(self):
        for member in self.team:
            print('-->', member.get_fullname())

# Створюємо об'єкти класів
eng_1 = Engineer('Alex', 'Johnson', 53000, 'Python')  # Змінені дані
eng_2 = Engineer('Jamie', 'Taylor', 62000, 'Java')  # Змінені дані

supervisor_1 = Supervisor('Emma', 'Williams', 95000, [eng_1])  # Змінені дані

print(supervisor_1.email)

supervisor_1.add_team_member(eng_2)
supervisor_1.remove_team_member(eng_2)

supervisor_1.display_team()


