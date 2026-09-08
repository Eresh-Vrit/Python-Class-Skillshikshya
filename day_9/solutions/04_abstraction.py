# ---------------------------------------------------------
# SOLUTION 4: ABSTRACT CLASSES 🚗🏍️🚤
# Classes that force child classes to implement methods.
# ---------------------------------------------------------

# An abstract class cannot be used directly.
# It defines methods that every child class MUST implement.


from abc import ABC, abstractmethod


class Vehicle(ABC):
    """Abstract base class for all vehicles."""

    @abstractmethod
    def go(self) -> None:
        pass

    @abstractmethod
    def stop(self) -> None:
        pass


class Car(Vehicle):
    """A car is a vehicle you drive."""

    def go(self) -> None:
        print("You drive the car.")

    def stop(self) -> None:
        print("The car stops.")


class Motorcycle(Vehicle):
    """A motorcycle is a vehicle you ride."""

    def go(self) -> None:
        print("You ride the motorcycle.")

    def stop(self) -> None:
        print("The motorcycle stops.")


class Boat(Vehicle):
    """A boat is a vehicle you sail."""

    def go(self) -> None:
        print("You sail the boat.")

    def stop(self) -> None:
        print("The boat anchors.")


# Create vehicle objects.
car = Car()
motorcycle = Motorcycle()
boat = Boat()


# Call go() and stop() on each vehicle.
car.go()
car.stop()
print()

motorcycle.go()
motorcycle.stop()
print()

boat.go()
boat.stop()


# BONUS: You cannot create an object from an abstract class.
# vehicle = Vehicle()  # This would raise TypeError.
