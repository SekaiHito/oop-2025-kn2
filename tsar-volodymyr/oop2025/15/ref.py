from typing import Tuple

class RegistrationService:
    """
    Сервіс, що відповідає за реєстрацію користувачів.
    Демонструє техніку 'Extract Method': складна логіка розбита на менші методи.
    """

    def register_user(self, username: str, password: str) -> None:
        """
        Головний метод, який керує процесом.
        Він читається як зміст книги завдяки винесенню деталей у під-методи.
        """
        print(f"🚀 Починаємо реєстрацію для: {username}")

        # 1. Валідація (Винесена в окремий метод)
        is_valid, error_message = self._validate_credentials(username, password)
        
        if not is_valid:
            print(f"❌ Реєстрацію скасовано: {error_message}")
            return

        # 2. Створення та збереження (Винесено в окремі методи)
        user_data = self._create_user_entity(username, password)
        self._save_to_database(user_data)
        
        print(f"✅ Успіх: Користувач {username} зареєстрований.")

    # --- EXTRACTED METHODS (Виокремлені методи) ---
    
    def _validate_credentials(self, username: str, password: str) -> Tuple[bool, str]:
        """
        Перевіряє валідіність даних.
        Повертає кортеж (успіх, повідомлення).
        Метод є 'чистим' — він не друкує нічого в консоль, лише повертає дані.
        """
        if len(username) < 4:
            return False, "Ім'я користувача занадто коротке (мін. 4 символи)."
        
        if len(password) < 8:
            return False, "Пароль занадто короткий (мін. 8 символів)."
        
        if not any(char.isdigit() for char in password):
            return False, "Пароль має містити хоча б одну цифру."
            
        return True, "OK"

    def _create_user_entity(self, username: str, password: str) -> dict:
        """Створює структуру даних користувача."""
        # У реальному проекті тут було б хешування пароля
        return {
            'username': username, 
            'password_hash': f"HASHED_{password}", # Імітація безпеки
            'role': 'user'
        }

    def _save_to_database(self, user_data: dict) -> None:
        """Імітує збереження в базу даних."""
        print(f"💾 [DB] INSERT INTO users VALUES ({user_data['username']}...)")


if __name__ == "__main__":
    service = RegistrationService()

    # Сценарій 1: Помилка (короткий пароль)
    print("--- Тест 1 ---")
    service.register_user("admin", "pass") 

    print("\n--- Тест 2 ---")
    # Сценарій 2: Успіх
    service.register_user("Volodymyr", "SuperSecret123")