class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("Олег", 20)

print(student1.name)
print(student1.age)

student1.age = 21
print(student1.age)