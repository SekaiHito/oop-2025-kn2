"""
Приклад перевантаження методів
"""

class Calculator:
    def add(self, a, b=None, c=None):
        """Приклад перевантаження методу add"""
        if b is None and c is None:
            return a
        elif c is None:
            return a + b
        else:
            return a + b + c

print("Перевантаження методів:")
calc = Calculator()
print(calc.add(5))           # 5
print(calc.add(5, 3))        # 8
print(calc.add(5, 3, 2))     # 10
