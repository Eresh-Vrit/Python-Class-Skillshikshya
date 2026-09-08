# ---------------------------------------------------------
# DAY 8 | HOMEWORK 4: METHODS
# Practice adding methods to the Car class.
# ---------------------------------------------------------


# ─────────────────────────────────────────────────────────
# EXERCISE 1: Add methods to the Car class
# ─────────────────────────────────────────────────────────
# Below is a Car class with only __init__. Add three methods:
#
#   drive(self) -> None
#       prints "You drive the COLOR MODEL"
#
#   stop(self) -> None
#       prints "You stop the COLOR MODEL"
#
#   describe(self) -> None
#       prints "YEAR COLOR MODEL"
#
# Then create 2 Car objects and call all three methods on each.

class Car:
    def __init__(self, model: str, year: int, color: str, for_sale: bool = False) -> None:
        self.model    = model
        self.year     = year
        self.color    = color
        self.for_sale = for_sale

    # TODO: def drive(self) -> None: ...
    # TODO: def stop(self) -> None: ...
    # TODO: def describe(self) -> None: ...

# TODO: Create two Car objects and test your methods


# ─────────────────────────────────────────────────────────
# EXERCISE 2: Add a custom method
# ─────────────────────────────────────────────────────────
# Add one NEW method of your own to the Car class.
# Ideas:
#   - mark_sold(self) -> None: sets for_sale to False and prints a message
#   - repaint(self, new_color: str) -> None: changes color and prints a message
#   - honk(self) -> None: prints a fun message
#
# Then create a Car object and call your custom method.

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

    # TODO: Add your custom method here

# TODO: Create a Car object and call your custom method


# ─────────────────────────────────────────────────────────
# EXERCISE 3: Method returning a value
# ─────────────────────────────────────────────────────────
# Add a method called 'age' to the Car class below.
#   age(self, current_year: int) -> int
#       returns current_year - self.year
#
# Create 2 cars and print each car's age using the current year 2025.

class Car:
    def __init__(self, model: str, year: int, color: str, for_sale: bool = False) -> None:
        self.model    = model
        self.year     = year
        self.color    = color
        self.for_sale = for_sale

    def describe(self) -> None:
        print(f"{self.year} {self.color} {self.model}")

    # TODO: def age(self, current_year: int) -> int: ...

# TODO: Create two cars and print their ages


# ─────────────────────────────────────────────────────────
# EXERCISE 4: Methods calling other methods
# ─────────────────────────────────────────────────────────
# Add a method called 'full_report' to the Car class below.
#   full_report(self, current_year: int) -> None
#       prints:
#           "MODEL is a COLOR YEAR model."
#           "Age: X years. For sale: True/False"
#       Use the age() method inside full_report() to calculate X.
#
# Create 2 cars and call full_report() on each.

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

    # TODO: def age(self, current_year: int) -> int: ...
    # TODO: def full_report(self, current_year: int) -> None: ...

# TODO: Create two cars and call full_report() on each
