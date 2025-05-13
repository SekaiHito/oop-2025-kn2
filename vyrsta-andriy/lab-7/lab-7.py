class CalorieCalculator:
    """Калькулятор калорій для продуктів харчування"""
    instance_count = 0  # Лічильник створених об'єктів

    def __init__(self, product_name, weight, calories_per_100g):
        """Ініціалізація об'єкта"""
        self.product_name = product_name
        self.weight = weight
        self.calories_per_100g = calories_per_100g
        self.total_calories = self.calculate_calories()

        CalorieCalculator.instance_count += 1  # Збільшуємо лічильник об'єктів

    def calculate_calories(self):
        """Розрахунок загальної калорійності продукту"""
        return (self.weight / 100) * self.calories_per_100g

    def describe(self):
        """Формування опису об'єкта"""
        return (f"Продукт: {self.product_name}\n"
                f"Маса: {self.weight} г\n"
                f"Калорійність: {self.calories_per_100g} ккал на 100 г\n"
                f"Загальні калорії: {self.total_calories:.2f} ккал")

    def run(self):
        """Запуск розрахунку через введення користувача"""
        print(self.describe())

    @classmethod
    def get_instance_count(cls):
        """Отримання кількості створених об'єктів"""
        return f"Створено об'єктів CalorieCalculator: {cls.instance_count}"

    @classmethod
    def from_string(cls, data_str):
        """Альтернативний конструктор з рядка (формат: 'Яблуко,150,52')"""
        product_name, weight, calories_per_100g = map(str.strip, data_str.split(','))
        return cls(product_name, float(weight), float(calories_per_100g))

    @staticmethod
    def is_valid_calorie_value(value):
        """Перевірка коректності введеного значення калорій"""
        return isinstance(value, (int, float)) and value >= 0


# === Основна логіка програми ===

# Створення об'єктів
food_items = [
    CalorieCalculator("Банан", 120, 89),
    CalorieCalculator("Авокадо", 200, 160),
    CalorieCalculator.from_string("Яблуко,150,52")
]

# Виклики
for food in food_items:
    food.run()

# Виведення загальної кількості створених об'єктів
print(CalorieCalculator.get_instance_count())

# Використання статичного методу для перевірки коректності значення калорій
print("Чи допустима калорійність -5?", CalorieCalculator.is_valid_calorie_value(-5))
print("Чи допустима калорійність 100?", food_items[0].is_valid_calorie_value(100))
