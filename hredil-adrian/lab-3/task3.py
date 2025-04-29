a = int(input())
b = int(input())

if a > 0 and b > 0:
    print("Обидва додатні")
elif a > 0 or b > 0:
    print("Хоча б одне додатнє")
else:
    print("Жодне не є додатнім")

if not a > 0:
    print("a не є додатнім")
