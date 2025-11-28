class OrderProcessor:
    def __init__(self, order_id, items, customer_type):
        self.order_id = order_id
        self.items = items
        self.customer_type = customer_type
        self.total_price = 0.0
        self.discount_amount = 0.0
        self.tax_amount = 0.0
        self.net_total = 0.0

    def process_order(self):
        print(f"--- Початок обробки замовлення #{self.order_id} ---")
        
        if not self.items:
            print("Помилка: Замовлення не містить товарів.")
            return False
        
        for item in self.items:
            if item.get('price', 0) <= 0 or item.get('quantity', 0) <= 0:
                print(f"Помилка: Некоректні дані для товару {item.get('name')}.")
                return False
        
        for item in self.items:
            self.total_price += item['price'] * item['quantity']
        
        if self.customer_type == 'VIP' and self.total_price > 1000:
            self.discount_amount = self.total_price * 0.15 
            print("Лог: Застосовано VIP-знижку 15%.")
        elif self.total_price > 500:
            self.discount_amount = self.total_price * 0.05 
            print("Лог: Застосовано стандартну знижку 5%.")
        
        final_after_discount = self.total_price - self.discount_amount

        TAX_RATE = 0.20
        self.tax_amount = final_after_discount * TAX_RATE
        self.net_total = final_after_discount + self.tax_amount
        
        print(f"\n--- Фінальний Звіт ---")
        print(f"1. Загальна вартість: ${self.total_price:.2f}")
        print(f"2. Знижка: ${self.discount_amount:.2f}")
        print(f"3. Сума до оподаткування: ${final_after_discount:.2f}")
        print(f"4. ПДВ ({TAX_RATE*100}%): ${self.tax_amount:.2f}")
        print(f"5. **До сплати**: ${self.net_total:.2f}")
        print("---------------------------------------")
        return True

order_items = [
    {"name": "Laptop", "price": 1200.0, "quantity": 1},
    {"name": "Mouse", "price": 25.0, "quantity": 2},
]
processor = OrderProcessor(order_id="A456", items=order_items, customer_type="VIP")
processor.process_order()