class Report:
    def __init__(self, data):
        self.data = data

    def generate(self):
        return f"Звіт: {self.data}"

    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            f.write(self.generate())

    def send_email(self, email):
        print(f"Відправляю {self.generate()} на {email}")

class ReportGenerator:
    def __init__(self, data):
        self.data = data

    def generate(self):
        return f"Звіт: {self.data}"

class ReportSaver:
    def save_to_file(self, report, filename):
        with open(filename, 'w') as f:
            f.write(report.generate())

class EmailSender:
    def send_email(self, report, email):
        print(f"Відправляю {report.generate()} на {email}")

report = ReportGenerator("Дані продажів")
saver = ReportSaver()
sender = EmailSender()

saver.save_to_file(report, "report.txt")
sender.send_email(report, "example@mail.com")