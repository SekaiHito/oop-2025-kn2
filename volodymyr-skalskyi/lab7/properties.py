"""
Приклад getter'ів, setter'ів та deleter'ів
"""

class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        """Getter для name"""
        return self._name

    @name.setter
    def name(self, value):
        """Setter для name"""
        if not isinstance(value, str):
            raise ValueError("Ім'я повинно бути рядком")
        self._name = value

    @name.deleter
    def name(self):
        """Deleter для name"""
        print(f"Видалення імені {self._name}")
        del self._name

print("Getter'и, Setter'и та Deleter'и:")
person = Person("Іван")
print(f"Ім'я: {person.name}")    # Іван
person.name = "Петро"
print(f"Нове ім'я: {person.name}")  # Петро
del person.name