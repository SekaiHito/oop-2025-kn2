# Батьківський клас
class AthleteBase:
    def __init__(self, name, sport, ranking):
        self.name = name
        self.sport = sport
        self.ranking = ranking

    def describe(self):
        return f"{self.name} ({self.sport}) - Рейтинг: {self.ranking}"

    # Магічний метод __str__ для представлення об'єкта у вигляді рядка
    def __str__(self):
        return f"Атлет: {self.name}, Вид спорту: {self.sport}, Рейтинг: {self.ranking}"

    # Магічний метод __lt__ для порівняння рейтингів
    def __lt__(self, other):
        return self.ranking < other.ranking

# Дочірній клас для тенісистів
class TennisPlayer(AthleteBase):
    def __init__(self, name, ranking):
        super().__init__(name, "Теніс", ranking)

    # Перевизначений метод describe
    def describe(self):
        return f"Тенісист {self.name} має рейтинг {self.ranking}."

# Дочірній клас для футболістів
class FootballPlayer(AthleteBase):
    def __init__(self, name, ranking):
        super().__init__(name, "Футбол", ranking)

    # Перевизначений метод describe
    def describe(self):
        return f"Футболіст {self.name} має рейтинг {self.ranking}."

# Дочірній клас для генерації звіту про спортсменів
class AthleteReport:
    def __init__(self, athletes):
        self.athletes = athletes

    def generate_report(self):
        print("=== Спортивний звіт ===")
        for athlete in self.athletes:
            print(athlete.describe())

# Тестування всіх класів
tennis_player = TennisPlayer("Новак Джокович", 1)
football_player = FootballPlayer("Ліонель Мессі", 5)

# Перевірка наслідування
print("Перевірка isinstance:")
print(isinstance(tennis_player, AthleteBase))  # True
print(isinstance(football_player, AthleteBase))  # True

print("\nПеревірка issubclass:")
print(issubclass(TennisPlayer, AthleteBase))  # True
print(issubclass(FootballPlayer, AthleteBase))  # True

# Використання магічного методу __str__
print("\nРядкове представлення об'єктів:")
print(tennis_player)
print(football_player)

# Використання магічного методу __lt__
print("\nПорівняння рейтингів:")
print(tennis_player < football_player)  # True (1 < 5)

# Генерація звіту
report = AthleteReport([tennis_player, football_player])
report.generate_report()