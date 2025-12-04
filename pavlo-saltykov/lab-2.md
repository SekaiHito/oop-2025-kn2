## Міністерство освіти і науки України
## Львівський національний університет ветеринарії і біотехнологій імені С.З.Ґжицького

# Звіт
про виконання лабораторної роботи №2 з дисципліни "**Об'єктно орієнтоване програмування**"  
на тему: **Вивчення структурних патернів проєктування на Python (Decorator, Facade, Proxy)**

Виконав: студент групи **КН-31** Салтиков Павло  
Прийняв: викл. **Н.Заплатинський**

Львів 2025

---

## **Мета**
Ознайомитися з основними структурними патернами проєктування (Structural Patterns) у мові Python 3, які описують способи побудови складних систем із простих об’єктів.

---

## **Хід роботи**

1. **Реалізував патерн Decorator.**  
   Дає змогу динамічно розширювати поведінку об’єктів.
   ```py
    def bold(func):
        def wrapper():
            return "(" + func() + ")"
    return wrapper

    @bold
    def func():
        return "Hello"

    print(func())  # (Hello)
   ```

2. **Реалізував патерн Facade.**  
   Спрощує роботу з комплексною системою, надаючи єдиний інтерфейс.
   ```py
    class CPU:
        def start(self):
            print("CPU started")

    class Memory:
        def load(self):
            print("Memory loaded")

    class ComputerFacade:
        def __init__(self):
            self.cpu = CPU()
            self.memory = Memory()
        def start_computer(self):
            self.cpu.start()
            self.memory.load()
            print("Computer is ready")

    computer = ComputerFacade()
    computer.start_computer()
   ```

3. **Реалізував патерн Proxy.**  
   Контролює доступ до об’єкта і додає додаткові дії при зверненні.
   ```py
    class Printer:
        def print(self, text):
            print(text)

    class ProxyPrinter:
        def __init__(self):
            self.printer = None
        def print(self, text):
            if not self.printer:
                self.printer = Printer()
            self.printer.print(text)

    printer = ProxyPrinter()
    printer.print("Hello")
    printer.print("World")
   ```

4. **Результат виконання програми:**
   ```
    (Hello)

    CPU started
    Memory loaded
    Computer is ready

    Hello
    World

---

## **Висновки**

Під час виконання лабораторної роботи я ознайомився з ключовими структурними патернами: Decorator, Facade та Proxy.
Вони допомагають спрощувати структуру програм, роблять її більш гнучкою та сприяють повторному використанню коду.