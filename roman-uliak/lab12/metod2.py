from abc import ABC, abstractmethod

class Beverage(ABC):
    @abstractmethod
    def get_cost(self):
        pass
    
    @abstractmethod
    def get_description(self):
        pass


class Coffee(Beverage):
    def get_cost(self):
        return 20
    
    def get_description(self):
        return "Coffee"

class BeverageDecorator(Beverage):
    def __init__(self, beverage: Beverage):
        self._beverage = beverage


class MilkDecorator(BeverageDecorator):
    def get_cost(self):
        return self._beverage.get_cost() + 5
    
    def get_description(self):
        return self._beverage.get_description() + ", Milk"


class SugarDecorator(BeverageDecorator):
    def get_cost(self):
        return self._beverage.get_cost() + 2
    
    def get_description(self):
        return self._beverage.get_description() + ", Sugar"


if __name__ == "__main__":
    drink = Coffee()                       
    drink = MilkDecorator(drink)          
    drink = SugarDecorator(drink)          

    print(drink.get_description())       
    print("Price:", drink.get_cost())      
