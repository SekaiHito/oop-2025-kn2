class Character:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
        print(f"{self.name} takes {damage} damage. Remaining health: {self.health}")

    def attack_enemy(self, enemy):
        damage = max(self.attack - enemy.defense, 0)
        enemy.take_damage(damage)
        print(f"{self.name} attacks {enemy.name} for {damage} damage.")

    def is_alive(self):
        return self.health > 0

    def heal(self, amount):
        self.health += amount
        print(f"{self.name} heals for {amount}. Current health: {self.health}")


class Warrior(Character):
    def __init__(self, name, health, attack, defense, shield_block):
        super().__init__(name, health, attack, defense)
        self.shield_block = shield_block

    def shield_attack(self, enemy):
        damage = max(self.attack + self.shield_block - enemy.defense, 0)
        enemy.take_damage(damage)
        print(f"{self.name} uses shield attack on {enemy.name} for {damage} damage.")


class Mage(Character):
    def __init__(self, name, health, attack, defense, mana):
        super().__init__(name, health, attack, defense)
        self.mana = mana

    def cast_spell(self, enemy):
        if self.mana >= 10:
            self.mana -= 10
            damage = self.attack * 2 - enemy.defense
            enemy.take_damage(damage)
            print(f"{self.name} casts a spell on {enemy.name} for {damage} damage.")
        else:
            print(f"{self.name} doesn't have enough mana to cast a spell.")


class Archer(Character):
    def __init__(self, name, health, attack, defense, range_attack):
        super().__init__(name, health, attack, defense)
        self.range_attack = range_attack

    def shoot_arrow(self, enemy):
        damage = max(self.range_attack - enemy.defense, 0)
        enemy.take_damage(damage)
        print(f"{self.name} shoots an arrow at {enemy.name} for {damage} damage.")


class BattleArena:
    def __init__(self, name):
        self.name = name

    def start_battle(self, character1, character2):
        print(f"Battle starts between {character1.name} and {character2.name}!")
        while character1.is_alive() and character2.is_alive():
            character1.attack_enemy(character2)
            if character2.is_alive():
                character2.attack_enemy(character1)

        if character1.is_alive():
            print(f"{character1.name} wins the battle!")
        else:
            print(f"{character2.name} wins the battle!")


warrior = Warrior("Arthur", 150, 20, 10, 15)
mage = Mage("Merlin", 100, 25, 5, 50)
archer = Archer("Robin", 120, 18, 8, 30)

battle_arena = BattleArena("Arena of the Lost")
battle_arena.start_battle(warrior, mage)

warrior.shield_attack(archer)
mage.cast_spell(warrior)
archer.shoot_arrow(mage)

warrior.heal(30)
mage.heal(20)

print(isinstance(warrior, Warrior))  
print(isinstance(mage, Mage))        
print(isinstance(archer, Warrior))   
print(issubclass(Warrior, Character)) 
print(issubclass(Mage, Archer))      

