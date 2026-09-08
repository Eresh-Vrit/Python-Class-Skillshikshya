# ---------------------------------------------------------
# DAY 8 | HOMEWORK 3: __init__ AND ATTRIBUTES
# Practice writing constructors with type annotations.
# ---------------------------------------------------------


# ─────────────────────────────────────────────────────────
# EXERCISE 1: Your first __init__
# ─────────────────────────────────────────────────────────
# Create a class called 'Car' with __init__ that takes:
#   model: str, year: int, color: str, for_sale: bool
# Store all four as attributes using self.
# Create 3 Car objects and print each in this format:
#   "MODEL (YEAR) - COLOR - For sale: True/False"

# TODO: Write your code here


# ─────────────────────────────────────────────────────────
# EXERCISE 2: Default values
# ─────────────────────────────────────────────────────────
# Create a class 'Car' with:
#   __init__(self, model: str, year: int, color: str, for_sale: bool = False) -> None
# Create:
#   car1 = Car("Toyota Camry", 2020, "blue")           # for_sale uses default
#   car2 = Car("Honda Civic", 2018, "red", True)       # for_sale overridden
#   car3 = Car("BMW X5", 2022, "black", False)         # for_sale explicitly False
# Print each car's details.

# TODO: Write your code here


# ─────────────────────────────────────────────────────────
# EXERCISE 3: Computed attributes
# ─────────────────────────────────────────────────────────
# Create a class 'Car' with:
#   __init__(self, model: str, year: int, color: str, for_sale: bool = False) -> None
#   Compute and store:
#       self.age = 2025 - year
# Create cars with years 2020, 2018, 2022 and print model + age.

# TODO: Write your code here


# ─────────────────────────────────────────────────────────
# EXERCISE 4: Understand self
# ─────────────────────────────────────────────────────────
# Look at this code. What will it print? Write your predictions
# as comments, THEN run it to verify.

class Car:
    def __init__(self, model: str, color: str = "white") -> None:
        self.model = model
        self.color = color


car1 = Car("Toyota Camry")
car2 = Car("Honda Civic", "red")
car3 = Car("BMW X5", "black")

car1.color = "silver"

print(car1.model, car1.color)   # -> ???
print(car2.model, car2.color)   # -> ???
print(car3.model, car3.color)   # -> ???


# ─────────────────────────────────────────────────────────
# EXERCISE 5: Mini challenge - Fuel level
# ─────────────────────────────────────────────────────────
# Create a class 'Car' with:
#   __init__(self, model: str, year: int, color: str, fuel_level: int = 100) -> None
#   Store all attributes including fuel_level.
# Create objects for 3 cars with different fuel levels.
# Print model and fuel level for each.

# TODO: Write your code here
