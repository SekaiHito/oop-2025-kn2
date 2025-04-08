def check_number_properties(number):
    """Перевірка різних властивостей числа"""
    properties = []
    
    # Перевірка на парність
    if number % 2 == 0:
        properties.append("парне")
    else:
        properties.append("непарне")
    
    # Перевірка на додатність
    if number > 0:
        properties.append("додатне")
    elif number < 0:
        properties.append("від'ємне")
    else:
        properties.append("нуль")
    
    # Перевірка на ділення на 3
    if number % 3 == 0:
        properties.append("ділиться на 3")
    
    return properties

def demonstrate_complex_conditions():
    try:
        # Отримання числа від користувача
        number = int(input("Введіть число для перевірки: "))
        
        # Отримання властивостей числа
        properties = check_number_properties(number)
        
        # Виведення результатів
        print(f"\nЧисло {number} є:")
        for property in properties:
            print(f"- {property}")
        
    except ValueError:
        print("Помилка: Будь ласка, введіть коректне ціле число")

if __name__ == "__main__":
    demonstrate_complex_conditions() 