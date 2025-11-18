# Оголошуємо 3 функції

def greet():
    print("Вітаю з моєї функції!")

def personalized_greeting(name, wish):
    print(f"Привіт, {name}, з моєї функції! Бажаю тобі {wish}.")

def add_numbers(num1, num2):
    return num1 + num2

# Викликаємо функцію привітання
greet()

# Виведе: "Привіт, Олексій, з моєї функції! Бажаю тобі чудового дня!"
personalized_greeting("Олексій", "чудового дня!")

# Після виконання цього рядка змінна result міститиме значення 3
result = add_numbers(1, 2)
print(f"Сума: {result:.1f}")

