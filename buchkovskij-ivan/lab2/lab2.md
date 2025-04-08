## Львівський національний університет ветеринарії і біотехнологій імені С.З.Ґжицького

# Звіт

Про виконання лаборатоної роботи №2 з дисципліни Об'єктно-орієнтоване програмування на тему **"Вивчення простих типів даних і методів роботи з ними у Python 3"**

Виконав: студента групи КН-21 Бучковський Іван

Прийняв: доц. А.Татомир

## Львів 2025

Мета: Метою роботи є вивчення основ розробки додатків на Python 3.

## Хід роботи

1. Ознайомились з типами даних і створила програму для повернення їх класів

```py
string_var = "String name"
integer_var = 25
float_var = 10.5

print(type(string_var))
print(type(integer_var))
print(type(float_var))
```
2. Навчився здійснювати базові операції та приведення типів. Написав програму для повернення результату математичних операцій

```py
x = True
y = False

print(x and y)  
print(x or y)   
print(not x)    
```
3. Ознайомився з типом “List”. Навчився задавати та зчитувати значення їх елементів. Написав програму для виведення списку

```py
list_variable = ['a', 'b', 'c']
print(list_variable)
```
4. Ознайомився з основними операторами мови Python 3. Створив програму для повернення обчислення операторів

```py
math_example = (2 + 2) ** 2 - (10 % 2)
print(math_example)
```
5. Навчився основам форматування стрічок і текстового виводу. Написав програму використовуючи синтаксис для маніпуляцій з стрічками

```py
data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."

print(format_string % data)
```
6. Освоїв роботу зі стрічками

```py
s = "Strings are awesome!"

print("Length of s = %d" % len(s))

print("The first occurrence of the letter a = %d" % s.index("a"))

print("a occurs %d times" % s.count("a"))

print("The first five characters are '%s'" % s[:5]) 
print("The next five characters are '%s'" % s[5:10]) 
print("The thirteenth character is '%s'" % s[12]) 
print("The characters with odd index are '%s'" %s[1::2]) 
print("The last five characters are '%s'" % s[-5:]) 

print("String in uppercase: %s" % s.upper())


print("String in lowercase: %s" % s.lower())

if s.startswith("Str"):
    print("String starts with 'Str'. Good!")

if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")

print("Split the words of the string: %s" % s.split(" "))
```
7. Ознайомився з типом даних “словник” (“Dictionary”).

```py
phonebook = {  
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}  

phonebook["Jake"] = 938273443  
del phonebook["Jill"]  

if "Jake" in phonebook:  
    print("Jake is listed in the phonebook.")
    
if "Jill" not in phonebook:      
    print("Jill is not listed in the phonebook.")
```
## Висновки
За сьогоднішнє заняття я навчився використовувати базові типи даних в Python та роботу з ними. А саме string, integer, float.
А також булеві значення True or False.