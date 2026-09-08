# ---------------------------------------------------------
# HOMEWORK 3: MULTIPLE & MULTI-LEVEL INHERITANCE 🦅🐇🐟
# Practice a class that inherits from more than one parent.
# ---------------------------------------------------------

# Multiple inheritance means a child class has two or more parents.
# Multi-level inheritance means a class inherits from a child class.


# TODO: Create a base class named `Animal`.
# It should have an `__init__` that accepts `name` and stores it.

class Animal:
    pass  # Replace with your code


# TODO: Create a class `Prey` that inherits from `Animal`.
# It should have a method `flee` that prints "<name> flees!".




# TODO: Create a class `Predator` that inherits from `Animal`.
# It should have a method `hunt` that prints "<name> is hunting!".




# TODO: Create a class `Rabbit` that inherits from `Prey`.
# Add a `speak` method that prints "<name> the Rabbit says: Squeak!".




# TODO: Create a class `Hawk` that inherits from `Predator`.
# Add a `speak` method that prints "<name> the Hawk says: Screech!".




# TODO: Create a class `Fish` that inherits from BOTH `Prey` and `Predator`.
# Add a `speak` method that prints "<name> the Fish says: Blub!".
# (Remember: class Fish(Prey, Predator) is multiple inheritance.)




# TODO: Create one object of Rabbit, Hawk, and Fish.




# TODO: Call flee(), hunt(), and speak() methods where they make sense.




# BONUS: Try changing the order to `class Fish(Predator, Prey):`.
# Does the output change? Why do you think that is?
