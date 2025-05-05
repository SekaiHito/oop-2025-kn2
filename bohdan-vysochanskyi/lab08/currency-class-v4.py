# Батьківський клас
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


# Дочірній клас для конвертації в USD
class USDConverter(CurrencyConverterBase):
    def __init__(self):
        super().__init__('UAH', 'USD', 1 / 43)


# Дочірній клас для конвертації в EUR
class EURConverter(CurrencyConverterBase):
    def __init__(self):
        super().__init__('UAH', 'EUR', 1 / 39)


# Дочірній клас, який працює з іншими дочірніми обʼєктами
class CurrencyReport(CurrencyConverterBase):
    def __init__(self, converters):
        # Тут не потрібен конкретний курс, тому передаємо умовні значення
        super().__init__('Multi', 'Report', 0)
        self.converters = converters

    def generate_report(self, amount):
        print("=== Валютний звіт ===")
        for converter in self.converters:
            result = converter.convert(amount)
            print(f"{amount} {converter.original} = {result:.2f} {converter.converted} "
                  f"(курс {converter.exchange_rate:.4f})")


# Тестування всіх класів

# Створення обʼєктів дочірніх класів
usd_converter = USDConverter()
eur_converter = EURConverter()

# Перевірка наслідування
print("Перевірка isinstance:")
print(isinstance(usd_converter, CurrencyConverterBase))  # True
print(isinstance(eur_converter, CurrencyConverterBase))  # True

print("\nПеревірка issubclass:")
print(issubclass(USDConverter, CurrencyConverterBase))  # True
print(issubclass(EURConverter, CurrencyConverterBase))  # True
print(issubclass(CurrencyReport, CurrencyConverterBase))  # True

# Використання дочірнього класу, який працює з іншими
report = CurrencyReport([usd_converter, eur_converter])
report.generate_report(1000)
