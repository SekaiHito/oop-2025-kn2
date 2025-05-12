class Item:
    total_items = 0
    item_type = "Block"

    def __init__(self, name, rarity, base_value):
        self.name = name
        self.rarity = rarity
        self.value = base_value * (1 + rarity * 0.1)
        Item.total_items += 1

    def describe(self):
        return f"{self.name} [Rarity: {self.rarity}]: {self.value:.2f} coins, Type: {self.item_type}"

    @classmethod
    def type_info(cls):
        return f"Item Type: {cls.item_type}"

    @classmethod
    def count_items(cls):
        return f"Total items: {cls.total_items}"

diamond = Item("Diamond", 5, 100)
iron_ingot = Item("Iron Ingot", 2, 20)

print(diamond.describe())
print(iron_ingot.describe())
print(Item.type_info())
print(Item.count_items())