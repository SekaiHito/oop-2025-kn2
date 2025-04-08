print("Демонстрація callback-функцій в Python")
print("-" * 40)

# 1. Проста callback-функція
def greet(name):
    """Функція привітання"""
    return f"Привіт, {name}!"

def process_name(name, callback):
    """Функція, яка приймає callback"""
    return callback(name)

print("\n1. Проста callback-функція:")
result = process_name("Володимир", greet)
print(result)
