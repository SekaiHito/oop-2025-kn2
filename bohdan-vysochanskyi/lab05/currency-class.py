class CurrencyConverter:
    def __init__(self, original, converted, exchange_rate, callback):
        self.original = original
        self.converted = converted
        self.exchange_rate = exchange_rate
        self.callback = callback

    def convert(self, amount):
        return self.callback(amount, self.exchange_rate)

    def run(self):
        print(f"Конвертер валют: {self.original} → {self.converted}. Курс: {self.exchange_rate}")
        try:
            amount = float(input(f"Введіть суму в {self.original}: "))
            result = self.convert(amount)
            print(f"{amount} {self.original} = {result:.2f} {self.converted}")
        except ValueError:
            print("Будь ласка, введіть коректне число.")

# Callback-функція для конвертації
def convert_currency(amount, rate):
    return amount * rate

# Створення об'єкта класу та запуск програми
converter = CurrencyConverter('UAH', 'USD', exchange_rate=1/43, callback=convert_currency)
converter.run()

converter2 = CurrencyConverter('UAH', 'AUD', exchange_rate=1/20, callback=convert_currency)
converter2.run()
