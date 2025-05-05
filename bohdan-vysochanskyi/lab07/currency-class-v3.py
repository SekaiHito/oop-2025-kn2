class CurrencyConverter:
    instance_count = 0  # змінна класу

    def __init__(self, original, converted, exchange_rate, callback):
        self.original = original
        self.converted = converted
        self.exchange_rate = exchange_rate
        self.callback = callback
        self.conversion_name = f"{original} → {converted}"
        CurrencyConverter.instance_count += 1

    def convert(self, amount):
        return self.callback(amount, self.exchange_rate)

    def describe(self):
        return f"Конвертер {self.conversion_name}. Курс: 1 {self.original} = {self.exchange_rate:.4f} {self.converted}."

    def run(self):
        print(self.describe())
        try:
            amount = float(input(f"Введіть суму в {self.original}: "))
            if not self.is_valid_rate(self.exchange_rate):
                print("Неприпустимий курс конвертації.")
                return
            result = self.convert(amount)
            print(f"{amount} {self.original} = {result:.2f} {self.converted}")
        except ValueError:
            print("Будь ласка, введіть коректне число.")

    @classmethod
    def get_instance_count(cls):
        return f"Створено обʼєктів CurrencyConverter: {cls.instance_count}"

    @classmethod
    def from_string(cls, data_str, callback):
        # Альтернативний конструктор: "UAH,USD,0.023"
        parts = data_str.split(',')
        original = parts[0].strip()
        converted = parts[1].strip()
        exchange_rate = float(parts[2])
        return cls(original, converted, exchange_rate, callback)

    @staticmethod
    def is_valid_rate(rate):
        return isinstance(rate, (int, float)) and rate > 0


def convert_currency(amount, rate):
    return amount * rate

# Використання основного конструктора
converter1 = CurrencyConverter('UAH', 'USD', 1/43, convert_currency)
converter2 = CurrencyConverter('UAH', 'AUD', 1/20, convert_currency)

# Альтернативний конструктор
converter3 = CurrencyConverter.from_string("UAH,EUR,0.025", convert_currency)

# Виклики
converter1.run()
converter2.run()
converter3.run()

# Метод класу
print(CurrencyConverter.get_instance_count())

# Статичний метод
print("Курс 0.0 допустимий?", CurrencyConverter.is_valid_rate(0.0))
print("Курс 1.0 допустимий?", converter1.is_valid_rate(1.0))
