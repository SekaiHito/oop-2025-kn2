def bold(func):
    def wrapper():
        return "(" + func() + ")"
    return wrapper

@bold
def func():
    return "Hello"

print(func())  # (Hello)


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


class RealPrinter:
    def print(self, text):
        print(text)

class ProxyPrinter:
    def __init__(self):
        self.real_printer = None
    def print(self, text):
        if not self.real_printer:
            self.real_printer = RealPrinter()
        self.real_printer.print(text)


printer = ProxyPrinter()
printer.print("Hello")
printer.print("World")
