# ---------------------------------------------------------
# DAY 9 | TOPIC 5: THE super() FUNCTION ⚡
# Call the parent class from inside a child class.
# ---------------------------------------------------------


# ─────────────────────────────────────────────────────────
# SECTION 1: PARENT CLASS
# ─────────────────────────────────────────────────────────
# Shape stores the color and whether it is filled.

class Shape:
    def __init__(self, color: str, is_filled: bool) -> None:
        self.color = color
        self.is_filled = is_filled

    def describe(self) -> None:
        status = "filled" if self.is_filled else "not filled"
        print(f"It is {self.color} and {status}")


# ─────────────────────────────────────────────────────────
# SECTION 2: CHILD CLASS USING super()
# ─────────────────────────────────────────────────────────
# Circle needs color, is_filled, AND a radius. Instead of
# writing self.color = color again, we call the parent's
# __init__ with super().__init__(...).

class Circle(Shape):
    def __init__(self, color: str, is_filled: bool, radius: float) -> None:
        # Let Shape handle color and is_filled
        super().__init__(color, is_filled)
        # Circle handles its own special data
        self.radius = radius

    def describe(self) -> None:
        # Circle adds extra info about itself
        area = 3.14 * self.radius ** 2
        print(f"It is a circle with area {area} cm^2")
        # Then it calls the parent's describe() for the rest
        super().describe()


# ─────────────────────────────────────────────────────────
# SECTION 3: USING THE CLASSES
# ─────────────────────────────────────────────────────────
# super() keeps our code DRY: we do not repeat color/filled
# logic in every child class.

circle = Circle("red", True, 5.0)

print("--- Circle Description ---")
circle.describe()
