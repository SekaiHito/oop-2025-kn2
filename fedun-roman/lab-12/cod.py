class Product:
    def get_price(self):
        return 100

class DiscountDecorator:
    def __init__(self, product):
        self.product = product

    def get_price(self):
        return self.product.get_price() * 0.9
item = Product()
discounted = DiscountDecorator(item)
print(discounted.get_price())