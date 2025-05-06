print("Демонстрація математичних функцій в Python")

import math

def calculate_trigonometry(angle_degrees):
    """Функція для обчислення тригонометричних функцій"""
    angle_radians = math.radians(angle_degrees)
    print(f"Синус: {math.sin(angle_radians):.4f}")
    print(f"Косинус: {math.cos(angle_radians):.4f}")
    print(f"Тангенс: {math.tan(angle_radians):.4f}")

print("\n2. Тригонометричні функції:")
calculate_trigonometry(45)
