# ---------------------------------------------------------
# SOLUTION 1: FOR LOOP BASICS 🔄
# ---------------------------------------------------------


# TASK 1: Loop through a list of favourites.
# `for X in list:` runs the body once for every item in the list.
favourites = ["pizza", "chess", "anime", "guitar", "coffee"]
for thing in favourites:
    print(f"I really like: {thing}")


# TASK 2: Length reporter.
words = ["apple", "banana", "cherry", "dragonfruit", "elderberry"]
for word in words:
    print(f"{word} -> {len(word)} letters")


# TASK 3: Pass or Fail Reporter.
scores = [85, 42, 91, 38, 77, 55]
for score in scores:
    if score >= 60:
        print(f"{score} -> PASS")
    else:
        print(f"{score} -> FAIL")


# ⭐ BONUS CHALLENGE: Loop over a string.
word = "python"
for letter in word:
    print(f"Letter: {letter.upper()}")
