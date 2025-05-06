class CurrencyConverter:
    def __init__(self, original, converted, exchange_rate):
        self.original = original
        self.converted = converted
        self._rate = exchange_rate  # захищений атрибут

    @property
    def rate(self):
        return self._rate

    @rate.setter
    def rate(self, value):
        if value <= 0:
            raise ValueError("Курс повинен бути додатним числом.")
        self._rate = value

    @rate.deleter
    def rate(self):
        print(f"Курс для {self.original} → {self.converted} було видалено.")
        self._rate = None

    def convert(self, amount):
        if self._rate is None:
            raise ValueError("Курс не встановлено.")
        return amount * self._rate

    def describe(self):
        return f"Конвертер {self.original} → {self.converted}, курс: {self._rate:.4f}"


# Тестування
converter = CurrencyConverter("UAH", "USD", 1/43)

# Вивід курсу через property (getter)
print("Поточний курс:", converter.rate)

# Зміна курсу через setter
converter.rate = 1/40
print("Оновлений курс:", converter.rate)

# Видалення курсу через deleter
del converter.rate

# Спроба використання після видалення
try:
    print(converter.convert(1000))
except ValueError as e:
    print("Помилка:", e)
