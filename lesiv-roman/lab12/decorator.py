
class Pizza:
    def cost(self):
        return 10
    def description(self):
        return "Plain pizza"

class PizzaDecorator(Pizza):
    def __init__(self, pizza):
        self._pizza = pizza


class Mozzarella(PizzaDecorator):
    def cost(self):
        return self._pizza.cost() + 3
    def description(self):
        return self._pizza.description() + " + моцарелла"

class Cheddar(PizzaDecorator):
    def cost(self):
        return self._pizza.cost() + 3
    def description(self):
        return self._pizza.description() + " + чеддер"

class Parmesan(PizzaDecorator):
    def cost(self):
        return self._pizza.cost() + 3.5
    def description(self):
        return self._pizza.description() + " + пармезан"

class Ham(PizzaDecorator):
    def cost(self):
        return self._pizza.cost() + 4
    def description(self):
        return self._pizza.description() + " + шинка"

class Pepperoni(PizzaDecorator):
    def cost(self):
        return self._pizza.cost() + 4.5
    def description(self):
        return self._pizza.description() + " + пеппероні"

class Bacon(PizzaDecorator):
    def cost(self):
        return self._pizza.cost() + 4
    def description(self):
        return self._pizza.description() + " + бекон"

class Chicken(PizzaDecorator):
    def cost(self):
        return self._pizza.cost() + 4.5
    def description(self):
        return self._pizza.description() + " + курка"

class Mushrooms(PizzaDecorator):
    def cost(self):
        return self._pizza.cost() + 2.5
    def description(self):
        return self._pizza.description() + " + гриби"

class Olives(PizzaDecorator):
    def cost(self):
        return self._pizza.cost() + 2
    def description(self):
        return self._pizza.description() + " + оливки"

class BellPepper(PizzaDecorator):
    def cost(self):
        return self._pizza.cost() + 1.5
    def description(self):
        return self._pizza.description() + " + болгарський перець"

class Onion(PizzaDecorator):
    def cost(self):
        return self._pizza.cost() + 1
    def description(self):
        return self._pizza.description() + " + цибуля"

class Spinach(PizzaDecorator):
    def cost(self):
        return self._pizza.cost() + 2
    def description(self):
        return self._pizza.description() + " + шпинат"

class TomatoSauce(PizzaDecorator):
    def cost(self):
        return self._pizza.cost() + 1
    def description(self):
        return self._pizza.description() + " + томатний соус"

class BBQSauce(PizzaDecorator):
    def cost(self):
        return self._pizza.cost() + 1.5
    def description(self):
        return self._pizza.description() + " + BBQ соус"

class PestoSauce(PizzaDecorator):
    def cost(self):
        return self._pizza.cost() + 2
    def description(self):
        return self._pizza.description() + " + соус песто"

class Pineapple(PizzaDecorator):
    def cost(self):
        return self._pizza.cost() + 2.5
    def description(self):
        return self._pizza.description() + " + ананас"

class Jalapeno(PizzaDecorator):
    def cost(self):
        return self._pizza.cost() + 1.5
    def description(self):
        return self._pizza.description() + " + халапеньо"

class BaconBits(PizzaDecorator):
    def cost(self):
        return self._pizza.cost() + 3
    def description(self):
        return self._pizza.description() + " + сматочки бекону"

class ExtraCheese(PizzaDecorator):
    def cost(self):
        return self._pizza.cost() + 2.5
    def description(self):
        return self._pizza.description() + " + екстра сир"

def show_pizza(pizza):
    print(f"${pizza.cost()} for {pizza.description()}")

mega_pizza = ExtraCheese(BaconBits(Jalapeno(Pineapple(Spinach(Onion(BellPepper(Olives(Mushrooms(Chicken(Pepperoni(Ham(Mozzarella(Cheddar(Parmesan(TomatoSauce(BBQSauce(PestoSauce(Pizza()))))))))))))))))))
show_pizza(mega_pizza)
