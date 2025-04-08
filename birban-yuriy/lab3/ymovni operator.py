age = int(input("Скільки тобі років? "))

if age < 18:
    print("Ти ще неповнолітній.")
elif age < 60:
    print("Ти дорослий.")
else:
    print("Ти пенсіонер.")