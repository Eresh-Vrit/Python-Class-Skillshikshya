# ---------------------------------------------------------
# DAY 4 | TOPIC 8: GRADE CALCULATOR 🎓
# Putting if, elif, else, and logical operators together!
# ---------------------------------------------------------


# 1. THE COMPLETE GRADE CALCULATOR
# This program uses everything we learned today:
#   - int(input()) to read numbers
#   - or to check if a value is invalid
#   - elif chain for multiple grade bands
#   - f-strings for personalised output

name = input("Student name: ")
score = int(input("Score (0[?]100): "))

if score < 0 or score > 100:
    print("Invalid score!")
elif score >= 90:
    print(f"{name}: A [?] Distinction! *")
elif score >= 80:
    print(f"{name}: B [?] Well done! OK")
elif score >= 70:
    print(f"{name}: C [?] Good effort.")
elif score >= 60:
    print(f"{name}: D [?] Passing.")
else:
    print(f"{name}: F [?] Study harder! [books]")


# 2. HOW IT WORKS
# Python checks each condition from TOP to BOTTOM.
# As soon as one is True, it runs that block and skips the rest.
# The 'or' catches scores that are outside the valid 0–100 range.
# The 'else' catches anything below 60.


# 3. TRY CHANGING THE INPUT
# What happens if score is 100? → A
# What happens if score is -5?  → "Invalid score!"
# What happens if score is 59?  → F
