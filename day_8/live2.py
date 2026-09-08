#-------------------------
#Homework:2 Parameters
#-------------------------

#Task 1: Personalisted Greeting
def great_user(username):
    print(f"Hello, {username}! Great to see you today.")

great_user("Albert")
great_user("John")
great_user("Emma")

#Task 2: Rectangle Info
def describe_rectagle(width,height):
    area = width * height
    print(f"Width: {width}, Height: {height}, Area: {area}")

describe_rectagle(5, 3)
describe_rectagle(10, 2)
describe_rectagle(7, 7)

# Task 3: Temperature Checker
def check_temperature(temp):
    if temp > 37:
        print("Too hot!")
    elif temp < 36:
        print("Too cold!")
    else:
        print("Normal temperature.")
check_temperature(38)
check_temperature(35)
check_temperature(36.5)

# Bonus challenge
def print_stars(n):
    print("*"*n)

print_stars(1)
print_stars(3)
print_stars(5)
print_stars(7)