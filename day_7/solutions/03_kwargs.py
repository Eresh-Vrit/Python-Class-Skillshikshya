# ---------------------------------------------------------
# SOLUTION 3: **kwargs 🗝️
# ---------------------------------------------------------
# **kwargs collects any number of NAMED values into a dictionary.


# TASK 1: Print profile — one key/value per line.
def print_profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_profile(name="Alice", age=30, job="Engineer")


# TASK 2: Flexible introduction.
def introduce(name, **kwargs):
    print(f"Hi, I'm {name}.")
    for key, value in kwargs.items():
        print(f"My {key} is {value}.")

introduce("Bob", age=25, job="developer", hobby="chess")


# TASK 3: count_settings — how many named values were passed.
def count_settings(**kwargs):
    print(f"You set {len(kwargs)} settings.")

count_settings(theme="dark", size=14)            # You set 2 settings.
count_settings(volume=8, brightness=5, wifi=True) # You set 3 settings.
