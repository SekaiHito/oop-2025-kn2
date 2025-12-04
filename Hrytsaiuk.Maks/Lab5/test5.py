class DataProcessor:
    def __init__(self, data):
        self.data = data
        self.total_processed_items = 0
        self.errors = []

    def process_monthly_report(self):
        if not self._validate_data():
            return
        total_revenue, average_price = self._calculate_metrics()

        self._print_report(total_revenue, average_price)

    def _validate_data(self) -> bool:
        if not self.data or len(self.data) == 0:
            self.errors.append("Помилка: Немає даних для обробки.")
            print("Обробку зупинено через відсутність даних.")
            return False

        for item in self.data:
            if item.get('quantity', 0) <= 0:
                self.errors.append(f"Помилка: Некоректна кількість для товару {item.get('name')}")
        
        if self.errors:
            print(f"Звіт містить {len(self.errors)} помилок валідації. Обробка неможлива.")
            return False
        
        print("Дані успішно валідовано.")
        return True

    def _calculate_metrics(self) -> tuple[float, float]:
        total_revenue = 0
        self.total_processed_items = 0 
        
        for item in self.data:
            revenue = item['price'] * item['quantity']
            total_revenue += revenue
            self.total_processed_items += item['quantity']
        
        average_price = total_revenue / len(self.data) if len(self.data) > 0 else 0
        
        return total_revenue, average_price

    def _print_report(self, total_revenue: float, average_price: float):
        print("\n--- ФІНАЛЬНИЙ МІСЯЧНИЙ ЗВІТ ---")
        print(f"Всього оброблено позицій: {self.total_processed_items}")
        print(f"Загальний дохід: ${total_revenue:.2f}")
        print(f"Середня вартість позиції: ${average_price:.2f}")
        print("---------------------------------")

sample_data = [
    {"name": "A", "price": 100.0, "quantity": 5},
    {"name": "B", "price": 50.0, "quantity": 10},
    {"name": "C", "price": 200.0, "quantity": 2}
]

processor = DataProcessor(sample_data)
processor.process_monthly_report()