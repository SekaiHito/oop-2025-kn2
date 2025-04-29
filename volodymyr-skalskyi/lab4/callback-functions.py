print("Демонстрація callback-функцій в Python")

# 1. Проста callback-функція
def greet(name):
    return f"Привіт, {name}!"

def process_name(name, callback):
    return callback(name)

print("\n1. Проста callback-функція:")
result = process_name("Володимир", greet)
print(result)
