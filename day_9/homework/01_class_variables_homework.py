# ---------------------------------------------------------
# HOMEWORK 1: CLASS VARIABLES 🏫
# Practice variables shared across all objects of a class.
# ---------------------------------------------------------

# Class variables belong to the class, not to one object.
# They are shared by every instance created from the class.


# TODO: Create a class named `Student`.
# Add two class variables:
#   - `class_year` set to 2025
#   - `num_students` set to 0

class Student:
    # Class variables go here
    

    # TODO: Create an `__init__` method that accepts `name` and `age`.
    # Inside __init__:
    #   - Store `name` and `age` as instance attributes.
    #   - Increase the `num_students` class variable by 1.
    
    def __init__(self, name: str, age: int) -> None:
        pass  # Replace with your code


# TODO: Create two or three Student objects below.
# Example names: "Alice", "Bob", "Carol"




# TODO: Print each student's name, age, class_year, and the total num_students.




# BONUS: Try changing `Student.class_year` to 2026.
# Print the class_year for one of your students again.
# What do you notice?
