
def process_data(data):
    cleaned = [d.strip().lower() for d in data]
    avg = sum(len(d) for d in cleaned) / len(cleaned)
    print(f"Середня довжина: {avg}")

def clean_data(data):
    return [d.strip().lower() for d in data]

def calculate_average(data):
    return sum(len(d) for d in data) / len(data)

def process_data(data):
    cleaned = clean_data(data)
    avg = calculate_average(cleaned)
    print(f"Середня довжина: {avg}")