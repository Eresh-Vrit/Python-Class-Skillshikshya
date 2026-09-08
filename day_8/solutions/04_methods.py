# ---------------------------------------------------------
# SOLUTION 4: METHODS
# ---------------------------------------------------------
# A method is just a function defined INSIDE a class.
# Its first parameter is always `self` (the object it's called on).


# EXERCISE 1: Add drive, stop, and describe to Car.
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


print("--- Exercise 1: Basic methods ---")
car1 = Car("Toyota Camry", 2020, "blue", True)
car2 = Car("Honda Civic", 2018, "red", False)

car1.drive()
car1.stop()
car1.describe()
print()
car2.drive()
car2.stop()
car2.describe()


# EXERCISE 2: Add a custom method.
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
        print(f"The {self.model} has been marked as sold.")

    def repaint(self, new_color: str) -> None:
        old_color = self.color
        self.color = new_color
        print(f"The {self.model} was repainted from {old_color} to {new_color}.")


print("\n--- Exercise 2: Custom method ---")
my_car = Car("Ford Mustang", 2021, "yellow", True)
my_car.describe()
my_car.repaint("black")
my_car.describe()
my_car.mark_sold()
print(f"For sale: {my_car.for_sale}")


# EXERCISE 3: Method returning a value.
class Car:
    def __init__(self, model: str, year: int, color: str, for_sale: bool = False) -> None:
        self.model    = model
        self.year     = year
        self.color    = color
        self.for_sale = for_sale

    def describe(self) -> None:
        print(f"{self.year} {self.color} {self.model}")

    def age(self, current_year: int) -> int:
        return current_year - self.year


print("\n--- Exercise 3: Method returning a value ---")
car3 = Car("Tesla Model 3", 2023, "white", True)
car4 = Car("Audi A4", 2019, "grey", False)

print(f"{car3.model} is {car3.age(2025)} years old.")
print(f"{car4.model} is {car4.age(2025)} years old.")


# EXERCISE 4: Methods calling other methods.
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
        print(f"{self.model} is a {self.color} {self.year} model.")
        print(f"  Age: {car_age} years. For sale: {self.for_sale}")


print("\n--- Exercise 4: Methods calling methods ---")
car5 = Car("Nissan Altima", 2017, "white", True)
car6 = Car("Hyundai Sonata", 2024, "blue", False)

car5.full_report(2025)
print()
car6.full_report(2025)
