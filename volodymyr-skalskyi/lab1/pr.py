print("Калькулятор індексу маси тіла (BMI)")
print("-" * 40)

weight = float(input("Введіть вагу (кг): "))
height_input = float(input("Введіть зріст (см): "))

height = height_input / 100

if weight <= 0 or height <= 0:
    print("Помилка: Вага та зріст повинні бути більше 0")
else:
    bmi = weight / (height ** 2)
    
    if bmi < 18.5:
        category = "Недостатня вага"
    elif 18.5 <= bmi < 25:
        category = "Нормальна вага"
    elif 25 <= bmi < 30:
        category = "Надмірна вага"
    else:
        category = "Ожиріння"
    
    print("\nРезультати:")
    print(f"Індекс маси тіла (BMI): {bmi:.2f}")
    print(f"Категорія: {category}")