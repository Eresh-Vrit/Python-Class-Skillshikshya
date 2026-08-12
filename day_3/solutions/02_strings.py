# ---------------------------------------------------------
# SOLUTION 2: STRINGS 🔤
# ---------------------------------------------------------


# TASK 1: Case & Strip
full_name = "  Alice Smith  "
print(full_name.upper())        # "  ALICE SMITH  "
print(full_name.lower())        # "  alice smith  "
print(full_name.title())        # "  Alice Smith  "
print(full_name.strip())        # "Alice Smith"

# Notice: upper(), lower(), title(), and strip() all return a NEW string.
# The original full_name variable stays the same!


# TASK 2: Checking & Replacing
sentence = "I love Python"
print(sentence.startswith("I"))            # True
print(sentence.endswith("Java"))           # False
print(sentence.replace("Python", "coding"))  # "I love coding"
print("love" in sentence)                  # True


# TASK 3: Indexing & Slicing
animal = "elephant"
print(animal[0])      # "e"
print(animal[-1])     # "t"
print(animal[0:3])    # "ele"


# TASK 4: String Length & Banner
clean_name = full_name.strip()
print(f"My name has {len(clean_name)} characters!")
print("=" * 30)
print(clean_name)
print("=" * 30)


# TASK 5: Input + f-string
animal = input("What is your favourite animal? ")
print(f"Wow, {animal.strip()} is a great choice! [paw]")


# ⭐ BONUS CHALLENGE:
typed_name = input("Type your name: ")
print("*** " + typed_name.upper() + " ***")
