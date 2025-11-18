from abc import ABC, abstractmethod
import copy

# === 1. Singleton ===
class SingletonMeta(type):
    """Мета-клас для створення одинак."""
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Config(metaclass=SingletonMeta):
    """Клас конфігурації програми (єдиний екземпляр)."""
    def __init__(self):
        self.settings = {"theme": "dark", "lang": "uk"}
    
    def __repr__(self):
        return f"<Config {self.settings}>"

# === 2. Factory Method ===
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Гав!"

class Cat(Animal):
    def speak(self):
        return "Мяу!"

class AnimalFactory:
    """Фабричний метод"""
    def create_animal(self, animal_type: str) -> Animal:
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        else:
            raise ValueError("Невідомий тип тварини")

# === 3. Abstract Factory ===
class Button(ABC):
    @abstractmethod
    def draw(self): pass

class WinButton(Button):
    def draw(self):
        return "Windows Button"

class MacButton(Button):
    def draw(self):
        return "Mac Button"

class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

class WinFactory(GUIFactory):
    def create_button(self):
        return WinButton()

class MacFactory(GUIFactory):
    def create_button(self):
        return MacButton()

# === 4. Prototype ===
class Shape:
    def __init__(self, color, size):
        self.color = color
        self.size = size

    def clone(self):
        return copy.deepcopy(self)

    def __repr__(self):
        return f"<Shape color={self.color}, size={self.size}>"

# === Використання ===
if __name__ == "__main__":
    # Singleton
    cfg1 = Config()
    cfg2 = Config()
    print("Singleton:", cfg1 is cfg2, cfg1)

    # Factory Method
    factory = AnimalFactory()
    dog = factory.create_animal("dog")
    cat = factory.create_animal("cat")
    print("Factory Method:", dog.speak(), cat.speak())

    # Abstract Factory
    factory = WinFactory()
    btn = factory.create_button()
    print("Abstract Factory:", btn.draw())

    # Prototype
    shape1 = Shape("red", 10)
    shape2 = shape1.clone()
    shape2.color = "blue"
    print("Prototype:", shape1, shape2)
