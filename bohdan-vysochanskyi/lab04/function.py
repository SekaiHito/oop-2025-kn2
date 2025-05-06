# Визначаємо 3 функції

def my_function():
    print("Привіт з моєї функції!")

def my_function_with_args(username, greeting):
    print("Привіт, %s, з моєї функції! Бажаю тобі %s." % (username, greeting))

def sum_two_numbers(a, b):
    return a + b

# Виводимо просте привітання
my_function()

# Виведе: "Привіт, John Doe, з моєї функції! Бажаю тобі чудового року!"
my_function_with_args("John Doe", "чудового року!")

# Після цього рядка змінна x буде містити значення 3
x = sum_two_numbers(1, 2)
print("Сума: %f" % (x))

