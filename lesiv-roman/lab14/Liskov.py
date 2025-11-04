from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def get_area(self) -> int:
        pass

class Rectangle(Shape):

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def get_area(self) -> int:
        return self.width * self.height

class Square(Shape):

    def __init__(self, size: int):
        self.size = size

    def get_area(self) -> int:
        return self.size * self.size


def print_shape_area(shape: Shape):
    area = shape.get_area()
    print(f"Площа {shape.__class__.__name__}: {area}")


rect = Rectangle(10, 5)
sq = Square(7)

print_shape_area(rect)
print_shape_area(sq)