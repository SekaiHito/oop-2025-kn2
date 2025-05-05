def round_standard(value):
    #Округлення до двох знаків після коми (стандартне)
    return round(value, 2)

def round_up(value):
    #Округлення в більший бік (ceil до 2 знаків)
    import math
    return math.ceil(value * 100) / 100

def round_down(value):
    #Округлення в менший бік (floor до 2 знаків)
    import math
    return math.floor(value * 100) / 100

def convert_currency(amount, rate, round_rule):
    usd = amount * rate
    return round_rule(usd)

def main(round_rule):
    print("Конвертер валют: гривня → долар США")
    try:
        uah = float(input("Введіть суму в гривнях: "))
        exchange_rate = 1/43 
        usd = convert_currency(uah, exchange_rate,round_rule)
        print(f"{uah} грн = {usd:.2f} USD")
    except ValueError:
        print("Будь ласка, введіть коректне число.")

main(round_up)
