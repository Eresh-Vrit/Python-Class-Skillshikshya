# ---------------------------------------------------------
# SOLUTION 2: INHERITANCE 🐕🐈🐁
# A parent class and child classes that override a method.
# ---------------------------------------------------------

# Inheritance lets a child class reuse code from a parent class.
# The child class gets all attributes and methods from the parent.


class Animal:
    """Parent class representing any animal."""

    def __init__(self, name: str) -> None:
        self.name = name

    def speak(self) -> None:
        print("*silence*")


class Dog(Animal):
    """A dog is a type of animal."""

    def speak(self) -> None:
        print(f"{self.name} the Dog says: Woof!")


class Cat(Animal):
    """A cat is a type of animal."""

    def speak(self) -> None:
        print(f"{self.name} the Cat says: Meow!")


class Mouse(Animal):
    """A mouse is a type of animal."""

    def speak(self) -> None:
        print(f"{self.name} the Mouse says: Squeak!")


# Create one object of each child class.
dog = Dog("Buddy")
cat = Cat("Whiskers")
mouse = Mouse("Nibbles")


# Call the speak method on each object.
dog.speak()
cat.speak()
mouse.speak()


# BONUS: Use a list to show polymorphism-like behavior.
print()
animals = [dog, cat, mouse]
for animal in animals:
    animal.speak()
