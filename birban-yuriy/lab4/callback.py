def calculate(a, b, operation):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return b - a
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        if b != 0:
            return a / b
        else:
            return "Ділення на нуль!"
    else:
        return "Невідома операція"

# Приклади використання:
print(calculate(10, 5, "add"))       # 15
print(calculate(10, 5, "multiply"))  # 50
print(calculate(10, 0, "divide"))    # Ділення на нуль!
print(calculate(10, 5, "subtract"))