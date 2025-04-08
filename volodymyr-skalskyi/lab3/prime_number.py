print("Програма для перевірки простих чисел")
print("-" * 40)

# Отримання числа від користувача
n = int(input("Введіть число для перевірки на простоту: "))

# Перевірка чи число просте
is_prime = True
if n < 2:
    is_prime = False
else:
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break

# Виведення результату перевірки
if is_prime:
    print(f"\nЧисло {n} є простим")
else:
    print(f"\nЧисло {n} не є простим")

# Демонстрація всіх простих чисел до n
if n > 1:
    print(f"\nПрості числа до {n}:")
    for i in range(2, n + 1):
        is_current_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_current_prime = False
                break
        if is_current_prime:
            print(i, end=" ")
    print()