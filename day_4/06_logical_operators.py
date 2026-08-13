# ---------------------------------------------------------
# DAY 4 | TOPIC 6: LOGICAL OPERATORS — and, or, not 🔗
# Combine multiple conditions into one!
# ---------------------------------------------------------


# 1. THE THREE LOGICAL OPERATORS
#
#   and  →  BOTH conditions must be True
#   or   →  AT LEAST ONE condition must be True
#   not  →  FLIPS True to False (and vice versa)


# 2. AND — both must be True
print("--- and ---")
age = 20
has_id = True

if age >= 18 and has_id:
    print("Welcome! You may enter. OK")
else:
    print("Entry denied. X")

# Try: age = 15, has_id = True  → denied (age fails)
# Try: age = 20, has_id = False → denied (id fails)
# Try: age = 20, has_id = True  → welcome!


# 3. OR — at least one must be True
print("\n--- or ---")
is_member = False
has_points = True

if is_member or has_points:
    print("You get a discount!")
else:
    print("No discount available.")


# 4. NOT — flips the boolean
print("\n--- not ---")
is_raining = False

if not is_raining:
    print("Great day for a walk! [sun]")
else:
    print("Stay inside [?] it's raining! [?][?]")

# 'not False' becomes True, so the first branch runs.


# 5. TRUTH TABLE — what does each operator produce?
print("\n--- Truth Table ---")
print(f"True  and True  = {True and True}")
print(f"True  and False = {True and False}")
print(f"False and True  = {False and True}")
print(f"False and False = {False and False}")
print(f"True  or  False = {True or False}")
print(f"False or  True  = {False or True}")
print(f"False or  False = {False or False}")
print(f"not True        = {not True}")
print(f"not False       = {not False}")

# and is strict — both must pass.
# or is generous — one is enough.
# not reverses the answer!
