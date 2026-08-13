# ---------------------------------------------------------
# SOLUTION 7: TRUTHY & FALSY VALUES 💡
# ---------------------------------------------------------


# TASK 1: bool() Explorer
print(bool(0))        # False
print(bool(5))        # True
print(bool(""))       # False
print(bool("hi"))     # True
print(bool([]))       # False
print(bool([1]))      # True
print(bool(None))     # False


# TASK 2: Using if with a string
colour = input("Favourite colour: ")
if colour:
    print("Nice choice!")
else:
    print("No colour? :(")


# TASK 3: Using if with a number
number = int(input("Enter a number: "))
if number:
    print("You picked something!")
else:
    print("Zero is falsy in Python!")


# ⭐ BONUS CHALLENGE: age with default
age_input = input("Your age: ")
if age_input:
    age = int(age_input)
else:
    age = 0

if age >= 18:
    print("You are an adult.")
else:
    print("You are not an adult yet.")
