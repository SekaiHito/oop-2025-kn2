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