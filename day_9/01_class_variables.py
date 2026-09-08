# ---------------------------------------------------------
# DAY 9 | TOPIC 1: CLASS VARIABLES 🏫
# Variables shared by every object made from the same class.
# ---------------------------------------------------------


# ─────────────────────────────────────────────────────────
# SECTION 1: WHAT IS A CLASS VARIABLE?
# ─────────────────────────────────────────────────────────
# Instance variables (self.name) are unique to each object.
# Class variables belong to the CLASS itself, so every
# instance sees the same value. They are defined inside the
# class but outside any method.

class Student:
    # Class variables - shared by ALL Student objects
    class_year: int = 2024
    num_students: int = 0

    def __init__(self, name: str, age: int) -> None:
        # Instance variables - unique to each Student object
        self.name = name
        self.age = age
        # Add 1 to the shared counter every time a student is created
        Student.num_students += 1


# ─────────────────────────────────────────────────────────
# SECTION 2: CREATING STUDENTS
# ─────────────────────────────────────────────────────────
# Each new student shares class_year and bumps the counter.

student1 = Student("SpongeBob", 30)
student2 = Student("Patrick", 35)
student3 = Student("Squidward", 40)


# ─────────────────────────────────────────────────────────
# SECTION 3: ACCESSING CLASS VARIABLES
# ─────────────────────────────────────────────────────────
# You can read class variables through the class name OR
# through any instance. Using the class name is clearer.

print("--- Student Info ---")
print(student1.name)
print(student2.name)
print(student3.name)

print("--- Shared Class Data ---")
print(Student.class_year)
print(Student.num_students)

# You can also read them through an instance, but the class
# name makes it obvious the value is shared.
print(student1.class_year)
