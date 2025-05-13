class Student:
    total_students = 0

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        Student.total_students += 1

    def get_info(self):
        return f"Ім'я: {self.name}, Вік: {self.age}, Оцінка: {self.grade}"

    @classmethod
    def get_total_students(cls):
        return f"Всього студентів: {cls.total_students}"

    @classmethod
    def from_string(cls, student_str):
        name, age, grade = student_str.split(";")
        return cls(name, int(age), grade)

    @staticmethod
    def is_adult(age):
        return age >= 18

s1 = Student("Андрій", 19, "B")
s2 = Student.from_string("Олена;17;A")

print(s1.get_info())
print(s2.get_info())
print(Student.get_total_students())
print(f"{s1.name} повнолітній? {Student.is_adult(s1.age)}")
print(f"{s2.name} повнолітня? {Student.is_adult(s2.age)}")
