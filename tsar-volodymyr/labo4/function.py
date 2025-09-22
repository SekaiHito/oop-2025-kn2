# Оголошуємо 3 функції

def say_hello():
    print("Вітаю з нової функції!")

def custom_greeting(person, message):
    print(f"Привіт, {person}, з моєї функції! Бажаю тобі {message}.")

def sum_values(value1, value2):
    return value1 + value2

# Викликаємо функцію привітання
say_hello()

# Виведе: "Привіт, Марія, з моєї функції! Бажаю тобі прекрасного дня!"
custom_greeting("Марія", "прекрасного дня!")

# Після виконання цього рядка змінна total міститиме значення 3
total = sum_values(1, 2)
print(f"Сума: {total:.1f}")



