"""
Приклад декораторів
"""

def debug(func):
    """Декоратор для відстеження викликів функцій"""
    def wrapper(*args, **kwargs):
        print(f"Виклик функції {func.__name__} з аргументами {args} та {kwargs}")
        result = func(*args, **kwargs)
        print(f"Результат: {result}")
        return result
    return wrapper

@debug
def multiply(a, b):
    return a * b

print("Декоратори:")
multiply(5, 3)  # Виведе інформацію про виклик та результат
