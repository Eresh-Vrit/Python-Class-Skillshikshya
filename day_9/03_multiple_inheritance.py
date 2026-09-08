# ---------------------------------------------------------
# DAY 9 | TOPIC 3: MULTIPLE & MULTI-LEVEL INHERITANCE 🕸️
# One class can inherit from more than one parent.
# ---------------------------------------------------------


# ─────────────────────────────────────────────────────────
# SECTION 1: MULTI-LEVEL INHERITANCE
# ─────────────────────────────────────────────────────────
# A child class can have its own children. That is called
# multi-level inheritance. Rabbit and Hawk are grandchildren
# of Animal because they inherit from Prey/Predator, which
# inherit from Animal.

class Animal:
    def __init__(self, name: str) -> None:
        self.name = name

    def eat(self) -> None:
        print(f"{self.name} is eating")

    def sleep(self) -> None:
        print(f"{self.name} is sleeping")


class Prey(Animal):
    def flee(self) -> None:
        print(f"{self.name} is fleeing")


class Predator(Animal):
    def hunt(self) -> None:
        print(f"{self.name} is hunting")


# ─────────────────────────────────────────────────────────
# SECTION 2: MULTIPLE INHERITANCE
# ─────────────────────────────────────────────────────────
# Fish inherits from BOTH Prey and Predator. That means a
# Fish object can use methods from Animal, Prey, and Predator.

class Rabbit(Prey):
    pass


class Hawk(Predator):
    pass


class Fish(Prey, Predator):
    pass


# ─────────────────────────────────────────────────────────
# SECTION 3: TESTING THE HIERARCHY
# ─────────────────────────────────────────────────────────
# Each object can do what its parent classes can do.

rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Nemo")

print("--- Rabbit (Prey) ---")
print(rabbit.name)
rabbit.eat()
rabbit.flee()

print("--- Hawk (Predator) ---")
print(hawk.name)
hawk.sleep()
hawk.hunt()

print("--- Fish (Prey + Predator) ---")
print(fish.name)
fish.eat()
fish.flee()
fish.hunt()
