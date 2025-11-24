def process_order(order):
    print("Обробка замовлення")
    total = 0
    for item in order:
        total += item["price"]
    print(f"Загальна сума: {total}")

def calculate_total(order):
    total = 0
    for item in order:
        total += item["price"]
    return total

def process_order(order):
    print("Обробка замовлення")
    total = calculate_total(order)
    print(f"Загальна сума: {total}")