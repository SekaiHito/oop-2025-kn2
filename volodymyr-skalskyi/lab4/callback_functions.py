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

# 2. Кілька callback-функцій
def square(x):
    """Функція для піднесення до квадрату"""
    return x ** 2

def cube(x):
    """Функція для піднесення до кубу"""
    return x ** 3

def apply_operation(number, operation):
    """Функція, яка застосовує операцію до числа"""
    return operation(number)

print("\n2. Кілька callback-функцій:")
number = 5
print(f"Квадрат числа {number}: {apply_operation(number, square)}")
print(f"Куб числа {number}: {apply_operation(number, cube)}")

# 3. Callback з додатковими параметрами
def format_number(number, format_type="decimal"):
    """Функція форматування числа"""
    if format_type == "binary":
        return bin(number)
    elif format_type == "hex":
        return hex(number)
    else:
        return str(number)

def process_number(number, formatter, format_type="decimal"):
    """Функція, яка використовує callback з додатковими параметрами"""
    return formatter(number, format_type)

print("\n3. Callback з додатковими параметрами:")
number = 42
print(f"Десяткове представлення: {process_number(number, format_number)}")
print(f"Двійкове представлення: {process_number(number, format_number, 'binary')}")
print(f"Шістнадцяткове представлення: {process_number(number, format_number, 'hex')}")

# 4. Callback з лямбда-функціями
def apply_to_list(numbers, operation):
    """Функція, яка застосовує операцію до кожного елемента списку"""
    return [operation(x) for x in numbers]

print("\n4. Callback з лямбда-функціями:")
numbers = [1, 2, 3, 4, 5]
print(f"Оригінальний список: {numbers}")
print(f"Подвоєні числа: {apply_to_list(numbers, lambda x: x * 2)}")
print(f"Квадрати чисел: {apply_to_list(numbers, lambda x: x ** 2)}")

# 5. Callback для фільтрації
def filter_numbers(numbers, predicate):
    """Функція, яка фільтрує список за заданою умовою"""
    return [x for x in numbers if predicate(x)]

print("\n5. Callback для фільтрації:")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Оригінальний список: {numbers}")
print(f"Парні числа: {filter_numbers(numbers, lambda x: x % 2 == 0)}")
print(f"Числа більше 5: {filter_numbers(numbers, lambda x: x > 5)}")

# 6. Callback для сортування
def custom_sort(items, key_func):
    """Функція, яка сортує список за заданою функцією"""
    return sorted(items, key=key_func)

print("\n6. Callback для сортування:")
words = ["банан", "яблуко", "апельсин", "груша"]
print(f"Оригінальний список: {words}")
print(f"Сортування за довжиною: {custom_sort(words, len)}")
print(f"Сортування за останньою літерою: {custom_sort(words, lambda x: x[-1])}") 