# ---------------------------------------------------------
# HOMEWORK 4: ABSTRACT CLASSES 🚗🏍️🚤
# Practice classes that force child classes to implement methods.
# ---------------------------------------------------------

# An abstract class cannot be used directly.
# It defines methods that every child class MUST implement.


# TODO: Import `ABC` and `abstractmethod` from the `abc` module.
from abc import ABC, abstractmethod


# TODO: Create an abstract class `Vehicle` that inherits from `ABC`.
# It should have two abstract methods:
#   - `go` with no body (just `pass`)
#   - `stop` with no body (just `pass`)

class Vehicle(ABC):
    pass  # Replace with your code


# TODO: Create a class `Car` that inherits from `Vehicle`.
# Implement go() to print "You drive the car."
# Implement stop() to print "The car stops."




# TODO: Create a class `Motorcycle` that inherits from `Vehicle`.
# Implement go() to print "You ride the motorcycle."
# Implement stop() to print "The motorcycle stops."




# TODO: Create a class `Boat` that inherits from `Vehicle`.
# Implement go() to print "You sail the boat."
# Implement stop() to print "The boat anchors."




# TODO: Create one object of Car, Motorcycle, and Boat.




# TODO: Call go() and stop() on each vehicle.




# BONUS: Try to create a `Vehicle` object directly.
# What error do you get? Why?
