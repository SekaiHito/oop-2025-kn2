"""
Модуль для роботи з банківським рахунком
"""

from datetime import datetime
from faker import Faker

# Ініціалізуємо Faker для української мови
fake = Faker('uk_UA')

class BankAccount:
    def __init__(self, owner=None, balance=0):
        """Ініціалізація рахунку"""
        self.owner = owner or fake.name()
        self.account_number = fake.iban()
        self.email = fake.email()
        self.phone = fake.phone_number()
        self.balance = balance
        self.transactions = []
        self._add_transaction("Створення рахунку", balance)

    def deposit(self, amount):
        """Поповнення рахунку"""
        if amount > 0:
            self.balance += amount
            self._add_transaction("Поповнення", amount)
            return f"Рахунок поповнено на {amount}. Поточний баланс: {self.balance}"
        return "Сума поповнення має бути більше 0"

    def withdraw(self, amount):
        """Зняття коштів з рахунку"""
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                self._add_transaction("Зняття", -amount)
                return f"Знято {amount}. Поточний баланс: {self.balance}"
            return "Недостатньо коштів на рахунку"
        return "Сума зняття має бути більше 0"

    def get_balance(self):
        """Отримання поточного балансу"""
        return f"Поточний баланс: {self.balance}"

    def get_transaction_history(self):
        """Отримання історії транзакцій"""
        history = "Історія транзакцій:\n"
        for transaction in self.transactions:
            history += f"{transaction['time']} - {transaction['type']}: {transaction['amount']}\n"
        return history

    def _add_transaction(self, transaction_type, amount):
        """Додавання транзакції в історію"""
        self.transactions.append({
            'time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'type': transaction_type,
            'amount': amount
        })

    def __str__(self):
        """Строкове представлення рахунку"""
        return f"Рахунок власника: {self.owner}\n" \
               f"Номер рахунку: {self.account_number}\n" \
               f"Email: {self.email}\n" \
               f"Телефон: {self.phone}\n" \
               f"Баланс: {self.balance}" 