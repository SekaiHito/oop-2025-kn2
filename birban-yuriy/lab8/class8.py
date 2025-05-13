class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_basic_info(self):
        return f"Ім'я: {self.name}, Вік: {self.age}"

    def is_adult(self):
        return self.age >= 18


class Student(Person):
    total_students = 0

    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade
        Student.total_students += 1

    def get_info(self):
        return f"{super().get_basic_info()}, Оцінка: {self.grade}"

    @classmethod
    def get_total_students(cls):
        return f"Всього студентів: {cls.total_students}"

    @classmethod
    def from_string(cls, student_str):
        name, age, grade = student_str.split(";")
        return cls(name, int(age), grade)

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
        self.students = []

    def assign_student(self, student):
        if isinstance(student, Student):
            self.students.append(student)

    def list_students(self):
        return [student.get_info() for student in self.students]


s1 = Student("Андрій", 19, "B")
s2 = Student.from_string("Олена;17;A")
t1 = Teacher("Іван Петрович", 40, "Математика")

t1.assign_student(s1)
t1.assign_student(s2)

print(s1.get_info())
print(s2.get_info())
print(Student.get_total_students())
print(f"{s1.name} повнолітній? {s1.is_adult()}")
print(f"{s2.name} повнолітня? {s2.is_adult()}")

print("\nСтуденти викладача:")
for info in t1.list_students():
    print(info)

print("\nПеревірки:")
print("s1 — Student?", isinstance(s1, Student))
print("s1 — Person?", isinstance(s1, Person))
print("Student наслідує Person?", issubclass(Student, Person))
print("Teacher наслідує Person?", issubclass(Teacher, Person))
