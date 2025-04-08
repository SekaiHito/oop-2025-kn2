def demonstrate_string_formatting():
    name = "Python"
    version = 3.9
    year = 2023
    
    # % оператор
    print("Форматування за допомогою % оператора:")
    print("Python версії %.1f випущено в %d році" % (version, year))
    
    # str.format()
    print("\nФорматування за допомогою str.format():")
    print("{} версії {} випущено в {} році".format(name, version, year))
    print("{0} версії {1} випущено в {2} році".format(name, version, year))
    print("{n} версії {v} випущено в {y} році".format(n=name, v=version, y=year))
    
    # f-strings
    print("\nФорматування за допомогою f-strings:")
    print(f"{name} версії {version} випущено в {year} році")
    
    # Форматування чисел
    pi = 3.14159
    print(f"\nФорматування чисел:")
    print(f"Pi з 2 знаками після коми: {pi:.2f}")
    print(f"Pi з 4 знаками після коми: {pi:.4f}")
    
    # Вирівнювання тексту
    text = "Python"
    print(f"\nВирівнювання тексту:")
    print(f"|{text:>10}|")  # праворуч
    print(f"|{text:<10}|")  # ліворуч
    print(f"|{text:^10}|")  # по центру
    
    # Заповнення
    print(f"\nЗаповнення:")
    print(f"{text:*>10}")  # заповнення зірочками
    print(f"{text:-<10}")  # заповнення дефісами

if __name__ == "__main__":
    demonstrate_string_formatting() 