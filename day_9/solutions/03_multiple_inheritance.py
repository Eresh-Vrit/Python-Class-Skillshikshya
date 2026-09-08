# ---------------------------------------------------------
# SOLUTION 3: MULTIPLE & MULTI-LEVEL INHERITANCE 🦅🐇🐟
# A class that inherits from more than one parent class.
# ---------------------------------------------------------

# Multiple inheritance means a child class has two or more parents.
# Multi-level inheritance means a class inherits from a child class.


class Animal:
    """Base class for all animals."""

    def __init__(self, name: str) -> None:
        self.name = name


class Prey(Animal):
    """Animals that can be hunted."""

    def flee(self) -> None:
        print(f"{self.name} flees!")


class Predator(Animal):
    """Animals that hunt other animals."""

    def hunt(self) -> None:
        print(f"{self.name} is hunting!")


class Rabbit(Prey):
    """A rabbit is prey."""

    def speak(self) -> None:
        print(f"{self.name} the Rabbit says: Squeak!")


class Hawk(Predator):
    """A hawk is a predator."""

    def speak(self) -> None:
        print(f"{self.name} the Hawk says: Screech!")


class Fish(Prey, Predator):
    """A fish can be both prey and predator."""

    def speak(self) -> None:
        print(f"{self.name} the Fish says: Blub!")


# Create objects.
rabbit = Rabbit("Bunny")
hawk = Hawk("Talon")
fish = Fish("Goldie")


# Call methods.
rabbit.flee()
rabbit.speak()
print()

hawk.hunt()
hawk.speak()
print()

fish.flee()
fish.hunt()
fish.speak()


# BONUS: Method Resolution Order (MRO) decides which method runs first.
print()
print(Fish.__mro__)
