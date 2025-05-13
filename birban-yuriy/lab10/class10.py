class Car:
    def __init__(self, brand, year):
        self._brand = brand
        self._year = year

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, new_brand):
        self._brand = new_brand

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, new_year):
        if new_year >= 1886:
            self._year = new_year
        else:
            print("Рік некоректний!")

    @year.deleter
    def year(self):
        print("Рік випуску видалено.")
        del self._year

    def show_info(self):
        print(f"Brand: {self._brand}, Year: {self._year}")

my_car = Car("Toyota", 2015)

print("Інформація про авто:")
my_car.show_info()

my_car.brand = "Honda"
my_car.year = 2020

print("\nПісля оновлення:")
my_car.show_info()

del my_car.year