class Rectangle:
    def __init__(self, a:float = 1, b:float = 1):
        self.a = a
        self.b = b

    @property
    def square(self) -> float:
        return self.a * self.b

    @property
    def perimeter(self) -> float:
        return self.a * 2 + self.b * 2
    
    @square.setter
    def square(self, value):
        print("setter of square called")
        if self.a != 0:
            self.b = value / self.a
        else:
            raise ValueError("Cannot set square when side 'a' is 0")
    
    @square.deleter
    def square(self):
        print("deleter of square called")
        self.a = 0
        self.b = 0

if __name__ == "__main__":
    r = Rectangle(4,5)

    print(r.square)
    print(r.perimeter)
