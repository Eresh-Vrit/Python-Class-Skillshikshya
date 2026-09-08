# ---------------------------------------------------------
# DAY 8 | HOMEWORK 5: PUTTING IT ALL TOGETHER
# Combine everything: class, __init__, attributes, methods, lists, loops.
# ---------------------------------------------------------


# ─────────────────────────────────────────────────────────
# EXERCISE 1: Build the Car class
# ─────────────────────────────────────────────────────────
# Complete the Car class below.
# It should have:
#   __init__(self, model: str, year: int, color: str, for_sale: bool = False) -> None
#   drive(self) -> None        prints "You drive the COLOR MODEL"
#   stop(self) -> None         prints "You stop the COLOR MODEL"
#   describe(self) -> None     prints "YEAR COLOR MODEL"
#   age(self, current_year: int) -> int
#                              returns current_year - year
#   mark_sold(self) -> None    sets for_sale to False and prints a message
#
# Then create at least 2 cars and call each method at least once.

class Car:
    def __init__(self, model: str, year: int, color: str, for_sale: bool = False) -> None:
        self.model    = model
        self.year     = year
        self.color    = color
        self.for_sale = for_sale

    # TODO: Add drive, stop, describe, age, and mark_sold methods

# TODO: Create cars and test your methods


# ─────────────────────────────────────────────────────────
# EXERCISE 2: Create a dealership inventory
# ─────────────────────────────────────────────────────────
# Create a list called 'inventory' with at least 4 Car objects.
# Loop through the list and call describe() on each car.

# TODO: Write your code here


# ─────────────────────────────────────────────────────────
# EXERCISE 3: Show only cars for sale
# ─────────────────────────────────────────────────────────
# Using the 'inventory' list from Exercise 2, loop through it
# and print only the cars where for_sale is True.
# Hint: use an if statement inside the loop.

# TODO: Write your code here


# ─────────────────────────────────────────────────────────
# EXERCISE 4: Test drive every car
# ─────────────────────────────────────────────────────────
# Using the 'inventory' list from Exercise 2, loop through it
# and call drive() and stop() on each car.

# TODO: Write your code here


# ─────────────────────────────────────────────────────────
# EXERCISE 5: Sell and repaint a car
# ─────────────────────────────────────────────────────────
# Using the 'inventory' list from Exercise 2:
#   1. Mark the first car as sold.
#   2. Repaint the second car to any new color you like.
#   3. Loop through the inventory and print the updated details.

# TODO: Write your code here


# ─────────────────────────────────────────────────────────
# EXERCISE 6: Find and fix the mistakes (BONUS)
# ─────────────────────────────────────────────────────────
# This code has 4 common OOP mistakes. Find and fix them all.

# class car:                                       # Mistake 1?
#     def __init__(model, year, color):            # Mistake 2?
#         model = model                            # Mistake 3?
#         self.year = year
#         self.color = color
#
#     def describe():                              # Mistake 4?
#         print(f"{self.year} {self.color} {model}")
#
# my_car = car("Toyota Camry", 2020, "blue")
# my_car.describe()

# TODO: Copy the code above, fix the mistakes, and test it.
