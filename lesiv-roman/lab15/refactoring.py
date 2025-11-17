class Order:
    def __init__(self, client_name, date, items):
        self.client_name = client_name
        self.date = date
        self.items = items

    def print_details(self):
        # 1. Обчислення загальної суми
        # Цей блок занадто деталізований для основного методу
        total = 0
        for item in self.items:
            # Припускаємо, що item є словником або об'єктом з price та quantity
            total += item['price'] * item['quantity']

        # 2. Друк деталей
        # Цей блок виконує окреме завдання друку
        print("-------------------------")
        print(f"Клієнт: {self.client_name}")
        print(f"Загальна сума: {total:.2f}")
        print(f"Дата: {self.date}")
        print("-------------------------")
#До рефакторингу 

class Order:
    def __init__(self, client_name, date, items):
        self.client_name = client_name
        self.date = date
        self.items = items

    # === Новий Метод 1: Обчислення ===
    # Приватний метод (зазвичай позначається _), який відповідає лише за обчислення.
    def _calculate_total(self):
        """Обчислює загальну суму замовлення."""
        total = 0
        for item in self.items:
            total += item['price'] * item['quantity']
        return total

    # === Новий Метод 2: Друк ===
    # Приватний метод, який відповідає лише за форматований друк.
    def _print_header_and_details(self, total):
        """Друкує заголовок і деталі замовлення."""
        print("-------------------------")
        print(f"Клієнт: {self.client_name}")
        print(f"Загальна сума: {total:.2f}")
        print(f"Дата: {self.date}")
        print("-------------------------")

    # === Основний Рефакторинговий Метод ===
    # Тепер він виглядає як послідовність високорівневих кроків (зміст)
    def print_details(self):
        """Керує процесом обчислення та друку деталей замовлення."""
        total = self._calculate_total()
        self._print_header_and_details(total)