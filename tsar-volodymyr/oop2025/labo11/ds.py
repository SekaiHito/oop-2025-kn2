from abc import ABC, abstractmethod

# --- Product Interface ---
class Transport(ABC):
    """
    Абстрактний базовий клас (Інтерфейс) для всіх транспортних засобів.
    Визначає спільну поведінку для всіх нащадків.
    """
    @abstractmethod
    def drive(self) -> None:
        """Виконує рух транспортного засобу."""
        pass

# --- Concrete Products ---
class Car(Transport):
    def drive(self) -> None:
        print("🚗 Я їду на машині (швидко і комфортно).")

class Bicycle(Transport):
    def drive(self) -> None:
        print("🚲 Я їду на велосипеді (екологічно і корисно).")

class Bus(Transport):
    def drive(self) -> None:
        print("🚌 Я їду на автобусі (громадський транспорт).")

# --- Creator (Factory) Interface ---
class TransportFactory(ABC):
    """
    Абстрактний клас фабрики. 
    Оголошує фабричний метод, який має повертати об'єкт типу Transport.
    """
    @abstractmethod
    def create_transport(self) -> Transport:
        """Створює і повертає екземпляр транспортного засобу."""
        pass

# --- Concrete Creators ---
class CarFactory(TransportFactory):
    """Фабрика для створення автомобілів."""
    def create_transport(self) -> Transport:
        return Car()

class BicycleFactory(TransportFactory):
    """Фабрика для створення велосипедів."""
    def create_transport(self) -> Transport:
        return Bicycle()

class BusFactory(TransportFactory):
    """Фабрика для створення автобусів."""
    def create_transport(self) -> Transport:
        return Bus()

# --- Client Code ---
def client_code(factory: TransportFactory) -> None:
    """
    Клієнтський код працює з фабрикою через спільний інтерфейс.
    Він не знає, який саме транспорт створюється, але знає, що він вміє їхати.
    """
    transport = factory.create_transport()
    transport.drive()

if __name__ == "__main__":
    print("--- Початок роботи транспортної системи ---\n")

    # Список фабрик, які ми хочемо використати
    factories = [
        CarFactory(), 
        BicycleFactory(), 
        BusFactory()
    ]
    
    for factory in factories:
        client_code(factory)
        
    print("\n--- Роботу завершено ---")