# Порушення SRP: клас виконує дві відповідальності
class Report:
    def __init__(self, content):
        self.content = content

    def generate(self):
        return f"Звіт: {self.content}"

    def save_to_file(self, filename):
        with open(filename, "w") as f:
            f.write(self.content)

# Виправлення SRP: розділення відповідальностей
class Report:
    def __init__(self, content):
        self.content = content

    def generate(self):
        return f"Звіт: {self.content}"

class ReportSaver:
    def save_to_file(self, report, filename):
        with open(filename, "w") as f:
            f.write(report.content)

# Використання
report = Report("Продажі за листопад")
saver = ReportSaver()
saver.save_to_file(report, "report.txt")