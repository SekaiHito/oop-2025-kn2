class MinecraftEntity:
    def __init__(self, name):
        self.name = name

    def interact(self):
        return f"{self.name} стоїть у світі Minecraft."

class Player(MinecraftEntity):
    def __init__(self, name, skin):
        super().__init__(name)
        self.skin = skin

    def interact(self):
        return f"Гравець {self.name} з скіном {self.skin} копає блоки."

class Creeper(MinecraftEntity):
    def __init__(self, name, power):
        super().__init__(name)
        self.power = power

    def interact(self):
        return f"Моб {self.name} вибухає з силою {self.power}!"

    def scare_player(self, player):
        if isinstance(player, Player):
            return f"Моб {self.name} лякає гравця {player.name}: {player.interact()}"
        else:
            return "Це не гравець!"

steve = Player("Стів", "Класика")
creeper = Creeper("Кріпер", 10)

print(steve.interact())
print(creeper.interact())
print(creeper.scare_player(steve))

print(isinstance(steve, MinecraftEntity))
print(isinstance(creeper, Player))
print(issubclass(Player, MinecraftEntity))
print(issubclass(Creeper, Player))