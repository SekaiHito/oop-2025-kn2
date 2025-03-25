height = float("Введіть зріст (у метрах)")
weight = float(input("Введіть масу(у кілограмах)"))
bmi = weight / (height * height)
if bmi < 18.5:
    category = "underweight"
elif 18.5 <= bmi < 24.9:
    category = "normal weight"
else:
    category = "overweight"
print("Your body mass index is:", round(bmi, 2), ", that is", category + ".")