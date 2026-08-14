# ---------------------------------------------------------
# DAY 5 | TOPIC 6: NESTED LOOPS — A Loop Inside a Loop 🪆
# For every round of the OUTER loop, the INNER loop runs ALL the way.
# ---------------------------------------------------------


# ─────────────────────────────────────────────────────────
# SECTION 1: A REAL-LIFE PICTURE
# ─────────────────────────────────────────────────────────
# Imagine 3 days, and on EACH day you eat 2 meals.
# The "day" is the OUTER loop. The "meal" is the INNER loop.
# For every single day, you go through ALL the meals.

for day in range(1, 4):          # outer loop: day 1, 2, 3
    print(f"Day {day}:")
    for meal in range(1, 3):     # inner loop: meal 1, 2 (runs fully each day)
        print(f"  Meal {meal}")

# Output:
# Day 1:
#   Meal 1
#   Meal 2
# Day 2:
#   Meal 1
#   Meal 2
# Day 3:
#   Meal 1
#   Meal 2


# ─────────────────────────────────────────────────────────
# SECTION 2: A SIMPLE MULTIPLICATION TABLE
# ─────────────────────────────────────────────────────────
# Outer loop picks a row number. Inner loop multiplies it by 1, 2, 3.

print("\n--- Small Times Table ---")
for row in range(1, 4):              # rows 1, 2, 3
    for col in range(1, 4):          # columns 1, 2, 3
        print(f"{row} x {col} = {row * col}")
    print()                          # blank line after each row


# ─────────────────────────────────────────────────────────
# SECTION 3: A SIMPLE STAR TRIANGLE
# ─────────────────────────────────────────────────────────
# Row 1 gets 1 star, row 2 gets 2 stars, and so on.
# The inner loop count depends on the outer loop number!

print("\n--- Star Triangle ---")
for row in range(1, 5):              # rows 1, 2, 3, 4
    for star in range(row):          # print "row" number of stars
        print("*", end=" ")          # end=" " keeps stars on the same line
    print()                          # move to the next line

# Output:
# *
# * *
# * * *
# * * * *
