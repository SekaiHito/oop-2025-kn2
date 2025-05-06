class CalorieCalculator:
    instance_count = 0  # Змінна класу для підрахунку створених об'єктів

    def __init__(self, product_name, weight, calories_per_100g):
        self.product_name = product_name
        self.weight = weight
        self.calories_per_100g = calories_per_100g

        # Атрибут, який залежить від інших
        self.total_calories = self.calculate_calories()

        CalorieCalculator.instance_count += 1  # Збільшуємо лічильник об'єктів

    # Метод для розрахунку калорій
    def calculate_calories(self):
        return (self.weight / 100) * self.calories_per_100g

    # Метод для формування опису об'єкта
    def describe(self):
        return (f"Продукт: {self.product_name}\n"
                f"Маса: {self.weight} г\n"
                f"Калорійність: {self.calories_per_100g} ккал на 100 г\n"
                f"Загальні калорії: {self.total_calories:.2f} ккал")

    # Метод запуску розрахунку через введення користувача
    def run(self):
        print(self.describe())

    @classmethod
    def get_instance_count(cls):
        return f"Створено об'єктів CalorieCalculator: {cls.instance_count}"

    @classmethod
    def from_string(cls, data_str):
        # Альтернативний конструктор: "Яблуко,150,52"
        parts = data_str.split(',')
        product_name = parts[0].strip()
        weight = float(parts[1])
        calories_per_100g = float(parts[2])
        return cls(product_name, weight, calories_per_100g)

    @staticmethod
    def is_valid_calorie_value(value):
        return isinstance(value, (int, float)) and value >= 0


# Створення об'єктів
food1 = CalorieCalculator("Банан", 120, 89)
food2 = CalorieCalculator("Авокадо", 200, 160)

# Використання альтернативного конструктора
food3 = CalorieCalculator.from_string("Яблуко,150,52")

# Виклики
food1.run()
food2.run()
food3.run()

# Метод класу
print(CalorieCalculator.get_instance_count())

# Статичний метод
print("Чи допустима калорійність -5?", CalorieCalculator.is_valid_calorie_value(-5))
print("Чи допустима калорійність 100?", food1.is_valid_calorie_value(100))