class Book:
    total_pages = 200
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
        return self.year_published < 1970

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
        return "Художня література"


books = [
    Book("1984", "Джордж Орвелл", 1949, "Антиутопія", "Секкер і Варбург", "Англійська"),
    Book.from_string("О дивний новий світ-Олдос Гакслі-1932-Антиутопія-Чатто і Віндус-Англійська"),
    Book("Гаррі Поттер і філософський камінь", "Джоан Ролінґ", 1997, "Фентезі", "Блумсбері", "Англійська"),
    Book("Володар перснів", "Джон Роналд Руел Толкін", 1954, "Фентезі", "Ален і Анвін", "Англійська"),
    Book.from_string("Убити пересмішника-Гарпер Лі-1960-Драма-Дж. Б. Ліппінкотт і Ко.-Англійська"),
    Book.from_string("Великий Гетсбі-Френсіс Скотт Фіцджеральд-1925-Трагікомедія-Чарльз Скрибнерз Санс-Англійська")
]

Book.change_pages(350)

for book in books:
    print(book.display_info())

print("Усього створено книг:", Book.get_total_books_created())
print("Тип книги:", Book.get_book_type())

book3 = books[2] 
book3.change_language("Українська")
print("Оновлена мова книги Гаррі Поттер:", book3.language)

