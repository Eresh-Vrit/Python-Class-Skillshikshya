# ---------------------------------------------------------
# SOLUTION 4: BOOLEANS ✅
# ---------------------------------------------------------


# TASK 1: Boolean variables — only two possible values: True or False.
do_you_like_music = True
do_you_have_a_pet = False
do_you_like_mornings = True
do_you_drink_coffee = True

print(f"Do I like music?      {do_you_like_music}")
print(f"Do I have a pet?      {do_you_have_a_pet}")
print(f"Do I like mornings?   {do_you_like_mornings}")
print(f"Do I drink coffee?    {do_you_drink_coffee}")


# TASK 2: Comparison operators — each one returns True or False.
age = 18
print(age == 18)   # True   (== means "is equal to")
print(age > 20)    # False  (18 is not greater than 20)
print(age < 21)    # True
print(age != 15)   # True   (!= means "is not equal to")
print(age >= 18)   # True   (>= means "greater than or equal to")


# TASK 3: More Comparisons
a = 7
b = 14
print(a == b)   # False
print(a != b)   # True
print(a > b)    # False
print(a <= b)   # True


# TASK 4: Real-World Comparison
rider_age = 10
print(rider_age >= 12)   # False — too young!


# ⭐ BONUS CHALLENGE: a comparison directly inside print().
score = int(input("Enter your exam score (0[?]100): "))
print(score >= 40)
