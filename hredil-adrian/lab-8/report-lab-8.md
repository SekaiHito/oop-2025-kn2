# МІНІСТЕРСТВО ОСВІТИ ТА НАУКИ

## Львівський національний університет ветеринарії і біотехнологій імені С.З.Ґжицького

# Звіт

**про виконання лаборатоної роботи №8**

**з дисципліни "Об'єктно-орієнтоване програмування"**

**на тему** 

**Використання методів класу і статичних методів**

Виконав: студент групи КН-21 Греділь Адріан

Перевірив: доц. А.Татомир

### Львів 2025

**Мета роботи - оволодіти концепцією наслідування класів.**


## Хід роботи

 1. Я навчився повторно використовувати існуючий код завдяки наслідуванню. Це дозволяє створювати нові класи, використовуючи вже існуючі властивості та методи, що економить час і зменшує дублювання коду.

```py

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        super().speak()
        print(f"{self.name} barks")

animal = Animal("Generic Animal")
dog = Dog("Buddy", "Golden Retriever")

animal.speak()
dog.speak()

```

2. Я створив один батьківський клас і декілька дочірніх. Дочірні класи успадковують частину властивостей та функціоналу від батьківського класу, що дозволяє зручно розширювати та модифікувати їх. Я освоїв використання методу super(), який дозволяє викликати методи батьківського класу з дочірнього.

```py

class Animal:
    def __init__(self, species, name):
        self.species = species
        self.name = name

    def make_sound(self):
        print(f"The {self.species} {self.name} makes a sound.")

class Dog(Animal):
    def __init__(self, species, name, breed):
        super().__init__(species, name)
        self.breed = breed

    def make_sound(self):
        super().make_sound()
        print(f"The dog {self.name}, a {self.breed}, barks.")

class Cat(Animal):
    def __init__(self, species, name, color):
        super().__init__(species, name)
        self.color = color

    def make_sound(self):
        super().make_sound()
        print(f"The cat {self.name}, who is {self.color}, meows.")

dog = Dog("dog", "Buddy", "Golden Retriever")
cat = Cat("cat", "Whiskers", "black")

dog.make_sound()
cat.make_sound()

```

3. В одному з дочірніх класів я організував використання методів об’єктів-представників іншого дочірнього класу, що дозволяє організувати взаємодію між різними частинами коду.

```py

class Animal:
    def __init__(self, species, name):
        self.species = species
        self.name = name

    def make_sound(self):
        print(f"The {self.species} {self.name} makes a sound.")

class Dog(Animal):
    def __init__(self, species, name, breed):
        super().__init__(species, name)
        self.breed = breed

    def make_sound(self):
        super().make_sound()
        print(f"The dog {self.name}, a {self.breed}, barks.")

class Cat(Animal):
    def __init__(self, species, name, color):
        super().__init__(species, name)
        self.color = color

    def make_sound(self):
        super().make_sound()
        print(f"The cat {self.name}, who is {self.color}, meows.")

    def interact_with_dog(self, dog):
        print(f"The cat {self.name} interacts with the dog {dog.name}.")
        dog.make_sound()

dog = Dog("dog", "Buddy", "Golden Retriever")
cat = Cat("cat", "Whiskers", "black")

cat.make_sound()
cat.interact_with_dog(dog)

```

4. Я ознайомився з методами instanceof та issubclassof. instanceof дозволяє перевіряти, чи є об’єкт екземпляром певного класу або його нащадка, а issubclassof — перевіряти, чи є клас нащадком іншого класу.

```py

class Animal:
    def __init__(self, species, name):
        self.species = species
        self.name = name

    def make_sound(self):
        print(f"The {self.species} {self.name} makes a sound.")

class Dog(Animal):
    def __init__(self, species, name, breed):
        super().__init__(species, name)
        self.breed = breed

    def make_sound(self):
        super().make_sound()
        print(f"The dog {self.name}, a {self.breed}, barks.")

dog = Dog("dog", "Buddy", "Golden Retriever")

print(isinstance(dog, Dog))
print(isinstance(dog, Animal))

print(issubclass(Dog, Animal))
print(issubclass(Animal, Dog))


```

## Висновок:

Я ознайомився з методами isinstance() та issubclass(), які дозволяють перевіряти, чи є об'єкт екземпляром певного класу або його нащадка, а також перевіряти, чи є один клас нащадком іншого. Це корисні інструменти для роботи з ієрархією класів і перевіркою типів у Python.

