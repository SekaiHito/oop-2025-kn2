class Price:
    def __init__(self, product:str = "none", value: float = 0):
        self.product = product
        self.value = value

    def __str__(self) -> str:
        return f"product: {self.product} cost: {self.value}"
    
    def __repr__(self) -> str:
        return f"product: {self.product} cost: {self.value}"

    def __add__(self,other) -> float:
        return self.value + other.value

    def __sub__(self,other) -> float:
        return self.value - other.value

if __name__ == "__main__":
    
    p1 = Price("milk",2)
    p2 = Price("apple",30)

    print(p1)
    print(p2)
    print(p1-p2)
    print(p1+p2)
