class TravelExpenseCalculator:
    # Змінна класу: лічильник створених об'єктів
    instance_count = 0

    def __init__(self, transport_cost, hotel_cost, daily_expenses, days):
        self.transport_cost = transport_cost
        self.hotel_cost = hotel_cost
        self.daily_expenses = daily_expenses
        self.days = days
        
        # Атрибут, сформований на основі інших
        self.total_cost = self.calculate_total_cost()

        # Збільшуємо лічильник об'єктів
        TravelExpenseCalculator.instance_count += 1

    # Метод для розрахунку загальних витрат
    def calculate_total_cost(self):
        return self.transport_cost + (self.hotel_cost * self.days) + (self.daily_expenses * self.days)

    # Метод, який формує опис обʼєкта
    def describe(self):
        return (f"Розрахунок витрат на подорож:\n"
                f"Транспорт: {self.transport_cost} грн\n"
                f"Готель ({self.days} днів): {self.hotel_cost * self.days} грн\n"
                f"Щоденні витрати ({self.days} днів): {self.daily_expenses * self.days} грн\n"
                f"Загальна сума: {self.total_cost} грн")

    # Метод запуску розрахунку з введенням
    def run(self):
        print(self.describe())

    # Метод класу — повертає кількість створених екземплярів
    @classmethod
    def get_instance_count(cls):
        return f"Створено обʼєктів TravelExpenseCalculator: {cls.instance_count}"


# Створення об'єктів
trip1 = TravelExpenseCalculator(1000, 500, 300, 5)
trip2 = TravelExpenseCalculator(1200, 700, 400, 7)

# Виклик методів через об'єкти
trip1.run()
trip2.run()

# Вивід опису та кількості об'єктів через клас і об'єкт
print(trip1.describe())
print(TravelExpenseCalculator.get_instance_count())