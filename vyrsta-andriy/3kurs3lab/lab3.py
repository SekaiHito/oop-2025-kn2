# Базовий інтерфейс стратегії оплати.
# Усі конкретні стратегії повинні реалізувати метод pay().
class PaymentStrategy:
    def pay(self, amount):
        pass  # Интерфейс — тут немає логіки, лише визначення методу.


# Конкретна стратегія оплати карткою.
class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        # Реалізація способу оплати карткою
        print(f"Оплата карткою: {amount} грн")


# Конкретна стратегія оплати через PayPal.
class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        # Реалізація способу оплати через PayPal
        print(f"Оплата PayPal: {amount} грн")


# Клієнтський клас — замовлення.
# Він НЕ залежить від конкретного способу оплати.
# Лише отримує та викликає вибрану стратегію.
class Order:
    def __init__(self, strategy: PaymentStrategy):
        # Зберігаємо обрану стратегію оплати
        self.strategy = strategy

    def checkout(self, amount):
        # Делегуємо оплату внутрішній стратегії
        self.strategy.pay(amount)


# --- Використання ---

# Створюємо замовлення з оплатою карткою
order = Order(CreditCardPayment())
order.checkout(100)  # Викликається стратегія CreditCardPayment

# Змінюємо стратегію на PayPal "на льоту"
order.strategy = PayPalPayment()
order.checkout(200)  # Викликається вже стратегія PayPalPayment

