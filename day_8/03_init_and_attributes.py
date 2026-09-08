# ---------------------------------------------------------
# DAY 8 | TOPIC 3: __init__ AND ATTRIBUTES
# __init__ is called automatically when you create an object.
# It is the CONSTRUCTOR - it sets up the object's starting state.
# ---------------------------------------------------------


# ---------------------------------------------------------
# SECTION 1: THE PROBLEM WITHOUT __init__
# ---------------------------------------------------------
# Without __init__, you set attributes manually after creation.
# This is risky - you might forget one or make a typo.

class CarBad:
    pass

c = CarBad()
c.model = "Toyota Camry"
c.year  = 2020
# We forgot to set c.color!
# Any code that uses c.color will CRASH:
# print(c.color)   # AttributeError: 'CarBad' object has no attribute 'color'

print("Without __init__: must set every attribute manually. Risky!")


# ---------------------------------------------------------
# SECTION 2: __init__ - THE CONSTRUCTOR
# ---------------------------------------------------------
# __init__ is a SPECIAL METHOD (note the double underscores).
# Python calls it AUTOMATICALLY the moment you create a new object.
# You use it to set up all the attributes in one safe place.
#
# Syntax:
#
#   class Car:
#       def __init__(self, model: str, year: int, color: str, for_sale: bool) -> None:
#           self.model = model
#           ...
#
# When you write:   car1 = Car("Toyota Camry", 2020, "blue", True)
# Python internally does:  Car.__init__(car1, "Toyota Camry", 2020, "blue", True)
#
# You NEVER call __init__ yourself - Python does it automatically.

class Car:
    def __init__(self, model: str, year: int, color: str, for_sale: bool) -> None:
        self.model    = model     # store model ON this object
        self.year     = year      # store year  ON this object
        self.color    = color     # store color ON this object
        self.for_sale = for_sale  # store for_sale ON this object


# Creating objects - __init__ is called instantly:
car1 = Car("Toyota Camry", 2020, "blue",  True)
car2 = Car("Honda Civic",  2018, "red",   False)
car3 = Car("BMW X5",       2022, "black", True)

print("\n--- __init__ in action ---")
print(f"car1: {car1.year} {car1.color} {car1.model}, for sale: {car1.for_sale}")
print(f"car2: {car2.year} {car2.color} {car2.model}, for sale: {car2.for_sale}")
print(f"car3: {car3.year} {car3.color} {car3.model}, for sale: {car3.for_sale}")


# ---------------------------------------------------------
# SECTION 3: UNDERSTANDING `self`
# ---------------------------------------------------------
# `self` is ALWAYS the first parameter of __init__ (and all methods).
# `self` refers to THE SPECIFIC OBJECT being created right now.
#
# When you write:   car1 = Car("Toyota Camry", 2020, "blue", True)
# Python passes car1 as `self` automatically.
#
# Inside __init__:
#   self.model = model
# means:
#   "On THIS specific car object, store a model attribute."
#
# self.model  -> stored ON the object permanently
# model       -> just a local variable, gone when __init__ finishes
#
# Think of self as "this object right here":
#   self.model = "Toyota Camry"  ->  "This car's model is Toyota Camry"
#   self.year  = 2020            ->  "This car's year is 2020"

print("\n--- self in action ---")
print(f"car1 -> model: {car1.model}, year: {car1.year}")
print(f"car2 -> model: {car2.model}, year: {car2.year}")

# Each object has its OWN copy of every attribute:
print(f"\ncar1.model = '{car1.model}'  <- car1's own model")
print(f"car2.model = '{car2.model}'  <- car2's own model")

# Changing one does NOT affect the other:
car1.color = "silver"
print(f"\nAfter change: car1 color = {car1.color}, car2 color = {car2.color}")


# ---------------------------------------------------------
# SECTION 4: STEP-BY-STEP - What Happens When You Create an Object
# ---------------------------------------------------------
# Let's trace:  car1 = Car("Toyota Camry", 2020, "blue", True)
#
#   Step 1: Python creates a new empty Car object in memory.
#   Step 2: Python calls __init__(that_new_object, "Toyota Camry", 2020, "blue", True)
#           -> self = the new object, model = "Toyota Camry", year = 2020, ...
#   Step 3: self.model = "Toyota Camry"  -> stored on the object
#   Step 4: self.year  = 2020            -> stored on the object
#   Step 5: self.color = "blue"          -> stored on the object
#   Step 6: self.for_sale = True         -> stored on the object
#   Step 7: __init__ finishes.
#   Step 8: Python returns the finished object and assigns it to car1.
#
# After that, car1.model is "Toyota Camry" - forever (until changed).


# ---------------------------------------------------------
# SECTION 5: DEFAULT VALUES IN __init__
# ---------------------------------------------------------
# __init__ can have default parameter values - just like regular functions.
# We give for_sale a default value of False so most cars start as not for sale.

class CarWithDefault:
    def __init__(self, model: str, year: int, color: str, for_sale: bool = False) -> None:
        self.model    = model
        self.year     = year
        self.color    = color
        self.for_sale = for_sale


car4 = CarWithDefault("Tesla Model 3", 2023, "white")             # for_sale defaults to False
car5 = CarWithDefault("Ford Mustang",  2021, "yellow", True)      # for_sale is True
car6 = CarWithDefault("Audi A4",       2019, "grey",  False)     # for_sale is explicitly False

print("\n--- Default values in __init__ ---")
print(f"{car4.model}: for sale = {car4.for_sale}")
print(f"{car5.model}: for sale = {car5.for_sale}")
print(f"{car6.model}: for sale = {car6.for_sale}")


# ---------------------------------------------------------
# SECTION 6: MODIFYING ATTRIBUTES AFTER CREATION
# ---------------------------------------------------------
# You can always change an attribute using dot notation.

print("\n--- Modifying attributes ---")
car4.for_sale = True       # The Tesla is now for sale
print(f"{car4.model}: for sale = {car4.for_sale}")

car5.year = 2022           # Update the Mustang's year
print(f"{car5.model}: year = {car5.year}")


# ---------------------------------------------------------
# SECTION 7: COMPUTED ATTRIBUTES IN __init__
# ---------------------------------------------------------
# __init__ can compute attributes from the input - not just store them.

class CarWithAge:
    def __init__(self, model: str, year: int, color: str, for_sale: bool = False) -> None:
        self.model    = model
        self.year     = year
        self.color    = color
        self.for_sale = for_sale
        self.age      = 2025 - year   # computed from input


car7 = CarWithAge("Nissan Altima", 2017, "white")
car8 = CarWithAge("Hyundai Sonata", 2024, "blue")

print("\n--- Computed attributes ---")
print(f"{car7.model}: age = {car7.age} years")
print(f"{car8.model}: age = {car8.age} years")
