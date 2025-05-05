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
car1.name = "BMW"
car1.color = "Чорний"
car1.kind = "Седан"
car1.value = 60000.00

# Створення другого транспортного засобу
car2 = Vehicle()
car2.name = "Ford"
car2.color = "Сірий"
car2.kind = "Універсал"
car2.value = 10000.00

# Вивід опису обʼєктів
print(car1.description())
print(car2.description())
