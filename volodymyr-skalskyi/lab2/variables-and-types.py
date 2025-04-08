def demonstrate_variables_and_types():
    # Числові типи
    integer = 42
    float_num = 3.14
    complex_num = 1 + 2j
    
    print("Числові типи:")
    print(f"integer: {integer}, тип: {type(integer)}")
    print(f"float_num: {float_num}, тип: {type(float_num)}")
    print(f"complex_num: {complex_num}, тип: {type(complex_num)}")
    
    # Рядковий тип
    string = "Hello, Python!"
    print(f"\nstring: {string}, тип: {type(string)}")
    
    # Булевий тип
    boolean = True
    print(f"boolean: {boolean}, тип: {type(boolean)}")
    
    # Приведення типів
    print("\nПриведення типів:")
    num_str = "123"
    num_int = int(num_str)
    num_float = float(num_str)
    
    print(f"Рядок '{num_str}' -> ціле число: {num_int}")
    print(f"Рядок '{num_str}' -> дробове число: {num_float}")
    
    # Динамічна типізація
    print("\nДинамічна типізація:")
    variable = 42
    print(f"variable = {variable}, тип: {type(variable)}")
    variable = "Тепер це рядок"
    print(f"variable = {variable}, тип: {type(variable)}")

if __name__ == "__main__":
    demonstrate_variables_and_types() 