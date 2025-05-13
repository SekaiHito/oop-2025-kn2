def apply_function(x, func):
    return func(x)

def square(n):
    return n * n

print("Квадрат числа 4:", apply_function(4, square))