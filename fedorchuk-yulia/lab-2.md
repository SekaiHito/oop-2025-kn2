## Міністерство освіти і науки України

## Львівський національний університет ветеринарії і біотехнологій імені С.З.Ґжицького

# Звіт

про виконання лаборатоної роботи №2 з дисципліни Об'єктно-орієнтоване програмування на тему **Вивчення простих типів даних і методів роботи з ними у Python 3**

Виконала: студентка групи КН-21 Федорчук Юлія

Прийняв: доц. А.Татомир

## Львів 2025

Мета: Метою роботи є вивчення основ розробки додатків на Python 3.

## Хід роботи

1. Ознайомились з типами даних і створила програму для повернення їх класів

```py
string="This is str"
integer=24
a_float=2.5

print(type(string))
print(type(integer))
print(type(a_float))
```
2. Навчилися здійснювати базові операції та приведення типів. Написала програму для повернення результату математичних операцій

```py
x = True
y = False

print(x and y)  
print(x or y)   
print(not x)    
```
3. Ознайомилися з типом “List”. Навчилися задавати та зчитувати значення
їх елементів. Написала програму для виведення списку

```py
my_list=[1, 2, 3]
print(my_list)
```
4. Ознайомилися з основними операторами мови Python 3. Створила програму для повернення обчислення операторів

```py
math=5+5*2**3/12
print(math)
```
5. Навчилися основам форматування стрічок і текстового виводу. Написала програму використовуючи синтаксис для маніпуляцій з стрічками

```py
data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."

print(format_string % data)
```
6. Освоїли роботу зі стрічками

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
7. Ознайомилися з типом даних “словник” (“Dictionary”).

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
За сьогоднішнє заняття я закріпила знання по git, повторила синтаксис по пайтону, вивчила новий. Також познайомилась з таким розширенням файлу як .md і навчилася в ньому працювати. Клонувала чужий репозиторій на свій комп'ютер