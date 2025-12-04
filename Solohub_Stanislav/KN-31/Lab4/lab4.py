class BadReport:
    def __init__(self, content):
        self.content = content

    def generate(self):
        return f"Звіт: {self.content}"

    def save_to_file(self, filename):
        with open(filename, "w") as f:
            f.write(self.content)
            print(f"Збережено у {filename}")

r = BadReport("Продати акції")
r.save_to_file("report.txt")