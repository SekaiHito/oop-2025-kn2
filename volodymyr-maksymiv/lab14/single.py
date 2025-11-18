# ПОГАНО: Клас має дві відповідальності

class Post:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def get_post_title(self):
        return self.title

    # !!! ЦЕЙ МЕТОД ПОРУШУЄ SRP !!!
    # Це відповідальність за ЗБЕРІГАННЯ
    def save_to_database(self):
        # ... код для підключення до бази даних ...
        print(f"Збереження '{self.title}' в базу даних...")
        # ...



# ДОБРЕ: Кожен клас має одну відповідальність

# Клас 1: Відповідає ТІЛЬКИ за дані поста
class Post:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def get_post_title(self):
        return self.title

# Клас 2: Відповідає ТІЛЬКИ за збереження поста
class PostRepository:
    def save(self, post):
        # ... код для підключення до бази даних ...
        print(f"Збереження '{post.get_post_title()}' в базу даних...")
        # ...