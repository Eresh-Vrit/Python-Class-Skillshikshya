# ---------------------------------------------------------
# SOLUTION 1: WHAT IS OOP?
# ---------------------------------------------------------


# EXERCISE 1: Add a third car using the same pattern.
# Notice how messy this is - that's the WHOLE point. OOP solves it!
car1_model    = "Toyota Camry"
car1_year     = 2020
car1_color    = "blue"
car1_for_sale = True

car2_model    = "Honda Civic"
car2_year     = 2018
car2_color    = "red"
car2_for_sale = False

car3_model    = "BMW X5"
car3_year     = 2022
car3_color    = "black"
car3_for_sale = True

print(f"{car1_model} ({car1_year}) - {car1_color} - For sale: {car1_for_sale}")
print(f"{car2_model} ({car2_year}) - {car2_color} - For sale: {car2_for_sale}")
print(f"{car3_model} ({car3_year}) - {car3_color} - For sale: {car3_for_sale}")


# EXERCISE 2: Match the vocabulary.
class Car:
    def __init__(self, model: str, year: int, color: str, for_sale: bool) -> None:
        self.model    = model
        self.year     = year
        self.color    = color
        self.for_sale = for_sale

    def describe(self) -> None:
        print(f"{self.year} {self.color} {self.model}")


my_car = Car("Toyota Camry", 2020, "red", True)
my_car.describe()

print("Car is a       : class")      # Car is a class (a blueprint)
print("my_car is an   : object")     # my_car is an object (an instance of Car)
print("my_car.model   : attribute")  # data stored on the object
print("my_car.describe(): method")   # a function that belongs to the class


# EXERCISE 3: Garage class skeleton.
# Attributes a Garage might have:
# 1. name (e.g. "Downtown Motors")
# 2. cars (a list of Car objects)
# 3. capacity (how many cars it can hold)

# Methods a Garage might have:
# 1. add_car(car)
# 2. show_inventory()

class Garage:
    pass


# EXERCISE 4: True or False.
# a) A class is a blueprint, objects are built from it.           -> True
# b) You can only create ONE object from a class.                 -> False (many!)
# c) Attributes store data; methods define behaviour.             -> True
# d) OOP helps keep related data bundled together.                -> True
# e) You must write a new class every time you need a new object. -> False (re-use!)
