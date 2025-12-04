class Transport:
    def deliver(self):
        pass

class Truck(Transport):
    def deliver(self):
        return "Доставка вантажівкою по дорозі"

class Ship(Transport):
    def deliver(self):
        return "Доставка кораблем по морю"

class LogisticsFactory:
    def create_transport(self, type):
        if type == "road":
            return Truck()
        elif type == "sea":
            return Ship()
        else:
            return None

factory = LogisticsFactory()
transport = factory.create_transport("sea")
print(transport.deliver())