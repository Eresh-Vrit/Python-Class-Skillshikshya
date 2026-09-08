# ---------------------------------------------------------
# DAY 8 | TOPIC 5: PUTTING IT ALL TOGETHER
# Complete mini-project using: class, __init__, methods, objects.
# ---------------------------------------------------------


# =========================================================
# MINI PROJECT: CAR DEALERSHIP
# =========================================================
# We will build a small car dealership program.
# Each car is an object created from the same Car class.
# We will store the cars in a list and loop through them.

class Car:
    def __init__(self, model: str, year: int, color: str, for_sale: bool = False) -> None:
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

    def age(self, current_year: int) -> int:
        return current_year - self.year

    def mark_sold(self) -> None:
        self.for_sale = False
        print(f"  The {self.model} has been marked as sold.")

    def repaint(self, new_color: str) -> None:
        old_color = self.color
        self.color = new_color
        print(f"  The {self.model} was repainted from {old_color} to {new_color}.")

    def full_report(self, current_year: int) -> str:
        status = "for sale" if self.for_sale else "sold"
        return f"{self.year} {self.color} {self.model} - {self.age(current_year)} years old - {status}"


# Create a list of cars for our dealership inventory.
inventory = [
    Car("Toyota Camry",  2020, "blue",   True),
    Car("Honda Civic",   2018, "red",    True),
    Car("BMW X5",        2022, "black",  True),
    Car("Tesla Model 3", 2023, "white",  False),
    Car("Ford Mustang",  2021, "yellow", True),
]

CURRENT_YEAR = 2025


# ---------------------------------------------------------
# PART 1: SHOW ALL CARS
# ---------------------------------------------------------
print("=" * 55)
print("  WELCOME TO THE CAR DEALERSHIP")
print("=" * 55)

print("\n--- Full inventory ---")
for car in inventory:
    print(f"  {car.full_report(CURRENT_YEAR)}")


# ---------------------------------------------------------
# PART 2: TEST DRIVE EACH CAR
# ---------------------------------------------------------
print("\n--- Test driving every car ---")
for car in inventory:
    car.drive()
    car.stop()


# ---------------------------------------------------------
# PART 3: SELL A CAR
# ---------------------------------------------------------
print("\n--- Selling the first car ---")
inventory[0].mark_sold()
print(f"  Updated status: {inventory[0].full_report(CURRENT_YEAR)}")


# ---------------------------------------------------------
# PART 4: REPAINT A CAR
# ---------------------------------------------------------
print("\n--- Repainting the BMW ---")
inventory[2].repaint("silver")
print(f"  Updated report: {inventory[2].full_report(CURRENT_YEAR)}")


# ---------------------------------------------------------
# PART 5: SHOW ONLY CARS THAT ARE FOR SALE
# ---------------------------------------------------------
print("\n--- Cars currently for sale ---")
for car in inventory:
    if car.for_sale:
        print(f"  {car.full_report(CURRENT_YEAR)}")


# ---------------------------------------------------------
# PART 6: INTERACTIVE SEARCH (OPTIONAL)
# ---------------------------------------------------------
# Ask the user to pick a car number and test drive it.
# input() returns a string, so we convert it to int.

print("\n--- Interactive test drive ---")
print("Available cars:")
for index, car in enumerate(inventory, start=1):
    print(f"  {index}. {car.model}")

choice = input("Enter a car number to test drive it: ")

# Convert the user's choice to an integer and pick that car.
# We subtract 1 because list indexes start at 0.
car_number = int(choice)
selected_car = inventory[car_number - 1]

print("\nYou selected:")
selected_car.describe()
selected_car.drive()
selected_car.stop()


# ---------------------------------------------------------
# COMMON MISTAKES - Don't Fall For These!
# ---------------------------------------------------------
# These are the most common errors beginners make with OOP.
#
# Mistake 1: Forgetting self in a method
#    def drive():          <- missing self -> TypeError!
#    def drive(self):      <- correct
#
# Mistake 2: Using model instead of self.model
#    self.model = model    <- stores on object
#    model = model         <- local var, gone!
#
# Mistake 3: Calling __init__ yourself
#    car.__init__("Camry", 2020, "blue", True)  <- never do this!
#    car = Car("Camry", 2020, "blue", True)     <- correct
#
# Mistake 4: Lowercase class names
#    class car:         <- not convention
#    class Car:         <- correct (PascalCase)

print("\n--- Common mistakes to avoid ---")
print("1. Every method needs 'self' as its first parameter.")
print("2. Use 'self.model' to store on the object, not just 'model'.")
print("3. Never call __init__ yourself - Python does it automatically.")
print("4. Class names always use PascalCase: Car, BankAccount, Student.")


# ---------------------------------------------------------
# WHAT WE USED TODAY - Quick Recap
# ---------------------------------------------------------
# class      - defined a blueprint
# __init__   - constructor, sets up every object the same safe way
# self       - the specific object being used; connects attributes to it
# attributes - data stored on each object (self.model, self.year)
# methods    - functions belonging to the class (drive, describe)
# objects    - car1, car2, ... all independent instances
