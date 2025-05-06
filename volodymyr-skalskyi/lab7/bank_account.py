class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def __add__(self, other):
        return BankAccount(self.balance + other.balance)

    def __sub__(self, other):
        if self.balance < other.balance:
            raise ValueError("Недостатньо коштів на рахунку")
        return BankAccount(self.balance - other.balance)

    def __mul__(self, percent):
        return BankAccount(self.balance * (1 + percent/100))

    def __str__(self):
        return f"Баланс: {self.balance} грн"
    @classmethod
    def create_with_bonus(cls, initial_balance, bonus_percent):
        """Створює новий рахунок з бонусом до початкового балансу"""
        bonus_amount = initial_balance * (bonus_percent / 100)
        return cls(initial_balance + bonus_amount)

print("Магічні методи:")
account1 = BankAccount(1000)
account2 = BankAccount(500)
print(f"account1 + account2 = {account1 + account2}")    # Баланс: 1500 грн
print(f"account1 - account2 = {account1 - account2}")    # Баланс: 500 грн
print(f"account1 * 10 = {account1 * 10}")               # Баланс: 1100 грн (10% річних)

# Використання create_with_bonus
account3 = BankAccount.create_with_bonus(1000, 10)
print(f"account3 = {account3}")  # Баланс: 1100 грн (10% бонус)
