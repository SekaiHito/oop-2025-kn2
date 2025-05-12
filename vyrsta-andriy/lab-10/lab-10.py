# Батьківський клас
class AthleteBase:
    def __init__(self, name, sport, ranking):
        self._name = name  # Використовуємо _name для інкапсуляції
        self._sport = sport
        self._ranking = ranking

    @property
    def name(self):
        """Getter для імені спортсмена"""
        return self._name

    @name.setter
    def name(self, new_name):
        """Setter для імені спортсмена"""
        if isinstance(new_name, str) and new_name.strip():
            self._name = new_name
        else:
            raise ValueError("Ім'я повинно бути непорожнім рядком")

    @property
    def ranking(self):
        """Getter для рейтингу"""
        return self._ranking

    @ranking.setter
    def ranking(self, new_ranking):
        """Setter для рейтингу"""
        if isinstance(new_ranking, int) and new_ranking > 0:
            self._ranking = new_ranking
        else:
            raise ValueError("Рейтинг повинен бути позитивним цілим числом")

    @ranking.deleter
    def ranking(self):
        """Delete’r для рейтингу"""
        print(f"Видаляю рейтинг для {self.name}")
        self._ranking = None

    def describe(self):
        return f"{self.name} ({self._sport}) - Рейтинг: {self.ranking}"

    def __str__(self):
        return f"Атлет: {self.name}, Вид спорту: {self._sport}, Рейтинг: {self.ranking}"

    def __lt__(self, other):
        return self.ranking < other.ranking


# Дочірній клас для тенісистів
class TennisPlayer(AthleteBase):
    def __init__(self, name, ranking):
        super().__init__(name, "Теніс", ranking)

    def describe(self):
        return f"Тенісист {self.name} має рейтинг {self.ranking}."


# Дочірній клас для футболістів
class FootballPlayer(AthleteBase):
    def __init__(self, name, ranking):
        super().__init__(name, "Футбол", ranking)

    def describe(self):
        return f"Футболіст {self.name} має рейтинг {self.ranking}."


# Тестування класів
tennis_player = TennisPlayer("Новак Джокович", 2)
football_player = FootballPlayer("Ліонель Мессі", 5)

# Використання getter’ів
print(f"Ім'я тенісиста: {tennis_player.name}")
print(f"Рейтинг футболіста: {football_player.ranking}")

# Використання setter’ів
tennis_player.name = "Рафаель Надаль"
football_player.ranking = 2

print("\nОновлена інформація:")
print(tennis_player.describe())
print(football_player.describe())

# Використання delete’ра
del football_player.ranking
print("\nПісля видалення рейтингу:")
print(football_player.describe())

# Генерація звіту
report = [tennis_player, football_player]
for athlete in report:
    print(athlete.describe())
