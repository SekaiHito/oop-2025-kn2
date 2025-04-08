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

# 4. Змінна кількість позиційних аргументів (*args)
def sum_numbers(*args):
    """Функція, що приймає змінну кількість позиційних аргументів"""
    return sum(args)

print("\n4. Змінна кількість позиційних аргументів:")
print(f"Сума чисел 1, 2, 3: {sum_numbers(1, 2, 3)}")
print(f"Сума чисел 1, 2, 3, 4, 5: {sum_numbers(1, 2, 3, 4, 5)}")

# 5. Змінна кількість іменованих аргументів (**kwargs)
def print_info(**kwargs):
    """Функція, що приймає змінну кількість іменованих аргументів"""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print("\n5. Змінна кількість іменованих аргументів:")
print_info(name="Володимир", age=20, city="Львів", hobby="Програмування")

# 6. Комбінація різних типів аргументів
def complex_function(pos1, pos2, /, *, kw1, kw2, **kwargs):
    """Функція з комбінацією різних типів аргументів"""
    print(f"Позиційні аргументи: {pos1}, {pos2}")
    print(f"Іменовані аргументи: {kw1}, {kw2}")
    print(f"Додаткові іменовані аргументи: {kwargs}")

print("\n6. Комбінація різних типів аргументів:")
complex_function(1, 2, kw1="перший", kw2="другий", extra="додатковий")

# 7. Розпакування аргументів
def unpack_demo(a, b, c):
    """Функція для демонстрації розпакування аргументів"""
    print(f"a = {a}, b = {b}, c = {c}")

print("\n7. Розпакування аргументів:")
numbers = [1, 2, 3]
unpack_demo(*numbers)  # Розпакування списку

params = {"a": 10, "b": 20, "c": 30}
unpack_demo(**params)  # Розпакування словника 