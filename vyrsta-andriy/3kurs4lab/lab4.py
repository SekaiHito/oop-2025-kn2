from abc import ABC, abstractmethod
from typing import Dict, Any

# --- Інтерфейси / абстракції (для легкого тестування та заміни реалізацій) ---
class IUserRepository(ABC):
    @abstractmethod
    def save(self, user_data: Dict[str, Any]) -> int:
        pass

class IEmailService(ABC):
    @abstractmethod
    def send(self, to: str, subject: str, body: str) -> None:
        pass

class IUserValidator(ABC):
    @abstractmethod
    def validate(self, user_data: Dict[str, Any]) -> None:
        pass

# --- Реальні реалізації (можуть бути замінені під час тестування) ---
class InMemoryUserRepository(IUserRepository):
    def __init__(self):
        self._store = {}
        self._next_id = 1

    def save(self, user_data: Dict[str, Any]) -> int:
        user_id = self._next_id
        self._store[user_id] = user_data
        self._next_id += 1
        return user_id

class SimpleEmailService(IEmailService):
    def send(self, to: str, subject: str, body: str) -> None:
        print(f"[Email] To: {to}\nSubject: {subject}\n\n{body}\n")

class UserValidator(IUserValidator):
    def validate(self, user_data: Dict[str, Any]) -> None:
        username = user_data.get("username")
        email = user_data.get("email")
        if not username or not username.strip():
            raise ValueError("username required")
        if not email or "@" not in email:
            raise ValueError("invalid email")

# --- Сервіс, що оркеструє роботу (має одну відповідальність: бізнес-логіку користувача) ---
class UserService:
    def __init__(self,
                 repository: IUserRepository,
                 email_service: IEmailService,
                 validator: IUserValidator):
        self._repo = repository
        self._email = email_service
        self._validator = validator

    def register_user(self, username: str, email: str) -> int:
        user_data = {"username": username, "email": email}
        self._validator.validate(user_data)
        user_id = self._repo.save(user_data)
        subject = "Welcome!"
        body = f"Hello {username}, welcome aboard!"
        self._email.send(email, subject, body)
        return user_id

# --- Приклад використання ---
if __name__ == "__main__":
    repo = InMemoryUserRepository()
    email_service = SimpleEmailService()
    validator = UserValidator()

    user_service = UserService(repo, email_service, validator)

    new_id = user_service.register_user("ivan", "ivan@example.com")
    print("Created user id:", new_id)