# === Observer ===
class Observer:
    def update(self, msg):
        print(f"[Observer] {msg}")

class Subject:
    def __init__(self): self.obs = []
    def attach(self, o): self.obs.append(o)
    def notify(self, msg):
        for o in self.obs: o.update(msg)

# === Strategy ===
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

# === Command ===
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

# === Демонстрація ===
if __name__ == "__main__":
    # Observer
    s = Subject(); o1, o2 = Observer(), Observer()
    s.attach(o1); s.attach(o2); s.notify("Подія сталася!")

    # Strategy
    ctx = Context(Add())
    print("10 + 5 =", ctx.run(10, 5))
    ctx.set(Sub())
    print("10 - 5 =", ctx.run(10, 5))

    # Command
    r = Remote()
    r.set(LightOn()); r.press()
    r.set(LightOff()); r.press()
