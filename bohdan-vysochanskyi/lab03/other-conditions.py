number = 25
second_number = 10
first_array = [2, 1, 4]
second_array = [1, 2]

if number > 15:
    print("Число більше 15")

if first_array:
    print("Список заповенено")
else :
    print("Список пустий")

if len(second_array) == 2:
    print("У другому списку два елементи")

if len(first_array) + len(second_array) == 5:
    print("У двох списках 5 елементів")

if first_array and first_array[0] == 1:
    print("Перший елемент списку один рівний 1")

if second_number == 10:
    print("Друге число рівне 10")

if not second_number:
    print("Друге число хибне або 0") 
