is_sunny = True
is_warm = False

if is_sunny and is_warm:
    print("Чудовий день для прогулянки!")
elif is_sunny and not is_warm:
    print("Сонячно, але холодно — вдягнись тепліше.")
elif not is_sunny and is_warm:
    print("Хмарно, але тепло — можна йти на вулицю.")
else:
    print("Погода не дуже. Може краще залишитись вдома.")