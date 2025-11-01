## Міністерство освіти і науки України
## Львівський національний університет ветеринарії і біотехнологій імені С.З.Ґжицького

# Звіт
про виконання лабораторної роботи №1 з дисципліни "**Об'єктно орієнтоване програмування**"  
на тему: **Вивчення патернів проєктування на Python 3 (Singleton, Factory, Abstract Factory)**

Виконав: студент групи **КН-31** Салтиков Павло 
Прийняв: викл. **Н.Заплатинський**

Львів 2025

---

## **Мета**
Ознайомитися з основними породжувальними патернами проєктування (creational patterns) у мові Python 3 та навчитися реалізовувати їх на практиці.

---

## **Хід роботи**

1. **Ознайомився з теоретичними основами патернів проєктування.**  
   Зокрема, з породжувальними патернами, які відповідають за створення об’єктів.

2. **Реалізував патерн Singleton.**  
   Одинак — це породжувальний патерн проектування, який гарантує, що клас має лише один екземпляр, та надає глобальну точку доступу до нього
   ```py
    class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    a = Singleton()
    b = Singleton()
    print(a is b)
   ```

3. **Реалізував патерн Factory Method.**  
   Фабричний метод дозволяє створювати об’єкти без необхідності вказувати їх конкретний тип.
   ```py
    class Character(ABC):
    @abstractmethod
    def attack(self):
        pass

    class Warrior(Character):
        def attack(self):
            print("Warrior attacks with sword!")

    class Archer(Character):
        def attack(self):
            print("Archer shoots an arrow!")

    def character_factory(type_):
        if type_ == "warrior":
            return Warrior()
        elif type_ == "archer":
            return Archer()
        else:
            raise ValueError("Unknown character")


    player = character_factory("mage")
    player.attack()  # Mage casts a spell

    player2 = character_factory("warrior")
    player2.attack()  # Warrior attacks with sword
   ```

4. **Реалізував патерн Abstract Factory.**  
   Дозволяє створювати цілі “сімейства” пов’язаних об’єктів без залежності від їх конкретних класів.
   ```py
   class Chair(ABC):
    @abstractmethod
    def sit(self):
        pass

    class ModernChair(Chair):
        def sit(self):
            print("Sitting on a Modern Chair")

    class VictorianChair(Chair):
        def sit(self):
            print("Sitting on a Victorian Chair")

    class FurnitureFactory(ABC):
        @abstractmethod
        def create_chair(self):
            pass

    class ModernFactory(FurnitureFactory):
        def create_chair(self):
            return ModernChair()

    class VictorianFactory(FurnitureFactory):
        def create_chair(self):
            return VictorianChair()

    factory = ModernFactory()
    chair = factory.create_chair()
    chair.sit()
   ```

6. **Запустив програму.**  
   Програма відпрацювала успішно:
   ```
    True
    Archer shoots an arrow!
    Warrior attacks with sword!
    Sitting on a Modern Chair

   ```

---

## **Висновки**

Під час виконання лабораторної роботи я вивчив породжувальні патерни проєктування у Python.
Реалізував і перевірив три патерни: Singleton, Factory Method та Abstract Factory.
Набув практичного досвіду у створенні гнучких та масштабованих архітектур програмного забезпечення.