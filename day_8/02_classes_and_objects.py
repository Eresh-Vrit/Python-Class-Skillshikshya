# ---------------------------------------------------------
# DAY 8 | TOPIC 2: CLASSES AND OBJECTS
# How to define a class and create objects from it.
# ---------------------------------------------------------


# ---------------------------------------------------------
# SECTION 1: DEFINING A CLASS
# ---------------------------------------------------------
# Syntax:
#
#   class ClassName:
#       [indented body]
#
# Rules:
#   - 'class' is a keyword (like 'def' for functions)
#   - ClassName uses CapWords / PascalCase: each word capitalised
#       Good:  Car, BankAccount, StudentRecord
#       Bad:   car, bank_account, studentrecord
#   - The body is indented (just like a function body)
#
# The simplest possible class - it does nothing yet:

class Car:
    pass    # 'pass' means: body is intentionally empty

print("Car class defined successfully!")
print(Car)          # <class '__main__.Car'>

# Analogy: class = blueprint, object = real car.
#    The blueprint (class Car) exists on paper - you cannot drive it.
#    car1 = Car() builds a REAL car from that blueprint.
#    Each object is independent - changing one does NOT affect others.


# ---------------------------------------------------------
# SECTION 2: CREATING OBJECTS (INSTANCES)
# ---------------------------------------------------------
# Once a class exists, create objects from it like this:
#
#   variable_name = ClassName()
#
# This is called INSTANTIATION - you are creating an INSTANCE.
# The words "object" and "instance" mean the same thing.

car1 = Car()   # car1 is one Car instance
car2 = Car()   # car2 is another Car instance
car3 = Car()   # car3 is a third Car instance

print("\n--- Three car objects ---")
print(car1)    # <__main__.Car object at 0x...> - shows memory address
print(car2)
print(car3)

# Are car1 and car2 the same object?
print("\n--- Are they the same? ---")
print(car1 == car2)   # False - different objects even with same class
print(car1 is car2)   # False - 'is' checks if same spot in memory


# ---------------------------------------------------------
# SECTION 3: GIVING OBJECTS ATTRIBUTES MANUALLY
# ---------------------------------------------------------
# You can attach data to an object after creation using dot notation:
#   object.attribute_name = value

car1.model = "Toyota Camry"
car1.year  = 2020
car1.color = "blue"

car2.model = "Honda Civic"
car2.year  = 2018
car2.color = "red"

car3.model = "BMW X5"
car3.year  = 2022
car3.color = "black"

print("\n--- Car attributes via dot notation ---")
print(f"Car 1: {car1.year} {car1.color} {car1.model}")
print(f"Car 2: {car2.year} {car2.color} {car2.model}")
print(f"Car 3: {car3.year} {car3.color} {car3.model}")

# This works, BUT it is fragile:
#   What if you forget to set car1.year?
#   What if someone sets car1.colour by typo?
# That is exactly what __init__ solves - coming next topic!


# ---------------------------------------------------------
# SECTION 4: READING AND USING ATTRIBUTES
# ---------------------------------------------------------
# Read any attribute using:   object.attribute

print("\n--- Reading attributes ---")
print(car1.model)    # Toyota Camry
print(car1.year)     # 2020

# Use them in expressions:
print(f"The {car1.model} is {2025 - car1.year} years old.")

# Change an attribute:
car1.year = 2021
print(f"After update: the {car1.model} is now a {car1.year} model.")


# ---------------------------------------------------------
# SECTION 5: type() AND isinstance() - Checking Object Identity
# ---------------------------------------------------------
# type(x) tells you the CLASS of any object.

print("\n--- type() checks ---")
print(type(car1))        # <class '__main__.Car'>
print(type(42))          # <class 'int'>
print(type("hello"))     # <class 'str'>
print(type([1, 2, 3]))   # <class 'list'>

# Everything in Python is an object!
#    int, str, list - all are classes.
#    When you write "hello" you are creating a str object.

# isinstance(x, ClassName) -> True or False
print("\n--- isinstance() checks ---")
print(isinstance(car1, Car))   # True  - car1 IS a Car
print(isinstance(42,  int))    # True  - 42  IS an int
print(isinstance(car1, int))   # False - car1 is NOT an int


# ---------------------------------------------------------
# SECTION 6: MANY OBJECTS FROM ONE CLASS
# ---------------------------------------------------------
# The class is defined ONCE. You can create unlimited objects.
# Each object is independent - changing one does NOT affect others.

car1.speed = 0
car2.speed = 60
car3.speed = 120

print("\n--- Many cars from one class ---")
for car in [car1, car2, car3]:
    print(f"  {car.model} going at {car.speed} km/h")

# Change one object's attribute - the others stay the same.
car1.speed = 80
print("\n--- After changing only car1's speed ---")
print(f"  car1 speed: {car1.speed}")
print(f"  car2 speed: {car2.speed}")
print(f"  car3 speed: {car3.speed}")

# One class -> unlimited objects. That is the power of OOP.
