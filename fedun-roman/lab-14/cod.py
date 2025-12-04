# class OrderSystemBad:
#     def __init__(self, customer_name, items):
#         self.customer_name = customer_name
#         self.items = items

#     def print_order(self):
#         print(f"****** ВИТРАТНА НАКЛАДНА (BAD) ******")
#         print(f"Клієнт: {self.customer_name}")
#         print("-" * 30)

#         total_amount = 0
#         for item in self.items:
#             item_price = item.get('price', 0)
#             item_qty = item.get('qty', 0)
#             total_amount += item_price * item_qty

#         print(f"Загальна сума до сплати: {total_amount} грн")
#         print("***************************************")
#         print()


class OrderSystemGood:
    def __init__(self, customer_name, items):
        self.customer_name = customer_name
        self.items = items

    def print_order(self):
        self._print_header()
        total_amount = self._calculate_total()
        self._print_details(total_amount)

    def _print_header(self):
        print(f"****** ВИТРАТНА НАКЛАДНА (GOOD) ******")
        print(f"Клієнт: {self.customer_name}")
        print("-" * 30)

    def _calculate_total(self) -> float:
        total = 0
        for item in self.items:
            total += item.get('price', 0) * item.get('qty', 0)
        return total

    def _print_details(self, total: float):
        print(f"Загальна сума до сплати: {total} грн")
        print("****************************************")
        print()