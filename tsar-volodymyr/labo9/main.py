class Vehicle:
    def move(self):
        return "Vehicle is in motion"

class Auto(Vehicle):
    def move(self):
        return "Auto is driving"

class Bike(Vehicle):
    def move(self):
        return "Bike is pedaling"

class File:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count

    def __str__(self):
        return f"File: {self.title}, {self.page_count} pages"

    def __len__(self):
        return self.page_count

    def __eq__(self, other):
        return self.page_count == other.page_count

    def __add__(self, other):
        return File(f"{self.title} & {other.title}", self.page_count + other.page_count)

vehicles = [Auto(), Bike(), Vehicle()]
for v in vehicles:
    print(v.move())

file1 = File("Analysis", 18)  # Змінена назва та кількість сторінок
file2 = File("Report", 12)  # Змінена назва та кількість сторінок

print(str(file1))
print(len(file1))
print(file1 == file2)

file3 = file1 + file2
print(file3)
