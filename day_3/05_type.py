# ---------------------------------------------------------
# DAY 3 | TOPIC 5: type() — WHAT KIND OF DATA IS THIS? 🔍
# Use type() to discover exactly what data type you are working with.
# ---------------------------------------------------------


# 1. THE type() DETECTIVE
# Not sure what data type a value is? Just ask Python!
print(type("Hello"))     # <class 'str'>
print(type(42))          # <class 'int'>
print(type(3.14))        # <class 'float'>
print(type(True))        # <class 'bool'>


# 2. TYPE CHECKING WITH VARIABLES
# type() works on variables too — very useful when debugging!
age = 25
price = 9.99
name = "Alice"
is_happy = True

print(f"\nType of age:      {type(age)}")
print(f"Type of price:    {type(price)}")
print(f"Type of name:     {type(name)}")
print(f"Type of is_happy: {type(is_happy)}")


# 3. THE input() TRAP
# input() ALWAYS returns a string — even if the user types a number!
user_input = input("Enter a number: ")
print(f"\nYou entered: '{user_input}'")
print(f"Its type is: {type(user_input)}")   # <class 'str'> — always!


# 4. TYPE CONVERSION (a.k.a. "Casting")
# You can change a value from one type to another.
print("\n--- Type Conversion ---")
print(int("100"))       # str → int   : 100
print(float("3.14"))    # str → float : 3.14
print(str(42))          # int → str   : "42"

# The classic fix pattern:
age = int(input("Your age: "))
print(f"Next year you will be {age + 1} years old!")

# Use float() for decimal inputs:
price = float(input("Price: "))
print(f"With tax: {price * 1.13}")
