## Міністерство освіти і науки України

## Львівський національний університет ветеринарії і біотехнологій імені С.З.Ґжицького

# Звіт

про виконання лаборатоної роботи №4 з дисципліни ***Об'єктно-орієнтоване програмування*** на тему **Основи процедурного програмування в Python 3**

Виконала: студентка групи КН-21 **Федорчук Юлія**

Прийняв: доц. А.Татомир

## Львів 2025

Мета: Мета роботи полягає у засвоєнні методів та прийомів роботи з
функціями.

## Хід роботи

1. Вивчили методи роботи з функціями, викликати функції, передавати їх
в якості параметрів у інші функції (“callback”).

```py
def list_benefits():
    return "More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"

def build_sentence(benefit):
    return f"{benefit} is a benefit of functions!"


def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions() #More organized code is a benefit of functions!
                                 #More readable code is a benefit of functions!
                                 #Easier code reuse is a benefit of functions!
                                 #Allowing programmers to share and connect code together is a benefit of functions!
```

## Висновки
Роблячи лабораторну роботу №4, я повторила як працювати з функціями.