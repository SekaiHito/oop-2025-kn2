## Міністерство освіти і науки України

## ЛЬВІВСЬКИЙ НАЦІОНАЛЬНИЙ УНІВЕРСИТЕТ ВЕТЕРИНАРНОЇ МЕДИЦИНИ ТА БІОТЕХНОЛОГІЙ ІМЕНІ С.З. ҐЖИЦЬКОГО

# Звіт
про виконання лаборотарної роботи #8 з дисциплини "об'єктно орієнтовне програмування" на тему **"Наслідування в об’єктно-орієнтованому програмуванні"**


Виконав: студент групи КН-21**Вирста Андрій**

Прийняв: доц. А.Татомир

## Львів 2025

Мета: Оволодіти концепцією наслідування класів


## Хід роботи

1.Я реалізував наслідування в Python, щоб повторно використовувати код. Створив батьківський клас AthleteBase, який містить загальні властивості для спортсменів:
    class AthleteBase:
    def __init__(self, name, sport, ranking):
        self.name = name
        self.sport = sport
        self.ranking = ranking

2.Потім створив дочірні класи TennisPlayer та FootballPlayer, які успадковують AthleteBase і використовують super() для виклику конструктора батьківського класу:
    class TennisPlayer(AthleteBase):
    def __init__(self, name, ranking):
        super().__init__(name, "Теніс", ranking)

class FootballPlayer(AthleteBase):
    def __init__(self, name, ranking):
        super().__init__(name, "Футбол", ranking)

3.Щоб організувати взаємодію між об'єктами різних класів, я створив AthleteReport, який приймає список спортсменів і викликає їхні методи:
    class AthleteReport:
    def __init__(self, athletes):
        self.athletes = athletes

    def generate_report(self):
        for athlete in self.athletes:
            print(athlete.describe())

4. Я також перевірив правильність наслідування за допомогою isinstance() та issubclass():
    print(isinstance(tennis_player, AthleteBase))  # True
print(issubclass(TennisPlayer, AthleteBase))  # True
[Переглянути `lab-8.py`](./lab-8.py)

## Висновок
На цій лабораторній роботі Я  реалізував принципи наслідування в Python, створивши батьківський клас та кілька дочірніх, що використовують super(). Також організував взаємодію між дочірніми класами через окремий клас звітності. Перевірка isinstance() та issubclass() підтвердила правильність успадкування. В цілому, код дозволяє ефективно повторно використовувати логіку та структурувати програму. 
