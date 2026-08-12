# ---------------------------------------------------------
# DAY 3 | TOPIC 4: BOOLEANS ✅
# Booleans are the simplest data type: only True or False!
# ---------------------------------------------------------


# 1. BOOLEAN VALUES
# A boolean can only be True or False. They power every decision your program makes!
is_raining = False
has_homework = True
is_python_fun = True
is_monday = False

print("Is it raining?     ", is_raining)
print("Is there homework? ", has_homework)
print("Is Python fun?     ", is_python_fun)
print("Is it Monday?      ", is_monday)


# 2. COMPARISON OPERATORS — these PRODUCE True or False
# == checks if two things are equal. = stores a value. Completely different!
x = 10
y = 20

print(f"\n--- Comparing {x} and {y} ---")
print(f"{x} == {y}  ->  {x == y}")    # equal to
print(f"{x} != {y}  ->  {x != y}")    # NOT equal to
print(f"{x} >  {y}  ->  {x > y}")     # greater than
print(f"{x} <  {y}  ->  {x < y}")     # less than
print(f"{x} >= {y}  ->  {x >= y}")    # greater than OR equal
print(f"{x} <= {y}  ->  {x <= y}")    # less than OR equal
