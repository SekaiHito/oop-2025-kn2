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

# Перевірка на додатність
if number > 0:
    properties.append("додатне")
elif number < 0:
    properties.append("від'ємне")
else:
    properties.append("нуль")

# Перевірка на ділення на 3
if number % 3 == 0:
    properties.append("ділиться на 3")

# Перевірка на ділення на 5
if number % 5 == 0:
    properties.append("ділиться на 5")

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

# Додаткова перевірка складних умов
print("\nДодаткові перевірки:")

# Перевірка на ділення на 3 або 5
if number % 3 == 0 or number % 5 == 0:
    print("- Ділиться на 3 або на 5")

# Перевірка на ділення на 3 і 5
if number % 3 == 0 and number % 5 == 0:
    print("- Ділиться і на 3, і на 5")

# Перевірка на діапазон і парність
if 0 <= number <= 100 and number % 2 == 0:
    print("- Парне число в діапазоні від 0 до 100")
        