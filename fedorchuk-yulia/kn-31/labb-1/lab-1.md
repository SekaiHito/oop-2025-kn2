## Міністерство освіти і науки України

## Львівський національний університет ветеринарії і біотехнологій імені С.З.Ґжицького

# Звіт

про виконання лаборатоної роботи №1 з дисципліни Об'єктно-орієнтоване програмування на тему **Вивчення патернів**

Виконала: студентка групи КН-31 Федорчук Юлія

Прийняв: Заплатинський Н. Б.

## Львів 2025

```py
import copy

class Book:
    def __init__(self, year, colour, rate):
        self.year=year
        self.colour=colour
        self.rate=rate

    def clone(self):
        return copy.deepcopy(self)

    def __str__(clone):
        return f"Book(year={self.year}, colour={self.colour}, rate={self.rate})"

not_clone=Book("1983", "White", "9.8")

clone_book=not_clone.clone()

clone_book.rate="9.9"
clone_book.year="1899"

print(not_clone)
print(clone_book)

```
