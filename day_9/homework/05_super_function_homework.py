# ---------------------------------------------------------
# HOMEWORK 5: THE super() FUNCTION 🔺🔵■
# Practice calling parent class methods from child classes.
# ---------------------------------------------------------

# `super()` lets a child class use methods from its parent class.
# It is very useful in __init__ so the parent sets shared attributes.


# TODO: Create a class `Shape` with these attributes:
#   - `color` (a string)
#   - `is_filled` (a boolean)
# Add a method `describe` that prints:
#   "It is <color> and filled=<is_filled>"

class Shape:
    pass  # Replace with your code


# TODO: Create a class `Circle` that inherits from `Shape`.
# It should:
#   - Accept `color`, `is_filled`, and `radius`.
#   - Use super().__init__ to set color and is_filled.
#   - Add an `area` method that returns 3.14 * radius * radius.
#   - Override `describe` to print "This is a circle." then call super().describe().




# TODO: Create a class `Square` that inherits from `Shape`.
# It should:
#   - Accept `color`, `is_filled`, and `side`.
#   - Use super().__init__ to set color and is_filled.
#   - Add an `area` method that returns side * side.
#   - Override `describe` to print "This is a square." then call super().describe().




# TODO: Create a class `Triangle` that inherits from `Shape`.
# It should:
#   - Accept `color`, `is_filled`, `base`, and `height`.
#   - Use super().__init__ to set color and is_filled.
#   - Add an `area` method that returns 0.5 * base * height.
#   - Override `describe` to print "This is a triangle." then call super().describe().




# TODO: Create one Circle, one Square, and one Triangle object.




# TODO: Call describe() and print the area for each shape.




# BONUS: Add a method `get_info` in Shape that returns a string.
# Call it from one of the child classes using super().
