print("Демонстрація роботи зі словниками в Python")
print("-" * 40)

# Створення словника
student = {
    'name': 'John',
    'age': 20,
    'grades': [85, 90, 88]
}

print("Базові операції зі словниками:")
print(f"Словник: {student}")

# Доступ до елементів
print(f"\nДоступ до елементів:")
print(f"Ім'я: {student['name']}")
print(f"Вік: {student['age']}")
print(f"Оцінки: {student['grades']}")

# Зміна значень
student['age'] = 21
print(f"\nПісля зміни віку: {student}")

# Додавання нових елементів
student['email'] = 'john@example.com'
print(f"Після додавання email: {student}")

# Видалення елементів
del student['grades']
print(f"Після видалення grades: {student}")

# Методи словників
print(f"\nМетоди словників:")
print(f"Ключі: {list(student.keys())}")
print(f"Значення: {list(student.values())}")
print(f"Пари ключ-значення: {list(student.items())}")

# Вкладені словники
course = {
    'name': 'Python Programming',
    'instructor': {
        'name': 'Dr. Smith',
        'department': 'Computer Science'
    },
    'students': ['John', 'Alice', 'Bob']
}

print(f"\nВкладені словники:")
print(f"Курс: {course}")
print(f"Інструктор: {course['instructor']['name']}")
print(f"Кафедра: {course['instructor']['department']}")

# Перевірка наявності ключа
print(f"\nПеревірка наявності ключа:")
print(f"'name' in student: {'name' in student}")
print(f"'grades' in student: {'grades' in student}") 