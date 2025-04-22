class Shape:
    def __init__(self, name):
        self.name = name
    
    def get_name(self):
        return self.name
    
    def area(self):
        raise NotImplementedError("Subclasses must implement area()")
    
    def perimeter(self):
        raise NotImplementedError("Subclasses must implement perimeter()")
    
    def __str__(self):
        return f"{self.name}"

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def __str__(self):
        return f"{super().__str__()}(width={self.width}, height={self.height})"

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.name = "Square"
    
    def __str__(self):
        return f"{self.name}(side={self.width})"

class ColorMixin:
    def __init__(self, color):
        self.color = color
    
    def get_color(self):
        return self.color

class ColoredShape(Shape, ColorMixin):
    def __init__(self, name, color):
        Shape.__init__(self, name)
        ColorMixin.__init__(self, color)
    
    def __str__(self):
        return f"{self.name}(color={self.color})"


# Створюємо екземпляри
rectangle = Rectangle(5, 10)
square = Square(7)
colored_shape = ColoredShape("ColoredShape", "red")

# Демонструємо наслідування
print("\n=== Базове наслідування ===")
print(f"Площа прямокутника: {rectangle.area()}")
print(f"Периметр прямокутника: {rectangle.perimeter()}")
print(f"Площа квадрата: {square.area()}")
print(f"Периметр квадрата: {square.perimeter()}")

# Демонструємо множинне наслідування
print("\n=== Множинне наслідування ===")
print(f"Назва кольорової фігури: {colored_shape.get_name()}")
print(f"Колір кольорової фігури: {colored_shape.get_color()}")

# Демонструємо isinstance та issubclass
print("\n=== Перевірка типів ===")
print(f"Чи є прямокутник фігурою? {isinstance(rectangle, Shape)}")
print(f"Чи є квадрат прямокутником? {isinstance(square, Rectangle)}")
print(f"Чи є Square підкласом Shape? {issubclass(Square, Shape)}")

# Демонструємо MRO
print("\n=== Порядок вирішення методів ===")
print("ColoredShape MRO:", [cls.__name__ for cls in ColoredShape.__mro__])

# Демонструємо рядкове представлення
print("\n=== Рядкове представлення ===")
print(rectangle)
print(square)
print(colored_shape) 