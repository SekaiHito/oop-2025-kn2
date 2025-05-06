import json
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

class Dota2Items:
    MAX_COST = 6825
    TYPE_VALUES = {
        "Carry": 1.0,
        "Support": 0.8,
        "Tank": 0.9,
        "Utility": 0.85
    }
    num_of_items = 0
    all_items = []  

    def __init__(self, name, type, cost, aura):
        if type not in Dota2Items.TYPE_VALUES:
            raise ValueError(f"Invalid item type: {type}. Allowed types: {list(Dota2Items.TYPE_VALUES.keys())}")
        
        self.name = name
        self.type = type
        self.cost = cost
        self.aura = aura
        self.value = self.calculate_value()
        Dota2Items.all_items.append(self)  
        Dota2Items.num_of_items += 1

    @classmethod
    def from_alternative_string(cls, item_string):
        name, type, cost, aura = item_string.split('-')
        return cls(name, type, int(cost), bool(int(aura)))
    
    @classmethod
    def get_average_cost_by_type(cls, item_type):
        filtered_items = [item for item in cls.all_items if item.type == item_type]
        if not filtered_items:
            return 0
        total_cost = sum(item.cost for item in filtered_items)
        return round(total_cost / len(filtered_items), 2)


    def calculate_value(self):
        aura_value = 1 if self.aura else 0
        normalized_cost = min(self.cost / Dota2Items.MAX_COST, 1)
        type_value = Dota2Items.TYPE_VALUES[self.type]
        value = 0.4 * aura_value + 0.3 * (1 - normalized_cost) + 0.3 * type_value
        return round(value, 2)


    @staticmethod
    def print_item_info(name):
        print(name)
        for item in Dota2Items.all_items:
            if item.name.lower() == name.lower():
                aura_status = "Так" if item.aura else "Ні"
                print(f"Назва: {item.name}")
                print(f"Тип: {item.type}")
                print(f"Вартість: {item.cost}")
                print(f"Аура: {aura_status}")
                print(f"Value: {item.value}")
                return
        print(f"Предмет з назвою '{name}' не знайдено.")

def print_items_table():
    print(f"{'Назва предмета':<25} | {'Тип':<10} | {'Кошт':<5} | {'Аура':<5} | {'Value':<5}")
    print("-" * 60)
    for item in Dota2Items.all_items:
        aura_status = "Так" if item.aura else "Ні"
        print(f"{item.name:<25} | {item.type:<10} | {item.cost:<5} | {aura_status:<5} | {item.value:<5}")

def load_items_from_csv(filename):
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue  
            parts = line.replace("'", "").split(",")
            if len(parts) != 4:
                print(f"Некоректний рядок: {line}")
                continue
            name = parts[0]
            type = parts[1]
            try:
                cost = int(parts[2])
                aura = bool(int(parts[3]))
                Dota2Items(name, type, cost, aura)
            except ValueError as e:
                print(f"Помилка при обробці рядка: {line} -> {e}")

load_items_from_csv("items.csv")
item_str = 'Nullifier-Carry-4325-0'
Nullifier = Dota2Items.from_alternative_string(item_str)
print_items_table()



print(Dota2Items.num_of_items)
Dota2Items.print_item_info('Radiance')


avg_cost = Dota2Items.get_average_cost_by_type("Carry")
print(f"Середня вартість предметів типу Carry: {avg_cost}")