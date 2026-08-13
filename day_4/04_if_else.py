# ---------------------------------------------------------
# DAY 4 | TOPIC 4: IF / ELSE — Making Decisions 🔀
# Python can choose what to do based on a condition!
# ---------------------------------------------------------


# 1. THE IF STATEMENT — only runs if the condition is True
print("--- Basic if ---")
age = 16

if age >= 18:
    print("You can vote! [?][?]")
else:
    print("Too young to vote.")

# The if block runs when True, else runs when False.
# Try changing age to 20 — the first path runs!


# 2. REAL EXAMPLE — Password Checker
print("\n--- Password Checker ---")
password = input("Enter password: ")

if password == "python123":
    print("OK Access granted!")
else:
    print("X Wrong password!")

# == compares two values. = assigns a value. Don't mix them up!


# 3. EVEN OR ODD
print("\n--- Even or Odd ---")
number = 7

if number % 2 == 0:
    print(f"{number} is EVEN")
else:
    print(f"{number} is ODD")

# % gives the remainder. 7 % 2 is 1, so it's odd.


# 4. SCORE PASS / FAIL
print("\n--- Score Pass/Fail ---")
score = 75

if score >= 60:
    print("You passed! :D")      # inside if — runs when score >= 60
    print("Well done!")          # still inside if — same indent level
else:
    print("You failed. :(")      # inside else

print("Exam is over.")           # NOT indented — always runs

# Python uses indentation (4 spaces) to know what is "inside" a block.
