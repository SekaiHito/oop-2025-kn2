print("Демонстрація математичних функцій в Python")
print("-" * 40)

import math

# 1. Базові математичні операції
def calculate_basic_math(a, b):
    """Функція для базових математичних операцій"""
    print(f"Додавання: {a + b}")
    print(f"Віднімання: {a - b}")
    print(f"Множення: {a * b}")
    print(f"Ділення: {a / b if b != 0 else 'Помилка: ділення на нуль'}")

print("\n1. Базові математичні операції:")
calculate_basic_math(10, 3)

# 2. Тригонометричні функції
def calculate_trigonometry(angle_degrees):
    """Функція для обчислення тригонометричних функцій"""
    angle_radians = math.radians(angle_degrees)
    print(f"Синус: {math.sin(angle_radians):.4f}")
    print(f"Косинус: {math.cos(angle_radians):.4f}")
    print(f"Тангенс: {math.tan(angle_radians):.4f}")

print("\n2. Тригонометричні функції:")
calculate_trigonometry(45)
