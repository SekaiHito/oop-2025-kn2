import collections.abc

class Page:
    """Простий клас, що представляє одну сторінку з номером та змістом."""
    def __init__(self, number: int, content: str):
        self.number = number
        self.content = content

    def __str__(self):
        return f"[Сторінка {self.number}: {self.content}]"

# книга
class Book(collections.abc.Iterable):
    """Клас книги, який тепер містить список об'єктів Page."""
    def __init__(self, title: str):
        self.title = title
        self._pages = []

    def add_page(self, content: str):
        page_number = len(self._pages) + 1
        self._pages.append(Page(page_number, content))

    def __len__(self):
        return len(self._pages)

    def __iter__(self) -> collections.abc.Iterator:
        """Повертає стандартний ітератор (з початку до кінця)."""
        return ForwardIterator(self._pages)

    def reverse(self) -> collections.abc.Iterator:
        """Спеціальний метод, що повертає реверсивний ітератор."""
        return ReverseIterator(self._pages)
#Прямий обхід
class ForwardIterator(collections.abc.Iterator):
    def __init__(self, pages: list[Page]):
        self._pages = pages
        self._current_pos = 0

    def __next__(self) -> Page:
        if self._current_pos < len(self._pages):
            page = self._pages[self._current_pos]
            self._current_pos += 1
            return page
        else:
            raise StopIteration

#Зворотний обхід
class ReverseIterator(collections.abc.Iterator):
    def __init__(self, pages: list[Page]):
        self._pages = pages
        # Починаємо з індексу останньої сторінки
        self._current_pos = len(self._pages) - 1

    def __next__(self) -> Page:
        if self._current_pos >= 0:
            page = self._pages[self._current_pos]
            self._current_pos -= 1
            return page
        else:
            raise StopIteration
        

my_practical_book = Book("Пригоди Патернів Проєктування")
my_practical_book.add_page("Розділ 1: Вступ до Ітератора.")
my_practical_book.add_page("Розділ 2: Чому він такий корисний?")
my_practical_book.add_page("Розділ 3: Практичні приклади.")
my_practical_book.add_page("Епілог: Наступні кроки.")

#1
print(f"Читаємо книгу '{my_practical_book.title}' з початку:")
for page in my_practical_book:
    print(page)

#2
print(f" Читаємо книгу '{my_practical_book.title}' з кінця:")
for page in my_practical_book.reverse():
    print(page)