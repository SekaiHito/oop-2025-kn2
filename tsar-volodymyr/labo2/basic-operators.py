x = object()
y = object()

# Створюємо списки за допомогою генераторів списків
x_list = [x for _ in range(10)]
y_list = [y for _ in range(10)]
big_list = x_list + y_list

# Виводимо інформацію про списки
print(f"x_list contains {len(x_list)} objects")
print(f"y_list contains {len(y_list)} objects")
print(f"big_list contains {len(big_list)} objects")

# Перевірка правильності створених списків
