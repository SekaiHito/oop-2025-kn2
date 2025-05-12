class Student:
    total_students = 0
    university = "Default University"

    def __init__(self, name, age):
        self.name, self.age = name, age
        Student.total_students += 1

    def info(self):
        return f"{self.name}, {self.age}, {Student.university}"

    @classmethod
    def set_univ(cls, name):
        cls.university = name
        return f"University: {name}"

    @classmethod
    def from_str(cls, s):
        name, age = s.split(',')
        return cls(name.strip(), int(age.strip()))

    @staticmethod
    def adult(age):
        return age >= 18

if __name__ == "__main__":
    s1 = Student("John", 20)
    print(s1.info())
    print(Student.set_univ("Tech Univ"))
    s2 = Student.from_str("Jane, 19")
    print(s2.info())
    print(f"Adult? {Student.adult(s1.age)}")
    print(f"Total: {Student.total_students}")