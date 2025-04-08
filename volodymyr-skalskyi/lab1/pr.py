def calculate_bmi(weight, height):
    return weight / (height ** 2)

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Недостатня вага"
    elif 18.5 <= bmi < 25:
        return "Нормальна вага"
    elif 25 <= bmi < 30:
        return "Надмірна вага"
    else:
        return "Ожиріння"

def main():
    print("Калькулятор індексу маси тіла (BMI)")
    print("-" * 40)
    
    try:
        weight = float(input("Введіть вагу (кг): "))
        height_input = float(input("Введіть зріст (см): "))

        height = height_input / 100
        
        if weight <= 0 or height <= 0:
            print("Помилка: Вага та зріст повинні бути більше 0")
            return
            
        bmi = calculate_bmi(weight, height)
        category = get_bmi_category(bmi)
        
        print("\nРезультати:")
        print(f"Індекс маси тіла (BMI): {bmi:.2f}")
        print(f"Категорія: {category}")
        
    except ValueError:
        print("Помилка: Будь ласка, введіть коректні числові значення")

if __name__ == "__main__":
    main() 