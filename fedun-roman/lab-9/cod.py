class MinecraftMob:
    def sound(self):
        return "Some Minecraft sound"

    def __str__(self):
        return f"{self.__class__.__name__} mob"

    def __len__(self):
        return 1

class Wolf(MinecraftMob):
    def sound(self):
        return "Bark!"

    def __len__(self):
        return 4

class Cat(MinecraftMob):
    def sound(self):
        return "Hiss!"

    def __len__(self):
        return 9

class Creeper(MinecraftMob):
    def sound(self):
        return "Sssss... BOOM!"

    def __len__(self):
        return 0

mobs = [Wolf(), Cat(), Creeper(), MinecraftMob()]

for mob in mobs:
    print(str(mob), "-", mob.sound(), "- hearts:", len(mob))