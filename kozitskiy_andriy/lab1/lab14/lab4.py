import re

print("=== ПОРУШЕННЯ SRP ===\n")

class AccountBad:
    def __init__(self, full_name: str, email_address: str):
        self.full_name = full_name
        self.email_address = email_address

    def validate_email(self):
        pattern = r'^[^\s@]+@[^\s@]+\.[^\s@]+$'
        if not re.match(pattern, self.email_address):
            raise ValueError("Невірний формат email")

    def save_to_db(self):
        print(f"Збереження акаунта {self.full_name} в базі даних")

    def send_welcome_email(self):
        print(f"Відправка привітального email на {self.email_address}")


bad_account = AccountBad("Марія Іванова", "maria.ivanova@example.com")
bad_account.validate_email()
bad_account.save_to_db()
bad_account.send_welcome_email()


print("\n=== ДОТРИМАННЯ SRP ===\n")

class Account:
    def __init__(self, full_name: str, email_address: str):
        self.full_name = full_name
        self.email_address = email_address

class EmailValidator:
    def validate(self, email: str):
        pattern = r'^[^\s@]+@[^\s@]+\.[^\s@]+$'
        if not re.match(pattern, email):
            raise ValueError("Невірний формат email")

class AccountRepository:
    def save(self, account: Account):
        print(f"Збереження акаунта {account.full_name} в базі даних")

class EmailService:
    def send_welcome_email(self, account: Account):
        print(f"Відправка привітального email на {account.email_address}")


# Новий користувач
account = Account("Олександр Коваль", "oleksandr.koval@example.com")

# Використання сервісів
validator = EmailValidator()
repository = AccountRepository()
email_service = EmailService()

validator.validate(account.email_address)
repository.save(account)
email_service.send_welcome_email(account)
