## Міністерство освіти і науки України

## Північний кампус Львівського національного університету ветеринарної медицини та біотехнологій імені С.З. Ґжицького.

# Звіт
Про виконання лаборотарної роботи №4 з дисциплини **"Об'єктно орієнтоване програмування"** на тему: **"Основи процедурного програмування в Python 3"**

Виконав: студент групи КН-22СП Лесів Роман

Прийняв: доц. А.Татомир
## Львів 2025

Мета: засвоїти методи та прийоми роботи з функціями.


## Хід роботи

1. Освоїв [синтаксис функцій в Python 3](https://docs.python.org/uk/3.13/library/functions.html).

2. Закріпив [поняття параметрів та аргументів функції](https://acode.com.ua/function-parameters-arguments-python/).

3. Вивчив методи [роботи з функціями, викликати функції, передавати їх
в якості параметрів у інші функції (“callback”).](https://understandinges6.denysdovhan.com/manuscript/03-Functions.html)

4. Розв’язав заданий приклад [[1]](functions.py):

```python
# Modify this function to return a list of strings as defined above
def list_benefits():
    return "More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"

# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(benefit):
    return "%s is a benefit of functions!" % benefit

def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()
```

## Висновки  
На цій практичні роботі я вивчив синтаксис функцій в Python 3, закріпив знання щодо поняття параметрів та аргументів функції, засвоїв методи роботи з функціями, викликати функції, передавати їх в якості параметрів у інші функції, розв'язав приклад по цій темі, де вклали виклик функції всередині функції.