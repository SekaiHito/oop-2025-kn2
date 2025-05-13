class Transport:
    def move(self):
        return "Transport is moving"

class Car(Transport):
    def move(self):
        return "Car is driving"

class Bicycle(Transport):
    def move(self):
        return "Bicycle is pedaling"

class Document:
    def __init__(self, name, pages):
        self.name = name
        self.pages = pages

    def __str__(self):
        return f"Document: {self.name}, {self.pages} pages"

    def __len__(self):
        return self.pages

    def __eq__(self, other):
        return self.pages == other.pages

    def __add__(self, other):
        return Document(f"{self.name} & {other.name}", self.pages + other.pages)

vehicles = [Car(), Bicycle(), Transport()]
for v in vehicles:
    print(v.move())

doc1 = Document("Report", 15)
doc2 = Document("Summary", 10)

print(str(doc1))
print(len(doc1))
print(doc1 == doc2)

doc3 = doc1 + doc2
print(doc3)

