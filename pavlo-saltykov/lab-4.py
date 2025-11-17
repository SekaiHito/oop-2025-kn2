class Order:
    def calculate_total(self):
            print("Calculating total")

class OrderSaving:
    def save(self, order):
        print("Saving order to database")

class EmailSend:
    def send(self, order):
        print("Sending email about order")

order = Order()
repo = OrderSaving()
email = EmailSend()

order.calculate_total()
repo.save(order)
email.send(order)



class PaymentProcessor:
        def pay(self, payment_type):
            if payment_type == "card":
                print("Paying by card")
            elif payment_type == "applepay":
                print("Paying by ApplePay")

class PaymentMethod:
    def pay(self):
            pass

class CardPayment(PaymentMethod):
    def pay(self):
        print("Paying by card")

class ApplePayPayment(PaymentMethod):
    def pay(self):
        print("Paying by ApplePay")

class PaymentProcessor:
    def process(self, method: PaymentMethod):
        method.pay()
    
# Тепер щоб додати новий метод робимо віддільний клас не змінюючи основний код
class GooglePayPayment(PaymentMethod):
    def pay(self):
        print("Paying by GooglePay")

processor = PaymentProcessor()

processor.process(CardPayment())
processor.process(ApplePayPayment())
processor.process(GooglePayPayment())
