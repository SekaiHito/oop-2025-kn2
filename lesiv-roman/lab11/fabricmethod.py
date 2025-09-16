from abc import ABC, abstractmethod

class Laptop(ABC):
    @abstractmethod
    def get_info(self):
        pass

class LenovoLaptop(Laptop):
    def get_info(self):
        return "Ноутбук Lenovo"

class HPLaptop(Laptop):
    def get_info(self):
        return "Ноутбук HP"

class AsusLaptop(Laptop):
    def get_info(self):
        return "Ноутбук Asus"

class LaptopStore(ABC):
    @abstractmethod
    def create_laptop(self) -> Laptop:
        pass

    def order_laptop(self):
        laptop = self.create_laptop()
        return f"Ви замовили: {laptop.get_info()}"

class LenovoStore(LaptopStore):
    def create_laptop(self) -> Laptop:
        return LenovoLaptop()

class HPStore(LaptopStore):
    def create_laptop(self) -> Laptop:
        return HPLaptop()

class AsusStore(LaptopStore):
    def create_laptop(self) -> Laptop:
        return AsusLaptop()

store = LenovoStore()
print(store.order_laptop())  

store = HPStore()
print(store.order_laptop())  

store = AsusStore()
print(store.order_laptop())  
