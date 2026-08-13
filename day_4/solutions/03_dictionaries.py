# ---------------------------------------------------------
# SOLUTION 3: DICTIONARIES — Key-Value Pairs 🗝️
# ---------------------------------------------------------


# TASK 1
book = {
    "title": "Python for Beginners",
    "author": "S. Coder",
    "year": 2022
}
print(book.get("title"))
print(book.get("pages", "unknown"))


# TASK 2
book.update({"year": 2024, "pages": 350})
print(book)


# TASK 3
removed = book.pop("year")
print("Removed:", removed)
print("Keys:", book.keys())
print("Values:", book.values())
print("Items:", book.items())


# TASK 4
backup = book.copy()
book.clear()
print("Original:", book)
print("Backup:", backup)


# BONUS CHALLENGE
student = {
    "name": "Omar",
    "score": 75
}
if student["score"] >= 60:
    print(student["name"], "passed!")
else:
    print(student["name"], "needs more practice.")
