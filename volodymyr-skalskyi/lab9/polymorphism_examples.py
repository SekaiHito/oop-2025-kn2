
# Базовий клас для фігур
class Shape:
    def area(self):
        """Метод, який буде перевизначений у дочірніх класах"""
        pass

    def perimeter(self):
        """Метод, який буде перевизначений у дочірніх класах"""
        pass

# Клас прямокутника
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """Перевизначення методу area для прямокутника"""
        return self.width * self.height

    def perimeter(self):
        """Перевизначення методу perimeter для прямокутника"""
        return 2 * (self.width + self.height)

# Клас кола
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Перевизначення методу area для кола"""
        return 3.14 * self.radius ** 2

    def perimeter(self):
        """Перевизначення методу perimeter для кола"""
        return 2 * 3.14 * self.radius

# Функція, яка демонструє поліморфізм
def print_shape_info(shape):
    """Функція приймає об'єкт будь-якої фігури і викликає її методи"""
    print(f"Площа: {shape.area()}")
    print(f"Периметр: {shape.perimeter()}")
    print()

# Створюємо об'єкти різних фігур
rectangle = Rectangle(5, 3)
circle = Circle(4)

# Демонструємо поліморфізм
print("Прямокутник:")
print_shape_info(rectangle)

print("Коло:")
print_shape_info(circle)
