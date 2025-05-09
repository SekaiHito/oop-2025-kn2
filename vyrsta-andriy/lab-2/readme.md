## Міністерство освіти і науки України
## Львівський національний унівеситет ветеринарії і біотехнологій...
# Звіт
про виконання лаборотарної роботи №2 з дисциплини "**об'єктно орієнтовне програмування**" на тему: **Вивчення простих типів даних і методів роботи з ними у Python 3**.

Виконав: студент групи КН-21 Вирста Андрій

Прийняв: доц. А.Татомир

Львів 2025

**Мета**: Метою роботи є вивчення основ розробки додатків на Python 3

**Хід роботи**

1.Ознайомився із основами синтаксису в Python 3.

2.Розглянув змінні та їх прості типи в Python 3.

3.Ознайомився із динамічною типізацію.

4.Розв'язав завдання.Навчився здійснювати базові операції та приведення типів.
```py
    mystring = "hello"

    myfloat = 10.0

    myint = 20

    if mystring == "hello":

        print("String: %s" % mystring)

    if isinstance(myfloat, float) and myfloat == 10.0:
        print("Float: %f" % myfloat)

    if isinstance(myint, int) and myint == 20:

        print("Integer: %d" % myint)
```

5.Ознайомився із типом "List".Розв'язав приклад.
```
    numbers = []

    strings = []

    names = ["John", "Eric", "Jessica"]

    second_name = None

    print(numbers)

    print(strings)

    print("The second name on the names list is %s" % second_name)
```
6.Ознайомився із основними операторами.
```
    x = object()

    y = object()

    x_list = [x]

    y_list = [y]

    big_list = []

    print("x_list contains %d objects" % len(x_list))
    print("y_list contains %d objects" % len(y_list))
    print("big_list contains %d objects" % len(big_list))

    if x_list.count(x) == 10 and y_list.count(y) == 10:

    print("Almost there...")

    if big_list.count(x) == 10 and big_list.count(y) == 10:

    print("Great!")
```
7.Навчитися основам форматування стрічок і текстового виводу.

8.Ознайомився зі стрічками як зі списками (“Lists”).

9.Ознайомитися з типом даних “словник” (“Dictionary”). Розв’язати
завдання.Розв'язав завдання.Ознайомився із 'словником'.
```
    phonebook = {  
        "John" : 938477566,
        "Jack" : 938377264,
        "Jill" : 947662781
    }  

    if "Jake" in phonebook:  
       print("Jake is listed in the phonebook.")
    
    if "Jill" not in phonebook:      
        print("Jill is not listed in the phonebook.")
```
## Висновки

Під час виконання цієї лабораторної роботи ознайомився та згадав базові основи синтаксису Пайтон.Також ознайомився із
типами та змінними.Виконав завдання по ключових питаннях.Та постараюсь засвоїти вивчене.
