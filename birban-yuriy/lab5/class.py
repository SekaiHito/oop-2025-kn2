class Car:

    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def show_info(self):
        print(f"Brand: {self.brand}, Year: {self.year}")

    def update_year(self, new_year):
        self.year = new_year

my_car = Car("Toyota", 2015)

print("Інформація про авто:")
my_car.show_info()

my_car.brand = "Honda"

my_car.update_year(2020)

print("\nПісля оновлення:")
my_car.show_info()
