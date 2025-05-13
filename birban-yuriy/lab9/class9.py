class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f"{self.name}, {self.age} років"

    def __str__(self):
        return self.get_info()

    def __eq__(self, other):
        return isinstance(other, Person) and self.name == other.name and self.age == other.age


class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def get_info(self):
        return f"{super().get_info()}, Оцінка: {self.grade}"


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
        self.students = []

    def assign(self, student):
        if isinstance(student, Student):
            self.students.append(student)

    def get_info(self):
        return f"{super().get_info()}, Предмет: {self.subject}"

    def __len__(self):
        return len(self.students)


s1 = Student("Андрій", 19, "B")
s2 = Student("Олена", 17, "A")
t1 = Teacher("Іван Петрович", 40, "Математика")
t1.assign(s1)
t1.assign(s2)

for person in [s1, s2, t1]:
    print(person)

print("К-сть студентів у викладача:", len(t1))
print("Студенти однакові?", s1 == s2)
