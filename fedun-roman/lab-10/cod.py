class MinecraftPlayer:
    def __init__(self, nickname):
        self._nickname = nickname

    @property
    def nickname(self):
        """Геттер для nickname"""
        return self._nickname

    @nickname.setter
    def nickname(self, value):
        """Сеттер для nickname"""
        if not value:
            raise ValueError("Нікнейм не може бути порожнім")
        self._nickname = value

    @nickname.deleter
    def nickname(self):
        """Делетер для nickname"""
        print("Видалення нікнейму гравця...")
        del self._nickname

player = MinecraftPlayer("Steve")
print(player.nickname)
player.nickname = "Alex"
print(player.nickname)
del player.nickname