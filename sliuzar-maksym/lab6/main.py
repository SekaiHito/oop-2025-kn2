class Course:
    object_count = 0

    def __init__(self, course_name, instructor, duration_in_weeks):
        self.course_name = course_name
        self.instructor = instructor
        self.duration_in_weeks = duration_in_weeks
        self.course_description = f"Course: {course_name}, Instructor: {instructor}, Duration: {duration_in_weeks} weeks"
        Course.object_count += 1

    def generate_description(self):
        return self.course_description

    @classmethod
    def get_object_count(cls):
        return cls.object_count


course1 = Course("C++ Programming", "John Doe", 12)
course2 = Course("Advanced C++", "Jane Smith", 16)
course3 = Course("C++ for Beginners", "Alice Johnson", 10)

print(course1.generate_description())
print(course2.generate_description())
print(course3.generate_description())

print(f"Total courses created: {Course.get_object_count()}")

