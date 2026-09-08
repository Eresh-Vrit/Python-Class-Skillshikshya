# ---------------------------------------------------------
# DAY 8 | HOMEWORK 2: CLASSES AND OBJECTS
# Practice defining a class and creating objects from it.
# ---------------------------------------------------------


# ─────────────────────────────────────────────────────────
# EXERCISE 1: Your first Car class
# ─────────────────────────────────────────────────────────
# Define a class called 'Car' (just use 'pass' in the body).
# Then create THREE Car objects: car1, car2, car3.
# Give each car these attributes manually using dot notation:
#   .model    (e.g. "Toyota Camry", "Honda Civic", "BMW X5")
#   .year     (e.g. 2020, 2018, 2022)
#   .color    (e.g. "blue", "red", "black")
#   .for_sale (e.g. True, False, True)
# Print all three cars in the format:
#   "MODEL (YEAR) - COLOR - For sale: True/False"

# TODO: Write your code here


# ─────────────────────────────────────────────────────────
# EXERCISE 2: type() and isinstance()
# ─────────────────────────────────────────────────────────
# Given this class and these objects, predict what each
# print() will output. Write your prediction as a comment,
# THEN run the code and check if you were right.

class Car:
    pass


car1 = Car()
car2 = Car()

car1.model = "Toyota Camry"
car2.model = "Honda Civic"

# Predict the output of each line below (write as comment):
print(type(car1))                  # -> ???
print(type(car2))                  # -> ???
print(isinstance(car1, Car))       # -> ???
print(isinstance("hello", Car))    # -> ???
print(car1 == car2)                # -> ???
print(car1 is car2)                # -> ???


# ─────────────────────────────────────────────────────────
# EXERCISE 3: Create and modify
# ─────────────────────────────────────────────────────────
# 1. Define a class called 'Car'
# 2. Create a car named 'my_car' with:
#       .model    = "Tesla Model 3"
#       .year     = 2023
#       .color    = "white"
#       .for_sale = True
# 3. Print the car's details.
# 4. Change the color to "silver" and print again.

# TODO: Write your code here


# ─────────────────────────────────────────────────────────
# EXERCISE 4: Mini dealership inventory
# ─────────────────────────────────────────────────────────
# Define a class called 'Car'.
# Create 4 car objects (camry, civic, x5, mustang).
# Give each: .model, .year, .color, .for_sale
# Store all 4 in a list called 'inventory'.
# Loop through the list and print each car's details.

# TODO: Write your code here
