class Memento:
    def __init__(self, state: str):
        self._state = state

    def get_state(self):
        return self._state


class TextEditor:
    def __init__(self):
        self._text = ""

    def write(self, text: str):
        self._text += text

    def save(self) -> Memento:
        return Memento(self._text)

    def restore(self, memento: Memento):
        self._text = memento.get_state()

    def get_text(self):
        return self._text


class History:
    def __init__(self):
        self._stack = []

    def push(self, memento: Memento):
        self._stack.append(memento)

    def pop(self) -> Memento:
        return self._stack.pop()


if __name__ == "__main__":
    editor = TextEditor()
    history = History()

    editor.write("Hello")
    history.push(editor.save())

    editor.write(", world!")
    history.push(editor.save())

    print(editor.get_text())      

    editor.restore(history.pop()) 
    print(editor.get_text())      

    editor.restore(history.pop())  
    print(editor.get_text())       
