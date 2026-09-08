# ---------------------------------------------------------
# SOLUTION 5: PUTTING IT ALL TOGETHER
# ---------------------------------------------------------


# EXERCISE 1: Complete Car class.
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
        print(f"The {self.model} has been marked as sold.")

    def repaint(self, new_color: str) -> None:
        old_color = self.color
        self.color = new_color
        print(f"The {self.model} was repainted from {old_color} to {new_color}.")


print("--- Exercise 1: Car class methods ---")
car1 = Car("Toyota Camry", 2020, "blue", True)
car1.drive()
car1.stop()
car1.describe()
print(f"Age: {car1.age(2025)} years")
car1.mark_sold()


# EXERCISE 2: Dealership inventory.
print("\n--- Exercise 2: Inventory ---")
inventory = [
    Car("Toyota Camry",  2020, "blue",   True),
    Car("Honda Civic",   2018, "red",    True),
    Car("BMW X5",        2022, "black",  True),
    Car("Tesla Model 3", 2023, "white",  False),
    Car("Ford Mustang",  2021, "yellow", True),
]

for car in inventory:
    car.describe()


# EXERCISE 3: Show only cars for sale.
print("\n--- Exercise 3: Cars for sale ---")
for car in inventory:
    if car.for_sale:
        car.describe()


# EXERCISE 4: Test drive every car.
print("\n--- Exercise 4: Test drive every car ---")
for car in inventory:
    car.drive()
    car.stop()


# EXERCISE 5: Sell and repaint.
print("\n--- Exercise 5: Sell and repaint ---")
inventory[0].mark_sold()
inventory[1].repaint("silver")

print("\nUpdated inventory:")
for car in inventory:
    car.describe()
    print(f"  For sale: {car.for_sale}")


# EXERCISE 6: Fixed mistakes.
print("\n--- Exercise 6: Fixed mistakes ---")
class Car:
    def __init__(self, model: str, year: int, color: str) -> None:
        self.model = model
        self.year  = year
        self.color = color

    def describe(self) -> None:
        print(f"{self.year} {self.color} {self.model}")


my_car = Car("Toyota Camry", 2020, "blue")
my_car.describe()
