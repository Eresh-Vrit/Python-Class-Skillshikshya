# ---------------------------------------------------------
# DAY 9 | TOPIC 6: POLYMORPHISM 🎭
# Many shapes, one method name: each responds in its own way.
# ---------------------------------------------------------


# ─────────────────────────────────────────────────────────
# SECTION 1: ABSTRACT BASE CLASS
# ─────────────────────────────────────────────────────────
# Shape is abstract: you cannot make a plain Shape object.
# It only promises that every real shape knows how to find
# its own area().

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass


# ─────────────────────────────────────────────────────────
# SECTION 2: CONCRETE SHAPES
# ─────────────────────────────────────────────────────────
# Each child class implements area() in its own way. That is
# polymorphism: the same method call behaves differently
# depending on the object's actual class.

class Circle(Shape):
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def area(self) -> float:
        return 3.14 * self.radius ** 2


class Square(Shape):
    def __init__(self, side: float) -> None:
        self.side = side

    def area(self) -> float:
        return self.side ** 2


class Triangle(Shape):
    def __init__(self, base: float, height: float) -> None:
        self.base = base
        self.height = height

    def area(self) -> float:
        return 0.5 * self.base * self.height


# ─────────────────────────────────────────────────────────
# SECTION 3: INHERITANCE + POLYMORPHISM
# ─────────────────────────────────────────────────────────
# Pizza is a Circle with an extra topping. It reuses Circle's
# area() and adds its own behavior.

class Pizza(Circle):
    def __init__(self, topping: str, radius: float) -> None:
        super().__init__(radius)
        self.topping = topping

    def describe(self) -> None:
        print(f"This is a {self.topping} pizza with area {self.area()}")


# ─────────────────────────────────────────────────────────
# SECTION 4: POLYMORPHISM IN ACTION
# ─────────────────────────────────────────────────────────
# We store different shapes in one list. The same loop calls
# area() on each object, but each object runs its own version.

shapes = [Circle(4), Square(5), Triangle(6, 7), Pizza("pepperoni", 15)]

print("--- Areas of Different Shapes ---")
for shape in shapes:
    print(shape.area())

print("--- Pizza Description ---")
pizza = Pizza("pepperoni", 15)
pizza.describe()
