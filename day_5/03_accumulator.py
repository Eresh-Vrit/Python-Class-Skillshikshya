# ---------------------------------------------------------
# DAY 5 | TOPIC 3: THE ACCUMULATOR PATTERN 🪣
# The most important loop pattern: start with a "bucket",
# fill it up a little each round of the loop!
# ---------------------------------------------------------


# ─────────────────────────────────────────────────────────
# SECTION 1: SUM & COUNT TOGETHER
# ─────────────────────────────────────────────────────────
# Pattern: create variables BEFORE the loop, update them INSIDE.
# You can track MULTIPLE things in the same loop!

scores = [85, 42, 91, 38, 77]

total = 0           # bucket for the sum
count = 0           # bucket for how many pass

for s in scores:
    total += s      # add each score to the total
    if s >= 60:
        count += 1  # only count if the score passes

print(f"Scores: {scores}")
print(f"Sum: {total}, Passing: {count}")


# ─────────────────────────────────────────────────────────
# SECTION 2: FINDING THE MAXIMUM (without using max())
# ─────────────────────────────────────────────────────────
# Imagine going through a list and keeping track of the
# biggest number you've seen so far.

numbers = [34, 78, 12, 99, 56]

biggest = numbers[0]   # start by assuming first is biggest

for n in numbers:
    if n > biggest:
        biggest = n  # found a new champion!

print(f"\nNumbers: {numbers}")
print(f"Biggest: {biggest}")


# ─────────────────────────────────────────────────────────
# SECTION 3: BUILDING A STRING CHARACTER BY CHARACTER
# ─────────────────────────────────────────────────────────
# Strings can be "accumulated" too — start with "", add each piece.

word = "python"
reversed_word = ""    # empty string bucket
for letter in word:
    reversed_word = letter + reversed_word  # add letter to the FRONT   "y" + "p" = "hontyp"

print(f"\nOriginal : {word}")
print(f"Reversed : {reversed_word}")


# ─────────────────────────────────────────────────────────
# SECTION 4: BUILDING A NEW LIST (filtering)
# ─────────────────────────────────────────────────────────
# Keep only the items you want by appending into a new list.

all_marks = [45, 82, 30, 91, 55, 74, 28, 66]
high_scorers = []     # empty list bucket

for mark in all_marks:
    if mark >= 70:
        high_scorers.append(mark)

print(f"\nAll marks   : {all_marks}")
print(f"High scorers: {high_scorers}")


# ─────────────────────────────────────────────────────────
# SECTION 5: PUTTING IT ALL TOGETHER — CLASS REPORT
# ─────────────────────────────────────────────────────────
student_scores = {
    "Alice": 88, "Bob": 45, "Charlie": 92,
    "Diana": 57, "Eve": 76, "Frank": 33
}

total_score = 0
pass_count  = 0

print("\n--- Class Report ---")
for student, score in student_scores.items():
    status = "PASS" if score >= 60 else "FAIL"
    print(f"  {student:<10} {score:>3}  {status}")
    total_score += score
    if score >= 60:
        pass_count += 1

average = total_score / len(student_scores)
print(f"\nClass average : {average:.1f}")
print(f"Students passed: {pass_count} / {len(student_scores)}")
