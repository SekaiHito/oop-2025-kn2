# Ініціалізація змінних
my_data = {
    "string": "hello",
    "float": 10.0,
    "integer": 20
}

# Перевірка значень і типів
for key, value in my_data.items():
    if isinstance(value, str) and value == "hello":
        print(f"String: {value}")
    elif isinstance(value, float) and value == 10.0:
        print(f"Float: {value:.1f}")
    elif isinstance(value, int) and value == 20:
        print(f"Integer: {value}")
