def do_order(order):
        total = 0
        for item in order.items:
            total += item.price * item.quantity

        print("Total:", total)
        file = open("log.txt", "a")
        file.write(f"Order total: {total}\n")
        file.close()
    

def calculate_total(order):
    return sum(item.price * item.qty for item in order.items)

def log_total(total):
    with open("log.txt", "a") as f:
        f.write(f"Order total: {total}\n")

def process_order(order):
    total = calculate_total(order)
    print("Total:", total)
    log_total(total)


def calc(a):
    return a * 3.14

def calculate_circle_area(radius):
    return radius * 3.14