# ---------------------------------------------------------
# SOLUTION 6: NESTED LOOPS 🪆
# A loop inside a loop. The INNER loop runs in full every
# time the OUTER loop takes one step.
# ---------------------------------------------------------


# TASK 1: Days and Activities
for day in range(1, 3):              # 2 days
    print(f"Day {day}")
    for activity in range(1, 4):    # 3 activities each day
        print(f"  Activity {activity}")


# TASK 2: Small Times Table
print("\nTimes table:")
for a in range(1, 4):               # 1, 2, 3
    for b in range(1, 4):           # 1, 2, 3
        print(f"{a} x {b} = {a * b}")


# TASK 3: Star Triangle
print("\nStar triangle:")
for row in range(1, 6):             # rows 1..5
    for star in range(row):         # "row" number of stars
        print("*", end=" ")
    print()                         # next line
