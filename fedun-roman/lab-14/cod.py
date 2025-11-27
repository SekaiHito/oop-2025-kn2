class Report:
    def __init__(self, content):
        self.content = content

    def generate(self):
        return f"Звіт: {self.content}"

class Report:
    def __init__(self, content):
        self.content = content

    def generate(self):
        return f"Звіт: {self.content}"

class ReportSaver:
    def save_to_file(self, report, filename):
        with open(filename, "w") as f:
            f.write(report.content)

report = Report("Sell in November")
saver = ReportSaver()
saver.save_to_file(report, "report.txt")