# ---------------------------------------------------------
# SOLUTION 5: THE super() FUNCTION 🔺🔵■
# Calling parent class methods from child classes.
# ---------------------------------------------------------

# `super()` lets a child class use methods from its parent class.
# It is very useful in __init__ so the parent sets shared attributes.


class Shape:
    """Parent class for geometric shapes."""

    def __init__(self, color: str, is_filled: bool) -> None:
        self.color = color
        self.is_filled = is_filled

    def describe(self) -> None:
        print(f"It is {self.color} and filled={self.is_filled}")

    def get_info(self) -> str:
        return f"A {self.color} shape, filled={self.is_filled}"


class Circle(Shape):
    """A circle is a shape with a radius."""

    def __init__(self, color: str, is_filled: bool, radius: float) -> None:
        super().__init__(color, is_filled)
        self.radius = radius

    def area(self) -> float:
        return 3.14 * self.radius * self.radius

    def describe(self) -> None:
        print("This is a circle.")
        super().describe()


class Square(Shape):
    """A square is a shape with a side length."""

    def __init__(self, color: str, is_filled: bool, side: float) -> None:
        super().__init__(color, is_filled)
        self.side = side

    def area(self) -> float:
        return self.side * self.side

    def describe(self) -> None:
        print("This is a square.")
        super().describe()


class Triangle(Shape):
    """A triangle is a shape with a base and height."""

    def __init__(self, color: str, is_filled: bool, base: float, height: float) -> None:
        super().__init__(color, is_filled)
        self.base = base
        self.height = height

    def area(self) -> float:
        return 0.5 * self.base * self.height

    def describe(self) -> None:
        print("This is a triangle.")
        super().describe()


# Create objects.
circle = Circle("red", True, 5.0)
square = Square("blue", False, 4.0)
triangle = Triangle("green", True, 6.0, 3.0)


# Call describe() and print area for each shape.
circle.describe()
print(f"Area: {circle.area()}")
print()

square.describe()
print(f"Area: {square.area()}")
print()

triangle.describe()
print(f"Area: {triangle.area()}")
print()


# BONUS: Use a parent method from a child object.
print(circle.get_info())
