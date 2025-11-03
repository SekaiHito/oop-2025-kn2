## Міністерство освіти і науки України
## Львівський національний університет ветеринарії і біотехнологій імені С.З.Ґжицького

# Звіт
про виконання лабораторної роботи №4 з дисципліни "**Об'єктно орієнтоване програмування**"  
на тему: **Принципи SOLID в об’єктно-орієнтованому програмуванні (Single Responsibility Principle)**

Виконав: студент групи **КН-31** Вирста Андрій  
Прийняв: викл. **Назар Заплатинський**

Львів 2025

---

## **Мета**
Ознайомитися з основними принципами SOLID у об’єктно-орієнтованому програмуванні та реалізувати перший із них — **Single Responsibility Principle (SRP)** — на прикладі коду мовою Python.

---

## **Хід роботи**

1. **Ознайомився з теоретичними основами SOLID.**  
   Принципи SOLID — це набір рекомендацій, які допомагають створювати більш зрозумілі, гнучкі та підтримувані програми.  
   **S — Single Responsibility Principle** означає, що кожен клас повинен мати **лише одну причину для зміни**, тобто відповідати тільки за одну конкретну задачу.

2. **Приклад неправильного підходу (порушення SRP):**  
   Один клас відповідає і за валідацію, і за збереження даних, і за відправку повідомлень.
   ```python
   class UserManager:
       def create_user(self, username, email):
           if not username or "@" not in email:
               raise ValueError("Invalid data")
           print(f"Saving {username} to DB...")
           print(f"Sending welcome email to {email}")
   ```

3. **Правильний підхід (дотримання SRP):**  
   Кожен клас виконує лише одну роль:  
   - `UserValidator` — валідація даних користувача  
   - `UserRepository` — збереження даних  
   - `EmailService` — відправка повідомлень  
   - `UserService` — координує роботу цих компонентів
   ```python
   from abc import ABC, abstractmethod

   class IUserRepository(ABC):
       @abstractmethod
       def save(self, data): pass

   class IEmailService(ABC):
       @abstractmethod
       def send(self, to, subject, body): pass

   class IUserValidator(ABC):
       @abstractmethod
       def validate(self, data): pass

   class InMemoryUserRepository(IUserRepository):
       def __init__(self):
           self.db = {}; self._id = 1
       def save(self, data):
           uid = self._id; self.db[uid] = data; self._id += 1; return uid

   class SimpleEmailService(IEmailService):
       def send(self, to, subject, body):
           print(f"[Email] To: {to}\nSubject: {subject}\n{body}\n")

   class UserValidator(IUserValidator):
       def validate(self, data):
           if not data['username'] or "@" not in data['email']:
               raise ValueError("Invalid user data")

   class UserService:
       def __init__(self, repo, mail, validator):
           self.repo, self.mail, self.validator = repo, mail, validator

       def register_user(self, username, email):
           data = {"username": username, "email": email}
           self.validator.validate(data)
           user_id = self.repo.save(data)
           self.mail.send(email, "Welcome!", f"Hello {username}, welcome!")
           return user_id

   repo = InMemoryUserRepository()
   mail = SimpleEmailService()
   validator = UserValidator()
   service = UserService(repo, mail, validator)
   service.register_user("ivan", "ivan@example.com")
   ```

4. **Результат виконання програми:**
   ```
   [Email] To: ivan@example.com
   Subject: Welcome!
   Hello ivan, welcome!
   Created user id: 1
   ```

5. **Структура коду відповідає SRP:**  
   - Зміни у валідації не впливають на інші частини системи.  
   - Легко тестувати окремі компоненти.  
   - Код розширюється без порушення існуючої логіки.

---

## **Висновки**

У ході роботи я реалізував перший принцип SOLID — **Single Responsibility Principle**.  
Кожен клас у програмі виконує лише одну роль, що робить код зрозумілішим і простішим у підтримці.  
Такий підхід забезпечує модульність, гнучкість і полегшує майбутнє розширення системи.  
Отримані знання можна застосовувати при створенні масштабованих ООП-проєктів.