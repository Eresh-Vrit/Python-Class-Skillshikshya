# ---------------------------------------------------------
# DAY 4 | TOPIC 5: ELIF — Multiple Choices 🎛️
# elif lets you handle MORE than two possible cases!
# ---------------------------------------------------------


# 1. THE PROBLEM WITH ONLY IF/ELSE
# What if you have 3, 4, or 5 different cases?
# elif (else-if) adds more branches to your decision tree.

# 2. GRADE CALCULATOR — classic elif chain
print("--- Grade Calculator ---")
score = int(input("Enter your score (0[?]100): "))

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Your grade is: {grade}")

# Python checks each condition from TOP to BOTTOM.
# As soon as one is True, it runs that block and SKIPS the rest.


# 3. TRAFFIC LIGHT — another clean example
print("\n--- Traffic Light ---")
light = input("Traffic light colour (red/yellow/green): ").lower()

if light == "red":
    print("STOP! [STOP]")
elif light == "yellow":
    print("Get ready... [READY]")
elif light == "green":
    print("GO! [GO]")
else:
    print("Unknown colour [?] please check the light!")


# 4. SEASON CHECKER
print("\n--- Season Checker ---")
month = int(input("Enter month number (1[?]12): "))

if month in [12, 1, 2]:
    print("Winter [snow]")
elif month in [3, 4, 5]:
    print("Spring [spring]")
elif month in [6, 7, 8]:
    print("Summer [sun]")
elif month in [9, 10, 11]:
    print("Autumn [autumn]")
else:
    print("That's not a valid month number!")

# Using 'in' with a list is a clean way to check multiple values at once.
