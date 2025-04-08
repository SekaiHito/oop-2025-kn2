print("Демонстрація різних типів циклів в Python")
print("-" * 40)

# Демонстрація циклу while
print("\nДемонстрація циклу while:")
count = 0
while count < 5:
    print(f"Лічильник: {count}")
    count += 1

# Демонстрація циклу for з range
print("\nДемонстрація циклу for з range:")
for i in range(5):
    print(f"Ітерація: {i}")

# Демонстрація циклу for зі списком
print("\nДемонстрація циклу for зі списком:")
fruits = ["яблуко", "банан", "апельсин"]
for fruit in fruits:
    print(f"Фрукт: {fruit}")

# Демонстрація break
print("\nДемонстрація break:")
for i in range(10):
    if i == 5:
        print("Досягнуто 5, вихід з циклу")
        break
    print(f"Число: {i}")

# Демонстрація continue
print("\nДемонстрація continue:")
for i in range(5):
    if i == 2:
        print("Пропускаємо 2")
        continue
    print(f"Число: {i}")

# Демонстрація вкладених циклів
print("\nДемонстрація вкладених циклів:")
for i in range(3):
    for j in range(3):
        print(f"i={i}, j={j}")

# Демонстрація циклу while з умовою
print("\nДемонстрація циклу while з умовою:")
number = 0
while number < 10:
    if number % 2 == 0:
        print(f"Парне число: {number}")
    number += 1

# Демонстрація циклу for з enumerate
print("\nДемонстрація циклу for з enumerate:")
for index, fruit in enumerate(fruits):
    print(f"Індекс {index}: {fruit}") 