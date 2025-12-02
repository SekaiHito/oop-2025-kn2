class OldSystem:
    """Старий клас, що приймає два числа."""
    def old_method(self, n1: int, n2: int) -> int:
        print(f"-> Old: Додавання {n1} та {n2}")
        return n1 + n2

class Adapter:
    """Робить OldSystem сумісною з NewSystem."""
    def __init__(self, adaptee: OldSystem) -> None:
        self._adaptee = adaptee

    def new_method(self, data: list) -> int:
        print("-> Adapter: Перетворення списку на два числа...")
        
        num1 = data[0] if len(data) > 0 else 0
        num2 = data[1] if len(data) > 1 else 0
        
        return self._adaptee.old_method(num1, num2)

def new_system_client(target):
    """Клієнтський код, який очікує метод new_method."""
    data_list = [1, 6, 15, 8]
    print(f"Клієнт: Надсилаємо дані: {data_list}")
    result = target.new_method(data_list)
    print(f"Клієнт: Отриманий результат: {result}")
    
old_instance = OldSystem()

adapter = Adapter(old_instance)

new_system_client(adapter)