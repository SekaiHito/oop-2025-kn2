## Міністерство освіти і науки України
## Львівський національний університет ветеринарії і біотехнологій імені С.З.Ґжицького

# Звіт
про виконання лабораторної роботи №3 з дисципліни "**Об'єктно орієнтоване програмування**"  
на тему: **Вивчення поведінкових патернів проєктування на Python 3 (Observer, Strategy, Command)**

Виконав: студент групи **КН-31** Салтиков Павло  
Прийняв: викл. **Н.Заплатинський**

Львів 2025

---

## **Мета**
Ознайомитися з основними поведінковими патернами проєктування у мові Python 3 та навчитися реалізовувати їх на практиці.

---

## **Хід роботи**

1. **Ознайомився з теоретичними основами поведінкових патернів.**  
   Ці патерни описують способи взаємодії об’єктів між собою, розподіляючи обов’язки між ними.

2. **Реалізував патерн Mediator (Посередник).**  
   Контролює взаємодію між об’єктами, щоб вони не залежали один від одного напряму.

   ```python
    class ChatRoom:
        def show_message(self, user, message):
            print(f"{user}: {message}")

    class User:
        def __init__(self, name, chat):
            self.name = name
            self.chat = chat
        def send(self, message):
            self.chat.show_message(self.name, message)

    room = ChatRoom()
    alice = User("Alice", room)
    bob = User("Bob", room)

    alice.send("Hi Bob!")
    bob.send("Hello Alice!")
   ```

3. **Реалізував патерн Command (Команда).**  
   Інкапсулює дію у вигляді об’єкта, щоб її можна було викликати пізніше, зберігати, відміняти.

   ```python
    class Light:
        def on(self):
            print("Light is ON")
        def off(self):
            print("Light is OFF")

    class SwitchOnCommand:
        def __init__(self, light):
            self.light = light
        def execute(self):
            self.light.on()

    light = Light()
    command = SwitchOnCommand(light)
    command.execute()
   ```

4. **Реалізував патерн Memento (Знімок).**  
   Знімок — це поведінковий патерн проектування, що дає змогу зберігати та відновлювати минулий стан об’єктів, не розкриваючи подробиць їхньої реалізації.

   ```python
    class Memento:
        def __init__(self, state):
            self.state = state

    class Editor:
        def __init__(self):
            self.text = ""
        def write(self, text):
            self.text = text
        def save(self):
            return Memento(self.text)
        def restore(self, memento):
                self.text = memento.state

    editor = Editor()
    editor.write("Hello")
    saved = editor.save()
    editor.write("Hello, World")
    print(editor.text)

    editor.restore(saved)
    print(editor.text)
   ```

5. **Запустив програму.**  
   ```

    Hi Bob!
    Hello Alice!

    Light is ON

    Hello, World
    Hello

   ```

---

## **Висновки**

Під час виконання лабораторної роботи я вивчив три ключові поведінкові патерни проєктування: Memento, Mediator та Command.
Я реалізував їхні приклади на Python 3 та перевірив їхню працездатність.
Це дало мені практичні навички у створенні гнучких систем із чітким розподілом відповідальності між об’єктами.