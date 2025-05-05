def convert_currency(amount, rate):
    return amount * rate

def main():
    print("Конвертер валют: гривня → долар США")
    try:
        uah = float(input("Введіть суму в гривнях: "))
        exchange_rate = 1/43 
        usd = convert_currency(uah, exchange_rate)
        print(f"{uah} грн = {usd:.2f} USD")
    except ValueError:
        print("Будь ласка, введіть коректне число.")
    main() #loop for console run
main()
