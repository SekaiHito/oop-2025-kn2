# МІНІСТЕРСТВО ОСВІТИ ТА НАУКИ

## Львівський національний університет ветеринарії і біотехнологій імені С.З.Ґжицького

# Звіт

**про виконання лаборатоної роботи №3**
**з дисципліни "Об'єктно-орієнтоване програмування"**
**на тему** 
**Основи процедурного програмування в Python 3**

Виконав: студент групи КН-21 Греділь Адріан

Перевірив: доц. А.Татомир

### Львів 2025

Мета: засвоєти студентами методів та прийомів роботи з функціями.

## Хід роботи

*1. Написавши примітивний код засвоїв роботу функцій в Python 3.*

```py
def calculate_area(length, width):
    area = length * width
    return area

result = calculate_area(5, 3)
print("The area is:", result)

```

2. Задаши функцію з параметром **name** викликва її з аргументом `"Adrian"`

```py
def greet(name):  
    print("Hello,", name)

greet("Adrian")    

```

3. Попрактикувався з колбеками рекурсивно викликвав `say_hallo` у `run_twice`

```py

def say_hello():
    print("Hello!")

def run_twice(callback):
    callback()
    callback()

run_twice(say_hello)


```

4. Розв’язати заданий приклад.

```py


def list_benefits():
    return "Більш упорядкований код», «Більше читабельний код», «Легше повторне використання коду», «Дозволяє програмістам ділитися та з’єднувати код разом"


def build_sentence(benefit):
    return "%s is a benefit of functions!" % benefit


def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()

```


## Висновки:

Виконавши лабораторну роботу N4 мені вдалось розібратись як працюють функціх в *python*, а саме: як виклакати функцію з аргументом, як працюють колбеки і в загальному як реалізовувати примітивні завдання з функцією.