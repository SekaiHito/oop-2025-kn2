print("Демонстрація базових операцій з рядками в Python")
print("-" * 40)

# Базові операції з рядками
str1 = "Python"
str2 = "Programming"

print("Базові операції з рядками:")
print(f"Конкатенація: {str1 + ' ' + str2}")
print(f"Повторення: {str1 * 3}")

# Методи рядків
text = "   python programming   "
print(f"\nМетоди рядків:")
print(f"Оригінал: '{text}'")
print(f"Верхній регістр: '{text.upper()}'")
print(f"Нижній регістр: '{text.lower()}'")
print(f"Видалення пробілів: '{text.strip()}'")

# Пошук та заміна
sentence = "Python is awesome. Python is powerful."
print(f"\nПошук та заміна:")
print(f"Оригінал: {sentence}")
print(f"Кількість 'Python': {sentence.count('Python')}")
print(f"Позиція першого 'Python': {sentence.find('Python')}")
print(f"Заміна 'Python' на 'Java': {sentence.replace('Python', 'Java')}")

# Розділення рядка
words = "Python,Java,C++,JavaScript"
print(f"\nРозділення рядка:")
print(f"Оригінал: {words}")
print(f"Список слів: {words.split(',')}")
