## Міністерство освіти і науки України
## Львівський національний університет ветеринарії і біотехнологій імені С.З.Ґжицького

# Звіт
про виконання лабораторної роботи №3 з дисципліни "**Об'єктно орієнтоване програмування**"  
на тему: **Вивчення патернів проєктування на Python 3 (Singleton, Factory, Abstract Factory, Prototype)**

Виконав: студент групи **КН-31** Вирста Андрій  
Прийняв: доц. **А. Татомир**

Львів 2025

---

## **Мета**
Ознайомитися з основними породжувальними патернами проєктування (creational patterns) у мові Python 3 та навчитися реалізовувати їх на практиці.

---

## **Хід роботи**

1. **Ознайомився з теоретичними основами патернів проєктування.**  
   Зокрема, з породжувальними патернами, які відповідають за створення об’єктів.

2. **Реалізував патерн Singleton.**  
   Цей патерн гарантує, що в системі існує лише один екземпляр певного класу, і забезпечує глобальну точку доступу до нього.
   ```py
   class SingletonMeta(type):
       _instances = {}
       def __call__(cls, *args, **kwargs):
           if cls not in cls._instances:
               cls._instances[cls] = super().__call__(*args, **kwargs)
           return cls._instances[cls]

   class Config(metaclass=SingletonMeta):
       def __init__(self):
           self.settings = {"theme": "dark", "lang": "uk"}
   ```

3. **Реалізував патерн Factory Method.**  
   Фабричний метод дозволяє створювати об’єкти без необхідності вказувати їх конкретний тип.
   ```py
   class Animal(ABC):
       @abstractmethod
       def speak(self): pass

   class Dog(Animal):
       def speak(self): return "Гав!"

   class Cat(Animal):
       def speak(self): return "Мяу!"

   class AnimalFactory:
       def create_animal(self, animal_type: str) -> Animal:
           if animal_type == "dog": return Dog()
           elif animal_type == "cat": return Cat()
   ```

4. **Реалізував патерн Abstract Factory.**  
   Дозволяє створювати цілі “сімейства” пов’язаних об’єктів без залежності від їх конкретних класів.
   ```py
   class GUIFactory(ABC):
       @abstractmethod
       def create_button(self): pass

   class WinFactory(GUIFactory):
       def create_button(self):
           return "Windows Button"
   ```

5. **Реалізував патерн Prototype.**  
   Дозволяє створювати нові об’єкти шляхом копіювання існуючих.
   ```py
   class Shape:
       def __init__(self, color, size):
           self.color = color
           self.size = size
       def clone(self):
           return copy.deepcopy(self)
   ```

6. **Запустив програму.**  
   Програма відпрацювала успішно:
   ```
   Singleton: True <Config {'theme': 'dark', 'lang': 'uk'}>
   Factory Method: Гав! Мяу!
   Abstract Factory: Windows Button
   Prototype: <Shape color=red, size=10> <Shape color=blue, size=10>
   ```

---

## **Висновки**

Під час виконання лабораторної роботи я ознайомився з породжувальними патернами проєктування у Python.  
Реалізував і протестував чотири основних патерни: **Singleton, Factory Method, Abstract Factory та Prototype**.  
Отримав практичні навички у створенні гнучких архітектур програмного забезпечення.
