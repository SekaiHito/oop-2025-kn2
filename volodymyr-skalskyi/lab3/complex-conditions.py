print("Програма для перевірки властивостей числа")
print("-" * 40)

# Отримання числа від користувача
number = int(input("Введіть число для перевірки: "))

# Перевірка різних властивостей числа
properties = []

# Перевірка на парність
if number % 2 == 0:
    properties.append("парне")
else:
    properties.append("непарне")

# Перевірка на діапазон
if 0 <= number <= 100:
    properties.append("в діапазоні від 0 до 100")
elif number > 100:
    properties.append("більше 100")
else:
    properties.append("менше 0")

# Виведення результатів
print(f"\nЧисло {number} є:")
for property in properties:
    print(f"- {property}")

        