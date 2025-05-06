# Приклад: Використання and, or, not
age = int(input("Введіть ваш вік: "))
has_permission = input("Чи є дозвіл батьків? (так/ні): ").lower() == "так"

# Використання and
if age >= 18 and has_permission:
    print("Доступ дозволено")
else:
    print("Доступ заборонено")

# Використання or
if age < 13 or age > 65:
    print("Ви в категорії знижок")
else:
    print("Знижка не застосовується")

# Використання not
is_raining = False
if not is_raining:
    print("Можна гуляти!")
else:
    print("Візьміть парасольку.")