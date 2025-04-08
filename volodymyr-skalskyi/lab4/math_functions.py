print("Демонстрація математичних функцій в Python")
print("-" * 40)

import math

# 1. Базові математичні операції
def calculate_basic_math(a, b):
    """Функція для базових математичних операцій"""
    return {
        "додавання": a + b,
        "віднімання": a - b,
        "множення": a * b,
        "ділення": a / b if b != 0 else "Помилка: ділення на нуль",
        "цілочисельне ділення": a // b if b != 0 else "Помилка: ділення на нуль",
        "остача від ділення": a % b if b != 0 else "Помилка: ділення на нуль",
        "піднесення до степеня": a ** b
    }

print("\n1. Базові математичні операції:")
a, b = 10, 3
results = calculate_basic_math(a, b)
for operation, result in results.items():
    print(f"{operation}: {result}")

# 2. Тригонометричні функції
def calculate_trigonometry(angle_degrees):
    """Функція для обчислення тригонометричних функцій"""
    angle_radians = math.radians(angle_degrees)
    return {
        "синус": math.sin(angle_radians),
        "косинус": math.cos(angle_radians),
        "тангенс": math.tan(angle_radians),
        "арксинус": math.degrees(math.asin(math.sin(angle_radians))),
        "арккосинус": math.degrees(math.acos(math.cos(angle_radians))),
        "арктангенс": math.degrees(math.atan(math.tan(angle_radians)))
    }

print("\n2. Тригонометричні функції:")
angle = 45
results = calculate_trigonometry(angle)
for func, result in results.items():
    print(f"{func}({angle}°) = {result:.4f}")

# 3. Логарифмічні функції
def calculate_logarithms(number, base=10):
    """Функція для обчислення логарифмів"""
    if number <= 0:
        return "Помилка: число має бути додатним"
    if base <= 0 or base == 1:
        return "Помилка: основа логарифма має бути додатним числом, відмінним від 1"
    
    return {
        "натуральний логарифм": math.log(number),
        f"логарифм за основою {base}": math.log(number, base)
    }

print("\n3. Логарифмічні функції:")
number = 100
results = calculate_logarithms(number)
for func, result in results.items():
    print(f"{func}({number}) = {result:.4f}")

# 4. Функції округлення
def demonstrate_rounding(number):
    """Функція для демонстрації різних методів округлення"""
    return {
        "округлення до найближчого цілого": round(number),
        "округлення вгору": math.ceil(number),
        "округлення вниз": math.floor(number),
        "відкидання дробової частини": math.trunc(number)
    }

print("\n4. Функції округлення:")
number = 3.7
results = demonstrate_rounding(number)
for method, result in results.items():
    print(f"{method}: {result}")

# 5. Статистичні функції
def calculate_statistics(numbers):
    """Функція для обчислення статистичних показників"""
    if not numbers:
        return "Помилка: список чисел порожній"
    
    return {
        "кількість елементів": len(numbers),
        "сума": sum(numbers),
        "середнє арифметичне": sum(numbers) / len(numbers),
        "мінімальне значення": min(numbers),
        "максимальне значення": max(numbers)
    }

print("\n5. Статистичні функції:")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
results = calculate_statistics(numbers)
for stat, result in results.items():
    print(f"{stat}: {result}")

# 6. Функції для роботи з комплексними числами
def work_with_complex_numbers(real, imag):
    """Функція для роботи з комплексними числами"""
    z = complex(real, imag)
    return {
        "комплексне число": z,
        "дійсна частина": z.real,
        "уявна частина": z.imag,
        "модуль": abs(z),
        "спряжене число": z.conjugate()
    }

print("\n6. Робота з комплексними числами:")
real, imag = 3, 4
results = work_with_complex_numbers(real, imag)
for operation, result in results.items():
    print(f"{operation}: {result}") 