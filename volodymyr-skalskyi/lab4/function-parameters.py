print("Демонстрація різних типів параметрів та аргументів функцій")
print("-" * 40)

# 1. Позиційні аргументи
def describe_person(name, age, city):
    """Функція з позиційними аргументами"""
    print(f"{name} має {age} років і живе в місті {city}")

print("\n1. Позиційні аргументи:")
describe_person("Володимир", 20, "Львів")

# 2. Іменовані аргументи
print("\n2. Іменовані аргументи:")
describe_person(name="Марія", age=19, city="Київ")
describe_person(city="Одеса", name="Петро", age=21)

# 3. Аргументи за замовчуванням
def create_profile(name, age=18, city="Львів", hobby=None):
    """Функція з аргументами за замовчуванням"""
    profile = f"Ім'я: {name}, Вік: {age}, Місто: {city}"
    if hobby:
        profile += f", Хобі: {hobby}"
    return profile

print("\n3. Аргументи за замовчуванням:")
print(create_profile("Анна"))
print(create_profile("Іван", 22))
print(create_profile("Олена", city="Харків"))
print(create_profile("Максим", hobby="Програмування"))

