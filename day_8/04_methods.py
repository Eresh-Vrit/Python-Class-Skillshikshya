# ---------------------------------------------------------
# DAY 8 | TOPIC 4: METHODS
# Methods are functions defined INSIDE a class.
# They define what an object CAN DO.
# ---------------------------------------------------------


# ---------------------------------------------------------
# SECTION 1: WHAT IS A METHOD?
# ---------------------------------------------------------
# A method is just a function defined inside a class.
# The difference from a regular function:
#   - It takes `self` as its first parameter (always!)
#   - You call it using dot notation:  object.method()
#
#   ATTRIBUTES  = what the object KNOWS   (data)
#   METHODS     = what the object CAN DO  (behaviour)

class Car:
    def __init__(self, model: str, year: int, color: str, for_sale: bool = False) -> None:
        self.model    = model
        self.year     = year
        self.color    = color
        self.for_sale = for_sale

    def drive(self) -> None:                 # <- method: no extra parameters
        print(f"You drive the {self.color} {self.model}")

    def stop(self) -> None:                  # <- method: no extra parameters
        print(f"You stop the {self.color} {self.model}")

    def describe(self) -> None:              # <- method: uses self attributes
        print(f"{self.year} {self.color} {self.model}")


car1 = Car("Toyota Camry", 2020, "blue",  True)
car2 = Car("Honda Civic",  2018, "red",   False)
car3 = Car("BMW X5",       2022, "black", True)

print("--- Calling methods ---")
car1.drive()       # You drive the blue Toyota Camry
car1.stop()        # You stop the blue Toyota Camry
car2.describe()    # 2018 red Honda Civic

# When car1.drive() runs:  self = car1, so self.color = "blue", self.model = "Toyota Camry"
# When car2.describe() runs: self = car2, so self.year = 2018, ...
# The SAME method produces different output for different objects!


# ---------------------------------------------------------
# SECTION 2: METHODS THAT MODIFY ATTRIBUTES
# ---------------------------------------------------------
# Methods can READ and CHANGE the object's own attributes (via self).
# This is how objects manage their own state.

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

    def mark_sold(self) -> None:
        self.for_sale = False
        print(f"  The {self.model} has been marked as sold.")

    def repaint(self, new_color: str) -> None:
        old_color = self.color
        self.color = new_color
        print(f"  The {self.model} was repainted from {old_color} to {new_color}.")


car4 = Car("Ford Mustang", 2021, "yellow", True)
print("\n--- Methods that modify attributes ---")
car4.describe()
car4.repaint("black")
car4.describe()
car4.mark_sold()
print(f"  For sale: {car4.for_sale}")


# ---------------------------------------------------------
# SECTION 3: METHODS THAT RETURN VALUES
# ---------------------------------------------------------
# Methods can return values just like regular functions.
# Use return when you want to USE the result somewhere else.

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

    def price_tag(self) -> str:
        status = "for sale" if self.for_sale else "not for sale"
        return f"{self.year} {self.color} {self.model} ({status})"


car5 = Car("Tesla Model 3", 2023, "white", True)
car6 = Car("Audi A4",       2019, "grey",  False)

print("\n--- Methods returning values ---")
print(f"{car5.model} is {car5.age(2025)} years old.")
print(f"{car6.model} is {car6.age(2025)} years old.")
print(car5.price_tag())
print(car6.price_tag())

# Use the returned value in another expression:
total_age = car5.age(2025) + car6.age(2025)
print(f"Combined age of both cars: {total_age} years")


# ---------------------------------------------------------
# SECTION 4: METHODS CALLING OTHER METHODS
# ---------------------------------------------------------
# A method can call another method on the same object using self.

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

    def full_report(self, current_year: int) -> None:
        car_age = self.age(current_year)     # <- calling another method via self
        print(f"  {self.model} is a {self.color} {self.year} model.")
        print(f"  Age: {car_age} years. For sale: {self.for_sale}")


car7 = Car("Nissan Altima",  2017, "white", True)
car8 = Car("Hyundai Sonata", 2024, "blue",  False)

print("\n--- Methods calling other methods ---")
car7.full_report(2025)
car8.full_report(2025)


# ---------------------------------------------------------
# SECTION 5: MANY OBJECTS - INDEPENDENT STATE
# ---------------------------------------------------------
# Each object keeps its OWN state.
# Calling a method on one object does NOT affect others.

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

    def repaint(self, new_color: str) -> None:
        self.color = new_color
        print(f"  The {self.model} is now {new_color}.")


car9  = Car("Toyota Camry", 2020, "blue",  True)
car10 = Car("Honda Civic",  2018, "red",   False)

print("\n--- Independent state ---")
car9.repaint("green")     # only car9 changes color
car10.drive()             # only car10 is affected here

print(f"\ncar9  color: {car9.color}")
print(f"car10 color: {car10.color}")
