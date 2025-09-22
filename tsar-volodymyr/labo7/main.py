class Book:
    total_pages = 300  # Змінена кількість сторінок
    total_books_created = 0

    def __init__(self, title, author, year_published, genre, publisher, language):
        self.title = title
        self.author = author
        self.year_published = year_published
        self.genre = genre
        self.publisher = publisher
        self.language = language
        Book.total_books_created += 1

    def display_info(self):
        return (f"Книга: «{self.title}», автор: {self.author}, жанр: {self.genre}, "
                f"рік видання: {self.year_published}, видавництво: {self.publisher}, "
                f"мова: {self.language}, сторінок: {self.total_pages}")

    def is_classic(self):
        return self.year_published < 1965  # Змінений рік для класики

    def change_language(self, new_language):
        self.language = new_language

    @classmethod
    def change_pages(cls, new_pages):
        cls.total_pages = new_pages

    @classmethod
    def from_string(cls, book_info):
        title, author, year_published, genre, publisher, language = book_info.split('-')
        return cls(title, author, int(year_published), genre, publisher, language)

    @classmethod
    def get_total_books_created(cls):
        return cls.total_books_created

    @staticmethod
    def get_book_type():
        return "Наукова фантастика"  # Змінений тип книги

books = [
    Book("Дюна", "Френк Герберт", 1965, "Фантастика", "Chilton Books", "Англійська"),
    Book.from_string("Фундація-Айзек Азімов-1951-Фантастика-Gnome Press-Англійська"),
    Book("Снігова катастрофа", "Ніл Стівенсон", 1992, "Кіберпанк", "Bantam Books", "Англійська"),
    Book("Часова машина", "Герберт Веллс", 1895, "Фантастика", "Heinemann", "Англійська"),
    Book.from_string("Після Армагеддону-Роберт Гайнлайн-1949-Фантастика-Scribner-Англійська"),
    Book.from_string("Сирітський цикл-Орсон Скотт Кард-1985-Фантастика-Tor Books-Англійська")
]

Book.change_pages(500)  # Змінена кількість сторінок

for book in books:
    print(book.display_info())

print("Усього створено книг:", Book.get_total_books_created())
print("Тип книги:", Book.get_book_type())

book3 = books[2] 
book3.change_language("Українська")
print("Оновлена мова книги Снігова катастрофа:", book3.language)
