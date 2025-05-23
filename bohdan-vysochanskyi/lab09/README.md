## Міністерство освіти і науки України

## ЛЬВІВСЬКИЙ НАЦІОНАЛЬНИЙ УНІВЕРСИТЕТ ВЕТЕРИНАРНОЇ МЕДИЦИНИ ТА БІОТЕХНОЛОГІЙ ІМЕНІ С.З. ҐЖИЦЬКОГО

# Звіт
про виконання лаборотарної роботи #9 з дисциплини "об'єктно орієнтовне програмування" на тему **"Поліморфізм в Python 3"**


Виконав: студент групи КН-22СП ***Височанський Богдан***

Прийняв: доц. А.Татомир

## Львів 2025

Мета: Засвоїти застосування принципу поліморфізму в об’єктно-орієнтованому програмуванні.



## Хід роботи

1. Ознайомився з поняттям **поліморфізму в обʼєктно-орієнтованому програмуванні**. Зрозумів, що поліморфізм дозволяє обʼєктам різних класів мати однаковий інтерфейс (однакові методи), але реалізовувати його по-різному.

2. Навчився **перевизначати поведінку методів** у дочірніх класах. Зокрема, метод `describe()` реалізовано по-іншому в різних конвертерах, хоча він має спільну назву з базовим класом.

3. Реалізував кілька **магічних методів** (`__str__`, `__repr__`, `__eq__`, `__lt__`) у базовому класі `CurrencyConverterBase`. Це дозволяє:
   - зручно виводити обʼєкти через `print()`,
   - порівнювати обʼєкти конвертерів за курсом обміну,
   - отримати представлення обʼєкта для налагодження.
   [Переглянути `currency-class-v5.py`](./currency-class-v5.py)

## Висновок
На цій практичній роботі я ознайомився з принципами поліморфізму в об’єктно-орієнтованому програмуванні ООП а саме мови програмування Python 3