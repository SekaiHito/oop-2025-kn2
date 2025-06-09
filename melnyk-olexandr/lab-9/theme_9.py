class Array:
    def __init__(self,arr:list = []) -> None:
        self.arr = arr
        self.n = len(self.arr)

    def __str__(self) -> str:
        return str(self.arr)

    def __repr__(self) -> str:
        return str(self.arr)

    def __add__(self,other) -> list:
        if len(self.arr) != len(other.arr):
            raise ValueError("length of arrays must be equal")
        else:
            return [self.arr[i] + other.arr[i] for i in range(self.n)]
        
    def __sub__(self,other) -> list:
        if len(self.arr) != len(other.arr):
            raise ValueError("length of arrays must be equal")
        else:
            return [self.arr[i] - other.arr[i] for i in range(self.n)]

if __name__ == "__main__":
    a1 = [1,2,3]
    a2 = [4,5,6]
    a3 = [7,8,9]

    a1 = Array(a1)
    a2 = Array(a2)
    a3 = Array(a3)
    
    print(a1 + a2)
    print(a1 - a2)
