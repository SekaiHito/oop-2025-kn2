#поганий приклад
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def is_email_valid(self):
        return "@" in self.email

    def save_to_database(self):
        print(f"Saving {self.name} to database...")

#правильне використання
class User:

    def __init__(self, name, email):
        self.name = name
        self.email = email


class UserValidator:
    
    @staticmethod
    def is_valid_email(email):
        return "@" in email


class UserRepository:
    
    @staticmethod
    def save(user: User):
        print(f"Користувача {user.name} збережено в базі")
