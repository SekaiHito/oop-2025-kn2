def demonstrate_loops():
    # Демонстрація циклу while
    print("Демонстрація циклу while:")
    count = 0
    while count < 5:
        print(f"Лічильник: {count}")
        count += 1
    
    # Демонстрація циклу for з range
    print("\nДемонстрація циклу for з range:")
    for i in range(5):
        print(f"Ітерація: {i}")
    
    # Демонстрація циклу for зі списком
    print("\nДемонстрація циклу for зі списком:")
    fruits = ["яблуко", "банан", "апельсин"]
    for fruit in fruits:
        print(f"Фрукт: {fruit}")
    
    # Демонстрація break
    print("\nДемонстрація break:")
    for i in range(10):
        if i == 5:
            print("Досягнуто 5, вихід з циклу")
            break
        print(f"Число: {i}")

if __name__ == "__main__":
    demonstrate_loops() 