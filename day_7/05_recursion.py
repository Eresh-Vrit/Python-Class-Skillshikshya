# ---------------------------------------------------------
# DAY 7 | TOPIC 5: RECURSION 🔁
# A function that calls ITSELF — with a stopping condition!
# ---------------------------------------------------------


# ─────────────────────────────────────────────────────────
# SECTION 1: WHAT IS RECURSION?
# ─────────────────────────────────────────────────────────
# Recursion means a function calls ITSELF to solve a problem.
#
# Every recursive function needs TWO things:
#   1. BASE CASE   — the condition to STOP (otherwise it runs forever!)
#   2. RECURSIVE CASE — the function calls itself with a SMALLER input
#
# Think of it like Russian dolls: each doll contains a smaller one
# until you reach the tiniest one — that's the base case.

# Here is the SIMPLEST possible recursive function:

def countdown(n):
    if n == 0:           # BASE CASE — stop here!
        print("Go!")
        return
    print(n)
    countdown(n - 1)     # RECURSIVE CASE — call with a smaller n

print("--- Countdown ---")
countdown(5)


# ─────────────────────────────────────────────────────────
# SECTION 2: FACTORIAL — A CLASSIC EXAMPLE
# ─────────────────────────────────────────────────────────
# 5! = 5 × 4 × 3 × 2 × 1 = 120
#
# Notice the pattern:
#   5! = 5 × 4!
#   4! = 4 × 3!
#   ...
#   1! = 1         <- base case
#
# In words: factorial(n) = n × factorial(n - 1)

def factorial(n):
    if n == 1:                      # BASE CASE
        return 1
    return n * factorial(n - 1)    # RECURSIVE CASE

print("\n--- Factorial ---")
print(f"3! = {factorial(3)}")    # 6
print(f"5! = {factorial(5)}")    # 120


# ─────────────────────────────────────────────────────────
# SECTION 3: ADD UP NUMBERS FROM 1 TO N
# ─────────────────────────────────────────────────────────
# add_up(3) = 3 + 2 + 1 = 6
#
# The pattern:
#   add_up(3) = 3 + add_up(2)
#   add_up(2) = 2 + add_up(1)
#   add_up(1) = 1            <- base case

def add_up(n):
    if n == 1:                  # BASE CASE
        return 1
    return n + add_up(n - 1)   # this number + the sum of the smaller ones

print("\n--- Add up from 1 to n ---")
print(add_up(3))     # 6
print(add_up(5))     # 15


# add_up(5)
# │
# ├── 5 + add_up(4)
# │       │
# │       ├── 4 + add_up(3)
# │       │       │
# │       │       ├── 3 + add_up(2)
# │       │       │       │
# │       │       │       ├── 2 + add_up(1)
# │       │       │       │       │
# │       │       │       │       └── 1
# │       │       │       │
# │       │       │       └── 2 + 1 = 3
# │       │       │
# │       │       └── 3 + 3 = 6
# │       │
# │       └── 4 + 6 = 10
# │
# └── 5 + 10 = 15


# ─────────────────────────────────────────────────────────
# SECTION 4: THE GOLDEN RULE — ALWAYS HAVE A BASE CASE
# ─────────────────────────────────────────────────────────
# Without a base case, recursion never stops and Python raises:
#   RecursionError: maximum recursion depth exceeded
#
# Always ask yourself BEFORE writing recursive code:
#   "When should the function STOP calling itself?"

def power(base, exp):
    if exp == 0:              # BASE CASE: anything to the power 0 is 1
        return 1
    return base * power(base, exp - 1)

print("\n--- Power function ---")
print(f"2^3  = {power(2, 3)}")    # 8
print(f"3^4  = {power(3, 4)}")    # 81
