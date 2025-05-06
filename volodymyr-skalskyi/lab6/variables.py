# Константи
MIN_BALANCE = 0
MAX_WITHDRAWAL = 10000
INTEREST_RATE = 0.05  # 5% річних

class BankAccount:
    # Змінна класу
    bank_name = "Український Банк"
    
    # Статична змінна
    total_accounts = 0
    
    def __init__(self, account_holder, initial_balance=0):
        # Змінні екземпляра
        self.account_holder = account_holder
        self.balance = initial_balance
        
        # Захищена змінна
        self._transaction_count = 0
        
        # Приватна змінна
        self.__account_number = None
        
        # Збільшуємо лічильник рахунків
        BankAccount.total_accounts += 1
    
    def set_account_number(self, account_number):
        # Метод для встановлення приватної змінної
        self.__account_number = account_number
    
    def get_account_number(self):
        # Метод для отримання приватної змінної
        return self.__account_number
    
    def deposit(self, amount):
        # Метод для поповнення рахунку
        if amount > 0:
            self.balance += amount
            self._transaction_count += 1
            return True
        return False
    
    def withdraw(self, amount):
        # Метод для зняття коштів
        if 0 < amount <= MAX_WITHDRAWAL and self.balance - amount >= MIN_BALANCE:
            self.balance -= amount
            self._transaction_count += 1
            return True
        return False
    
    def get_transaction_count(self):
        # Метод для отримання захищеної змінної
        return self._transaction_count

 # Створюємо об'єкти класу BankAccount
account1 = BankAccount("Іван Петренко", 1000)
account2 = BankAccount("Марія Коваленко", 5000)

# Встановлюємо номери рахунків
account1.set_account_number("UA123456789")
account2.set_account_number("UA987654321")

# Виконуємо операції
account1.deposit(500)
account1.withdraw(200)
account2.deposit(1000)
account2.withdraw(3000)

# Виводимо інформацію про рахунки
print(f"Банк: {BankAccount.bank_name}")
print(f"Загальна кількість рахунків: {BankAccount.total_accounts}")
print("\nІнформація про рахунки:")
print(f"Рахунок 1: {account1.account_holder}")
print(f"Номер рахунку: {account1.get_account_number()}")
print(f"Баланс: {account1.balance} грн")
print(f"Кількість транзакцій: {account1.get_transaction_count()}")

print(f"\nРахунок 2: {account2.account_holder}")
print(f"Номер рахунку: {account2.get_account_number()}")
print(f"Баланс: {account2.balance} грн")
print(f"Кількість транзакцій: {account2.get_transaction_count()}")

# Демонстрація констант
print(f"\nКонстанти:")
print(f"Мінімальний баланс: {MIN_BALANCE} грн")
print(f"Максимальна сума зняття: {MAX_WITHDRAWAL} грн")
print(f"Відсоткова ставка: {INTEREST_RATE * 100}%")