class Student:
    student_count = 0

    def __init__(self, name, surname, grades):
        self.name = name
        self.surname = surname
        self.grades = grades
        self.average = sum(grades) / len(grades)

        Student.student_count += 1

    def describe(self):
        return f"Студент: {self.name} {self.surname}, середній бал: {self.average:.2f}"

    @classmethod
    def total_students(cls):
        return f"Загальна кількість студентів: {cls.student_count}"


student1 = Student("Оля", "Іваненко", [90, 85, 92])
student2 = Student("Ігор", "Коваль", [78, 80, 75])
student3 = Student("Марія", "Сидоренко", [95, 88, 100])

print(student1.describe())
print(student2.describe())
print(student3.describe())

print(Student.total_students())