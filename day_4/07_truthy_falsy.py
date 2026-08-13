# ---------------------------------------------------------
# DAY 4 | TOPIC 7: TRUTHY & FALSY VALUES 💡
# Python treats some values as True/False automatically!
# ---------------------------------------------------------


# 1. THE bool() FUNCTION
# bool() tells you whether Python sees a value as True or False.

print("--- Falsy values ---")
print(bool(0))        # False — zero
print(bool(""))       # False — empty string
print(bool([]))       # False — empty list
print(bool(None))     # False — no value at all

print("\n--- Truthy values ---")
print(bool(1))        # True — any non-zero number
print(bool("hello"))  # True — non-empty string
print(bool([1, 2]))   # True — non-empty list
print(bool(True))     # True — obviously!


# 2. USING TRUTHINESS IN if STATEMENTS
# You don't always need '== True' — Python checks truthiness directly!

print("\n--- if name: ---")
name = input("Your name: ")

if name:
    print(f"Hello, {name}!")
else:
    print("You didn't type anything!")

# If the user presses Enter without typing, name is "" (empty string).
# Empty string is FALSY, so the else block runs!
