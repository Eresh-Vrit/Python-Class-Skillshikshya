# ---------------------------------------------------------
# DAY 4 | TOPIC 2: TUPLES — Fixed Collections 📦
# Tuples are like lists, but they cannot be changed.
# Tuples are IMMUTABLE — once created, they stay the same.
# ---------------------------------------------------------


# 1. CREATING A TUPLE
print("--- Creating a tuple ---")
point = (10, 20)
colour = (255, 0, 128, 255)
days = ("Monday", "Tuesday", "Wednesday", "Tuesday")

print(point)
print(colour)
print(days)


# 2. ACCESSING ITEMS BY INDEX
print("\n--- Accessing items ---")
print(point[0])   # x coordinate
print(point[1])   # y coordinate
print(days[-1])   # last day


# 3. TUPLES ARE IMMUTABLE
print("\n--- Tuples cannot change ---")
# point[0] = 99   # This would crash! Tuples cannot be changed.
print("Tuples are immutable, so we cannot change point.")


# 4. TUPLE METHODS: index() and count()
print("\n--- Tuple methods ---")
print("Index of 'Tuesday':", days.index("Tuesday"))
print("Count of 'Tuesday':", days.count("Tuesday"))
print("Length of days:", len(days))


# 5. WHEN TO USE A TUPLE
print("\n--- Good tuple uses ---")
# Use tuples for data that should stay fixed:
# - screen coordinates (x, y)
# - RGB colours (255, 0, 0)
# - dates like (year, month, day)

birthday = (2009, 7, 15)
print(birthday)


# 6. LIST VS TUPLE
print("\n--- List vs Tuple ---")
print("List []  -> changeable, use when items will grow or change")
print("Tuple () -> fixed, use when values should never change")
