from abc import ABC, abstractmethod
import json

class ReportFormat(ABC):
    @abstractmethod
    def generate(self, data: dict) -> str:
        pass

class PdfReportFormat(ReportFormat):
    def generate(self, data: dict) -> str:
        content = f"===== ЗВІТ У ФОРМАТІ PDF (Текст) =====\n"
        content += f"Звіт згенеровано: {__class__.__name__}\n"
        for key, value in data.items():
            content += f"* {key.upper()}: {value}\n"
        return content

class JsonReportFormat(ReportFormat):
    """
    Нова стратегія: Форматування у JSON.
    Цей клас додано без зміни існуючих.
    """
    def generate(self, data: dict) -> str:
        return json.dumps(data, indent=4, ensure_ascii=False)

class CsvReportFormat(ReportFormat):
    """
    Ще одна нова стратегія: Форматування у CSV.
    Система легко розширюється новими класами.
    """
    def generate(self, data: dict) -> str:
        headers = ",".join(data.keys())
        values = ",".join(map(str, data.values()))
        return f"{headers}\n{values}"

class ReportGenerator:
    """
    Клас-генератор, який залежить від абстракції ReportFormat.
    Йому не важливо, який саме конкретний формат використовується.
    """
    def __init__(self, formatter: ReportFormat):
        self._formatter = formatter
    
    def output_report(self, data: dict) -> str:
        """Делегує виконання роботи обраній стратегії-форматеру."""
        print(f"--- Запуск генерації звіту через {type(self._formatter).__name__} ---")
        return self._formatter.generate(data)

report_data = {
    "продукт": "Смартфон Alpha", 
    "продажі_за_місяць": 320, 
    "прибуток_USD": 16000
}
pdf_generator = ReportGenerator(PdfReportFormat())
print(pdf_generator.output_report(report_data))
print("\n" + "="*50 + "\n")
json_generator = ReportGenerator(JsonReportFormat())
print(json_generator.output_report(report_data))
print("\n" + "="*50 + "\n")
csv_generator = ReportGenerator(CsvReportFormat())
print(csv_generator.output_report(report_data))