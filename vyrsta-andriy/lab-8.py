# Батьківський клас
class AthleteBase:
    def __init__(self, name, sport, ranking):
        self.name = name
        self.sport = sport
        self.ranking = ranking

    def describe(self):
        return f"{self.name} ({self.sport}) - Рейтинг: {self.ranking}"

# Дочірній клас для тенісистів
class TennisPlayer(AthleteBase):
    def __init__(self, name, ranking):
        super().__init__(name, "Теніс", ranking)

# Дочірній клас для футболістів
class FootballPlayer(AthleteBase):
    def __init__(self, name, ranking):
        super().__init__(name, "Футбол", ranking)

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

# Генерація звіту
report = AthleteReport([tennis_player, football_player])
report.generate_report()