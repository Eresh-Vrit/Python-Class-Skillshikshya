# ---------------------------------------------------------
# SOLUTION 8: GRADE CALCULATOR 🎓
# ---------------------------------------------------------


# TASK 1: Build Your Own Grade Calculator
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


# TASK 2: Temperature Warning System
temp = int(input("Current temperature: "))
if temp > 40:
    print("Extreme heat! Stay inside! [hot]")
elif temp > 30:
    print("It's hot. Drink water! [sun]")
elif temp > 20:
    print("Nice weather. :)")
elif temp > 10:
    print("A bit chilly. [coat]")
else:
    print("Freezing! [snow]")


# TASK 3: Simple Login System
username = input("Username: ")
password = input("Password: ")

if username == "admin" and password == "1234":
    print("Welcome, admin! :D")
elif username == "admin":
    print("Wrong password.")
else:
    print("Unknown user.")


# ⭐ BONUS CHALLENGE: Leap Year
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year! [?][?]")
else:
    print(f"{year} is NOT a leap year.")
