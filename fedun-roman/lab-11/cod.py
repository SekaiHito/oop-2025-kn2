class Product:
    def get_info(self):
        pass

class Book(Product):
    def get_info(self):
        return "Це книга"

class Laptop(Product):
    def get_info(self):
        return "Це ноутбук"

class ProductFactory:
    def create(self, type):
        if type == "book":
            return Book()
        elif type == "laptop":
            return Laptop()
factory = ProductFactory()
item = factory.create("book")
print(item.get_info())