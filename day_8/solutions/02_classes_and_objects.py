# ---------------------------------------------------------
# SOLUTION 2: CLASSES AND OBJECTS
# ---------------------------------------------------------


# EXERCISE 1: First class - Car.
# `pass` is a placeholder body so Python doesn't error on an empty class.
# We then attach attributes one-by-one to each object via dot notation.
class Car:
    pass


car1 = Car()
car1.model    = "Toyota Camry"
car1.year     = 2020
car1.color    = "blue"
car1.for_sale = True

car2 = Car()
car2.model    = "Honda Civic"
car2.year     = 2018
car2.color    = "red"
car2.for_sale = False

car3 = Car()
car3.model    = "BMW X5"
car3.year     = 2022
car3.color    = "black"
car3.for_sale = True

print("--- Exercise 1: Three cars ---")
for car in (car1, car2, car3):
    print(f"{car.model} ({car.year}) - {car.color} - For sale: {car.for_sale}")


# EXERCISE 2: type() and isinstance().
class Car:
    pass


car1 = Car()
car2 = Car()
car1.model = "Toyota Camry"
car2.model = "Honda Civic"

print("\n--- Exercise 2: type() checks ---")
print(type(car1))                  # -> <class '__main__.Car'>
print(type(car2))                  # -> <class '__main__.Car'>
print(isinstance(car1, Car))       # -> True
print(isinstance("hello", Car))    # -> False
print(car1 == car2)                # -> False (different objects)
print(car1 is car2)                # -> False (different memory addresses)


# EXERCISE 3: Create + modify a Car object.
class Car:
    pass


my_car = Car()
my_car.model    = "Tesla Model 3"
my_car.year     = 2023
my_car.color    = "white"
my_car.for_sale = True

print("\n--- Exercise 3: Create and modify ---")
print(f"{my_car.model} ({my_car.year}) - {my_car.color} - For sale: {my_car.for_sale}")

my_car.color = "silver"            # change the attribute on an existing object
print(f"{my_car.model} ({my_car.year}) - {my_car.color} - For sale: {my_car.for_sale}")


# EXERCISE 4: Mini dealership inventory.
class Car:
    pass


camry   = Car()
camry.model    = "Toyota Camry"
camry.year     = 2020
camry.color    = "blue"
camry.for_sale = True

civic   = Car()
civic.model    = "Honda Civic"
civic.year     = 2018
civic.color    = "red"
civic.for_sale = False

x5      = Car()
x5.model    = "BMW X5"
x5.year     = 2022
x5.color    = "black"
x5.for_sale = True

mustang = Car()
mustang.model    = "Ford Mustang"
mustang.year     = 2021
mustang.color    = "yellow"
mustang.for_sale = True

inventory = [camry, civic, x5, mustang]

print("\n--- Exercise 4: Mini inventory ---")
for car in inventory:
    print(f"{car.model} ({car.year}) - {car.color} - For sale: {car.for_sale}")
