# ---------------------------------------------------------
# DAY 4 | TOPIC 3: DICTIONARIES — Key-Value Pairs 🗝️
# Dictionaries store data as labels (keys) with values.
# ---------------------------------------------------------


# 1. CREATING A DICTIONARY
print("--- Creating a dictionary ---")
student = {
    "name": "Aisha",
    "age": 14,
    "grade": "A"
}
print(student)


# 2. ACCESSING VALUES
print("\n--- Reading values ---")
print(student["name"])
print(student.get("age"))
print(student.get("school", "Not found"))   # safe way with default


# 3. CHANGING A VALUE
print("\n--- Changing a value ---")
student["age"] = 15
print(student)


# 4. ADDING NEW KEY-VALUE PAIRS
print("\n--- Adding new keys ---")
student["school"] = "Central High"
print(student)


# 5. UPDATE MULTIPLE VALUES AT ONCE
print("\n--- Update multiple ---")
student.update({"age": 16, "city": "Karachi"})
print(student)


# 6. REMOVING ITEMS
print("\n--- Removing items ---")
grade = student.pop("grade")
print("Removed grade:", grade)
print(student)


# 7. GETTING ALL KEYS, VALUES, AND ITEMS
print("\n--- Keys, values, items ---")
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())


# 8. CHECKING IF A KEY EXISTS
print("\n--- Checking for a key ---")
if "name" in student:
    print("Name is stored:", student["name"])


# 9. CLEARING A DICTIONARY
print("\n--- Clearing ---")
backup = student.copy()
student.clear()
print("After clear:", student)
print("Backup:", backup)


# 10. DICTIONARY LENGTH
print("\n--- Dictionary length ---")
print(len(backup))
