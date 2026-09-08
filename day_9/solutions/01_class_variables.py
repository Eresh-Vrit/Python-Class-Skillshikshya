# ---------------------------------------------------------
# SOLUTION 1: CLASS VARIABLES 🏫
# Variables shared across all objects of a class.
# ---------------------------------------------------------

# Class variables belong to the class, not to one object.
# They are shared by every instance created from the class.


class Student:
    # Class variables: shared by every Student instance.
    class_year: int = 2025
    num_students: int = 0

    def __init__(self, name: str, age: int) -> None:
        # Instance attributes: unique to each Student object.
        self.name = name
        self.age = age
        # Increase the shared counter every time a student is created.
        Student.num_students += 1


# Create some Student objects.
student_1 = Student("Alice", 17)
student_2 = Student("Bob", 18)
student_3 = Student("Carol", 17)


# Print details for each student.
print(f"{student_1.name} is {student_1.age} years old.")
print(f"Class year: {student_1.class_year}")
print(f"Total students: {Student.num_students}")
print()

print(f"{student_2.name} is {student_2.age} years old.")
print(f"Class year: {student_2.class_year}")
print(f"Total students: {Student.num_students}")
print()

print(f"{student_3.name} is {student_3.age} years old.")
print(f"Class year: {student_3.class_year}")
print(f"Total students: {Student.num_students}")
print()


# BONUS: Changing the class variable affects every instance.
Student.class_year = 2026
print(f"Updated class year for student_1: {student_1.class_year}")
