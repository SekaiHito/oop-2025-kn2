def demonstrate_conditional_operators():
    # Проста умова if
    number = int(input("Введіть число: "))
    
    if number > 0:
        print("Число додатне")
    elif number < 0:
        print("Число від'ємне")
    else:
        print("Число дорівнює нулю")
    
    # Демонстрація булевої логіки
    age = int(input("\nВведіть ваш вік: "))
    
    if age >= 18:
        print("Ви повнолітній")
    else:
        print("Ви неповнолітній")
    
    # Демонстрація оператора in
    fruits = ["яблуко", "банан", "апельсин"]
    fruit = input("\nВведіть назву фрукта: ").lower()
    if fruit in fruits:
        print(f"{fruit} є в списку фруктів")
    else:
        print(f"{fruit} відсутній в списку фруктів")

if __name__ == "__main__":
    demonstrate_conditional_operators() 