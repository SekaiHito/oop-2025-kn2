def register_user(username, password):
    
    # 1. Валідація (Перевірка)
    if len(username) < 4:
        print("Помилка: Ім'я користувача занадто коротке!")
        return
    if len(password) < 8:
        print("Помилка: Пароль занадто короткий!")
        return
    if not any(char.isdigit() for char in password):
        print("Помилка: Пароль має містити хоча б одну цифру!")
        return
    
    # 2. Створення2

    user = {'name': username, 'pass': password}
    print(f"Користувача {username} створено.")
    
    # 3. Збереження
    # ... (уявний код збереження в базу даних) ...
    print("Користувача збережено.")



def register_user(username, password):
    
    # 1. Валідація (стала одним рядком)
    if not is_credentials_valid(username, password):
        return
    
    # 2. Створення
    user = {'name': username, 'pass': password}
    print(f"Користувача {username} створено.")
    
    # 3. Збереження
    # ... (уявний код збереження в базу даних) ...
    print("Користувача збережено.")

# --- ВИОКРЕМЛЕНИЙ МЕТОД ---
def is_credentials_valid(username, password):
    """Перевіряє, чи ім'я та пароль відповідають правилам."""
    if len(username) < 4:
        print("Помилка: Ім'я користувача занадто коротке!")
        return False
    if len(password) < 8:
        print("Помилка: Пароль занадто короткий!")
        return False
    if not any(char.isdigit() for char in password):
        print("Помилка: Пароль має містити хоча б одну цифру!")
        return False
        
    return True