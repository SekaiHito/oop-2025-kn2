print("Введіть числа (0 для завершення):")
total = 0
while True:
    num = int(input())
    if num == 0:
        break
    total += num
print(f"Сума введених чисел: {total}")

n = int(input("Введіть число для виведення парних чисел: "))
print("Парні числа від 1 до", n, ":")
for i in range(1, n + 1):
    if i % 2 == 0:
        print(i, end=" ")
print()  # Новий рядок