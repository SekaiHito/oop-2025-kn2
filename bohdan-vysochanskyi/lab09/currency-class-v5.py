class CurrencyConverterBase:
    def __init__(self, original_currency, target_currency, exchange_rate):
        self.original = original_currency
        self.converted = target_currency
        self.exchange_rate = exchange_rate
        self.name = f"{original_currency} → {target_currency}"

    def convert(self, amount):
        return amount * self.exchange_rate

    def describe(self):
        return f"{self.name}: курс {self.exchange_rate:.4f}"

    # Магічний метод для друку
    def __str__(self):
        return f"[{self.name}] курс: {self.exchange_rate:.4f}"

    # Магічний метод для налагодження
    def __repr__(self):
        return f"CurrencyConverterBase('{self.original}', '{self.converted}', {self.exchange_rate})"

    # Порівняння еквівалентності
    def __eq__(self, other):
        if isinstance(other, CurrencyConverterBase):
            return self.exchange_rate == other.exchange_rate
        return False

    # Порівняння за курсом
    def __lt__(self, other):
        if isinstance(other, CurrencyConverterBase):
            return self.exchange_rate < other.exchange_rate
        return NotImplemented


# Дочірній клас для USD
class USDConverter(CurrencyConverterBase):
    def __init__(self):
        super().__init__('UAH', 'USD', 1 / 43)

    # Перевизначення методу describe
    def describe(self):
        return f"Конвертер у USD. Поточний курс: {self.exchange_rate:.4f}"


# Дочірній клас для EUR
class EURConverter(CurrencyConverterBase):
    def __init__(self):
        super().__init__('UAH', 'EUR', 1 / 39)

    def describe(self):
        return f"Конвертер у EUR. Поточний курс: {self.exchange_rate:.4f}"


# Тестування
usd = USDConverter()
eur = EURConverter()

# Поліморфний виклик методу describe()
for converter in [usd, eur]:
    print(converter.describe())

# Використання магічних методів
print(str(usd))
print(repr(eur))

print("USD == EUR?", usd == eur)
print("USD < EUR?", usd < eur)
print("USD > EUR?", usd > eur)
