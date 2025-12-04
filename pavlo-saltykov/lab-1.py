from abc import ABC, abstractmethod

class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

a = Singleton()
b = Singleton()
print(a is b)


class Character(ABC):
    @abstractmethod
    def attack(self):
        pass

class Warrior(Character):
        def attack(self):
            print("Warrior attacks with sword!")

class Archer(Character):
        def attack(self):
            print("Archer shoots an arrow!")

def character_factory(type_):
    if type_ == "warrior":
        return Warrior()
    elif type_ == "archer":
        return Archer()
    else:
        raise ValueError("Unknown character")
    
player = character_factory("archer")
player.attack()  # Mage casts a spell

player2 = character_factory("warrior")
player2.attack()  # Warrior attacks with sword


class Chair(ABC):
    @abstractmethod
    def sit(self):
        pass

class ModernChair(Chair):
    def sit(self):
        print("Sitting on a Modern Chair")

class VictorianChair(Chair):
    def sit(self):
        print("Sitting on a Victorian Chair")

class FurnitureFactory(ABC):
    @abstractmethod
    def create_chair(self):
        pass

class ModernFactory(FurnitureFactory):
    def create_chair(self):
        return ModernChair()

class VictorianFactory(FurnitureFactory):
    def create_chair(self):
        return VictorianChair()


factory = ModernFactory()
chair = factory.create_chair()
chair.sit()