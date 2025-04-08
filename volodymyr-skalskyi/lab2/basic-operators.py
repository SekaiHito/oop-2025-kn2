def demonstrate_operators():
    # Арифметичні оператори
    a = 10
    b = 3
    
    print("Арифметичні оператори:")
    print(f"Додавання: {a} + {b} = {a + b}")
    print(f"Віднімання: {a} - {b} = {a - b}")
    print(f"Множення: {a} * {b} = {a * b}")
    print(f"Ділення: {a} / {b} = {a / b}")
    print(f"Цілочисельне ділення: {a} // {b} = {a // b}")
    print(f"Остача від ділення: {a} % {b} = {a % b}")
    print(f"Піднесення до степеня: {a} ** {b} = {a ** b}")
    
    # Порівняння
    print("\nОператори порівняння:")
    print(f"{a} > {b}: {a > b}")
    print(f"{a} < {b}: {a < b}")
    print(f"{a} == {b}: {a == b}")
    print(f"{a} != {b}: {a != b}")
    
    # Логічні оператори
    x = True
    y = False
    print("\nЛогічні оператори:")
    print(f"x and y: {x and y}")
    print(f"x or y: {x or y}")
    print(f"not x: {not x}")

if __name__ == "__main__":
    demonstrate_operators() 