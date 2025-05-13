# МІНІСТЕРСТВО ОСВІТИ ТА НАУКИ

## Львівський національний університет ветеринарії і біотехнологій імені С.З.Ґжицького

# Звіт

**про виконання лаборатоної роботи №6**

**з дисципліни "Об'єктно-орієнтоване програмування"**

**на тему** 

**Створення та використання класів.**

Виконав: студент групи КН-21 Греділь Адріан

Перевірив: доц. А.Татомир

### Львів 2025

Мета роботи – ознайомитися з різними типами змінних в об’єктно-орієнтованому програмуванні

## Хід роботи

Я набув навичок у створенні класів. Створив клас, який приймає кілька аргументів. На основі цих аргументів у конструкторі класу я створив набір атрибутів об'єкта, один з яких розраховується на основі інших.

```py

class Book:
    def __init__(self, title, author, year, pages):
        self.title = title
        self.author = author
        self.year = year
        self.pages = pages
        self.age = 2025 - self.year

    def display_info(self):
        print(f"Назва: {self.title}")
        print(f"Автор: {self.author}")
        print(f"Рік випуску: {self.year}")
        print(f"Кількість сторінок: {self.pages}")
        print(f"Вік: {self.age} років")

my_book = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925, 218)
my_book.display_info()


```
2. Я реалізував метод, який генерує опис об'єкта на основі його властивостей. Цей метод створює текст, що містить інформацію про об'єкт, використовуючи його атрибути.

```py
class Book:
    def __init__(self, title, author, year, pages):
        self.title = title
        self.author = author
        self.year = year
        self.pages = pages
        self.age = 2025 - self.year

    def generate_description(self):
        return f"Це книга '{self.title}' авторства {self.author}, видана в {self.year} році. Кількість сторінок: {self.pages}. Вік: {self.age} років."

my_book = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925, 218)
description = my_book.generate_description()
print(description)


```
3. Я навчився створювати об'єкти на основі класу. Створив кілька об'єктів і викликав реалізований метод, використовуючи як об'єкти, так і сам клас. Це дозволило краще зрозуміти, як працювати з інстанціями класу та їх методами.

```py
class Book:
    def __init__(self, title, author, year, pages):
        self.title = title
        self.author = author
        self.year = year
        self.pages = pages
        self.age = 2025 - self.year

    def generate_description(self):
        return f"Це книга '{self.title}' авторства {self.author}, видана в {self.year} році. Кількість сторінок: {self.pages}. Вік: {self.age} років."


book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925, 218)
book2 = Book("1984", "George Orwell", 1949, 328)
book3 = Book("To Kill a Mockingbird", "Harper Lee", 1960, 281)


print(book1.generate_description())
print(book2.generate_description())
print(book3.generate_description())


```
4. Я познайомився з поняттям змінної класу. Реалізував змінну класу, яка зберігає спільне значення для всіх об'єктів класу, та метод, який використовує цю змінну для виконання певних операцій, наприклад, підрахунку кількості створених об'єктів.

```py
class Book:
    total_books = 0

    def __init__(self, title, author, year, pages):
        self.title = title
        self.author = author
        self.year = year
        self.pages = pages
        self.age = 2025 - self.year
        Book.total_books += 1

    def generate_description(self):
        return f"Це книга '{self.title}' авторства {self.author}, видана в {self.year} році. Кількість сторінок: {self.pages}. Вік: {self.age} років."

    @classmethod
    def get_total_books(cls):
        return f"Кількість створених книг: {cls.total_books}"

book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925, 218)
book2 = Book("1984", "George Orwell", 1949, 328)

print(book1.generate_description())
print(book2.generate_description())

print(Book.get_total_books())


```
5. Я реалізував лічильник створених об'єктів за допомогою класу. Для цього використав змінну класу, яка автоматично збільшується кожного разу, коли створюється новий об'єкт. Це дозволило відстежувати кількість об'єктів, створених на основі класу.

```py
class Book:
    counter = 0

    def __init__(self, title, author, year, pages):
        self.title = title
        self.author = author
        self.year = year
        self.pages = pages
        self.age = 2025 - self.year
        Book.counter += 1

    def generate_description(self):
        return f"Це книга '{self.title}' авторства {self.author}, видана в {self.year} році. Кількість сторінок: {self.pages}. Вік: {self.age} років."

    @classmethod
    def get_object_count(cls):
        return f"Кількість створених книг: {cls.counter}"

book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925, 218)
book2 = Book("1984", "George Orwell", 1949, 328)
book3 = Book("To Kill a Mockingbird", "Harper Lee", 1960, 281)

print(book1.generate_description())
print(book2.generate_description())
print(book3.generate_description())

print(Book.get_object_count())


```
## Висновок:

Під час роботи я навчився ствроювати класи та об'єкти в Python, а також працювати з їхніми аттрибутами та методами. Створив методи для генерування опису об'єкта на основі його властивостей і використовував змінну класу для підрахунку кількості створених об'єктів. Це дозволило краще зрозуміти, як працюють класи та об'єкти, а також як управлляти спільними властивостями для всіх об'єктів класу. Зокрема, реалізація лічильника створених об'єктів допомогла освоїти принципи роботи з класами та їхніми методами.