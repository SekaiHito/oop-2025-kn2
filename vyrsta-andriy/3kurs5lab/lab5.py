class Order:
    def __init__(self, items):
        self.items = items  # список (назва, кількість, ціна)

    def print_invoice(self):
        # Метод занадто великий: і підраховує, і виводить
        total = 0
        print("=== РАХУНОК ===")
        for name, qty, price in self.items:
            subtotal = qty * price
            print(f"{name}: {qty} x {price} = {subtotal}")
            total += subtotal
        print("----------------")
        print(f"Разом: {total} грн")


# Демонстрація роботи до рефакторингу
order1 = Order([
    ("Хліб", 2, 25),
    ("Молоко", 1, 35),
    ("Сир", 1, 80)
])
order1.print_invoice()


# -------------------------------------------------------
# ✅ Після рефакторингу (SRP + короткі методи)
# -------------------------------------------------------

class OrderRefactored:
    def __init__(self, items):
        self.items = items

    def calculate_total(self):
        """Рахує суму окремо."""
        return sum(qty * price for _, qty, price in self.items)

    def generate_invoice_text(self):
        """Формує текст рахунку (без виводу)."""
        lines = ["=== РАХУНОК ==="]
        for name, qty, price in self.items:
            subtotal = qty * price
            lines.append(f"{name}: {qty} x {price} = {subtotal}")
        lines.append("----------------")
        lines.append(f"Разом: {self.calculate_total()} грн")
        return "\n".join(lines)

    def print_invoice(self):
        """Виводить рахунок (окремий метод)."""
        print(self.generate_invoice_text())


# Демонстрація після рефакторингу
print("\nПісля рефакторингу:\n")
order2 = OrderRefactored([
    ("Хліб", 2, 25),
    ("Молоко", 1, 35),
    ("Сир", 1, 80)
])
order2.print_invoice()
