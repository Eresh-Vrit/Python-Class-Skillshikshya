# ---------------------------------------------------------
# DAY 7 | TOPIC 3: **kwargs — Accept Any Number of Named Values 🗝️
# Like *args, but for named (keyword) arguments!
# ---------------------------------------------------------


# ─────────────────────────────────────────────────────────
# SECTION 1: WHAT IS **kwargs?
# ─────────────────────────────────────────────────────────
# *args collects plain values into a TUPLE.
# **kwargs collects NAMED values (like name="Alice") into a
# DICTIONARY. Two stars instead of one.

def show_profile(**info): 
    print(f"Values: {info}")      # a dictionary

print("--- **kwargs is a dictionary ---")
show_profile(name="Alice", age=30, city="Paris")
# Values: {'name': 'Alice', 'age': 30, 'city': 'Paris'}


# ─────────────────────────────────────────────────────────
# SECTION 2: LOOPING THROUGH **kwargs
# ─────────────────────────────────────────────────────────
# Since it is a dictionary, you loop through it with .items().

def print_info(**info):
    for key, value in info.items():
        print(f"  {key}: {value}")

print("\n--- Looping through kwargs ---")
print("Product details:")
print_info(name="Laptop", brand="TechCo", price=999)


# ─────────────────────────────────────────────────────────
# SECTION 3: A NORMAL PARAMETER CAN COME FIRST
# ─────────────────────────────────────────────────────────
# Just like with *args, a regular parameter can come before
# **kwargs. The named extras land in the dictionary.

def introduce(name, **extra):
    print(f"Hi, I'm {name}.")
    for key, value in extra.items():
        print(f"My {key} is {value}.")

print("\n--- Regular parameter + **kwargs ---")
introduce("Bob", age=25, job="developer", hobby="chess")


# ─────────────────────────────────────────────────────────
# SECTION 4: *args AND **kwargs TOGETHER
# ─────────────────────────────────────────────────────────
# You can use both. The order MUST be:
#   1. regular parameters
#   2. *args   (plain values)
#   3. **kwargs (named values)

def make_order(table, *items, **options):
    print(f"\nTable {table}:")
    for item in items:
        print(f"  - {item}")
    for key, value in options.items():
        print(f"  {key}: {value}")

print("\n--- *args + **kwargs together ---")
make_order(5, "pizza", "salad", "juice",
           payment="card", notes="window seat")
