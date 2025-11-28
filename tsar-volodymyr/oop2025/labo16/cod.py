from abc import ABC, abstractmethod
from pathlib import Path
from dataclasses import dataclass

# --- 1. Domain Entity (Сутність) ---
# Відповідальність: Зберігання даних та бізнес-логіка звіту.
@dataclass
class Report:
    title: str
    content: str

    def generate_formatted(self) -> str:
        """Форматує звіт для виводу."""
        return f"📊 ЗВІТ: {self.title}\n{'-'*20}\n{self.content}"


# --- 2. Abstraction (Інтерфейс) ---
# Ми створюємо контракт. Будь-хто, хто хоче зберігати звіти, має реалізувати цей метод.
class IReportSaver(ABC):
    @abstractmethod
    def save(self, report: Report, destination: str) -> None:
        pass


# --- 3. Implementation (Реалізація) ---
# Відповідальність: Технічні деталі запису у файл.
class FileReportSaver(IReportSaver):
    def save(self, report: Report, destination: str) -> None:
        file_path = Path(destination)
        print(f"💾 Збереження у файл: {file_path.absolute()}")
        
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(report.generate_formatted())
            print("✅ Успішно збережено.")
        except IOError as e:
            print(f"❌ Помилка запису: {e}")


# --- Client Code ---
if __name__ == "__main__":
    # 1. Створення звіту (Бізнес-логіка)
    my_report = Report(
        title="Продажі за Листопад", 
        content="Загальний дохід: $12,000\nНових клієнтів: 45"
    )

    # 2. Вибір способу збереження (Інфраструктура)
    # Ми використовуємо конкретну реалізацію FileReportSaver
    saver: IReportSaver = FileReportSaver()
    
    # 3. Виконання дії
    saver.save(my_report, "november_report.txt")