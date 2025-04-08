age = int(input())
has_ticket = input() == "так"
is_vip = input() == "так"

if (age >= 18 and has_ticket) or is_vip:
    print("Вхід дозволено")
else:
    print("Вхід заборонено")
