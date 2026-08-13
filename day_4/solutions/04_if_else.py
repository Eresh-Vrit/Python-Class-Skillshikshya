# ---------------------------------------------------------
# SOLUTION 4: IF / ELSE — Making Decisions 🔀
# ---------------------------------------------------------


# TASK 1: Password Checker
password = input("Enter password: ")
if password == "secret":
    print("[unlock] Welcome!")
else:
    print("[NO] Access denied!")


# TASK 2: Even or Odd
number = int(input("Enter a whole number: "))
if number % 2 == 0:
    print(f"{number} is EVEN")
else:
    print(f"{number} is ODD")


# TASK 3: Score Pass / Fail
score = 55
if score >= 60:
    print("You passed! :D")
else:
    print("You failed. Study harder! [books]")
print("Exam finished.")


# ⭐ BONUS CHALLENGE: Movie age check
age = int(input("Enter your age: "))
if age >= 13:
    print("You can watch this movie. [popcorn]")
else:
    print("This movie is rated 13+. [NO]")
