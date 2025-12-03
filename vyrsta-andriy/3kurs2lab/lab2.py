# Старий інтерфейс (клас), який уже існує в системі.
# Він має метод print_text, але його формат нас більше не влаштовує.
class OldPrinter:
    def print_text(self, text):
        print(f"Old printer: {text}")


# Новий інтерфейс, який ми хочемо використовувати в програмі.
# Усі сучасні "принтери" повинні реалізувати метод display().
class NewPrinterInterface:
    def display(self, message):
        pass  # Це просто інтерфейс (базовий клас).


# Клас Адаптер.
# Він "обгортає" старий клас (OldPrinter) і робить його сумісним
# із новим інтерфейсом (NewPrinterInterface).
class PrinterAdapter(NewPrinterInterface):

    def __init__(self, old_printer):
        # Зберігаємо старий об'єкт, який потрібно адаптувати.
        self.old_printer = old_printer

    def display(self, message):
        # Ми реалізуємо сучасний метод display(),
        # але всередині викликаємо старий метод print_text().
        # Тобто адаптер перетворює один інтерфейс на інший.
        self.old_printer.print_text(message)


# Використання
old = OldPrinter()               # Є старий принтер (старий інтерфейс)
adapter = PrinterAdapter(old)    # Створюємо адаптер, що робить його "новим"
adapter.display("Привіт, адаптер!")  # Викликаємо новий метод, який всередині використовує старий

