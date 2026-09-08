# ---------------------------------------------------------
# DAY 8 | TOPIC 1: WHAT IS OOP?
# Understanding WHY OOP exists before learning HOW to use it.
# ---------------------------------------------------------


# ---------------------------------------------------------
# SECTION 1: THE PROBLEM - Code Without OOP
# ---------------------------------------------------------
# Imagine you are building a program to track cars in a dealership.
# Without OOP, you track each car using separate variables:

car1_model    = "Toyota Camry"
car1_year     = 2020
car1_color    = "blue"
car1_for_sale = True

car2_model    = "Honda Civic"
car2_year     = 2018
car2_color    = "red"
car2_for_sale = False

car3_model    = "BMW X5"
car3_year     = 2022
car3_color    = "black"
car3_for_sale = True

print("--- Cars (without OOP) ---")
print(f"{car1_model}, Year: {car1_year}, Color: {car1_color}, For sale: {car1_for_sale}")
print(f"{car2_model}, Year: {car2_year}, Color: {car2_color}, For sale: {car2_for_sale}")
print(f"{car3_model}, Year: {car3_year}, Color: {car3_color}, For sale: {car3_for_sale}")

# What is wrong with this approach?
#   Adding a 4th car means 4 MORE variables.
#   Easy to mix up: car1_color vs car2_color.
#   100 cars = 400 variables - impossible to manage!
#   The data for one car is scattered across 4 separate variables.


# ---------------------------------------------------------
# SECTION 2: WHAT IS OOP? - The Big Idea
# ---------------------------------------------------------
# OOP = Object-Oriented Programming
#
# The core idea is simple:
#   Instead of tracking data in separate variables,
#   BUNDLE the related data AND behaviour together into one unit.
#
# That unit is called an OBJECT.
#
# An object holds:
#   ATTRIBUTES (data)    -> what it KNOWS    (model, year, color, for_sale)
#   METHODS (functions)  -> what it CAN DO   (drive, stop, describe)
#
# To create objects, you first define a CLASS - a blueprint.
#
#   CLASS  = blueprint / template     (the cookie cutter)
#   OBJECT = a real thing from the blueprint (the actual cookie)
#
# You define the class ONCE. Then create as many objects as you need.


# ---------------------------------------------------------
# SECTION 3: REAL-WORLD OBJECTS - Attributes and Methods
# ---------------------------------------------------------
# Think about objects you see every day. Each one has:
#   - attributes (what it knows about itself)
#   - methods (what it can do)
#
# Example 1: PHONE
#   Attributes: brand, model, battery_level, color
#   Methods   : call(number), take_photo(), charge()
#
# Example 2: CUP
#   Attributes: color, material, capacity_ml, is_full
#   Methods   : fill(), drink(), wash()
#
# Example 3: BOOK
#   Attributes: title, author, page_count, is_open
#   Methods   : open(page), close(), read_line()
#
# In every case, the object bundles its data (attributes)
# with the actions it can perform (methods).

print("\n--- Real-world objects ---")
print("Phone: knows brand/battery, can call or take photos")
print("Cup:   knows color/capacity, can be filled or drunk from")
print("Book:  knows title/author, can be opened or read")


# ---------------------------------------------------------
# SECTION 4: A FIRST LOOK - A Car Object
# ---------------------------------------------------------
# Do not worry about every detail yet. Just READ what it does.
# We will build this step by step in the next topics.

class Car:
    def __init__(self, model: str, year: int, color: str, for_sale: bool) -> None:
        self.model    = model
        self.year     = year
        self.color    = color
        self.for_sale = for_sale

    def drive(self) -> None:
        print(f"You drive the {self.color} {self.model}")

    def stop(self) -> None:
        print(f"You stop the {self.color} {self.model}")

    def describe(self) -> None:
        print(f"{self.year} {self.color} {self.model}")


# Create objects from the blueprint:
car1 = Car("Toyota Camry", 2020, "blue",  True)
car2 = Car("Honda Civic",  2018, "red",   False)
car3 = Car("BMW X5",       2022, "black", True)

print("\n--- Cars (with OOP) ---")
car1.describe()
car2.describe()
car3.describe()

# What changed?
#   Each car is its OWN object - data bundled together.
#   Adding a 4th car: car4 = Car("Tesla Model 3", 2023, "white", True) - ONE line.
#   No chance of mixing up car1's color with car2's color.
#   The methods live WITH the data, not floating around.


# ---------------------------------------------------------
# SECTION 5: OOP VOCABULARY - The 4 Key Words
# ---------------------------------------------------------
# These are words you will see everywhere in OOP:
#
#   CLASS      - the blueprint / template
#   OBJECT     - a real instance created from the class
#   ATTRIBUTE  - data stored inside an object   (self.model)
#   METHOD     - a function that belongs to the class  (drive)
#
# Real-world example:
#   "Car"           is a CLASS.
#   My car "camry"  is an OBJECT (also called an INSTANCE).
#   camry's model, year, color -> ATTRIBUTES.
#   camry.drive(), camry.stop() -> METHODS.

print("\n--- OOP vocabulary in action ---")
print("Class     -> Car     (the blueprint)")
print("Object    -> car1, car2, car3  (real car objects)")
print(f"Attribute -> car1.model is '{car1.model}'")
print("Method    -> car1.drive() prints what happens when you drive")


# ---------------------------------------------------------
# SECTION 6: CLASS = BLUEPRINT FOR OBJECTS
# ---------------------------------------------------------
# The class describes what EVERY object of that type should have.
# It does not create the objects by itself - you create them from the class.
#
#   class Car:                <- the blueprint
#       ...
#
#   car1 = Car(...)           <- build one real car from the blueprint
#   car2 = Car(...)           <- build another real car
#
# That is the heart of OOP: define once, create many.

print("\n--- The big picture ---")
print("A CLASS is a blueprint for objects.")
print("An OBJECT is a real thing built from that blueprint.")
print("With one Car class, we can make as many car objects as we want.")
