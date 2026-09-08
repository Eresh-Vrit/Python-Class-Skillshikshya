# ---------------------------------------------------------
# DAY 7 | TOPIC 2: *args — Accept Any Number of Values ✳️
# What if you don't know how many arguments you'll get?
# ---------------------------------------------------------


# ─────────────────────────────────────────────────────────
# SECTION 1: THE PROBLEM — UNKNOWN NUMBER OF ARGUMENTS
# ─────────────────────────────────────────────────────────
# Imagine writing a function to add numbers.
# How many numbers will the caller pass? 2? 5? 100?

def add_two(a, b):
    return a + b

def add_three(a, b, c):
    return a + b + c

# This doesn't scale. We'd need a new function for every count.
# We need a better way!


# ─────────────────────────────────────────────────────────
# SECTION 2: INTRODUCING *args
# ─────────────────────────────────────────────────────────
# Put a * in front of a parameter name. Python then collects
# ALL the values you pass into a TUPLE that you can loop over.
# The name 'args' is just a habit — the * is what matters.

def add_all(*numbers):
    total = 0
    for n in numbers:        # numbers is a tuple — loop through it
        total = total + n
    return total

print("--- *args in action ---")
print(add_all(1, 2))               # 3
print(add_all(1, 2, 3))            # 6
print(add_all(10, 20, 30, 40))     # 100


# ─────────────────────────────────────────────────────────
# SECTION 3: WHAT IS *args EXACTLY?
# ─────────────────────────────────────────────────────────
# Inside the function it is just a TUPLE of everything passed.
# So you can print it, loop it, or count it with len().

def show(*items):
    print(f"Values: {items}")     # a tuple
    print(f"Count:  {len(items)}")

print("\n--- Looking at *args ---")
show("apple", "banana", "cherry")
# Values: ('apple', 'banana', 'cherry')
# Count:  3


# ─────────────────────────────────────────────────────────
# SECTION 4: A NORMAL PARAMETER CAN COME FIRST
# ─────────────────────────────────────────────────────────
# You can have a regular parameter BEFORE *args.
# The regular one fills first, then *args catches the rest.

def greet_all(greeting, *names):
    for name in names:
        print(f"{greeting}, {name}!")

print("\n--- Regular parameter + *args ---")
greet_all("Hello", "Alice", "Bob", "Charlie")
greet_all("Hey", "Zoe")
# 'greeting' gets "Hello", *names gets ("Alice", "Bob", "Charlie")
