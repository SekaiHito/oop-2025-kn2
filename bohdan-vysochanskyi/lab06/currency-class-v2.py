class CurrencyConverter:
    # Змінна класу: лічильник створених об'єктів
    instance_count = 0

    def __init__(self, original, converted, exchange_rate, callback):
        self.original = original
        self.converted = converted
        self.exchange_rate = exchange_rate
        self.callback = callback

        # Атрибут, сформований на основі інших
        self.conversion_name = f"{original} → {converted}"

        # Збільшуємо лічильник об'єктів
        CurrencyConverter.instance_count += 1

    # Метод для конвертації
    def convert(self, amount):
        return self.callback(amount, self.exchange_rate)

    # Метод, який формує опис обʼєкта
    def describe(self):
        return (f"Конвертер {self.conversion_name}. "
                f"Курс: 1 {self.original} = {self.exchange_rate:.4f} {self.converted}.")

    # Метод запуску конвертації з введенням
    def run(self):
        print(self.describe())
        try:
            amount = float(input(f"Введіть суму в {self.original}: "))
            result = self.convert(amount)
            print(f"{amount} {self.original} = {result:.2f} {self.converted}")
        except ValueError:
            print("Будь ласка, введіть коректне число.")

    # Метод класу — повертає кількість створених екземплярів
    @classmethod
    def get_instance_count(cls):
        return f"Створено обʼєктів CurrencyConverter: {cls.instance_count}"


# Callback-функція
def convert_currency(amount, rate):
    return amount * rate


# Створення об'єктів
converter1 = CurrencyConverter('UAH', 'USD', exchange_rate=1/43, callback=convert_currency)
converter2 = CurrencyConverter('UAH', 'AUD', exchange_rate=1/20, callback=convert_currency)

# Виклик методів через об'єкти
converter1.run()
converter2.run()

# Вивід опису та кількості об'єктів через клас і об'єкт
print(converter1.describe())
print(CurrencyConverter.get_instance_count())
