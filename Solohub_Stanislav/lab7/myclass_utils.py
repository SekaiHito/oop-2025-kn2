class MyClass:
    @staticmethod
    def is_even(number):
        return number % 2 == 0

print(MyClass.is_even(10))
print(MyClass.is_even(7))