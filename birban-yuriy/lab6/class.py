class Book:

    total_books = 0

    def __init__(self, title, author, year):

        self.title = title
        self.author = author
        self.year = year

        self.description = f"{self.title} by {self.author} ({self.year})"

        Book.total_books += 1

    def get_info(self):
        return f"Книга: {self.title}, Автор: {self.author}, Рік: {self.year}"

    @classmethod
    def get_total_books(cls):
        return f"Всього створено книг: {cls.total_books}"

book1 = Book("Місто", "Валер'ян Підмогильний", 1927)
book2 = Book("Кобзар", "Тарас Шевченко", 1840)

print(book1.get_info())
print(book2.get_info())

print("\nАвтоматичний опис:")
print(book1.description)
print(book2.description)

print("\nЛічильник:")
print(book1.get_total_books())
print(Book.get_total_books())
