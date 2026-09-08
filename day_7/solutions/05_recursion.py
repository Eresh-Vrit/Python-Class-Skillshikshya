# ---------------------------------------------------------
# SOLUTION 5: RECURSION 🔁
# ---------------------------------------------------------
# A recursive function calls ITSELF on a smaller problem,
# until it hits a BASE CASE (a tiny problem it can answer directly).


# TASK 1: Count up — recursive call BEFORE the print.
def count_up(n):
    if n == 0:                  # base case: stop counting
        return
    count_up(n - 1)             # do the smaller problem first
    print(n)                    # then print this number on the way "back up"

count_up(5)                     # prints 1, 2, 3, 4, 5


# TASK 2: Multiply up (same idea as factorial).
def multiply_up(n):
    if n == 1:                  # base case
        return 1
    return n * multiply_up(n - 1)

print(multiply_up(4))           # 24
print(multiply_up(1))           # 1


# TASK 3: Repeat a string with recursion (no * operator).
def repeat(text, times):
    if times == 0:
        return ""               # base case
    return text + repeat(text, times - 1)

print(repeat("hi", 3))          # hihihi
print(repeat("hi", 0))          # (empty line)
