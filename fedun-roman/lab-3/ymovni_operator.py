score = int(input("Введіть оцінку (0-100): "))

if score >= 90 and score <= 100:
    print("Відмінно")
elif score >= 75 and score <= 89:
    print("Добре")
elif score >= 60 and score <= 74:
    print("Задовільно")
elif score >= 0 and score <= 59:
    print("Незадовільно")
else:
    print("Некоректна оцінка")