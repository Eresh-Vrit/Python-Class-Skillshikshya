# ---------------------------------------------------------
# SOLUTION 2: TUPLES — Fixed Collections 📦
# ---------------------------------------------------------


# TASK 1
screen_size = (1920, 1080)
print("Width:", screen_size[0])
print("Height:", screen_size[1])


# TASK 2
days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "Monday", "Monday")
print("First day:", days[0])
print("Last day:", days[-1])
print("Count of Monday:", days.count("Monday"))
print("Index of Wednesday:", days.index("Wednesday"))


# TASK 3
# screen_size[1] = 800   # This would crash! Tuples cannot be changed.
print("Tuples are immutable, so we cannot change screen_size.")


# BONUS CHALLENGE
rgb = (34, 139, 34)
print("RGB colour:", rgb)
print("This tuple cannot be changed.")
print("Length:", len(rgb))
