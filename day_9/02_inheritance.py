# ---------------------------------------------------------
# DAY 9 | TOPIC 2: INHERITANCE 🧬
# A child class gets the attributes and methods of its parent.
# ---------------------------------------------------------


# ─────────────────────────────────────────────────────────
# SECTION 1: THE PARENT CLASS
# ─────────────────────────────────────────────────────────
# Animal is the parent (or base) class. It stores data and
# behavior that many animals have in common.

class Animal:
    def __init__(self, name: str) -> None:
        self.name = name
        self.is_alive = True

    def eat(self) -> None:
        print(f"{self.name} is eating")

    def sleep(self) -> None:
        print(f"{self.name} is sleeping")


# ─────────────────────────────────────────────────────────
# SECTION 2: CHILD CLASSES
# ─────────────────────────────────────────────────────────
# Dog, Cat, and Mouse inherit from Animal by putting Animal
# inside the parentheses. They automatically get __init__,
# eat(), and sleep(). Each child adds its own special sound.

class Dog(Animal):
    def speak(self) -> None:
        print("Woof!")


class Cat(Animal):
    def speak(self) -> None:
        print("Meow!")


class Mouse(Animal):
    def speak(self) -> None:
        print("Squeak!")


# ─────────────────────────────────────────────────────────
# SECTION 3: USING INHERITED METHODS
# ─────────────────────────────────────────────────────────
# Each animal can use methods from Animal AND its own class.

dog = Dog("Buddy")
cat = Cat("Whiskers")
mouse = Mouse("Squeaky")

print("--- Dog ---")
print(dog.name)
print(dog.is_alive)
dog.eat()
dog.sleep()
dog.speak()

print("--- Cat ---")
print(cat.name)
cat.eat()
cat.speak()

print("--- Mouse ---")
print(mouse.name)
mouse.sleep()
mouse.speak()
