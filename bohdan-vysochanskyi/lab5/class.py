# Оголошення класу Транспортний засіб (Vehicle)
class Vehicle:
    name = ""         # назва транспортного засобу
    kind = "car"      # тип (типово — "автомобіль")
    color = ""        # колір
    value = 100.00    # вартість

    # Метод для опису обʼєкта
    def description(self):
        desc_str = "%s — це %s %s вартістю $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str

# Створення першого транспортного засобу
car1 = Vehicle()
car1.name = "Fer"
car1.color = "червоний"
car1.kind = "кабріолет"
car1.value = 60000.00

# Створення другого транспортного засобу
car2 = Vehicle()
car2.name = "Jump"
car2.color = "синій"
car2.kind = "фургон"
car2.value = 10000.00

# Вивід опису обʼєктів
print(car1.description())
print(car2.description())
