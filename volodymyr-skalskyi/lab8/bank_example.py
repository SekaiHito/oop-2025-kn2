"""
Приклад використання модуля BankAccount
"""

from bank_account import BankAccount

# Створюємо рахунок з вказаним власником
print("\nСтворюємо рахунок:")
named_account = BankAccount()
print(named_account)

# Виконуємо операції з рахунком
print("\nВиконуємо операції з рахунком:")
print(named_account.deposit(500))
print(named_account.withdraw(200))
print(named_account.get_balance())
print(named_account.get_transaction_history())