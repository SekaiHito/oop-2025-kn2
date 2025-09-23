import copy

class Book:
    def __init__(self, year, colour, rate):
        self.year=year
        self.colour=colour
        self.rate=rate

    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return f"Book:year={self.year}, colour={self.colour}, rate={self.rate}"

not_clone=Book("1983", "White", "9.8")

clone_book=not_clone.clone()

clone_book.rate="9.9"
clone_book.year="1899"

print(not_clone)
print(clone_book)