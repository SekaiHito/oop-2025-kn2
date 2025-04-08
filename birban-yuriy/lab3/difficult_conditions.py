age = int(input("Введи свій вік: "))
energy = int(input("Скільки у тебе енергії (0-100)? "))
has_internet = input("Чи є у тебе інтернет? (так/ні): ").lower() == "так"

if (age >= 12 and energy >= 50 and has_internet) or (age >= 18 and energy >= 30):
    print("Ти можеш грати!")
else:
    print("На жаль, не можеш грати зараз.")