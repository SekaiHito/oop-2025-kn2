def demonstrate_lists():
    # Створення списків
    numbers = [1, 2, 3, 4, 5]
    mixed = [1, "hello", 3.14, True]
    
    print("Базові операції зі списками:")
    print(f"numbers: {numbers}")
    print(f"mixed: {mixed}")
    
    # Доступ до елементів
    print(f"\nПерший елемент numbers: {numbers[0]}")
    print(f"Останній елемент numbers: {numbers[-1]}")
    
    # Зміна елементів
    numbers[0] = 10
    print(f"\nПісля зміни першого елемента: {numbers}")
    
    # Додавання елементів
    numbers.append(6)
    print(f"Після додавання елемента: {numbers}")
    
    # Видалення елементів
    numbers.remove(3)
    print(f"Після видалення елемента 3: {numbers}")
    
    # Зрізи
    print(f"\nЗріз [1:3]: {numbers[1:3]}")
    print(f"Зріз [::2]: {numbers[::2]}")
    
    # Методи списків
    numbers.sort()
    print(f"\nВідсортований список: {numbers}")
    print(f"Довжина списку: {len(numbers)}")
    
    # Список списків
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(f"\nМатриця 3x3: {matrix}")
    print(f"Елемент [1][1]: {matrix[1][1]}")

if __name__ == "__main__":
    demonstrate_lists() 