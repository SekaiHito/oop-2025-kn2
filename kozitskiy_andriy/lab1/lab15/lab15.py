import re
import random

print("=== ПОРУШЕННЯ SRP ===\n")

def register_user_bad(name: str, email: str) -> int:
    # Перевірка email
    email_regex = r'^[^\s@]+@[^\s@]+\.[^\s@]+$'
    if not re.match(email_regex, email):
        raise ValueError("Невірний формат email")

    # Перевірка імені
    if not name or name.strip() == "":
        raise ValueError("Ім'я не може бути порожнім")
    if len(name) < 2:
        raise ValueError("Ім'я занадто коротке")

    # Збереження користувача
    print(f"Збереження користувача {name} в БД...")
    user_id = random.randint(1, 10000)
    print(f"Користувач збережено з ID: {user_id}")

    # Відправка email
    print(f"Відправка привітального email на {email}...")
    print("Email відправлено!")

    # Логування
    print(f"[LOG] Користувач {user_id} зареєстровано. Email: {email}")

    # Створення профілю
    print(f"Створення профілю для користувача {name}...")
    print("Профіль створено!")

    return user_id

try:
    register_user_bad("Марія Іванова", "maria.ivanova@example.com")
except ValueError as error:
    print(f"Помилка: {error}")

print("\n=== ДОТРИМАННЯ SRP ===\n")

# Константи
EMAIL_REGEX = r'^[^\s@]+@[^\s@]+\.[^\s@]+$'
MIN_NAME_LENGTH = 2
ERROR_MESSAGES = {
    "INVALID_EMAIL": "Невірний формат email",
    "EMPTY_NAME": "Ім'я не може бути порожнім",
    "SHORT_NAME": "Ім'я занадто коротке"
}

# Функції SRP
def validate_email(email: str):
    if not re.match(EMAIL_REGEX, email):
        raise ValueError(ERROR_MESSAGES["INVALID_EMAIL"])

def validate_name(name: str):
    if not name or name.strip() == "":
        raise ValueError(ERROR_MESSAGES["EMPTY_NAME"])
    if len(name) < MIN_NAME_LENGTH:
        raise ValueError(ERROR_MESSAGES["SHORT_NAME"])

def save_user(name: str) -> int:
    print(f"Збереження користувача {name} в БД...")
    user_id = random.randint(1, 10000)
    print(f"Користувач збережено з ID: {user_id}")
    return user_id

def send_welcome_email(email: str):
    print(f"Відправка привітального email на {email}...")
    print("Email відправлено!")

def log_user_registration(user_id: int, email: str):
    print(f"[LOG] Користувач {user_id} зареєстровано. Email: {email}")

def create_profile(name: str):
    print(f"Створення профілю для користувача {name}...")
    print("Профіль створено!")

def register_user(name: str, email: str) -> int:
    validate_email(email)
    validate_name(name)

    user_id = save_user(name)
    send_welcome_email(email)
    log_user_registration(user_id, email)
    create_profile(name)

    return user_id

try:
    register_user("Олександр Коваль", "oleksandr.koval@example.com")
except ValueError as error:
    print(f"Помилка: {error}")
