# ---------------------------------------------------------
# DAY 9 | TOPIC 4: ABSTRACTION 🚗
# Force child classes to implement specific methods.
# ---------------------------------------------------------


# ─────────────────────────────────────────────────────────
# SECTION 1: ABSTRACT PARENT CLASS
# ─────────────────────────────────────────────────────────
# Vehicle says: "Every vehicle MUST know how to go() and
# stop()." It does not provide the details itself; child
# classes must fill them in.

from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def go(self) -> None:
        pass

    @abstractmethod
    def stop(self) -> None:
        pass


# ─────────────────────────────────────────────────────────
# SECTION 2: CONCRETE VEHICLE CLASSES
# ─────────────────────────────────────────────────────────
# Each child class implements the required methods in its
# own way. If a class forgets one, Python raises an error.

class Car(Vehicle):
    def go(self) -> None:
        print("You drive the car")

    def stop(self) -> None:
        print("You stop the car")


class Motorcycle(Vehicle):
    def go(self) -> None:
        print("You ride the motorcycle")

    def stop(self) -> None:
        print("You stop the motorcycle")


class Boat(Vehicle):
    def go(self) -> None:
        print("You sail the boat")

    def stop(self) -> None:
        print("You anchor the boat")


# ─────────────────────────────────────────────────────────
# SECTION 3: USING ABSTRACT CLASSES
# ─────────────────────────────────────────────────────────
# You can treat all vehicles the same way, even though each
# one behaves differently.

car = Car()
motorcycle = Motorcycle()
boat = Boat()

vehicles = [car, motorcycle, boat]

print("--- Vehicles in Motion ---")
for vehicle in vehicles:
    vehicle.go()

print("--- Vehicles Stopping ---")
for vehicle in vehicles:
    vehicle.stop()

# You cannot create a Vehicle object directly:
# vehicle = Vehicle()  # This would raise TypeError!
