def get_discount(price):
    if price > 1000:
        return price * 0.1
    else:
        return 0

def print_receipt(price):
    print("--- Формування чеку ---")
    
    discount = get_discount(price) 
    final_price = price - discount
    
    print(f"Сума: {price}")
    print(f"Знижка: {discount}")
    print(f"До сплати: {final_price}")

print_receipt(1500)