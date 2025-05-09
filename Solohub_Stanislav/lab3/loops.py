n = int(input("Введіть N: "))
sum_even = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        print(f"Парне число: {i}")
        sum_even += i

print(f"Сума всіх парних чисел від 1 до {n} = {sum_even}")