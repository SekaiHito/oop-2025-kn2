class MinecraftVillager:
    villagers_count = 0
    village_name = "Default Village"

    def __init__(self, nickname, years):
        # Спавн нового жителя
        self.nickname = nickname
        self.years = years
        MinecraftVillager.villagers_count += 1

    def villager_info(self):
        # Інфо про жителя
        return f"{self.nickname}, {self.years} років, {MinecraftVillager.village_name}"

    @classmethod
    def set_village(cls, name):
        # Змінити назву села
        cls.village_name = name
        return f"Village: {name}"

    @classmethod
    def spawn_from_string(cls, s):
        # Спавн жителя з рядка
        nickname, years = s.split(',')
        return cls(nickname.strip(), int(years.strip()))

    @staticmethod
    def is_adult(years):
        # Чи дорослий житель (може працювати на фермі)
        return years >= 18

if __name__ == "__main__":
    villager1 = MinecraftVillager("Steve", 20)
    print(villager1.villager_info())
    print(MinecraftVillager.set_village("BlockTown"))
    villager2 = MinecraftVillager.spawn_from_string("Alex, 19")
    print(villager2.villager_info())
    print(f"Дорослий? {MinecraftVillager.is_adult(villager1.years)}")
    print(f"Всього жителів: {MinecraftVillager.villagers_count}")