# ---------------------------------------------------------
# DAY 8 | HOMEWORK 1: WHAT IS OOP?
# Answer each question by writing code or comments below it.
# Run your file after each section to check your output.
# ---------------------------------------------------------


# ─────────────────────────────────────────────────────────
# EXERCISE 1: Spot the problem
# ─────────────────────────────────────────────────────────
# Below is messy non-OOP code for tracking cars in a dealership.
# Each car needs 4 separate variables. Add a THIRD car (any model,
# year, color, and for_sale value you like) using the same pattern,
# then print all three cars.

car1_model    = "Toyota Camry"
car1_year     = 2020
car1_color    = "blue"
car1_for_sale = True

car2_model    = "Honda Civic"
car2_year     = 2018
car2_color    = "red"
car2_for_sale = False

# TODO: Add car3 here (4 variables)

# TODO: Print all three cars in the format:
# "MODEL (YEAR) - COLOR - For sale: True/False"


# ─────────────────────────────────────────────────────────
# EXERCISE 2: Match the vocabulary
# ─────────────────────────────────────────────────────────
# Look at the code below and fill in the blanks in the print statements.

class Car:
    def __init__(self, model: str, year: int, color: str, for_sale: bool) -> None:
        self.model    = model
        self.year     = year
        self.color    = color
        self.for_sale = for_sale

    def describe(self) -> None:
        print(f"{self.year} {self.color} {self.model}")


my_car = Car("Toyota Camry", 2020, "red", True)
my_car.describe()

# TODO: Fill in the blanks - replace ??? with the correct term
#       (class / object / attribute / method)
print("Car is a       : ???")    # Car is a ____
print("my_car is an   : ???")    # my_car is an ____
print("my_car.model   : ???")    # my_car.model is an ____
print("my_car.describe(): ???")  # describe is a ____


# ─────────────────────────────────────────────────────────
# EXERCISE 3: Design your own class (on paper first!)
# ─────────────────────────────────────────────────────────
# Think about a "Garage" that stores cars.
# Before writing code, answer:
#   - What ATTRIBUTES would a Garage have?  (data it knows)
#   - What METHODS would a Garage have?     (things it can do)
#
# Write your answers as comments below, then write a very simple
# class (just the class line and pass for now - no __init__ yet):

# Attributes a Garage might have:
# 1. ???
# 2. ???
# 3. ???

# Methods a Garage might have:
# 1. ???
# 2. ???

# TODO: Write the class skeleton here (class Garage: ... pass)


# ─────────────────────────────────────────────────────────
# EXERCISE 4: True or False?
# ─────────────────────────────────────────────────────────
# Write True or False for each statement as a comment.

# a) A class is like a blueprint, and objects are things built from it.  -> ???
# b) You can only create ONE object from a class.                         -> ???
# c) Attributes store data; methods define behaviour.                     -> ???
# d) OOP helps keep related data bundled together.                        -> ???
# e) You must write a new class every time you need a new object.         -> ???
