class Student:
    # Змінна класу: лічильник об'єктів
    student_count = 0

    def __init__(self, name, surname, grades):
        # Змінні об'єкта
        self.name = name
        self.surname = surname
        self.grades = grades
        self.average = sum(grades) / len(grades)  # атрибут, що створюється на основі інших

        # Кожного разу, коли створюється студент — збільшуємо лічильник
        Student.student_count += 1

    # Метод, який генерує опис об'єкта
    def describe(self):
        return f"Студент: {self.name} {self.surname}, середній бал: {self.average:.2f}"

    # Метод класу, який використовує змінну класу
    @classmethod
    def total_students(cls):
        return f"Загальна кількість студентів: {cls.student_count}"


# === Створення об'єктів ===
student1 = Student("Оля", "Іваненко", [90, 85, 92])
student2 = Student("Ігор", "Коваль", [78, 80, 75])
student3 = Student("Марія", "Сидоренко", [95, 88, 100])

# === Виклик методу describe() через обʼєкти ===
print(student1.describe())
print(student2.describe())
print(student3.describe())

# === Виклик методу класу для підрахунку студентів ===
print(Student.total_students())