from abc import ABC, abstractmethod

class Transport(ABC):
    @abstractmethod
    def drive(self) -> None:
        pass

class Car(Transport):
    def drive(self) -> None:
        print("Я їду на машині")


class Bicycle(Transport):
    def drive(self) -> None:
        print("Я їду на велосипеді")

class Bus(Transport):
    def drive(self) -> None:
        print("Я їду на автобусі")

class TransportFactory(ABC):
    @abstractmethod
    def create_transport(self) -> Transport:
        pass

class CarFactory(TransportFactory):
    def create_transport(self) -> Transport:
        return Car()

class BicycleFactory(TransportFactory):
    def create_transport(self) -> Transport:
        return Bicycle()
    
class BusFactory(TransportFactory):
    def create_transport(self) -> Transport:
        return Bus()



if __name__ == "__main__":
    factories = [CarFactory(), BicycleFactory(), BusFactory()]
    
    for factory in factories:
        transport = factory.create_transport()
        transport.drive()

