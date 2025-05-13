class MyClass:
    @staticmethod
    def is_even(number):
        return number % 2 == 0

n = int(input("Вкажіть число: "))
print(MyClass.is_even(n))