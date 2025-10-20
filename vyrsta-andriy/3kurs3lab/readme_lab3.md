## Міністерство освіти і науки України
## Львівський національний університет ветеринарії і біотехнологій імені С.З.Ґжицького

# Звіт
про виконання лабораторної роботи №3 з дисципліни "**Об'єктно орієнтоване програмування**"  
на тему: **Вивчення поведінкових патернів проєктування на Python 3 (Observer, Strategy, Command)**

Виконав: студент групи **КН-31** Вирста Андрій  
Прийняв: викл. **Н.Заплатинський**

Львів 2025

---

## **Мета**
Ознайомитися з основними поведінковими патернами проєктування у мові Python 3 та навчитися реалізовувати їх на практиці.

---

## **Хід роботи**

1. **Ознайомився з теоретичними основами поведінкових патернів.**  
   Ці патерни описують способи взаємодії об’єктів між собою, розподіляючи обов’язки між ними.

2. **Реалізував патерн Observer (Спостерігач).**  
   Цей патерн дозволяє об’єктам отримувати повідомлення про зміни стану іншого об’єкта.

   ```python
   class Observer:
       def update(self, msg):
           print(f"[Observer] {msg}")

   class Subject:
       def __init__(self): self.obs = []
       def attach(self, o): self.obs.append(o)
       def notify(self, msg):
           for o in self.obs: o.update(msg)

   s = Subject(); o1, o2 = Observer(), Observer()
   s.attach(o1); s.attach(o2); s.notify("Подія сталася!")
   ```

3. **Реалізував патерн Strategy (Стратегія).**  
   Дає змогу змінювати алгоритм роботи програми під час виконання.

   ```python
   class Strategy:
       def execute(self, a, b): pass
   class Add(Strategy):
       def execute(self, a, b): return a + b
   class Sub(Strategy):
       def execute(self, a, b): return a - b
   class Context:
       def __init__(self, s): self.s = s
       def set(self, s): self.s = s
       def run(self, a, b): return self.s.execute(a, b)

   ctx = Context(Add())
   print("10 + 5 =", ctx.run(10, 5))
   ctx.set(Sub())
   print("10 - 5 =", ctx.run(10, 5))
   ```

4. **Реалізував патерн Command (Команда).**  
   Інкапсулює запит у вигляді об’єкта, що дозволяє відкладати, комбінувати або скасовувати дії.

   ```python
   class Command:
       def execute(self): pass
   class LightOn(Command):
       def execute(self): print("Світло увімкнено")
   class LightOff(Command):
       def execute(self): print("Світло вимкнено")
   class Remote:
       def __init__(self): self.cmd = None
       def set(self, c): self.cmd = c
       def press(self): self.cmd.execute()

   r = Remote()
   r.set(LightOn()); r.press()
   r.set(LightOff()); r.press()
   ```

5. **Запустив програму.**  
   Програма відпрацювала успішно:
   ```
   [Observer] Подія сталася!
   [Observer] Подія сталася!
   10 + 5 = 15
   10 - 5 = 5
   Світло увімкнено
   Світло вимкнено
   ```

---

## **Висновки**

Під час виконання лабораторної роботи я ознайомився з трьома основними поведінковими патернами проєктування: **Observer, Strategy та Command**.  
Реалізував їхні приклади на мові **Python 3** та перевірив коректність роботи.  
Отримав практичні навички створення гнучких систем із чітким розподілом відповідальності між об’єктами.
