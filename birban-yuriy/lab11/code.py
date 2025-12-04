class Transport:
    def deliver(self):
        pass

class Truck(Transport):
    def deliver(self):
        return "Доставляю вантажівкою."

class Ship(Transport):
    def deliver(self):
        return "Доставляю кораблем."

class Logistics:
    def create(self):
        """Фабричний метод"""
        pass

class RoadLogistics(Logistics):
    def create(self):
        return Truck()

class SeaLogistics(Logistics):
    def create(self):
        return Ship()

road = RoadLogistics()
print(road.create().deliver())

sea = SeaLogistics()
print(sea.create().deliver())