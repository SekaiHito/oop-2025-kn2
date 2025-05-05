# Оголошення пустого списку
numbers = []
strings = []

# Список імен
names = ["Іван", "Петро", "Jessica"]

# Отримуємо друге ім’я (індексація з 0)
second_name = names[1]

# Додаємо числа до списку
numbers.append(1)
numbers.append(2)
numbers.append(15)

# Додаємо рядки до списку
strings.append("Рядок 1")
strings.append("Рядок 2 ")

# Виводимо результати
print("Список чисел:", numbers)
print("Список рядків:", strings)
print("Друге ім’я у списку імен — %s" % second_name)
