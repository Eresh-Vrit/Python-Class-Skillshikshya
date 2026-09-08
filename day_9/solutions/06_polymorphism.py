# ---------------------------------------------------------
# SOLUTION 6: POLYMORPHISM 🍕🔺🔵■
# Many classes sharing the same method name.
# ---------------------------------------------------------

# Polymorphism means "many forms".
# Different objects can respond to the same method call in their own way.


class Shape:
    """Base shape with a default area of 0."""

    def area(self) -> float:
        return 0


class Circle(Shape):
    """A circle calculates area from its radius."""

    def __init__(self, radius: float) -> None:
        self.radius = radius

    def area(self) -> float:
        return 3.14 * self.radius * self.radius


class Square(Shape):
    """A square calculates area from its side length."""

    def __init__(self, side: float) -> None:
        self.side = side

    def area(self) -> float:
        return self.side * self.side


class Triangle(Shape):
    """A triangle calculates area from base and height."""

    def __init__(self, base: float, height: float) -> None:
        self.base = base
        self.height = height

    def area(self) -> float:
        return 0.5 * self.base * self.height


class Pizza:
    """A pizza is not a shape, but it also has an area."""

    def __init__(self, radius: float) -> None:
        self.radius = radius

    def area(self) -> float:
        return 3.14 * self.radius * self.radius


# Create a list of different objects that all have an area() method.
shapes = [
    Circle(5.0),
    Square(4.0),
    Triangle(6.0, 3.0),
    Pizza(8.0),
]


# Loop through and call area() on each object.
for shape in shapes:
    print(f"Area: {shape.area()}")


# BONUS: A function that works with any object that has an area() method.
def print_area(shape) -> None:
    print(f"This shape has an area of {shape.area()}")


print()
for shape in shapes:
    print_area(shape)
