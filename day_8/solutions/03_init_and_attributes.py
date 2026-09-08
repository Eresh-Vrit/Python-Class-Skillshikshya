# ---------------------------------------------------------
# SOLUTION 3: __init__ AND ATTRIBUTES
# ---------------------------------------------------------
# __init__ runs AUTOMATICALLY when you create a new object.
# `self` refers to "this particular object" - that's how data sticks to it.


# EXERCISE 1: Car class with __init__.
class Car:
    def __init__(self, model: str, year: int, color: str, for_sale: bool) -> None:
        self.model    = model
        self.year     = year
        self.color    = color
        self.for_sale = for_sale


car1 = Car("Toyota Camry", 2020, "blue", True)
car2 = Car("Honda Civic", 2018, "red", False)
car3 = Car("BMW X5", 2022, "black", True)

print("--- Exercise 1: __init__ in action ---")
for car in (car1, car2, car3):
    print(f"{car.model} ({car.year}) - {car.color} - For sale: {car.for_sale}")


# EXERCISE 2: Default for_sale value.
class Car:
    def __init__(self, model: str, year: int, color: str, for_sale: bool = False) -> None:
        self.model    = model
        self.year     = year
        self.color    = color
        self.for_sale = for_sale


car1 = Car("Toyota Camry", 2020, "blue")
car2 = Car("Honda Civic", 2018, "red", True)
car3 = Car("BMW X5", 2022, "black", False)

print("\n--- Exercise 2: Default values ---")
for car in (car1, car2, car3):
    print(f"{car.model}: for sale = {car.for_sale}")


# EXERCISE 3: Computed attribute - age.
class Car:
    def __init__(self, model: str, year: int, color: str, for_sale: bool = False) -> None:
        self.model    = model
        self.year     = year
        self.color    = color
        self.for_sale = for_sale
        self.age      = 2025 - year


print("\n--- Exercise 3: Computed attributes ---")
for car in (Car("Toyota Camry", 2020, "blue"),
            Car("Honda Civic", 2018, "red"),
            Car("BMW X5", 2022, "black")):
    print(f"{car.model}: age = {car.age} years")


# EXERCISE 4: Understanding self.
class Car:
    def __init__(self, model: str, color: str = "white") -> None:
        self.model = model
        self.color = color


car1 = Car("Toyota Camry")
car2 = Car("Honda Civic", "red")
car3 = Car("BMW X5", "black")

car1.color = "silver"

print("\n--- Exercise 4: self in action ---")
print(car1.model, car1.color)   # -> Toyota Camry silver
print(car2.model, car2.color)   # -> Honda Civic red
print(car3.model, car3.color)   # -> BMW X5 black


# EXERCISE 5: Fuel level mini challenge.
class Car:
    def __init__(self, model: str, year: int, color: str, fuel_level: int = 100) -> None:
        self.model      = model
        self.year       = year
        self.color      = color
        self.fuel_level = fuel_level


print("\n--- Exercise 5: Fuel level ---")
car_a = Car("Toyota Camry", 2020, "blue", 85)
car_b = Car("Honda Civic", 2018, "red", 42)
car_c = Car("BMW X5", 2022, "black")

for car in (car_a, car_b, car_c):
    print(f"{car.model}: fuel level = {car.fuel_level}%")
