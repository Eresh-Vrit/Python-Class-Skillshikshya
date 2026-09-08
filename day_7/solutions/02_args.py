# ---------------------------------------------------------
# SOLUTION 2: *args ✳️
# ---------------------------------------------------------
# *args collects any number of POSITIONAL values into a tuple,
# so a function can accept "as many" values as you want.


# TASK 1: my_sum — add any number of numbers.
def my_sum(*args):
    total = 0
    for n in args:              # args is a tuple — loop through it
        total = total + n
    return total

print(my_sum(1, 2))             # 3
print(my_sum(5, 10, 15))        # 30
print(my_sum(1, 2, 3, 4, 5))    # 15


# TASK 2: print_all — label + variable items.
def print_all(label, *items):
    print(f"{label}:")
    for item in items:
        print(f"- {item}")

print_all("Fruits", "apple", "mango", "banana")


# TASK 3: count_them — how many values were passed.
def count_them(*args):
    print(f"You passed {len(args)} values.")

count_them("a", "b", "c")       # You passed 3 values.
count_them(1, 2, 3, 4, 5)       # You passed 5 values.
