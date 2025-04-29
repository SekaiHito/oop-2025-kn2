class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def calculate_area(self):
        return self.width * self.height
    
    def calculate_perimeter(self):
        return 2 * (self.width + self.height)
    
    def is_square(self):
        return self.width == self.height
    
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

# Creating two rectangle objects
rectangle1 = Rectangle(5, 10)
rectangle2 = Rectangle(7, 7)

# Demonstrating object properties and methods
print("Rectangle 1:")
print(rectangle1)
print(f"Area: {rectangle1.calculate_area()}")
print(f"Perimeter: {rectangle1.calculate_perimeter()}")
print(f"Is square: {rectangle1.is_square()}\n")

print("Rectangle 2:")
print(rectangle2)
print(f"Area: {rectangle2.calculate_area()}")
print(f"Perimeter: {rectangle2.calculate_perimeter()}")
print(f"Is square: {rectangle2.is_square()}") 