import os

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)


class Dota2Items:
    MAX_COST = 6825
    all_items = []

    def __init__(self, name, cost, aura):
        self.name = name
        self._cost = cost  # Використовуємо _cost, бо додано геттер/сеттер
        self.aura = aura
        self.type = "Base"
        self.value = 0  # Тимчасово
        Dota2Items.all_items.append(self)

    def calculate_value(self):
        aura_val = 1 if self.aura else 0
        norm_cost = min(self._cost / Dota2Items.MAX_COST, 1)
        type_val = getattr(self, 'type_value', 0.5)
        return round(0.4 * aura_val + 0.3 * (1 - norm_cost) + 0.3 * type_val, 2)

    @property
    def cost(self):
        return self._cost

    @cost.setter
    def cost(self, new_cost):
        if new_cost < 0 or new_cost > Dota2Items.MAX_COST:
            raise ValueError("Недійсна вартість.")
        self._cost = new_cost
        self.value = self.calculate_value()

    @cost.deleter
    def cost(self):
        print(f"🗑 Вартість предмета '{self.name}' видалена.")
        self._cost = 0
        self.value = self.calculate_value()

    def __str__(self):
        return f"{self.name} ({self.type}) – Кошт: {self._cost}, Аура: {'Так' if self.aura else 'Ні'}, Value: {self.value}"

    def info(self):
        aura_status = "Так" if self.aura else "Ні"
        print(f"Назва: {self.name}")
        print(f"Тип: {self.type}")
        print(f"Кошт: {self.cost}")
        print(f"Аура: {aura_status}")
        print(f"Value: {self.value}")

    def __str__(self):
        aura_status = "Так" if self.aura else "Ні"
        return f"{self.name} ({self.type}) — Кошт: {self.cost}, Аура: {aura_status}, Value: {self.value}"

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.cost}, {int(self.aura)})"

    def __eq__(self, other):
        return isinstance(other, Dota2Items) and self.value == other.value

    def __lt__(self, other):
        return isinstance(other, Dota2Items) and self.value < other.value

    @classmethod
    def print_items_table(cls):
        print(f"{'Назва':<25} | {'Тип':<10} | {'Кошт':<5} | {'Аура':<5} | {'Value':<5}")
        print("-" * 60)
        for item in cls.all_items:
            aura = "Так" if item.aura else "Ні"
            print(f"{item.name:<25} | {item.type:<10} | {item.cost:<5} | {aura:<5} | {item.value:<5}")

    @classmethod
    def get_average_cost(cls, type_name):
        items = [i for i in cls.all_items if i.type == type_name]
        if not items:
            return 0
        return round(sum(i.cost for i in items) / len(items), 2)

    @staticmethod
    def print_item_info(name):
        for item in Dota2Items.all_items:
            if item.name.lower() == name.lower():
                item.info()
                return
        print(f"Предмет з назвою '{name}' не знайдено.")


# Дочірні класи
class CarryItem(Dota2Items):
    def __init__(self, name, cost, aura):
        self.type_value = 1.0
        super().__init__(name, cost, aura)
        self.type = "Carry"
        self.value = self.calculate_value()  # Перерахуємо value після ініціалізації

    def calculate_value(self):
        base = super().calculate_value()
        if not self.aura:
            base += 0.05
        return round(base, 2)

class SupportItem(Dota2Items):
    def __init__(self, name, cost, aura):
        self.type_value = 0.8
        super().__init__(name, cost, aura)
        self.value = self.calculate_value()
        self.type = "Support"

    def boost_carry(self, carry_item):
        if isinstance(carry_item, CarryItem):
            print(f"\nSupport '{self.name}' підсилює Carry '{carry_item.name}':")
            carry_item.info()
        else:
            print("Це не CarryItem!")


class TankItem(Dota2Items):
    def __init__(self, name, cost, aura):
        self.type_value = 0.9
        super().__init__(name, cost, aura)
        self.value = self.calculate_value()
        self.type = "Tank"


class UtilityItem(Dota2Items):
    def __init__(self, name, cost, aura):
        self.type_value = 0.85
        super().__init__(name, cost, aura)
        self.value = self.calculate_value()
        self.type = "Utility"


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
            name, type_name, cost_str, aura_str = parts
            try:
                cost = int(cost_str)
                aura = bool(int(aura_str))
                if type_name == "Carry":
                    CarryItem(name, cost, aura)
                elif type_name == "Support":
                    SupportItem(name, cost, aura)
                elif type_name == "Tank":
                    TankItem(name, cost, aura)
                elif type_name == "Utility":
                    UtilityItem(name, cost, aura)
                else:
                    print(f"Невідомий тип: {type_name}")
            except ValueError as e:
                print(f"Помилка при обробці рядка: {line} -> {e}")


load_items_from_csv("items.csv")

item_str = 'Nullifier-Carry-4325-0'
name, type_name, cost, aura = item_str.split('-')
cost = int(cost)
aura = bool(int(aura))

if type_name == "Carry":
    nullifier = CarryItem(name, cost, aura)
elif type_name == "Support":
    nullifier = SupportItem(name, cost, aura)
elif type_name == "Tank":
    nullifier = TankItem(name, cost, aura)
elif type_name == "Utility":
    nullifier = UtilityItem(name, cost, aura)

Dota2Items.print_items_table()

print(f"\nЗагальна кількість предметів: {len(Dota2Items.all_items)}")

Dota2Items.print_item_info("Radiance")


avg = Dota2Items.get_average_cost("Carry")
print(f"\nСередня вартість предметів типу Carry: {avg}")

first_support = next((i for i in Dota2Items.all_items if isinstance(i, SupportItem)), None)
first_carry = next((i for i in Dota2Items.all_items if isinstance(i, CarryItem)), None)

if first_support and first_carry:
    first_support.boost_carry(first_carry)
# Сортування предметів за value
sorted_items = sorted(Dota2Items.all_items)
print("\n📊 Відсортовані предмети за value:")
for item in sorted_items:
    print(item)

# Порівняння двох предметів
if Dota2Items.all_items[0] == Dota2Items.all_items[1]:
    print("\nПерший і другий предмети мають однакове значення.")
else:
    print("\nПерший і другий предмети різні за значенням.")
# Отримання вартості (getter)
radiance_item = next((i for i in Dota2Items.all_items if i.name.lower() == "radiance"), None)
if radiance_item:
    print(f"💰 Вартість Radiance: {radiance_item.cost}")
    # Зміна вартості
    radiance_item.cost = 3000
    print(f"🔧 Нова вартість Radiance: {radiance_item.cost}, нове value: {radiance_item.value}")
    # Видалення
    del radiance_item.cost
    print(f"🗑 Після видалення: {radiance_item.cost}, value: {radiance_item.value}")
else:
    print("❗ Radiance не знайдено.")

