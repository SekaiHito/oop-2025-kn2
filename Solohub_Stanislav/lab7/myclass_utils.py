class MyClass:
    @staticmethod
    def is_even(number):
        """Перевіряє, чи є число парним"""
        return number % 2 == 0

print(MyClass.is_even(10))
print(MyClass.is_even(7))