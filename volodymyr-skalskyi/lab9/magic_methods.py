"""
Приклад магічних методів
"""

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def __add__(self, other):
        """Перевизначення оператора + для додавання коштів"""
        return BankAccount(self.balance + other.balance)

    def __sub__(self, other):
        """Перевизначення оператора - для зняття коштів"""
        if self.balance < other.balance:
            raise ValueError("Недостатньо коштів на рахунку")
        return BankAccount(self.balance - other.balance)

    def __mul__(self, percent):
        """Перевизначення оператора * для нарахування відсотків"""
        return BankAccount(self.balance * (1 + percent/100))

    def __str__(self):
        """Перевизначення методу str()"""
        return f"Баланс: {self.balance} грн"

print("Магічні методи:")
account1 = BankAccount(1000)
account2 = BankAccount(500)
print(f"account1 + account2 = {account1 + account2}")    # Баланс: 1500 грн
print(f"account1 - account2 = {account1 - account2}")    # Баланс: 500 грн
print(f"account1 * 10 = {account1 * 10}")               # Баланс: 1100 грн (10% річних)
