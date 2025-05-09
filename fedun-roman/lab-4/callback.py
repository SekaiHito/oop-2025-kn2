def apply_operation(x, y, operation):
    return operation(x, y)

def multiply(a, b):
    return a * b

def subtract(a, b):
    return a - b

print(apply_operation(10, 5, multiply))
print(apply_operation(10, 5, subtract))

print(apply_operation(10, 5, lambda x, y: x + y))