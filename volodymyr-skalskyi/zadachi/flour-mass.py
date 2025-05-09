m = float(input())
dough_percentage = 100 - 60
flour_percentage = 100 - 30
flour_mass = m * (dough_percentage / 100) * (flour_percentage / 100) * 1000
print(flour_mass) 