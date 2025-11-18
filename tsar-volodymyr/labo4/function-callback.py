# Функції округлення значень
def standard_round(value):
    return round(value, 2)  # Стандартне округлення до двох знаків

def ceil_round(value):
    import math
    return math.ceil(value * 150) / 150  # Округлення в більший бік

def floor_round(value):
    import math
    return math.floor(value * 75) / 75  # Округлення в менший бік

# Конвертація валюти
def currency_converter(amount, rate, rounding_function):
    usd_value = amount * rate
    return rounding_function(usd_value)

# Основна функція
def execute_conversion(rounding_function):
    print("Конвертер валют: гривня → долар США")
    try:
        uah_amount = float(input("Введіть суму в гривнях: "))
        exchange_rate = 1 / 37  # Змінене значення курсу
        usd_amount = currency_converter(uah_amount, exchange_rate, rounding_function)
        print(f"{uah_amount} грн = {usd_amount:.2f} USD")
    except ValueError:
        print("Будь ласка, введіть коректне число.")

execute_conversion(ceil_round)

